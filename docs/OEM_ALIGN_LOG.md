# 按 OEM 源码对齐 —— 执行记录

来源：`android_16.0_kernel_MT6989.tar.gz`（厂商内核源码，Makefile VERSION=6 PATCHLEVEL=1 SUBLEVEL=145，
与设备内核 6.1.145 一致）。解压于 `D:\neiheidaima\vivo_src`。

全树逐文件比对（git blob 哈希，AOSP `android14-6.1-2025-09` vs OEM）：

    79131 个文件    相同 78907    不同 195    仅 AOSP 有 26

其中相当一部分是「厂商树停在较早的 AOSP 修订」造成的漂移，而非厂商自创
（证据：`android/abi_gki_aarch64.stg.allowed_breaks` AOSP 比 OEM 多 9 条 ABI 变更记录；
 `kernel/time/posix-cpu-timers.c` OEM 少一整段 AOSP 新增代码；
 `enum lockdep_lock_type` OEM 少 AOSP 后加的 `LD_LOCK_WAIT_OVERRIDE`）。

## 已执行的组

| 组 | commit | 文件数 | 内容 |
|---|---|---|---|
| 1 | ab1acc6b | 3 | 锁定子系统去掉 `LD_LOCK_WAIT_OVERRIDE`（lockdep_types.h / lockdep.h / lockdep.c，三处同步） |
| 2 | dc47f1ae | 13 | HID 子系统整体对齐（含 `wacom_wac.h`+`wacom_sys.c`+`wacom_wac.c` 三件套，删 `inputmode_field_index` 并同步调用点） |
| 3 | e37900de | 5 | 追踪钩子：`android_vh_do_async_mmap_readahead` 与 `android_vh_throttle_direct_reclaim_bypass` 的声明+调用点+EXPORT 五处同步删 |
| 4 | bc54b99a | 1 | `include/linux/mm_types.h` 还原为 OEM 写法（去掉 `mm_struct_abi_extend`，改回 `ANDROID_KABI_RESERVE(1)`） |
| 5 | f391a458 | 5 | dma-buf 任务记账特性整组对齐（fdtable.h / file.h / fs/file.c / dma-buf.h / dma-buf.c） |

## 第 5 组的更正（重要）

f391a458 的提交信息里我写了「装入 OEM 版本后 dma_buf_account_task 等均为 0 次残留」，
**这是错的**。实测自检结果为：

    dma_buf_account_task     7 次
    dma_buf_unaccount_task   5 次
    task_dma_buf_info       18 次

正确理解：OEM **仍有**这套 dma-buf 任务记账特性，差异是**同一特性的不同修订**，不是有无之别。

已核实编译安全性：OEM 的 `include/linux/dma-buf.h` 第 808/809 行仍声明
`dma_buf_account_task` / `dma_buf_unaccount_task`（并有 static inline 兜底），
OEM 自己的 `mm/mmap.c` 也仍在调用它们（2 次）=> AOSP 版 `mm/mmap.c` 的调用点不会悬挂。

另注：`include/linux/fdtable.h` 里新增的 `struct task_dma_buf_info *dmabuf_info` 被
`#ifndef __GENKSYMS__` 包着，**因此它本身不影响 CRC**；本组对齐的目的是消除修订漂移、
避免编译悬挂，不指望它提升 CRC 命中。

## 教训（已固化为流程）

每次照搬 OEM 文件前，必须做两件事：
1. **引用面核查**：被删/被改的标识符在整树里还有哪些使用点，那些点是否也在 OEM 差异清单里（是则整组照搬）。
2. **装完后自检**：实际统计残留引用次数，用实测结果写提交信息，**不写预期值**。