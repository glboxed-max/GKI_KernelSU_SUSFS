# vivo V2339A(PD2339) 自编译内核 —— ABI/CRC 调查状态总览

> 本文件是跨会话的状态快照：**已知事实 / 已排除假设 / 待求证问题 / 数据资产 / 操作记录**。
> 目的：任何接手者（人或 agent）读完即可继续，不必重新推导。

---

## 0. 目标与硬约束

| 项 | 内容 |
|---|---|
| **原始目标** | 修复「自编译内核在 vivo V2339A(PD2339) 上加载不了厂商模块」——定位 modversions CRC（尤其 `module_layout`）不一致的原因，产出可刷入、能开机、厂商模块能正常加载的内核 |
| **硬约束** | **不得使用任何关闭/绕过版本校验的手段**（不开 `CONFIG_MODULE_FORCE_LOAD`，不改 CRC 表） |
| **用户后来说明的真实诉求** | **「我只要能开机能用就行」** |
| **用户态度** | 「我拒绝放弃」——要求穷尽调查 |

---

## 1. 设备与环境（实测）

```
设备          vivo V2339A / PD2339    序列号 10AE1J0FLZ000SN    SoC MT6989
手机内核      6.1.145-android14-11-maybe-dirty
手机 vermagic 6.1.145-android14-11-maybe-dirty SMP preempt mod_unload modversions vivo aarch64
已加载模块    585 个
              vivo_ts(4177920B) / sensors_class / fpsgo / mtk_fpsgo —— 全部【已加载】
              kernelsu(217088B) —— KernelSU 以【可加载模块(LKM)】形式在跑
/end        su 可用（context=u:r:ksu:s0，KernelSU 提供）
adb root     不可用（"adbd cannot run as root in production builds"）
配置         /proc/config.gz = 9246 行 / 3028 项
```

**推断（重要）**：`vivo_ts.ko` 能加载 ⇒ 手机内核的 `module_layout` 必须是 `0xe4a1dbce`
⇒ **手机当前跑的不是我们编的内核**（我们的恒为 `0x973d4800` / `0xcb472513`）。

**KernelSU 已正常工作的证据**（dmesg）：`KernelSU: handle_setresuid from 0 to 10285`、
`hook_manager: unmark … exec /system/bin/cp`、`libksud.so: KernelSU: ksu fd installed`。

---

## 2. 数据资产（路径）

| 资产 | 路径 | 说明 |
|---|---|---|
| **厂商内核源码** | `D:\neiheidaima\vivo_src` | 解自 `android_16.0_kernel_MT6989.tar.gz`（228MB，用户提供）。`Makefile`: 6.1.145，`NAME=Curry Ramen`。84229 条目 |
| AOSP 树（无工作区） | `D:\neiheidaima\_aosp\common` | 分支 `android14-6.1-2025-09`，用 `git show HEAD:<path>` 取内容 |
| 厂商模块 | `D:\neiheidaima\_re\modules\{vivo_ts,sensors_class,mtk_fpsgo,fpsgo}.ko` | 金标准 `__versions` |
| 对照模块（小米） | `D:\neiheidaima\_re\modules_other\{binder_gki,cfg80211}.ko` | 小米 PLK110 6.1.157 |
| 原厂内核 | `D:\neiheidaima\_re\stock.elf` | 42360347 B，type=EXEC，6 节区。**对 4 个模块 0 不符** |
| 原厂内嵌配置 | `D:\neiheidaima\_re\stock_embedded_config.txt` | 从 stock.elf 抠出，与 /proc/config.gz **sha256 相同** |
| 设备配置 | `…\default-workspace\device_config.txt`（+ `device_config.gz`） | 从手机 root 拉取 |
| 我们的构建产物 | `D:\neiheidaima\_out\crcprobe_<sha>\Image` / `…\sukisu_build\Image` | 各炉 |
| 全树比对结果 | `D:\neiheidaima\_re\src_diff\{diff_files.txt,ALL_DIFFS.txt,SUMMARY.txt,REAL_DIFF.txt,CRLF_ONLY.txt}` | 195 条差异 + 完整 diff |
| 内核 fork | `D:\neiheidaima\GKI_KernelSU_SUSFS` | remote `https://github.com/glboxed-max/GKI_KernelSU_SUSFS.git` |
| 会话脚本 | `…\default-workspace\*.py` | 见 §8 |

---

## 3. 已证实的核心事实

### 3.1 金标准与我们的差距

```
                        厂商模块要求 / 原厂内核        我们各炉
module_layout           0xe4a1dbce                 0x973d4800（设备config）/ 0xcb472513（SukiSU全功能）
不符符号数（4 模块合计） 0 / 0 / 0 / 0              142 / 7 / 43 / 1 = 193 / 需求 558
kmalloc_caches          0xb5c66f9d                 0x21f38a09 / 0x1f5281e9
```

- **被测模块与需求**：`vivo_ts.ko` 306 个、`sensors_class.ko` 15、`mtk_fpsgo.ko` 200、`fpsgo.ko` 37
- **未导出符号**：9 / 0 / 58 / 34（`vivo_ts` 那 9 个是厂商模块间的相互导出，非内核问题）

### 3.2 工具链是正常的（关键反证）

**小米 PLK110（6.1.157）的厂商模块要求的 CRC 值 = 我们标准 GKI 构建算出的值（`0xea759d7f`）**
⇒ **我们的工具链能复现标准 GKI**，**偏差是 vivo 这一侧特有的**。

### 3.3 源码层面几乎相同

```
逐文件比对（git blob 哈希）：AOSP 79131 个文件
   相同 78907    不同仅 195    仅 AOSP 有 26
```

**195 条里相当一部分是「厂商树停在较早的 AOSP 修订」，而非厂商自创**：
- `android/abi_gki_aarch64.stg.allowed_breaks`：AOSP 比 OEM 多 9 条 ABI 变更记录
  （其中 `struct mm_struct` +`mm_struct_abi_extend`、`struct files_struct` +`task_dma_buf_info`）
