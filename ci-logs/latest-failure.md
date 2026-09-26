# 最近失败的 CRC Probe 运行 36278613280

## 元信息
```
name=CRC Probe (原厂 config ABI 对齐验证)
sha=4195a579f4fcb77754cdbd4a122202adb18a3ed7
conclusion=failure
created=2026-09-26T23:10:37Z
updated=2026-09-26T23:15:08Z
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
  10 completed/success 失败时上传 bazel 日志（供无 token 的协作者取用）
  11 completed/skipped 收集产物
  12 completed/skipped 上传 Image
  13 completed/skipped 把 Image 挂到公开 Release（便于无 token 获取）
  26 completed/success Post Checkout Repository
  27 completed/success Complete job
```

## 编译错误行（已过滤）
```
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9693196Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4395542Z 26:arch/arm64/configs/gki_defconfig:4:warning: unexpected data: ﻿#
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4397025Z 45:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/mm_types.h:559:1: error: extraneous closing brace ('}')
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4453041Z 1137:make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:118: arch/arm64/kernel/asm-offsets.s] Error 1
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4453925Z 1138:make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:1369: prepare0] Error 2
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4476593Z make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:118: arch/arm64/kernel/asm-offsets.s] Error 1
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4477449Z make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:1369: prepare0] Error 2
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4478507Z make: *** [Makefile:256: __sub-make] Error 2
```

