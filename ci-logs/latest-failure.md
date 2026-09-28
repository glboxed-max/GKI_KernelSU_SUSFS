# 最近失败的 CRC Probe 运行 36456105445

## 元信息
```
name=CRC Probe (原厂 config ABI 对齐验证)
sha=6c7675349a07a847bc1116ac039037e4d510bdf1
conclusion=failure
created=2026-09-28T17:09:10Z
updated=2026-09-28T17:13:13Z
```

## 各步骤状态
```
JOB probe completed/failure
  1 completed/success Set up job
  2 completed/success Checkout Repository
  3 completed/success 释放磁盘空间
  4 completed/success 安装 repo 工具 + 准备目录
  5 completed/success 同步 AOSP 内核源码（android14-6.1 / 2025-09 = 6.1.145）
  6 completed/success 用原厂 config 覆盖 gki_defconfig
  7 completed/success 关掉 WERROR（-Warray-bounds 会误伤，且不影响 ABI）
  8 completed/success 应用 BTF 反推的 ABI 补丁
  9 completed/failure 构建 Image（自动补齐 module_outs 并重试）
  10 completed/success 打印生效后的 .config 关键项（诊断导出裁剪机制）
  11 completed/success 失败时上传 bazel 日志（供无 token 的协作者取用）
  12 completed/skipped 收集产物
  13 completed/skipped 上传 Image
  14 completed/skipped 把 Image 挂到公开 Release（便于无 token 获取）
  28 completed/success Post Checkout Repository
  29 completed/success Complete job
```

## 编译错误行（已过滤）
```
probe	UNKNOWN STEP	2026-09-28T17:12:41.7291793Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
```