- `enum lockdep_lock_type`：OEM 少 AOSP 后加的 `LD_LOCK_WAIT_OVERRIDE`
- `kernel/time/posix-cpu-timers.c`：OEM 少 AOSP 新增的一整段
- `include/linux/mm_types.h`：OEM 用 `ANDROID_KABI_RESERVE(1)`（AOSP 已改成 `ANDROID_KABI_USE(1, mm_struct_abi_extend *)`）

### 3.4 ★ 最重要的一条负面结论

**把 OEM 相对 AOSP 的 150 个 ABI 相关文件全部照搬对齐，整树编译通过，CRC 逐位未变：**

```
                对齐前(a706a096)      对齐后(22ee1afa，158 补丁文件)
vivo_ts 不符           142                   142
sensors_class 不符       7                     7
mtk_fpsgo 不符          43                    43
fpsgo 不符               1                     1
module_layout    0x973d4800            0x973d4800   ← 逐位相同
kmalloc_caches   0x21f38a09            0x21f38a09   ← 逐位相同
```

⇒ **厂商模块的 CRC 分歧不来自源码。**

### 3.5 配置层面完全相同

- 设备 `/proc/config.gz` 与 `stock.elf` 内嵌配置：**sha256 完全相同**（`68551B58…`），0 处差异
- 补丁文件用到的 **561 个 `CONFIG_*` 守卫宏**，设备 vs 我们 defconfig：**0 处取值不一致**
- `CONFIG_TRIM_UNUSED_KSYMS` 在 AOSP 树、设备 config、我们 defconfig 里**都是 `not set`**

### 3.6 ★ 量级最大的差异：导出符号数与体积

```
                    原厂（手机上跑的）        我们（SukiSU 全功能）
__ksymtab 符号数       15532                   8274
Image 大小            42360347 B              37431808 B      （差 4.9 MB）
```

**原厂多出的符号是通用子系统**：`pci_*` 271、`scsi_*` 98、`devlink_*` 100、`drm_*` 633、
`snd_*` 428、`v4l2_*` 206、`usb_*` 297、`nf_*` 197、`crypto_*` 171、`phy_*` 148…
—— **这些都不在 GKI 的 KMI 白名单里 ⇒ 原厂内核不裁剪，我们的被裁过。**

### 3.7 vermagic 已打通 ✓（本轮唯一确定的成果）

```
厂商模块要求 : 6.1.145-android14-11-maybe-dirty SMP preempt mod_unload modversions vivo aarch64
SukiSU 产物  : 6.1.145-android14-11-maybe-dirty SMP preempt mod_unload modversions vivo aarch64  ✓
旧构建       : …modversions aarch64   ✗ 缺 vivo
```
实现方式：`build.yml` 的 `oem_vermagic` 输入（默认值 `'vivo aarch64'`），
由 `.github/actions/oem-vendor-compat/action.yml` 对齐 `MODULE_ARCH_VERMAGIC` 与 UTS 版本串。

---

## 4. 已排除的假设（不要再往这些方向试）

| # | 假设 | 排除依据 |
|---|---|---|
| 1 | config 不同（OEM 预留字段 / KABI / 补丁集） | 两份 config **逐字节相同** |
| 2 | 厂商源码有 ABI 相关改动 | **150 个文件全对齐后 CRC 逐位不变** |
| 3 | 结构体成员差异（逐个复刻） | 11 处、13 处、158 处三批对齐，**计数与数值均不变** |
| 4 | 追踪钩子 / HID / 锁定子系统 / KVM / f2fs / dma-buf 等具体子系统 | 逐组对齐后无变化；且这些类型不在目标符号闭包内 |
| 5 | genksyms 工具链版本问题 | 小米模块要求的值 = 我们的标准 GKI 值 |
| 6 | 机型符号表机制（KMI whitelist per-device） | `apply-device-patches` 只对 `android15-6.6` 生效 |
| 7 | 内核版本串不匹配 | 版本串逐字符相同；`vermagic` 现已对齐 |

---

## 5. 待求证的问题（按优先级）

### ✔ P1【已结案·负结果】KMI 符号表裁剪 —— 查清了，但**不是** CRC 分歧的原因

**症状**：原厂导出 15,532 个符号，我们只有 8,274；Image 差 4.9 MB。

**证据（从两边内核内嵌的 `.config` 直接抠出，不需等构建）**：

```
                        我们的构建（裁剪版）    原厂（手机上跑的）
CONFIG_TRIM_UNUSED_KSYMS     =y              # ... is not set
CONFIG_UNUSED_KSYMS_WHITELIST="abi_symbollist.raw"  (未出现)
配置项总数                2189 / 2237        3031
=m（模块数）                75 / 62           665
```

**机制（在 AOSP 的 `BUILD.bazel` 里找到）**：

```
BUILD.bazel:143   "kmi_symbol_list": "android/abi_gki_aarch64",
BUILD.bazel:146   "additional_kmi_symbol_lists": [":aarch64_additional_kmi_symbol_lists"],
BUILD.bazel:147   "protected_exports_list": "android/abi_gki_protected_exports_aarch64",
```

⇒ Kleaf 依据 `kmi_symbol_list` 生成 `abi_symbollist.raw`，据此开启
`TRIM_UNUSED_KSYMS=y` + 白名单，把导出裁到 8,274 个。

**正确开关（在 Kleaf 源码 `kernel/build` 里找到，浅克隆于 `D:\neiheidaima\kleaf_src`）**：