## 失败步骤完整日志
```
probe	构建 Image（自动补齐 module_outs 并重试）	﻿2026-09-26T23:14:14.9688660Z ##[group]Run set -uo pipefail
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9689007Z ^[[36;1mset -uo pipefail^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9689330Z ^[[36;1msed -i 's/check_defconfig//' ./common/build.config.gki^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9689850Z ^[[36;1msed -i '/name = "kernel_aarch64",/a\    check_defconfig = "disabled",' common/BUILD.bazel^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9690279Z ^[[36;1mok=0^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9690482Z ^[[36;1mfor i in 1 2 3 4; do^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9690739Z ^[[36;1m  echo "===== Bazel 构建 第 $i 次 ====="^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9691176Z ^[[36;1m  if tools/bazel build --config=fast --disk_cache=/home/runner/.cache/bazel \^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9691689Z ^[[36;1m       //common:kernel_aarch64/Image > /tmp/bazel.log 2>&1; then^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9692040Z ^[[36;1m    ok=1; break^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9692264Z ^[[36;1m  fi^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9692512Z ^[[36;1m  echo "----- 真实 error 行（最多 40 条）-----"^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9693196Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9693892Z ^[[36;1m  echo "----- tail 40 -----"^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9694167Z ^[[36;1m  tail -40 /tmp/bazel.log || true^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9694693Z ^[[36;1m  python3 "$GITHUB_WORKSPACE/.github/tools/bazel_module_outs.py" /tmp/bazel.log common/BUILD.bazel || break^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9695196Z ^[[36;1mdone^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9695415Z ^[[36;1m[ "$ok" = "1" ] || { echo "构建失败"; exit 1; }^[[0m
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9759065Z shell: /usr/bin/bash -e {0}
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9759329Z env:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9759602Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9759951Z ##[endgroup]
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:14:14.9871091Z ===== Bazel 构建 第 1 次 =====
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4376723Z ----- 真实 error 行（最多 40 条）-----
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4395542Z 26:arch/arm64/configs/gki_defconfig:4:warning: unexpected data: ﻿#
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4397025Z 45:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/mm_types.h:559:1: error: extraneous closing brace ('}')
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4399350Z 305:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4400988Z 328:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4402143Z 351:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4403266Z 374:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4404359Z 397:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:139:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4405717Z 420:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:140:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4406825Z 443:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4408348Z 466:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4410203Z 489:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:144:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4411853Z 512:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4413892Z 535:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4416014Z 558:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4418093Z 581:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4419701Z 604:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:139:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4421299Z 627:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:140:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4422667Z 650:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4423637Z 673:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4424615Z 696:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:144:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4425560Z 719:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4426515Z 742:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4427461Z 765:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4428705Z 788:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4429683Z 811:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:139:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4431103Z 834:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:140:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4432807Z 857:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:8: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4434560Z 880:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:24: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4436354Z 903:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:144:3: note: expanded from macro '_SIG_SET_BINOP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4438411Z 926:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:173:27: note: expanded from macro '_SIG_SET_OP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4440433Z 929:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:185:24: note: expanded from macro '_sig_not'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4442195Z 952:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:173:10: note: expanded from macro '_SIG_SET_OP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4443959Z 975:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:174:20: note: expanded from macro '_SIG_SET_OP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4445742Z 978:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:185:24: note: expanded from macro '_sig_not'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4447485Z 1001:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:174:3: note: expanded from macro '_SIG_SET_OP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4449800Z 1024:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:176:27: note: expanded from macro '_SIG_SET_OP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4450871Z 1027:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:185:24: note: expanded from macro '_sig_not'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4452050Z 1050:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:176:10: note: expanded from macro '_SIG_SET_OP'
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4453041Z 1137:make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:118: arch/arm64/kernel/asm-offsets.s] Error 1
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4453925Z 1138:make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:1369: prepare0] Error 2
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4454433Z ----- tail 40 -----
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4454885Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/fs.h:33:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4455658Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/percpu-rwsem.h:7:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4456445Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/rcuwait.h:6:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4457226Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/sched/signal.h:6:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4458690Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:241:10: warning: array index 1 is past the end of the array (that has type 'unsigned long[1]') [-Warray-bounds]
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4459514Z         case 2: set->sig[1] = 0;
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4459754Z                 ^        ~
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4460329Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/uapi/asm-generic/signal.h:62:2: note: array 'sig' declared here
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4460949Z         unsigned long sig[_NSIG_WORDS];
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4461205Z         ^
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4461676Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/arch/arm64/kernel/asm-offsets.c:10:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4462489Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/arm_sdei.h:8:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4463261Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/acpi/ghes.h:5:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4463990Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/acpi/apei.h:9:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4464724Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/acpi.h:15:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4465470Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/device.h:32:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4466248Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/device/driver.h:21:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4467166Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/module.h:19:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4468195Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/elf.h:6:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4468968Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/arch/arm64/include/asm/elf.h:141:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4469727Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/fs.h:33:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4470500Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/percpu-rwsem.h:7:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4471295Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/rcuwait.h:6:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4472083Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/sched/signal.h:6:
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4473155Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:254:10: warning: array index 1 is past the end of the array (that has type 'unsigned long[1]') [-Warray-bounds]
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4474097Z         case 2: set->sig[1] = -1;
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4474344Z                 ^        ~
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4474908Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/uapi/asm-generic/signal.h:62:2: note: array 'sig' declared here
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4475535Z         unsigned long sig[_NSIG_WORDS];
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4475783Z         ^
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4475973Z 49 warnings and 1 error generated.
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4476593Z make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:118: arch/arm64/kernel/asm-offsets.s] Error 1
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4477449Z make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:1369: prepare0] Error 2
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4478214Z make[1]: *** Waiting for unfinished jobs....
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4478507Z make: *** [Makefile:256: __sub-make] Error 2
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4478830Z Target //common:kernel_aarch64/Image failed to build
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4479243Z Use --verbose_failures to see the command lines of failed build steps.
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4479645Z INFO: Elapsed time: 49.309s, Critical Path: 22.69s
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4480036Z INFO: 276 processes: 265 internal, 1 local, 10 processwrapper-sandbox.
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4480416Z ERROR: Build did NOT complete successfully
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4654864Z 没有解析到缺失模块
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4690779Z 构建失败
probe	构建 Image（自动补齐 module_outs 并重试）	2026-09-26T23:15:04.4704588Z ##[error]Process completed with exit code 1.
```