## 失败步骤完整日志
```
probe	UNKNOWN STEP	2026-09-28T17:12:41.3252915Z Finalizing sync state...
probe	UNKNOWN STEP	2026-09-28T17:12:41.3253499Z repo sync has finished successfully.
probe	UNKNOWN STEP	2026-09-28T17:12:41.3463586Z Kernel repository initialization and sync succeeded on attempt 1.
probe	UNKNOWN STEP	2026-09-28T17:12:41.3493306Z ##[end-action id=__self.sync;outcome=success;conclusion=success;duration_ms=82695]
probe	UNKNOWN STEP	2026-09-28T17:12:41.3498850Z ##[start-action display=Capture Kernel Common Commit Metadata;id=__self.__run]
probe	UNKNOWN STEP	2026-09-28T17:12:41.3519628Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-28T17:12:41.3519925Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3520154Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3520554Z ^[[36;1mif [[ ! -d common ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3520959Z ^[[36;1m  echo "WARNING: common folder not found; skipping commit metadata capture."^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3521366Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3521556Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3521743Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3521923Z ^[[36;1mcd common^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3522122Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3522308Z ^[[36;1mif [[ ! -d .git ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3522711Z ^[[36;1m  echo "WARNING: common is not a git checkout; skipping commit metadata capture."^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3523279Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3523470Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3523656Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3523882Z ^[[36;1mCOMMIT_DATE=$(git log -1 --format=%cI)^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3524204Z ^[[36;1mCOMMIT_MSG=$(git log -1 --format=%s)^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3524518Z ^[[36;1mCOMMIT_SHA=$(git rev-parse HEAD)^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3524782Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3525045Z ^[[36;1mecho "KERNEL_SOURCE_COMMIT=$COMMIT_SHA" >> "$GITHUB_ENV"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3525434Z ^[[36;1mecho "Kernel common commit date: $COMMIT_DATE"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3525789Z ^[[36;1mecho "Kernel common commit msg: $COMMIT_MSG"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3526145Z ^[[36;1mecho "Kernel common commit SHA: $COMMIT_SHA"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3588913Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
probe	UNKNOWN STEP	2026-09-28T17:12:41.3589307Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T17:12:41.3725702Z Kernel common commit date: 2026-09-28T15:21:38Z
probe	UNKNOWN STEP	2026-09-28T17:12:41.3726624Z Kernel common commit msg: ANDROID: KVM: arm64: Prevent integer overflow in rb_cpu_fits checks
probe	UNKNOWN STEP	2026-09-28T17:12:41.3728304Z Kernel common commit SHA: 6351cedd9888e533ebb79e476ede8d5a7658faac
probe	UNKNOWN STEP	2026-09-28T17:12:41.3739448Z ##[end-action id=__self.__run;outcome=success;conclusion=success;duration_ms=23]
probe	UNKNOWN STEP	2026-09-28T17:12:41.3807177Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-28T17:12:41.3807493Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3807843Z ^[[36;1mcp "$GITHUB_WORKSPACE/.github/config/vivo_pd2339_a16_defconfig" \^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3808331Z ^[[36;1m   "$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3808900Z ^[[36;1mecho "配置行数: $(grep -c . "$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig")"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.3866295Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T17:12:41.3866547Z env:
probe	UNKNOWN STEP	2026-09-28T17:12:41.3866837Z   KERNEL_SOURCE_COMMIT: 6351cedd9888e533ebb79e476ede8d5a7658faac
probe	UNKNOWN STEP	2026-09-28T17:12:41.3867183Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T17:12:41.3980185Z 配置行数: 8766
probe	UNKNOWN STEP	2026-09-28T17:12:41.4028495Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-28T17:12:41.4028807Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4029174Z ^[[36;1mD="$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4029652Z ^[[36;1msed -i 's/^CONFIG_WERROR=y/# CONFIG_WERROR is not set/' "$D"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4030122Z ^[[36;1mgrep -q '^\(# \)\?CONFIG_WERROR' "$D" || echo '# CONFIG_WERROR is not set' >> "$D"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4030843Z ^[[36;1mgrep -n 'CONFIG_WERROR' "$D"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4088061Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T17:12:41.4088319Z env:
probe	UNKNOWN STEP	2026-09-28T17:12:41.4088594Z   KERNEL_SOURCE_COMMIT: 6351cedd9888e533ebb79e476ede8d5a7658faac
probe	UNKNOWN STEP	2026-09-28T17:12:41.4088940Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T17:12:41.4222549Z 27:# CONFIG_WERROR is not set
probe	UNKNOWN STEP	2026-09-28T17:12:41.4255338Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-28T17:12:41.4255663Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4255950Z ^[[36;1mSRC="$GITHUB_WORKSPACE/.github/patches/abi"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4256292Z ^[[36;1mcd "$GITHUB_WORKSPACE/kernel/common"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4256564Z ^[[36;1mn=0^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4256766Z ^[[36;1mwhile IFS= read -r f; do^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4257017Z ^[[36;1m  rel="${f#$SRC/}"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4257252Z ^[[36;1m  cp "$f" "$rel"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4257478Z ^[[36;1m  echo "[+] 覆盖 $rel"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4257707Z ^[[36;1m  n=$((n+1))^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4257937Z ^[[36;1mdone < <(find "$SRC" -type f)^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4258195Z ^[[36;1mecho "共应用 $n 个头文件补丁"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.4314605Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T17:12:41.4314858Z env:
probe	UNKNOWN STEP	2026-09-28T17:12:41.4315129Z   KERNEL_SOURCE_COMMIT: 6351cedd9888e533ebb79e476ede8d5a7658faac
probe	UNKNOWN STEP	2026-09-28T17:12:41.4315472Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T17:12:41.4426539Z [+] 覆盖 lib/debugobjects.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4442560Z [+] 覆盖 arch/arm64/include/asm/cputype.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4458057Z [+] 覆盖 arch/arm64/include/asm/kvm_arm.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4473957Z [+] 覆盖 arch/arm64/include/asm/tlbflush.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4489505Z [+] 覆盖 arch/arm64/include/asm/kvm_mmu.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4505215Z [+] 覆盖 arch/arm64/gunyah/gunyah_hypercall.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4521348Z [+] 覆盖 arch/arm64/kernel/cpu_errata.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4536890Z [+] 覆盖 arch/arm64/kernel/sys_compat.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4552974Z [+] 覆盖 arch/arm64/kernel/fpsimd.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4568292Z [+] 覆盖 arch/arm64/kernel/head.S
probe	UNKNOWN STEP	2026-09-28T17:12:41.4583989Z [+] 覆盖 arch/arm64/Kconfig
probe	UNKNOWN STEP	2026-09-28T17:12:41.4600176Z [+] 覆盖 arch/arm64/boot/dts/arm/vexpress-v2m-rs1.dtsi
probe	UNKNOWN STEP	2026-09-28T17:12:41.4616118Z [+] 覆盖 arch/arm64/kvm/hyp/vhe/tlb.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4631893Z [+] 覆盖 arch/arm64/kvm/hyp/pgtable.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4650607Z [+] 覆盖 arch/arm64/kvm/hyp/include/hyp/switch.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4666909Z [+] 覆盖 arch/arm64/kvm/hyp/include/nvhe/pkvm.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4685605Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/mem_protect.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4702946Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/tlb.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4719394Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/hyp-main.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4736241Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/trace.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4754716Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/ffa.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4771038Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/pkvm.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4787419Z [+] 覆盖 arch/arm64/kvm/arm.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.4803462Z [+] 覆盖 include/trace/events/mmflags.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4819230Z [+] 覆盖 include/trace/hooks/mm.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4835043Z [+] 覆盖 include/trace/hooks/vmscan.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4851269Z [+] 覆盖 include/uapi/drm/drm_mode.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4867140Z [+] 覆盖 include/uapi/linux/input.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4883661Z [+] 覆盖 include/uapi/linux/android/binder.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4899333Z [+] 覆盖 include/uapi/linux/userfaultfd.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4915807Z [+] 覆盖 include/dt-bindings/input/linux-event-codes.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4931606Z [+] 覆盖 include/dt-bindings/clock/qcom,dispcc-sm8350.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4947329Z [+] 覆盖 include/dt-bindings/clock/qcom,dispcc-sm8150.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4963800Z [+] 覆盖 include/linux/suspend.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4980040Z [+] 覆盖 include/linux/mm.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.4996156Z [+] 覆盖 include/linux/mmzone.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5011936Z [+] 覆盖 include/linux/page-flags.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5027659Z [+] 覆盖 include/linux/cgroup_subsys.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5044797Z [+] 覆盖 include/linux/sched.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5061845Z [+] 覆盖 include/linux/workqueue.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5077913Z [+] 覆盖 include/linux/pageblock-flags.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5094164Z [+] 覆盖 include/linux/lockdep_types.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5109951Z [+] 覆盖 include/linux/fdtable.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5126170Z [+] 覆盖 include/linux/lockdep.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5142470Z [+] 覆盖 include/linux/fs.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5164062Z [+] 覆盖 include/linux/task_io_accounting.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5180116Z [+] 覆盖 include/linux/blk_types.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5195627Z [+] 覆盖 include/linux/file.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5211517Z [+] 覆盖 include/linux/slub_def.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5237279Z [+] 覆盖 include/linux/mm_types.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5253045Z [+] 覆盖 include/linux/local_lock.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5268403Z [+] 覆盖 include/linux/pgsize_migration.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5284121Z [+] 覆盖 include/linux/local_lock_internal.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5299842Z [+] 覆盖 include/linux/blk-mq.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5315884Z [+] 覆盖 include/linux/dma-buf.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5331649Z [+] 覆盖 include/linux/hid.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5347255Z [+] 覆盖 include/linux/gunyah.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5363542Z [+] 覆盖 include/net/sock.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5379250Z [+] 覆盖 include/net/af_unix.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5395285Z [+] 覆盖 kernel/fork.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5413147Z [+] 覆盖 kernel/cgroup/cgroup.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5428871Z [+] 覆盖 kernel/Makefile
probe	UNKNOWN STEP	2026-09-28T17:12:41.5444078Z [+] 覆盖 kernel/.gitignore
probe	UNKNOWN STEP	2026-09-28T17:12:41.5459937Z [+] 覆盖 kernel/sched/sched.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5476642Z [+] 覆盖 kernel/futex/futex.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5493937Z [+] 覆盖 kernel/futex/requeue.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5510010Z [+] 覆盖 kernel/locking/rtmutex_api.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5526754Z [+] 覆盖 kernel/locking/lockdep.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5543589Z [+] 覆盖 kernel/locking/rtmutex.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5559224Z [+] 覆盖 kernel/locking/spinlock.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5575224Z [+] 覆盖 kernel/time/posix-cpu-timers.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5591550Z [+] 覆盖 kernel/signal.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5607345Z [+] 覆盖 kernel/power/process.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5623055Z [+] 覆盖 kernel/power/suspend.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5638522Z [+] 覆盖 kernel/power/power.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5654351Z [+] 覆盖 kernel/power/hibernate.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5670083Z [+] 覆盖 kernel/power/user.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5686147Z [+] 覆盖 kernel/power/main.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5702423Z [+] 覆盖 kernel/exit.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5718583Z [+] 覆盖 android/abi_gki_aarch64_mtk
probe	UNKNOWN STEP	2026-09-28T17:12:41.5734548Z [+] 覆盖 android/abi_gki_aarch64_pixel
probe	UNKNOWN STEP	2026-09-28T17:12:41.5750720Z [+] 覆盖 android/abi_gki_aarch64_vivo
probe	UNKNOWN STEP	2026-09-28T17:12:41.5796519Z [+] 覆盖 android/abi_gki_aarch64.stg
probe	UNKNOWN STEP	2026-09-28T17:12:41.5815032Z [+] 覆盖 android/abi_gki_aarch64_qcom
probe	UNKNOWN STEP	2026-09-28T17:12:41.5831044Z [+] 覆盖 android/abi_gki_aarch64.stg.allowed_breaks
probe	UNKNOWN STEP	2026-09-28T17:12:41.5847843Z [+] 覆盖 scripts/dummy-tools/objcopy
probe	UNKNOWN STEP	2026-09-28T17:12:41.5863749Z [+] 覆盖 scripts/dummy-tools/nm
probe	UNKNOWN STEP	2026-09-28T17:12:41.5879908Z [+] 覆盖 drivers/base/power/wakeup.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5895853Z [+] 覆盖 drivers/md/dm-bow.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5911727Z [+] 覆盖 drivers/hid/wacom_wac.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.5927688Z [+] 覆盖 drivers/hid/hid-vivaldi-common.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5943693Z [+] 覆盖 drivers/hid/hid-primax.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5959577Z [+] 覆盖 drivers/hid/hid-core.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5976343Z [+] 覆盖 drivers/hid/wacom_wac.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.5993007Z [+] 覆盖 drivers/hid/hid-multitouch.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6009197Z [+] 覆盖 drivers/hid/hid-gfrm.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6028375Z [+] 覆盖 drivers/hid/hid-logitech-dj.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6046345Z [+] 覆盖 drivers/hid/wacom_sys.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6066926Z [+] 覆盖 drivers/hid/hid-logitech-hidpp.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6083632Z [+] 覆盖 drivers/hid/hid-magicmouse.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6100656Z [+] 覆盖 drivers/virtio/virtio_input.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6117616Z [+] 覆盖 drivers/usb/gadget/function/f_uvc.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6136035Z [+] 覆盖 drivers/usb/gadget/function/uvc.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.6153208Z [+] 覆盖 drivers/usb/gadget/function/uvc_v4l2.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6169926Z [+] 覆盖 drivers/usb/gadget/function/f_accessory.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6186469Z [+] 覆盖 drivers/usb/gadget/configfs.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6203037Z [+] 覆盖 drivers/staging/greybus/hid.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6219495Z [+] 覆盖 drivers/android/binder_internal.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.6236435Z [+] 覆盖 drivers/android/vendor_hooks.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6254260Z [+] 覆盖 drivers/android/binder.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6270674Z [+] 覆盖 drivers/android/dbitmap.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.6287781Z [+] 覆盖 drivers/virt/gunyah/rsc_mgr.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6304566Z [+] 覆盖 drivers/dma-buf/dma-buf.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6321242Z [+] 覆盖 fs/fuse/backing.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6341015Z [+] 覆盖 fs/fuse/dev.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6359112Z [+] 覆盖 fs/fuse/inode.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6378879Z [+] 覆盖 fs/f2fs/super.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6396831Z [+] 覆盖 fs/f2fs/file.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6414792Z [+] 覆盖 fs/f2fs/node.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6431872Z [+] 覆盖 fs/eventpoll.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6448743Z [+] 覆盖 fs/proc/base.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6465330Z [+] 覆盖 fs/file.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6482105Z [+] 覆盖 fs/exec.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6503998Z [+] 覆盖 mm/huge_memory.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6524918Z [+] 覆盖 mm/page_idle.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6546448Z [+] 覆盖 mm/page_alloc.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6566871Z [+] 覆盖 mm/pgsize_migration.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6587915Z [+] 覆盖 mm/mmap.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6607952Z [+] 覆盖 mm/vmstat.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6628861Z [+] 覆盖 mm/memory.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6649915Z [+] 覆盖 mm/vmscan.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6668186Z [+] 覆盖 mm/filemap.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6694419Z [+] 覆盖 mm/damon/paddr.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6706937Z [+] 覆盖 mm/userfaultfd.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6737724Z [+] 覆盖 mm/rmap.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6771209Z [+] 覆盖 net/tipc/msg.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6784864Z [+] 覆盖 net/ipv4/udp_offload.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6809670Z [+] 覆盖 net/ipv4/ip_output.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6833502Z [+] 覆盖 net/ipv4/esp4.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6858630Z [+] 覆盖 net/bluetooth/rfcomm/sock.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6880988Z [+] 覆盖 net/bluetooth/sco.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6901718Z [+] 覆盖 net/ipv6/exthdrs.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6921705Z [+] 覆盖 net/ipv6/esp6.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6942667Z [+] 覆盖 net/core/gro.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6968486Z [+] 覆盖 net/core/skbuff.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.6996629Z [+] 覆盖 net/nfc/llcp_core.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7022627Z [+] 覆盖 net/nfc/llcp_sock.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7034710Z [+] 覆盖 net/l2tp/l2tp_netlink.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7054816Z [+] 覆盖 net/l2tp/l2tp_ip6.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7074695Z [+] 覆盖 net/l2tp/l2tp_core.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7095604Z [+] 覆盖 net/l2tp/l2tp_eth.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7117296Z [+] 覆盖 net/l2tp/l2tp_debugfs.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7137092Z [+] 覆盖 net/l2tp/l2tp_core.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.7161078Z [+] 覆盖 net/l2tp/l2tp_ip.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7181004Z [+] 覆盖 net/l2tp/l2tp_ppp.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7201373Z [+] 覆盖 net/unix/af_unix.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7223239Z [+] 覆盖 net/unix/garbage.c
probe	UNKNOWN STEP	2026-09-28T17:12:41.7243614Z [+] 覆盖 block/elevator.h
probe	UNKNOWN STEP	2026-09-28T17:12:41.7244008Z 共应用 158 个头文件补丁
probe	UNKNOWN STEP	2026-09-28T17:12:41.7281160Z ##[group]Run set -uo pipefail
probe	UNKNOWN STEP	2026-09-28T17:12:41.7281531Z ^[[36;1mset -uo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7281852Z ^[[36;1msed -i 's/check_defconfig//' ./common/build.config.gki^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7282361Z ^[[36;1msed -i '/name = "kernel_aarch64",/a\    check_defconfig = "disabled",' common/BUILD.bazel^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7282930Z ^[[36;1m# 关掉 KMI 符号表裁剪：Kleaf 依据 kmi_symbol_list 生成 abi_symbollist.raw，并自动开启^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7283466Z ^[[36;1m# CONFIG_TRIM_UNUSED_KSYMS=y + CONFIG_UNUSED_KSYMS_WHITELIST="abi_symbollist.raw"，^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7283918Z ^[[36;1m# 只导出清单内符号（实测 8274 个）。原厂内核完全不裁剪（两项都没设），导出 15532 个。^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7284367Z ^[[36;1m# 为对齐原厂形态，去掉 kmi_symbol_list / additional_kmi_symbol_lists / protected_exports_list。^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7284834Z ^[[36;1mecho "===== 关闭 KMI 裁剪（对齐原厂不裁剪形态）====="^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7285374Z ^[[36;1mgrep -n -E '"kmi_symbol_list"|"protected_exports_list"|"additional_kmi_symbol_lists"' common/BUILD.bazel || true^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7286019Z ^[[36;1msed -i -E '/^[[:space:]]*"kmi_symbol_list":/d' common/BUILD.bazel^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7286486Z ^[[36;1msed -i -E '/^[[:space:]]*"additional_kmi_symbol_lists":/d' common/BUILD.bazel^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7286962Z ^[[36;1msed -i -E '/^[[:space:]]*"protected_exports_list":/d' common/BUILD.bazel^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7287339Z ^[[36;1mecho "----- 处理后 -----"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7287855Z ^[[36;1mgrep -n -E '"kmi_symbol_list"|"protected_exports_list"|"additional_kmi_symbol_lists"' common/BUILD.bazel || echo "（已全部移除）"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7288448Z ^[[36;1mok=0^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7288680Z ^[[36;1mfor i in 1 2 3 4; do^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7288932Z ^[[36;1m  echo "===== Bazel 构建 第 $i 次 ====="^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7289352Z ^[[36;1m  if tools/bazel build --config=fast --disk_cache=/home/runner/.cache/bazel \^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7290015Z ^[[36;1m       //common:kernel_aarch64/Image > /tmp/bazel.log 2>&1; then^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7290662Z ^[[36;1m    ok=1; break^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7290901Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7291125Z ^[[36;1m  echo "----- 真实 error 行（最多 40 条）-----"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7291793Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7292436Z ^[[36;1m  echo "----- tail 40 -----"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7292710Z ^[[36;1m  tail -40 /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7293232Z ^[[36;1m  python3 "$GITHUB_WORKSPACE/.github/tools/bazel_module_outs.py" /tmp/bazel.log common/BUILD.bazel || break^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7293735Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7293950Z ^[[36;1m[ "$ok" = "1" ] || { echo "构建失败"; exit 1; }^[[0m
probe	UNKNOWN STEP	2026-09-28T17:12:41.7358091Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T17:12:41.7358365Z env:
probe	UNKNOWN STEP	2026-09-28T17:12:41.7358645Z   KERNEL_SOURCE_COMMIT: 6351cedd9888e533ebb79e476ede8d5a7658faac
probe	UNKNOWN STEP	2026-09-28T17:12:41.7359137Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T17:12:41.7470807Z ===== 关闭 KMI 裁剪（对齐原厂不裁剪形态）=====
probe	UNKNOWN STEP	2026-09-28T17:12:41.7484279Z 143:        "kmi_symbol_list": "android/abi_gki_aarch64",
probe	UNKNOWN STEP	2026-09-28T17:12:41.7485094Z 146:        "additional_kmi_symbol_lists": [":aarch64_additional_kmi_symbol_lists"],
probe	UNKNOWN STEP	2026-09-28T17:12:41.7485762Z 147:        "protected_exports_list": "android/abi_gki_protected_exports_aarch64",
probe	UNKNOWN STEP	2026-09-28T17:12:41.7486214Z 154:        "kmi_symbol_list": "android/abi_gki_aarch64",
probe	UNKNOWN STEP	2026-09-28T17:12:41.7486637Z 157:        "additional_kmi_symbol_lists": [":aarch64_additional_kmi_symbol_lists"],
probe	UNKNOWN STEP	2026-09-28T17:12:41.7487139Z 158:        "protected_exports_list": "android/abi_gki_protected_exports_aarch64",
probe	UNKNOWN STEP	2026-09-28T17:12:41.7487591Z 165:        "kmi_symbol_list": "android/abi_gki_aarch64",
probe	UNKNOWN STEP	2026-09-28T17:12:41.7488006Z 168:        "additional_kmi_symbol_lists": [":aarch64_additional_kmi_symbol_lists"],
probe	UNKNOWN STEP	2026-09-28T17:12:41.7488508Z 169:        "protected_exports_list": "android/abi_gki_protected_exports_aarch64",
probe	UNKNOWN STEP	2026-09-28T17:12:41.7489211Z 181:        "protected_exports_list": "android/abi_gki_protected_exports_x86_64",
probe	UNKNOWN STEP	2026-09-28T17:12:41.7489698Z 188:        "protected_exports_list": "android/abi_gki_protected_exports_x86_64",
probe	UNKNOWN STEP	2026-09-28T17:12:41.7542418Z ----- 处理后 -----
probe	UNKNOWN STEP	2026-09-28T17:12:41.7556300Z （已全部移除）
probe	UNKNOWN STEP	2026-09-28T17:12:41.7556952Z ===== Bazel 构建 第 1 次 =====
probe	UNKNOWN STEP	2026-09-28T17:13:08.5552129Z ----- 真实 error 行（最多 40 条）-----
probe	UNKNOWN STEP	2026-09-28T17:13:08.5559622Z ----- tail 40 -----
probe	UNKNOWN STEP	2026-09-28T17:13:08.5575745Z Extracting Bazel installation...
probe	UNKNOWN STEP	2026-09-28T17:13:08.5576333Z Starting local Bazel server and connecting to it...
probe	UNKNOWN STEP	2026-09-28T17:13:08.5577052Z INFO: Invocation ID: 0e8c137f-335e-43fe-8431-356a6af6d390
probe	UNKNOWN STEP	2026-09-28T17:13:08.5577599Z Loading: 
probe	UNKNOWN STEP	2026-09-28T17:13:08.5577912Z Loading: 
probe	UNKNOWN STEP	2026-09-28T17:13:08.5578320Z Loading: 1 packages loaded
probe	UNKNOWN STEP	2026-09-28T17:13:08.5578750Z Loading: 1 packages loaded
probe	UNKNOWN STEP	2026-09-28T17:13:08.5579215Z     currently loading: common
probe	UNKNOWN STEP	2026-09-28T17:13:08.5579815Z Analyzing: target //common:kernel_aarch64/Image (2 packages loaded)
probe	UNKNOWN STEP	2026-09-28T17:13:08.5580994Z Analyzing: target //common:kernel_aarch64/Image (2 packages loaded, 0 targets configured)
probe	UNKNOWN STEP	2026-09-28T17:13:08.5582074Z Analyzing: target //common:kernel_aarch64/Image (46 packages loaded, 5152 targets configured)
probe	UNKNOWN STEP	2026-09-28T17:13:08.5583153Z Analyzing: target //common:kernel_aarch64/Image (53 packages loaded, 78920 targets configured)
probe	UNKNOWN STEP	2026-09-28T17:13:08.5584245Z INFO: Analyzed target //common:kernel_aarch64/Image (53 packages loaded, 93443 targets configured).
probe	UNKNOWN STEP	2026-09-28T17:13:08.5585054Z  checking cached actions
probe	UNKNOWN STEP	2026-09-28T17:13:08.5585440Z INFO: Found 1 target...
probe	UNKNOWN STEP	2026-09-28T17:13:08.5585941Z [0 / 7] [Prepa] BazelWorkspaceStatusAction stable-status.txt
probe	UNKNOWN STEP	2026-09-28T17:13:08.5586864Z [120 / 263] [Prepa] Writing repo mapping manifest for //build/kernel/kleaf:search_and_cp_output [for tool]
probe	UNKNOWN STEP	2026-09-28T17:13:08.5587985Z [132 / 270] [Prepa] Creating symlinks to in-tree tools @//build/kernel:hermetic-tools/zipinfo
probe	UNKNOWN STEP	2026-09-28T17:13:08.5590157Z [250 / 278] [Prepa] action 'SolibSymlink _solib_x86_64/_U_S_Sprebuilts_Skernel-build-tools_Clinux_Ux86_Uimported_Ulibs_Ulinux-x86_Slib64_Slibcrypto.so___Uprebuilts_Skernel-build-tools_Slinux-x86_Slib64/libcrypto.so'
probe	UNKNOWN STEP	2026-09-28T17:13:08.5593233Z [267 / 278] Creating wrapper for rsync: @//build/kernel:hermetic-tools; 0s remote-cache, processwrapper-sandbox ... (2 actions running)
probe	UNKNOWN STEP	2026-09-28T17:13:08.5594686Z [268 / 278] Creating wrapper for rsync: @//build/kernel:hermetic-tools; 1s remote-cache, processwrapper-sandbox
probe	UNKNOWN STEP	2026-09-28T17:13:08.5595852Z [270 / 278] [Prepa] Creating build environment (lto=fast;trim) @//common:kernel_aarch64_env
probe	UNKNOWN STEP	2026-09-28T17:13:08.5597252Z [271 / 278] Creating abi_symbollist and report @//common:kernel_aarch64_kmi_symbol_list; 0s remote-cache, processwrapper-sandbox ... (2 actions running)
probe	UNKNOWN STEP	2026-09-28T17:13:08.5598896Z [273 / 278] Creating abi_symbollist.raw @//common:kernel_aarch64_raw_kmi_symbol_list; 0s remote-cache, processwrapper-sandbox
probe	UNKNOWN STEP	2026-09-28T17:13:08.5602092Z ERROR: /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/BUILD.bazel:139:22: Creating abi_symbollist.raw @//common:kernel_aarch64_raw_kmi_symbol_list failed: (Exit 1): bash failed: error executing RawKmiSymbolList command (from target //common:kernel_aarch64_raw_kmi_symbol_list) /bin/bash -c ... (remaining 1 argument skipped)
probe	UNKNOWN STEP	2026-09-28T17:13:08.5604306Z 
probe	UNKNOWN STEP	2026-09-28T17:13:08.5604869Z Use --sandbox_debug to see verbose messages from the sandbox and retain the sandbox build root for debugging
probe	UNKNOWN STEP	2026-09-28T17:13:08.5605772Z Traceback (most recent call last):
probe	UNKNOWN STEP	2026-09-28T17:13:08.5608179Z   File "/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/out/bazel/output_user_root/f7dc5b3f01f576e02ee1db74f5035252/sandbox/processwrapper-sandbox/10/execroot/__main__/bazel-out/k8-opt-exec-ST-10ba2ffbdcc7/bin/build/kernel/abi_flatten_symbol_list.runfiles/__main__/build/kernel/abi/flatten_symbol_list.py", line 38, in <module>
probe	UNKNOWN STEP	2026-09-28T17:13:08.5610813Z     sys.exit(main())
probe	UNKNOWN STEP	2026-09-28T17:13:08.5613371Z   File "/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/out/bazel/output_user_root/f7dc5b3f01f576e02ee1db74f5035252/sandbox/processwrapper-sandbox/10/execroot/__main__/bazel-out/k8-opt-exec-ST-10ba2ffbdcc7/bin/build/kernel/abi_flatten_symbol_list.runfiles/__main__/build/kernel/abi/flatten_symbol_list.py", line 29, in main
probe	UNKNOWN STEP	2026-09-28T17:13:08.5615844Z     sl.read_file(sys.stdin)
probe	UNKNOWN STEP	2026-09-28T17:13:08.5616404Z   File "internal/stdlib/configparser.py", line 720, in read_file
probe	UNKNOWN STEP	2026-09-28T17:13:08.5617135Z   File "internal/stdlib/configparser.py", line 1062, in _read
probe	UNKNOWN STEP	2026-09-28T17:13:08.5617854Z AttributeError: 'NoneType' object has no attribute 'append'
probe	UNKNOWN STEP	2026-09-28T17:13:08.5618512Z Target //common:kernel_aarch64/Image failed to build
probe	UNKNOWN STEP	2026-09-28T17:13:08.5619220Z Use --verbose_failures to see the command lines of failed build steps.
probe	UNKNOWN STEP	2026-09-28T17:13:08.5619920Z INFO: Elapsed time: 26.672s, Critical Path: 5.04s
probe	UNKNOWN STEP	2026-09-28T17:13:08.5620990Z INFO: 274 processes: 265 internal, 9 processwrapper-sandbox.
probe	UNKNOWN STEP	2026-09-28T17:13:08.5650917Z ERROR: Build did NOT complete successfully
probe	UNKNOWN STEP	2026-09-28T17:13:08.5765641Z 没有解析到缺失模块
probe	UNKNOWN STEP	2026-09-28T17:13:08.5798553Z 构建失败
probe	UNKNOWN STEP	2026-09-28T17:13:08.5811206Z ##[error]Process completed with exit code 1.
probe	UNKNOWN STEP	2026-09-28T17:13:08.5860920Z ##[group]Run set -uo pipefail
probe	UNKNOWN STEP	2026-09-28T17:13:08.5861276Z ^[[36;1mset -uo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5861508Z ^[[36;1mCFG=""^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5861932Z ^[[36;1mfor c in bazel-bin/common/kernel_aarch64/.config common/bazel-bin/common/kernel_aarch64/.config; do^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5862431Z ^[[36;1m  [ -f "$c" ] && CFG="$c" && break^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5862690Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5862902Z ^[[36;1mif [ -z "$CFG" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5863177Z ^[[36;1m  echo "=== 找不到生效 .config，全树查找 ==="^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5863616Z ^[[36;1m  find . -maxdepth 7 -name '.config' -path '*kernel_aarch64*' 2>/dev/null | head^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5864214Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5864408Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5864601Z ^[[36;1mecho "=== 生效配置: $CFG ==="^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5864969Z ^[[36;1mecho "  总行数: $(grep -c . "$CFG")    CONFIG_* 行数: $(grep -c '^CONFIG_' "$CFG")"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5865453Z ^[[36;1mecho "  （对照：设备实际 config 为 9246 行 / 3028 项）"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5865754Z ^[[36;1mecho "=== 裁剪 / 导出 / LTO 相关 ==="^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5866432Z ^[[36;1mgrep -E '^#? ?CONFIG_(TRIM_UNUSED_KSYMS|UNUSED_KSYMS_WHITELIST|MODVERSIONS|MODULE_SIG|LTO_CLANG|LTO_CLANG_THIN|LTO_CLANG_FULL|LTO_NONE)' "$CFG" || echo "  （以上各项均未出现）"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5867131Z ^[[36;1mecho "=== 驱动内建/模块统计 ==="^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5867465Z ^[[36;1mecho "  =y : $(grep -c '=y$' "$CFG")    =m : $(grep -c '=m$' "$CFG")"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5867869Z ^[[36;1mecho "=== System.map 里的导出符号条目数（直接印证 __ksymtab 数）==="^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5868427Z ^[[36;1mfor m in bazel-bin/common/kernel_aarch64/System.map common/bazel-bin/common/kernel_aarch64/System.map; do^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5868947Z ^[[36;1m  if [ -f "$m" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5869186Z ^[[36;1m    echo "  $m"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5869467Z ^[[36;1m    echo "    __ksymtab_ 条目: $(grep -c '__ksymtab_' "$m")"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5869847Z ^[[36;1m    echo "    __kcrctab_ 条目: $(grep -c '__kcrctab_' "$m")"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5870564Z ^[[36;1m    echo "    module_layout : $(grep -m1 ' __ksymtab_module_layout$' "$m" || echo '(未找到)')"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5870985Z ^[[36;1m    break^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5871191Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5871385Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5871612Z ^[[36;1mecho "=== bazel 配置串（看 lto=...;trim 是否存在）==="^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5872056Z ^[[36;1mgrep -m 3 -E 'Building kernel \(' /tmp/bazel.log 2>/dev/null || echo "  （日志中未出现）"^[[0m
probe	UNKNOWN STEP	2026-09-28T17:13:08.5974094Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T17:13:08.5974338Z env:
probe	UNKNOWN STEP	2026-09-28T17:13:08.5974617Z   KERNEL_SOURCE_COMMIT: 6351cedd9888e533ebb79e476ede8d5a7658faac
probe	UNKNOWN STEP	2026-09-28T17:13:08.5974961Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T17:13:08.6056910Z === 找不到生效 .config，全树查找 ===
probe	UNKNOWN STEP	2026-09-28T17:13:08.7537269Z ##[group]Run actions/upload-artifact@v4
probe	UNKNOWN STEP	2026-09-28T17:13:08.7537568Z with:
probe	UNKNOWN STEP	2026-09-28T17:13:08.7537753Z   name: bazel-log
probe	UNKNOWN STEP	2026-09-28T17:13:08.7537961Z   path: /tmp/bazel.log
probe	UNKNOWN STEP	2026-09-28T17:13:08.7538186Z   if-no-files-found: ignore
probe	UNKNOWN STEP	2026-09-28T17:13:08.7538418Z   compression-level: 6
probe	UNKNOWN STEP	2026-09-28T17:13:08.7538623Z   overwrite: false
probe	UNKNOWN STEP	2026-09-28T17:13:08.7538829Z   include-hidden-files: false
probe	UNKNOWN STEP	2026-09-28T17:13:08.7539050Z env:
probe	UNKNOWN STEP	2026-09-28T17:13:08.7539303Z   KERNEL_SOURCE_COMMIT: 6351cedd9888e533ebb79e476ede8d5a7658faac
probe	UNKNOWN STEP	2026-09-28T17:13:08.7539636Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T17:13:08.9248000Z (node:3953) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
probe	UNKNOWN STEP	2026-09-28T17:13:08.9249474Z (Use `node --trace-deprecation ...` to show where the warning was created)
probe	UNKNOWN STEP	2026-09-28T17:13:08.9318047Z With the provided path, there will be 1 file uploaded
probe	UNKNOWN STEP	2026-09-28T17:13:08.9340971Z Artifact name is valid!
probe	UNKNOWN STEP	2026-09-28T17:13:08.9341911Z Root directory input is valid!
probe	UNKNOWN STEP	2026-09-28T17:13:09.2902799Z Beginning upload of artifact content to blob storage
probe	UNKNOWN STEP	2026-09-28T17:13:09.3128848Z (node:3953) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
probe	UNKNOWN STEP	2026-09-28T17:13:09.5222092Z Uploaded bytes 1396
probe	UNKNOWN STEP	2026-09-28T17:13:09.5828869Z Finished uploading artifact content to blob storage!
probe	UNKNOWN STEP	2026-09-28T17:13:09.5830667Z SHA256 digest of uploaded artifact zip is b9c021a53d6cbba9617e3e54799eaf86f30b3272e1c2d67e8bbd614046dd9d7a
probe	UNKNOWN STEP	2026-09-28T17:13:09.5832666Z Finalizing artifact upload
probe	UNKNOWN STEP	2026-09-28T17:13:09.8563722Z Artifact bazel-log.zip successfully finalized. Artifact ID 10985389021
probe	UNKNOWN STEP	2026-09-28T17:13:09.8565125Z Artifact bazel-log has been successfully uploaded! Final size is 1396 bytes. Artifact ID is 10985389021
probe	UNKNOWN STEP	2026-09-28T17:13:09.8572172Z Artifact download URL: https://github.com/glboxed-max/GKI_KernelSU_SUSFS/actions/runs/36456105445/artifacts/10985389021
probe	UNKNOWN STEP	2026-09-28T17:13:09.8758593Z Post job cleanup.
probe	UNKNOWN STEP	2026-09-28T17:13:09.9639298Z [command]/usr/bin/git version
probe	UNKNOWN STEP	2026-09-28T17:13:09.9685078Z git version 2.55.0
probe	UNKNOWN STEP	2026-09-28T17:13:09.9723653Z Temporarily overriding HOME='/home/runner/work/_temp/31fa5047-0775-4885-b266-e80ccaf30c2c' before making global git config changes
probe	UNKNOWN STEP	2026-09-28T17:13:09.9724979Z Adding repository directory to the temporary git global config as a safe directory
probe	UNKNOWN STEP	2026-09-28T17:13:09.9729018Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS
probe	UNKNOWN STEP	2026-09-28T17:13:09.9768281Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
probe	UNKNOWN STEP	2026-09-28T17:13:09.9804478Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
probe	UNKNOWN STEP	2026-09-28T17:13:10.0079349Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
probe	UNKNOWN STEP	2026-09-28T17:13:10.0097662Z http.https://github.com/.extraheader
probe	UNKNOWN STEP	2026-09-28T17:13:10.0111343Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
probe	UNKNOWN STEP	2026-09-28T17:13:10.0147034Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
probe	UNKNOWN STEP	2026-09-28T17:13:10.0403593Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
probe	UNKNOWN STEP	2026-09-28T17:13:10.0445248Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
probe	UNKNOWN STEP	2026-09-28T17:13:10.0872574Z Cleaning up orphan processes
probe	UNKNOWN STEP	2026-09-28T17:13:10.1296081Z Terminate orphan process: pid (3367) (java.lang=ALL-UNNAMED)
probe	UNKNOWN STEP	2026-09-28T17:13:10.1315115Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```