```
kleaf/bazelrc/flags.bazelrc:60
    build --flag_alias=notrim=@kleaf//build/kernel/kleaf/impl:force_disable_trim
kleaf/impl/abi/abi_transitions.bzl:51-59
    """notrim: like _with_vmlinux, but trim_nonlisted_kmi = False"""
    return _with_vmlinx_transition_impl(settings, attr) | { FORCE_DISABLE_TRIM: True }
kleaf/impl/kernel_build.bzl:1094
    Label(".../defconfig:notrim_defconfig"): "False"
```

**已实施**：`c38378f7` 给 bazel 命令加 `--notrim` ⇒ 构建串从 `(lto=fast;trim)` 变成 `(lto=fast;notrim)` ✓

**结果（`crc-probe-c38378f7`）**：

```
导出符号数:  8,274  →  15,361      （原厂 15,532，几乎追平 ✓）
Image 大小:  37.4 MB → 35.5 MB

但 CRC 一位未变：
                         裁剪版        不裁剪版       原厂
module_layout        0x973d4800    0x973d4800    0xe4a1dbce
kmalloc_caches       0x21f38a09    0x21f38a09    0xb5c66f9d
wake_up_process      0xc84578e3    0xc84578e3    0x30d402ab
不符计数             142/7/43/1    142/7/43/1    0
```

**⇒ 结论：KMI 裁剪不是 CRC 分歧的原因。**（此前"导出机制进闭包"的推理是错的 ——
genksyms 逐符号对**声明文本**哈希，与最终导出哪些符号无关。）

**但这一炉并非白做**：构建形态现已与原厂一致（导出集合、`=m` 数量都更接近），
对**模块加载的其他环节**（不只 CRC）是有意义的对齐；
并且它把「构建形态」这最后一个假设也排除了。

#### 失败的中间尝试（`6c767534`，已回滚 `d9cd1062`）

直接 `sed` 删 `BUILD.bazel` 里的 `kmi_symbol_list` 等属性 ⇒ 构建失败：
```
ERROR: common/BUILD.bazel:139:22: Creating abi_symbollist.raw
       @//common:kernel_aarch64_raw_kmi_symbol_list failed (Exit 1)
```
原因：该属性被 `//common:kernel_aarch64_raw_kmi_symbol_list` 目标依赖。
**教训：改"行为开关"，不要删"声明"。**

---

### ★★★ P6【重大发现】厂商源码包是**不完整的** —— 缺 `kernel/vivo_rsc/`

**发现路径**：对比导出符号清单（原厂 `stock.elf` vs 我们 `--notrim` 后的产物）

```
原厂  15532 个导出符号
我们  15361 个
原厂独有 171    我们独有 0        ← 我们是原厂的【严格子集】，一个都不多
```

**缺的 171 个里，最大一块是 `rsc:*` 共 67 个**：
`rsc_root_dir` / `rsc_chown_to_system` / `rsc_cpu_maxcore` / `rsc_debug` / `rsc_init_done` …

**而 `rsc_*` 正是 `mtk_fpsgo.ko` 那"58 个未导出符号"的来源。**

**追到根**：

```
vivo_src/Kconfig:34            source "kernel/vivo_rsc/Kconfig"
vivo_src/kernel/vivo_rsc/      不存在 ✗
vivo_src/kernel/ 子目录        bpf cgroup configs debug dma entry events futex gcov irq
                               kcsan livepatch locking module power printk rcu sched time trace
                               ← 没有 vivo_rsc
OEM 独有文件（全树仅 3 个）     project.config
                               include/linux/sensors.h
                               include/soc/nvt/vis_display.h
```

⇒ **厂商源码包引用了自己没带上的目录 `kernel/vivo_rsc/`。**

**影响（重要）**：

1. **这份 tar 包无法忠实复现设备内核** —— 至少缺一整个 `vivo_rsc` 子系统（提供 67 个厂商模块依赖的导出符号）
2. **路线 C（用厂商源码当基座）因此受阻** —— 除非用户能拿到缺失的 `kernel/vivo_rsc/`
3. 这也与另一个独立证据吻合：**该源码包编不出 vermagic 里的 `vivo` 标记**
   ⇒ 两个证据共同说明：**它不是设备内核的完整构建源**
4. **但不影响 P2 的结论** —— `module_layout` 的 CRC 差异仍然与源码无关（闭包内文件都已对齐）

**待用户行动**：
- 向厂商/社区索取完整的 `kernel/vivo_rsc/` 目录（或描述其内容的文档）
- 或确认该 tar 包是否为"开源合规包"（只含 AOSP 部分 + 少量头文件）

**另注（次要，但有用）**：那 171 个里还有一批 `__SCK__tp_func_android_vh_*`
（静态调用键）—— 对应的是我在"追踪钩子"那一组**主动撤掉**的钩子
（`android_vh_do_async_mmap_readahead`、`android_vh_throttle_direct_reclaim_bypass` 等）。
若要与原厂导出集合完全一致，那些钩子应保留 —— 但实测证明它们与 CRC 无关。

---

### ★★★ P7【重大发现】从手机 A/B 槽提取镜像 —— 确认活动槽与 KernelSU 的真实加载方式

**抓取的分区**（`su` + `dd`，保存于 `D:\neiheidaima\_re\phone_boot\`）：

```
boot_a=sdc38  100663296 B      boot_b=sdc72  100663296 B
vendor_boot_a=sdc39 134217728 B   vendor_boot_b=sdc73 134217728 B
init_boot_a=sdc40    8388608 B    init_boot_b=sdc74    8388608 B
```

**① 活动槽是 B**（`getprop ro.boot.slot_suffix = _b`）—— **我第一次抓的是非活动槽 A**，所以最初的结论全部要按槽位修正。

**② 两个槽的内核版本不同**（把 LZ4-legacy 压缩的 ramdisk/内核解出后读版本串）：

| 槽 | 内核版本串 | vermagic | module_layout |
|---|---|---|---|
| **A（非活动）** | `6.1.124-android14-11-maybe-dirty` | `…6.1.124… modversions vivo aarch64` | — |
| **B（活动 ✓）** | `6.1.145-android14-11-maybe-dirty` | `…6.1.145… modversions vivo aarch64` | **0xe4a1dbce** ✓ |

**③ 活动槽内核 = 我们的金标准**：把 `boot_b.img` 里的内核解出来（36,952,576 B）后测量：

```
boot_b.kernel :  module_layout = 0xe4a1dbce   对 4 个厂商模块 0 / 0 / 0 / 0 不符 ✓
stock.elf     :  module_layout = 0xe4a1dbce   0 / 0 / 0 / 0 ✓
```

⇒ **`stock.elf` 确实就是手机正在跑的内核**，我们一直用的比对基准是对的 ✓

**④ ★ 关键：KernelSU 模块的真实状态**（两个槽的 `init_boot` 里都有 `kernelsu.ko`，386,720 B）：

```
init_boot_a → kernelsu.ko    vermagic: 6.1.166-dirty SMP preempt mod_unload modversions aarch64
init_boot_b → kernelsu.ko    vermagic: 6.1.166-dirty SMP preempt mod_unload modversions aarch64
                                        ^^^^^^^                    ^^^^^^
                              不是运行内核的 6.1.145              没有 vivo 标记
```

⇒ **这个模块的 vermagic 与正在运行的 6.1.145 内核根本对不上**（版本不同 + 缺 `vivo`），
正常 `insmod` **必然被 `check_modinfo()` 拒绝**；但它确实出现在 `/proc/modules` 且 dmesg 有
KernelSU 活动日志 ⇒ **它只能是通过 bypass 方式加载的**。

**⇒ 对用户诉求的意义（重要）**：
这台手机**当前可用的 KernelSU 方案本身就走着 bypass**（模块 vermagic 与内核不匹配）。
也就是说，用户"不得使用任何关闭版本校验的绕过手段"这条约束，
**比这台手机现在实际能用的方案还要严格**。

**⑤ 附带确认**：`boot_a`/`boot_b` 里的内核与 ramdisk 都是 **LZ4-legacy 分块压缩**
（magic `02 21 4C 18` + 逐块 `size(4)+data`）；解压脚本见 `parse_bootimg.py` / `extract_cpio.py`
（cpio 解析需校验 13 个十六进制字段，否则会把压缩流里的字面量误认成 cpio 头）。

---

### ★ P9 `vr.ko` 与 `vivo_rsc.ko` 的发现（含对我前面两次结论的更正）

**起因**：用户要求再查一遍 vendor_boot 解出的文件里有没有 `vr.ko`。

**找到的东西**（`vendor_boot_b` 的 ramdisk，1281 个 cpio 成员里）：

```
lib/modules/vr.ko             厂商套  210,560 B
lib/modules/6.1-gki/vr.ko     GKI 套  211,296 B
lib/modules/vivo_rsc.ko       厂商套   10,232 B
lib/modules/6.1-gki/vivo_rsc.ko GKI 套 10,232 B
vklp：整个 ramdisk 里出现 0 次 —— 该名字确实不存在
```

#### 更正 ①：`vr.ko` **是存在的**

我早前说"设备上找不到 `vr.ko`"——**错了**。它在 `vendor_boot` 的 **ramdisk** 里；
运行时的 ramdisk 内容**不以文件形式可见**（`/proc/modules` 只有已加载的 585 个，里面没有它），
所以全盘 `find` 找不到 ≠ 不存在。**教训：要找首阶段模块必须解 ramdisk，不能只在文件系统里搜。**

#### 更正 ②：`vivo_rsc.ko` 是**假模块**，P6 的结论**依然成立**

```
description = "VIVO RSC Driver Fake v0.2"      ← 名字里就写着 Fake
name        = vivo_rsc
__versions  = 只有 2 条（_printk / module_layout）
未定义符号  = 只有 _printk、__this_module
导出符号    = 无（没有任何 __ksymtab_ 符号）
字符串      = "rsc_fake: rsc init" / "rsc_fake: rsc exit"
```

**⇒ 它是个空壳占位模块，不提供任何符号。**
⇒ 所以"`rsc_*` 不由任何模块提供"这一判断**成立**，`rsc_*` 只能来自内核，
   而内核里提供它的正是源码包缺失的 `kernel/vivo_rsc/` ✓
⇒ **这个 "Fake" 桩本身就是旁证**：厂商把真正的 RSC 代码放在内核里，模块侧只留了个假的。

#### 两套 `vr.ko` 的实测对照（重要）

| | 厂商套 `vr.ko` | GKI 套 `vr.ko` |
|---|---|---|
| vermagic | `6.1.145… modversions **vivo** aarch64` | `6.1.145… modversions aarch64` ← **无 vivo** |
| `module_layout` | **`0xe4a1dbce`** | **`0xea759d7f`** |
| `__versions` | 127 条 | 125 条 |
| 对原厂内核 | **一致 127 / 不符 0** ✓ | 一致 86 / 不符 39 |
| 对我们内核 | 一致 92 / **不符 35** | 一致 86 / **不符 39** |

**⇒ 两点结论**：

1. **两套模块的 vermagic 互斥**：厂商套要 `vivo` 标记、GKI 套不要。
   我们现在为对齐厂商套加了 `vivo` ⇒ **反过来会拒掉 GKI 套**。
2. **GKI 套不属于我们**：它对我们内核（86/39）与对原厂内核（86/39）**结果完全相同**
   ⇒ 我们的内核在它眼里与原厂内核一样不匹配。
   ⇒ 它是厂商另做的一个 GKI 风味构建（`module_layout` 恰为 GKI 值，但逐符号 CRC 不同）。
   ⇒ **用"6.1-gki 那套模块绕过 CRC 难题"这条路，到此用 125 个符号逐一验过，确认不通。**

---

### ★★★★ P8【改变判断的发现】vendor_boot 里装着**两套**模块，面向**两个不同 ABI**

**方法**：用用户提供的 `magiskboot.exe`（Windows 版）解包，结果与手写解析器**字节数完全一致**
（kernel 36,952,576 / init_boot ramdisk 7,967,192）⇒ 两条路径互相验证：

```
boot_b        HEADER_VER 4  KERNEL_SZ 17422634  KERNEL_FMT lz4_legacy  → kernel
init_boot_b   HEADER_VER 4  RAMDISK_SZ 4030428  RAMDISK_FMT lz4_legacy → ramdisk.cpio
vendor_boot_b VENDOR_BOOT_HDR v4  RAMDISK_SZ 119871812  RAMDISK_FMT raw → ramdisk.cpio + dtb(451179)
```

**`vendor_boot_b` 的 ramdisk（120 MB / 81 个分片）展开后 = 180,338,688 B，cpio 成员 1282 个，
其中 604 个 `.ko` 模块**（已全部抽出到 `D:\neiheidaima\_re\phone_boot\vendor_mods\`）。

**★★ 关键：这 604 个模块是两套，面向两个不同内核：**

| 目录 | 面向 | `module_layout` |
|---|---|---|
| `lib/modules/*.ko` | **厂商内核**（手机现在跑的） | **`0xe4a1dbce`** ✓ 与 stock.elf 一致 |
| **`lib/modules/6.1-gki/*.ko`** | **标准 GKI 内核** | **`0xea759d7f`** ★ |

**⇒ `0xea759d7f` 正是①我们标准 GKI 构建算出的值、②小米 PLK110(6.1.157) 厂商模块要求的值。**
**⇒ 也就是说：这台设备本来就预置了一整套面向标准 GKI 的厂商模块，且是厂商自己编译的。**

**⇒ 这条发现直接改变判断**：

```
之前：厂商模块只认 0xe4a1dbce ⇒ 我们的 GKI 内核永远加载不了它们（死路）
现在：设备里另有一套面向 0xea759d7f 的模块 ⇒ "自编译 GKI 内核"路线重新可行 ✓
```

**同时解释了验收脚本第一次"失败"的原因**：我把两套面向不同 ABI 的模块混在一起统计，
二者互不匹配本来就是应该的（原厂内核对 GKI 那套也会大量不符）。

**验收工具**：`accept_all.py`（内核侧从 ELF 的 `__ksymtab`/`__kcrctab` 建 `name→CRC`；
模块侧解析 `__versions`，条目 64 字节 = u64 crc + char name[56]）。
**已单点验证两侧解析器都正确**：

```
stock.elf    module_layout=0xe4a1dbce  kmalloc_caches=0xb5c66f9d   ✓ 与真值一致
Image.elf    module_layout=0x973d4800  kmalloc_caches=0x21f38a09   ✓ 与 measure.py 一致
vivo_ts.ko   __versions=306 条  module_layout=0xe4a1dbce          ✓ 与真值一致
```

**另**：在全部 604 个模块里搜 `rsc_*` —— **只有引用（`system_heap.ko`），没有任何模块定义它**
⇒ 进一步确认 `rsc_*` 由内核里缺失的 `kernel/vivo_rsc/` 提供 ✓

---

### ★★ P2【唯一剩下的层次】genksyms 的输入文本 / 工具版本

**排除进度**：

```
源码      ✗ 已排除（150 处全对齐、编译通过、CRC 逐位不变）
配置      ✗ 已排除（设备 config 与内嵌 config 逐字节相同；561 个守卫宏 0 处不一致）
构建形态  ✗ 刚排除（导出 8.3k → 15.4k，CRC 仍逐位不变）
工具链    ✗ 已排除（小米 PLK110 厂商模块要求的值 = 我们标准 GKI 的值 0xea759d7f）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
剩下  ⇒  genksyms 的【输入文本】本身，或 genksyms 自身的版本
```

**新条件（有利）**：两边导出集合已几乎相同（15,361 vs 15,532），
所以可以开始做"同一前提下的文本级对比"。

**候选做法**：

| # | 做法 | 说明 |
|---|---|---|
| P2-a | **对比两边符号清单的差集** | 我们 15,361 vs 原厂 15,532 ⇒ 171 个差异，看是否有系统性缺失 |
| P2-b | **查 genksyms 版本** | 从 `vmlinux`/构建环境取证；厂商可能用了不同版本的 `scripts/genksyms` |
| P2-c | **dump `module_layout` 的预处理产物** | 对 `struct module` 闭包做 `gcc -E`（带 `-D__GENKSYMS__`），与厂商同流程对比 |
| P2-d | **直接跑 genksyms 对比输出** | 同一份 `version.c` + 头文件，两边各跑一次，diff 结果 |

**方法要点**：genksyms 哈希**预处理后的文本**，所以差异来源可能是：
1. 某个 `#ifdef` 分支（但 561 个守卫宏已排查，0 处不一致 ✗ 可能性低）
2. **typedef / `const` / 宏展开的写法**（OEM 源码已对齐 ✗）
3. **genksyms 自身版本差异** ← 现在最可疑

### P2：`module_layout` 闭包 100% 相同、CRC 却不同 —— 到底差在哪一层？

- 事实：`module_layout` 的类型闭包 1428 个类型，具名类型 1027 个**逐项一致（含成员名）**；
  5 个参数的原型也逐一相同
- ⇒ 其差异**不可能是 BTF 可见的结构差异**，只能是 ① 预处理文本 ② genksyms 本身 ③ 构建形态（P1）
- 待做：P1 结果出来后重测；若 P1 无效，则需对比两边 genksyms 的**输入文本**（可用 `make` 的 `--save-temps` 或直接跑 genksyms 对比）

### P3：`vr.ko` / `vklp.ko`

- 用户要求「列入 cmdline 黑名单」，**但这两个模块在设备上根本不存在**：
  root 权限 `find /` 全盘搜索为空；`/proc/modules`（585 个）没有；
  `/vendor/lib/modules`（295 项）、`/system_dlkm`（7 项）、ramdisk 都没有
- 已做的：`module_blacklist=vr,vklp` 已加入 `CONFIG_CMDLINE`（commit `f3d87981`），预置生效
- **待用户澄清**：这两个名字是从哪看到的？（另一个内核？某个刷机包的 `modules.load`？拼写差异？）

### P4：f2fs 的结论要复核

- 源码：`fs/f2fs` 31 个文件，**28 个逐行相同**；仅 `super.c`(48)、`file.c`(32)、`node.c`(10) 有差异
- 但 BTF：`struct f2fs_sb_info` 原厂 8608 B vs 我们 4264 B（**2 倍**）
- **源码相同而结构体差 2 倍 ⇒ 只能是 CONFIG 造成**（但设备与我们的 f2fs 配置项一致）
- ⇒ **此矛盾未解**，需在 P1 的诊断数据出来后一并复核（可能与"驱动内建/模块"同源）

### P5：我们的内核能否真的刷入并开机？

- 用户此前刷过一版**不开机**，随后刷回原厂；此后未再实测
- 现成可刷包：workflow artifact `6.1.145-android14-2025-09-SukiSU-Ultra-AnyKernel3`（19.2 MB）
  - run `36439916960`（含 158 个 abi_patches）
  - run `36439513247`（不含）
- **未验证**：刷入后是否开机、厂商模块是否开始加载（vermagic 已对齐，CRC 仍未对齐）

---

## 6. 关键判据（用来看进展）

1. **不符计数**：`vivo_ts / sensors_class / mtk_fpsgo / fpsgo = 142 / 7 / 43 / 1`（目标全 0）
2. **`module_layout`**：期望 `0xe4a1dbce`
3. **导出符号数**：期望接近 15532（现 8274）
4. **被推动的符号数**：`不符 ∩ 已变化`（第 1 批时 45/169，说明只有 `readahead_control`+`skb_shared_info` 与它们相关）

---

## 7. 操作记录

### 7.1 仓库提交（`glboxed-max/GKI_KernelSU_SUSFS`）

```
c7976a01  ci(crc-probe): 增加诊断步骤 —— 打印生效 .config 与导出符号数   ← 当前 HEAD
d7c7a809  (同上的一次提交，message-file 版本)  / 9300f6e4 之前
a706a096  revert(abi): 撤掉我加的 11 个实验性补丁 —— 零 CRC 改善、只增风险
a416fedb  甲类第 11 批 sched_switch +7 字段
e1aa56fb  甲类第 10 批 loop_device +RT 三件套
5c417d79  回退 hid_data（删字段未删引用导致编译失败）
cf000090 / dc8606bc / 6f11dac8 / 56cf4f28 / d1d84af0 / ab2387de  甲类第 2~9 批
e1d1b4b6  fix(abi): mm_types.h 删除残留 '}'（修编译失败）   ← 保留
f3d87981  module_blacklist=vr,vklp 加入 CONFIG_CMDLINE
22ee1afa  OEM 全量对齐（158 个补丁文件，编译成功）
ab1acc6b / dc47f1ae / e37900de / bc54b99a / f391a458  OEM 对齐第 1~5 组
```

### 7.2 构建/工作流

- `crc-probe.yml`：设备 defconfig + ABI 补丁 → bazel → 公开 Release `crc-probe-<sha8>`
  - inputs: `os_patch_level`(默认 2025-09)、`use_device_defconfig`(默认 true)、`use_abi_patches`(默认 true)
  - 触发：`push`（`.github/patches/**`、config、自身）+ `workflow_dispatch`
- `baseline-probe.yml`（tag `baseline-*`）、`gki-probe.yml`（tag `gki-*`）：对照用
- `main.yml` → `build.yml`：**真正的刷机包构建**，inputs 见 §7.3
- `dsh-fetch-log.yml`：定时把日志提交回仓库（无 token 通道）
- 已知构建坑：
  - 顶层 `Kconfig` 不能照搬 OEM（它会 `source kernel/vivo_rsc/Kconfig`，厂商专有目录不存在）
  - netfilter UAPI 头是「转发壳」，不能单侧照搬（会与 AOSP 的 `.c` 配不上）

### 7.3 SukiSU-Ultra 刷机包构建（已成功两次）

```
root_flavor          : SukiSU-Ultra
kernel_build_version : 6.1.x-android14
os_patch_level       : 145                 ← 锁定 6.1.145
brand_name           : vivo
abi_patches          : true / false（两炉）
commit_mode          : latest
oem_vermagic         : vivo aarch64        ← build.yml 默认值
全部功能开关          : use_susfs/use_nomount/use_bbg/use_net/use_ds/
                       use_ntsync/use_ptrace/use_unicode/use_bpf/use_perf = true
                       ★ use_perf 默认 false，需显式打开
release_type         : Pre-Release
```

API 触发：
```
POST /repos/glboxed-max/GKI_KernelSU_SUSFS/actions/workflows/main.yml/dispatches
{"ref":"main","inputs":{...}}     ← workflow_dispatch 的 inputs 必须是字符串
```

---

## 8. 工具清单（`…\default-workspace\`）

| 脚本 | 用途 |
|---|---|
| `measure.py` | **金标准比对**：Image → ELF，解析 `__ksymtab`/`__kcrctab`，对比厂商模块 `__versions` |
| `export_diff.py` | 独立实现（ELF `.symtab` 路线），结果与 `measure.py` 逐项一致 |
| `watch_by_tag.py` | 无 token 看门：轮询 tag → 下载 Release 产物 → 自动跑 measure.py |
| `btf_diff.py` | BTF 结构差异（自写解析器，**可用**） |
| `struct_members.py` | **两边完整成员表 + 字节偏移对齐**（`btf_diff` 只打印差异项，看不到全貌） |
| `btf_global_diff.py` / `enum_dump.py` / `func_proto.py` / `dup_check.py` / `module_layout_closure.py` | BTF 侧分析 |
| `src_tree_diff.py` | AOSP vs OEM 全树哈希比对 |
| `src_diff_detail.py` / `src_diff_normalize.py` / `audit_chains.py` / `audit_chains2.py` / `cfg_guard_compare.py` | 差异明细与链路/配置审计 |
| `align_all_oem.py` | 批量把 OEM 文件装成整文件覆盖补丁 |
| `carve_config.py` / `img_config.py` / `ver_check2.py` | 配置提取与版本核对 |
| `oc.py` | 驱动 OpenCode 会话（本次协作方） |
| 文档 | `STATUS.md`、`JIA_FIX_LIST.md`、`ROOT_CAUSE_FINAL.md`、仓库内 `docs/OEM_ALIGN_LOG.md` |

---

## 9. 交接注意事项（踩过的坑）

1. **不要**在 `D:\neiheidaima\GKI_KernelSU_SUSFS` 里执行 `git checkout -- .`（曾毁掉协作者的未提交工作）
2. **不要**暴露 GitHub token / OpenCode 服务密码
3. 推送用：`git -c credential.helper= -c credential.helper=store -c credential.interactive=false push`
   （系统级 `credential.helper=manager` 会弹窗；本地 `store` 才是有效的）
4. 提交信息含 `[` `]` `*` 时，**用 `git commit -F <文件>`**，否则 PowerShell 会把它们当 pathspec
5. **不要**用内联 `python -c "…"`（PowerShell 会吃掉引号）——**一律写 `.py` 文件再跑**
6. PowerShell 变量名**不区分大小写**（`$a` 与 `$A` 是同一个变量，曾因此写坏脚本）
7. Windows 保留设备名（`aux`/`con`/`nul`…，带扩展名也不行）会导致解压/检出失败，需过滤
8. 改结构体前**先 grep 引用面**（曾因删 `inputmode_field_index` 未删 5 处引用导致编译失败）
9. 「整批照搬」时要单独排除：**跨目录汇总文件**（`Kconfig`/`Makefile`）、**转发壳文件**（只含 `#include` 的同名头）

---

## 10. 一句话现状

**已确定**：源码不是原因（150 处全对齐、编译通过、CRC 逐位不变）；配置不是原因（逐字节相同）；
工具链正常（小米模块反证）；`vermagic` 已对齐 ✓。
**唯一剩下的、量级匹配的线索**：原厂内核导出 15532 个符号、我们只有 8274 ——
构建日志里的 `(lto=fast;trim)` 指向某个尚未定位的裁剪机制。
**诊断步骤已上（`c7976a01`），等这一炉 crc-probe 的结果。**

---

## 11. 已知的错误方向（不要再走）

### 11.1 方法论上的错误（判断错，浪费了时间）

| # | 错误方向 | 为什么错 | 代价 |
|---|---|---|---|
| 1 | **把"不符计数不降"当作没进展的判据** | genksyms CRC 是**不可分哈希**：只复刻部分差异时，CRC 会移动但**永远不会落到目标值**。中间态计数必然持平 | 一度误判为 blocked（用户纠正后才重新审视） |
| 2 | **把 BTF 里"原厂有、我们没有"的字段全部当成厂商改动** | `btf_diff` 取的是**第一个**同名类型，原厂 BTF 里有**重名类型**（如 `kyber_queue_data` 两份、size 600/640）⇒ 部分是工具假象 | 白做了 `discard_cmd` / `discard_cmd_control` / `discard_policy` 三批 |
| 3 | **以为 f2fs 有厂商特有字段**（`discard_time_lock` / `sub_policy` / `force_discard_type`） | 拿到 OEM 源码后一查：**两个源码树里都没有这些名字**；`fs/f2fs/f2fs.h` 两边 4702 行**逐行相同** | 同上三批补丁建立在错误前提上（已全部撤回） |
| 4 | **以为 `/proc/config.gz` 可能不是手机真实配置** | 从 `stock.elf` 内嵌配置抠出来对比：**sha256 完全相同**（`68551B58…`），0 处差异 | 误判一轮 |
| 5 | **试图从二进制反推 genksyms 的输入文本** | genksyms 哈希的是**预处理后的声明文本**（typedef 拼写、`const`、宏展开），BTF 只记录**布局**，原厂 `Image` 里**没有 DWARF**（仅 6 个节区）⇒ **信息论上不可恢复** | 这是整条"复刻结构体"路线的根本障碍 |
| 6 | **在本地尝试构建** | 用户明确要求用 GitHub CI；且本机只有 `cpp`，没有 gcc/make/bison/flex | — |

### 11.2 技术上踩的坑（都导致过编译失败或白跑一炉）

| # | 坑 | 教训 |
|---|---|---|
| 7 | 删结构体成员却不删引用（`hid_data::inputmode_field_index`，AOSP 里 5 处引用） | **改结构体前先 grep 引用面**；头文件+所有消费者必须同批改 |
| 8 | 照搬 OEM 的**顶层 `Kconfig`** | 它 `source kernel/vivo_rsc/Kconfig`（厂商专有目录，AOSP 没有）⇒ kconfig 阶段直接死。**跨目录汇总文件（Kconfig/Makefile）必须单独排除** |
| 9 | 照搬 OEM 的 **netfilter UAPI 头**（`xt_connmark.h` 只有 7 行，是转发壳） | 与 AOSP 的 `.c` 配不上 ⇒ 定义凭空消失。**转发壳文件不能单侧照搬** |
| 10 | 在**与目标模块无 ABI 关系**的子系统上反复折腾 | netfilter 那一整组（13 文件）与 vivo_ts/sensors_class/fpsgo **毫无关系**，最后整组撤掉 |
| 11 | 用"预期值"而不是"实测值"写提交信息 | 曾写"残留 0 次"，实测是 7/5/18。**提交信息必须写实测结果** |
| 12 | 内联 `python -c "…"` | PowerShell 会吃掉引号 ⇒ **一律写 `.py` 文件再跑** |
| 13 | PowerShell 变量名**不区分大小写**（`$a` 覆盖了 `$A` 路径） | 脚本里变量名必须语义化且不冲突 |
| 14 | 提交信息里的 `[` `]` `*` 被当成 pathspec | 用 `git commit -F <文件>` |
| 15 | 以为机型符号表机制（`apply-device-patches`）有用 | 它**只对 `android15-6.6` 生效**，与 vivo 6.1.145 无关 |
| 16 | 被 `(lto=fast;trim)` 里的 `trim` 直接对号入座到 `CONFIG_TRIM_UNUSED_KSYMS` | 三处配置里该项**都是 `not set`** ⇒ **不能靠猜，必须先打印生效配置** |

### 11.3 被硬约束排除的方向（不要碰）

| # | 方向 | 原因 |
|---|---|---|
| 17 | 打开 `CONFIG_MODULE_FORCE_LOAD` | **用户硬约束：不得关闭/绕过版本校验** |
| 18 | 直接改写内核 `__kcrctab` 里的 CRC 值 | 同上（属于绕过） |
| 19 | 修改厂商 `.ko` 的 `__versions` | 同上，且会破坏模块签名/完整性 |

---

## 12. 可能要走的方向

### ★ A. 主线：查清并关掉裁剪机制（当前正在做）

- **依据**：导出符号 15532 vs 8274（差近一倍）；`module_layout` 闭包含 `struct kernel_symbol` 与整个导出机制
- **动作**：等 `c7976a01` 诊断结果 → 按 §5 P1 的三种分支处理
- **成功标志**：`module_layout` 从 `0xcb472513` 变成 `0xe4a1dbce`

### B. 若 A 无效：对比两边 genksyms 的**输入文本**

- 手段：`KBUILD_MODVERSIONS` 的中间产物（`make --save-temps` 或直接对同一头文件跑 `genksyms`）
- 目标：找出 `module_layout` 闭包内哪个类型的**预处理文本**不同
- 障碍：需要能跑完整内核构建环境（CI 上可以做）

### C. 若 A、B 都无效：**以厂商源码为基座**（换基座路线）

- 直接用 `D:\neiheidaima\vivo_src` 构建 → 它的 ABI **天然匹配**厂商模块
- 然后移植 SukiSU / SUSFS
- **已知要补的**：该源码包**编不出** vermagic 里的 `vivo` 标记
  （`arch/arm64/include/asm/vermagic.h`、`module.h`、`setlocalversion` 里都没有）
  ⇒ 说明厂商构建环境另有本地定制 ⇒ 需自行补 `MODULE_ARCH_VERMAGIC "vivo aarch64"`
- 这也是**最接近"自己的内核 + 能开机"**的路线

### ★★ D. 最短路径：KernelSU LKM 模式（可能根本不需要自编译内核）

- **事实**：手机现在就是这条路 —— `kernelsu` 以**可加载模块**形式在跑，
  dmesg 显示 KernelSU 工作正常（`handle_setresuid`、`hook_manager`、`ksud` fd 安装）
- **含义**：**"能开机能用"这个诉求已经达成**，厂商模块全部正常加载、触摸可用
- **待确认**：KernelSU 的授权是否正常（可跑 `adb shell su -c id`，已实测返回 `uid=0`，context `u:r:ksu:s0`）✓
- ⇒ **如果用户接受"够用就行"，这条路线到此就是终点**，自编译内核只是为了"用自己的内核"

### E. 若目标是"必须用自己的内核"

| 子方向 | 说明 | 风险 |
|---|---|---|
| E1 | 厂商源码 + 厂商完整构建配置 + 补 vermagic 定制 → 构建 | 中（源码包可能不完整） |
| E2 | 在 AOSP 树上继续查裁剪/构建形态差异 | 低（已在进行） |
| E3 | 只替换内核的一部分（`vendor_boot` 内的 GKI 模块 / `boot` 分区） | 中 |
| E4 | 向厂商索要**完整构建环境或未公开补丁**（源码包显然缺了生成 `vivo` vermagic 的那部分） | 依赖外部 |

### F. 仍待解的小问题（不影响主线，但别忘）

- **P3**：`vr.ko` / `vklp.ko` 来源（设备上不存在，需用户澄清）
- **P4**：f2fs 源码 28/31 相同、`f2fs_sb_info` 却差 2 倍（8608 vs 4264）——**此矛盾未解**，
  可能与 A 的"驱动内建/模块"同源，建议在 A 的诊断数据出来后一并复核
- **P5**：我们的刷机包**从未实测刷入**（用户此前刷过一版不开机后刷回）；
  现成可刷包：`6.1.145-android14-2025-09-SukiSU-Ultra-AnyKernel3`（run `36439916960` 含 abi_patches / `36439513247` 不含）

---

## 13. 建议的决策顺序

```
① 等 c7976a01 诊断 → 判定 trim 机制
      ├─ 能关掉 → 重出 → 看 module_layout 是否变 0xe4a1dbce
      │     ├─ 变了 → 问题解决，继续出正式刷机包
      │     └─ 没变 → 转 ②
      └─ 与 trim 无关 → 转 ②
② 对比两边 genksyms 输入文本（CI 上做）
      └─ 找到差异 → 复刻 → 重测
③ 都不行 → 换基座（C：用厂商源码构建 + 补 vermagic 定制）
④ 若用户接受"够用就好" → 走 D（KernelSU LKM，手机现状即是答案），全程结束
```

