# 最近失败的 CRC Probe 运行 36405188758

## 元信息
```
name=CRC Probe (原厂 config ABI 对齐验证)
sha=fdc6c9a2a44f401f4ba44e1aeb8d928733e95f2a
conclusion=failure
created=2026-09-28T09:42:23Z
updated=2026-09-28T09:56:03Z
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
probe	UNKNOWN STEP	2026-09-28T09:46:08.6038087Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-28T09:56:00.4577667Z 25:arch/arm64/configs/gki_defconfig:4:warning: unexpected data: ﻿#
probe	UNKNOWN STEP	2026-09-28T09:56:00.4579017Z 42:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:39:14: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4580371Z 48:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:40:7: error: use of undeclared identifier 'XT_CONNMARK_SET'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4581803Z 51:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:42:29: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4583084Z 57:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:42:45: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4584226Z 63:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:43:11: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4585604Z 69:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:43:26: error: use of undeclared identifier 'D_SHIFT_RIGHT'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4587037Z 72:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:44:20: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4589026Z 78:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:46:20: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4590366Z 84:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:53:7: error: use of undeclared identifier 'XT_CONNMARK_SAVE'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4591807Z 87:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:54:37: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4593504Z 93:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:55:11: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4594894Z 99:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:55:26: error: use of undeclared identifier 'D_SHIFT_RIGHT'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4596230Z 102:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:56:27: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4597626Z 108:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:58:27: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4599102Z 114:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:60:41: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4600423Z 120:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:67:7: error: use of undeclared identifier 'XT_CONNMARK_RESTORE'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4601928Z 123:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:68:47: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4603297Z 129:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:69:11: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4604580Z 135:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:69:26: error: use of undeclared identifier 'D_SHIFT_RIGHT'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4605453Z 138:fatal error: too many errors emitted, stopping now [-ferror-limit=]
probe	UNKNOWN STEP	2026-09-28T09:56:00.4606306Z 140:make[4]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:250: net/netfilter/xt_connmark.o] Error 1
probe	UNKNOWN STEP	2026-09-28T09:56:00.4607677Z 141:make[3]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: net/netfilter] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4608799Z 143:make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: net] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4609838Z 145:make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:2068: .] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4610687Z 146:make: *** [Makefile:256: __sub-make] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4612990Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:60:41: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4618385Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:67:7: error: use of undeclared identifier 'XT_CONNMARK_RESTORE'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4620761Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:68:47: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4642271Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:69:11: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4646616Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:69:26: error: use of undeclared identifier 'D_SHIFT_RIGHT'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4648255Z fatal error: too many errors emitted, stopping now [-ferror-limit=]
probe	UNKNOWN STEP	2026-09-28T09:56:00.4649464Z make[4]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:250: net/netfilter/xt_connmark.o] Error 1
probe	UNKNOWN STEP	2026-09-28T09:56:00.4650575Z make[3]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: net/netfilter] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4652327Z make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: net] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4653634Z make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:2068: .] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4654231Z make: *** [Makefile:256: __sub-make] Error 2
```

## 失败步骤完整日志
```
probe	UNKNOWN STEP	2026-09-28T09:44:42.8244718Z ^[[36;1m  else^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8244874Z ^[[36;1m    rc=$?^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8245114Z ^[[36;1m    echo "repo init or branch preflight failed with exit code $rc."^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8245390Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8245543Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8245727Z ^[[36;1m  if [ $attempt -lt $MAX_RETRIES ]; then^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8246052Z ^[[36;1m    echo "Cleaning workspace and retrying after ${RETRY_DELAY_SHORT}s..."^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8246366Z ^[[36;1m    clean_workspace || true^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8246584Z ^[[36;1m    sleep $RETRY_DELAY_SHORT^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8246787Z ^[[36;1m  else^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8246991Z ^[[36;1m    echo "All $MAX_RETRIES attempts failed." >&2^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8247229Z ^[[36;1m    exit $rc^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8247395Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8247563Z ^[[36;1m  attempt=$((attempt+1))^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8247762Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-28T09:44:42.8308829Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
probe	UNKNOWN STEP	2026-09-28T09:44:42.8309134Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T09:44:42.8413890Z Attempt 1/3: initialize and sync kernel repository (depth=1, sync timeout 15m)...
probe	UNKNOWN STEP	2026-09-28T09:44:42.8428945Z /dev/root       145G   37G  108G  26% /
probe	UNKNOWN STEP	2026-09-28T09:44:44.8656572Z 
probe	UNKNOWN STEP	2026-09-28T09:44:44.8657186Z repo has been initialized in /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel
probe	UNKNOWN STEP	2026-09-28T09:46:06.4159841Z Finalizing sync state...
probe	UNKNOWN STEP	2026-09-28T09:46:06.4160292Z repo sync has finished successfully.
probe	UNKNOWN STEP	2026-09-28T09:46:06.4384397Z Kernel repository initialization and sync succeeded on attempt 1.
probe	UNKNOWN STEP	2026-09-28T09:46:06.4410541Z ##[end-action id=__self.sync;outcome=success;conclusion=success;duration_ms=83623]
probe	UNKNOWN STEP	2026-09-28T09:46:06.4415402Z ##[start-action display=Capture Kernel Common Commit Metadata;id=__self.__run]
probe	UNKNOWN STEP	2026-09-28T09:46:06.4432796Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-28T09:46:06.4433053Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4433239Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4433403Z ^[[36;1mif [[ ! -d common ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4433716Z ^[[36;1m  echo "WARNING: common folder not found; skipping commit metadata capture."^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4434037Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4434203Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4434346Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4434490Z ^[[36;1mcd common^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4434646Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4434796Z ^[[36;1mif [[ ! -d .git ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4435130Z ^[[36;1m  echo "WARNING: common is not a git checkout; skipping commit metadata capture."^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4435601Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4435755Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4435901Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4436076Z ^[[36;1mCOMMIT_DATE=$(git log -1 --format=%cI)^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4436322Z ^[[36;1mCOMMIT_MSG=$(git log -1 --format=%s)^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4436558Z ^[[36;1mCOMMIT_SHA=$(git rev-parse HEAD)^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4436767Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4436976Z ^[[36;1mecho "KERNEL_SOURCE_COMMIT=$COMMIT_SHA" >> "$GITHUB_ENV"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4437283Z ^[[36;1mecho "Kernel common commit date: $COMMIT_DATE"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4437556Z ^[[36;1mecho "Kernel common commit msg: $COMMIT_MSG"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4437835Z ^[[36;1mecho "Kernel common commit SHA: $COMMIT_SHA"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4492678Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
probe	UNKNOWN STEP	2026-09-28T09:46:06.4492985Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T09:46:06.4612680Z Kernel common commit date: 2026-09-25T22:24:02Z
probe	UNKNOWN STEP	2026-09-28T09:46:06.4613571Z Kernel common commit msg: UPSTREAM: Bluetooth: ISO: fix UAF in iso_recv_frame
probe	UNKNOWN STEP	2026-09-28T09:46:06.4614168Z Kernel common commit SHA: 489c6def208fb01674c02d18df10bfe0bbaa4d66
probe	UNKNOWN STEP	2026-09-28T09:46:06.4624314Z ##[end-action id=__self.__run;outcome=success;conclusion=success;duration_ms=20]
probe	UNKNOWN STEP	2026-09-28T09:46:06.4680792Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-28T09:46:06.4681047Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4681330Z ^[[36;1mcp "$GITHUB_WORKSPACE/.github/config/vivo_pd2339_a16_defconfig" \^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4682012Z ^[[36;1m   "$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4682472Z ^[[36;1mecho "配置行数: $(grep -c . "$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig")"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4731634Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T09:46:06.4731876Z env:
probe	UNKNOWN STEP	2026-09-28T09:46:06.4732110Z   KERNEL_SOURCE_COMMIT: 489c6def208fb01674c02d18df10bfe0bbaa4d66
probe	UNKNOWN STEP	2026-09-28T09:46:06.4732388Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T09:46:06.4876684Z 配置行数: 8766
probe	UNKNOWN STEP	2026-09-28T09:46:06.4918999Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-28T09:46:06.4919250Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4919542Z ^[[36;1mD="$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4919924Z ^[[36;1msed -i 's/^CONFIG_WERROR=y/# CONFIG_WERROR is not set/' "$D"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4920303Z ^[[36;1mgrep -q '^\(# \)\?CONFIG_WERROR' "$D" || echo '# CONFIG_WERROR is not set' >> "$D"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4920625Z ^[[36;1mgrep -n 'CONFIG_WERROR' "$D"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.4972656Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T09:46:06.4972870Z env:
probe	UNKNOWN STEP	2026-09-28T09:46:06.4973096Z   KERNEL_SOURCE_COMMIT: 489c6def208fb01674c02d18df10bfe0bbaa4d66
probe	UNKNOWN STEP	2026-09-28T09:46:06.4973371Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T09:46:06.5159160Z 27:# CONFIG_WERROR is not set
probe	UNKNOWN STEP	2026-09-28T09:46:06.5185543Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-28T09:46:06.5185788Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5186012Z ^[[36;1mSRC="$GITHUB_WORKSPACE/.github/patches/abi"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5186293Z ^[[36;1mcd "$GITHUB_WORKSPACE/kernel/common"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5186512Z ^[[36;1mn=0^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5186679Z ^[[36;1mwhile IFS= read -r f; do^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5186886Z ^[[36;1m  rel="${f#$SRC/}"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5187073Z ^[[36;1m  cp "$f" "$rel"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5187258Z ^[[36;1m  echo "[+] 覆盖 $rel"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5187446Z ^[[36;1m  n=$((n+1))^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5187635Z ^[[36;1mdone < <(find "$SRC" -type f)^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5187841Z ^[[36;1mecho "共应用 $n 个头文件补丁"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:06.5238978Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T09:46:06.5239271Z env:
probe	UNKNOWN STEP	2026-09-28T09:46:06.5239601Z   KERNEL_SOURCE_COMMIT: 489c6def208fb01674c02d18df10bfe0bbaa4d66
probe	UNKNOWN STEP	2026-09-28T09:46:06.5240014Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T09:46:06.5545339Z [+] 覆盖 lib/debugobjects.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.5936458Z [+] 覆盖 arch/arm64/include/asm/cputype.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.5953278Z [+] 覆盖 arch/arm64/include/asm/kvm_arm.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.6027536Z [+] 覆盖 arch/arm64/include/asm/tlbflush.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.6043934Z [+] 覆盖 arch/arm64/include/asm/kvm_mmu.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.6232042Z [+] 覆盖 arch/arm64/gunyah/gunyah_hypercall.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.6342417Z [+] 覆盖 arch/arm64/kernel/cpu_errata.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.6349034Z [+] 覆盖 arch/arm64/kernel/sys_compat.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.6363459Z [+] 覆盖 arch/arm64/kernel/fpsimd.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.6431932Z [+] 覆盖 arch/arm64/kernel/head.S
probe	UNKNOWN STEP	2026-09-28T09:46:06.6446272Z [+] 覆盖 arch/arm64/Kconfig
probe	UNKNOWN STEP	2026-09-28T09:46:06.7133041Z [+] 覆盖 arch/arm64/boot/dts/arm/vexpress-v2m-rs1.dtsi
probe	UNKNOWN STEP	2026-09-28T09:46:06.7232020Z [+] 覆盖 arch/arm64/kvm/hyp/vhe/tlb.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.7435726Z [+] 覆盖 arch/arm64/kvm/hyp/pgtable.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.7533144Z [+] 覆盖 arch/arm64/kvm/hyp/include/hyp/switch.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.7547059Z [+] 覆盖 arch/arm64/kvm/hyp/include/nvhe/pkvm.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.7629362Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/mem_protect.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.7648331Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/tlb.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.7742743Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/hyp-main.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.8509159Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/trace.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.8537414Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/ffa.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.8833412Z [+] 覆盖 arch/arm64/kvm/hyp/nvhe/pkvm.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.8949686Z [+] 覆盖 arch/arm64/kvm/arm.c
probe	UNKNOWN STEP	2026-09-28T09:46:06.8952491Z [+] 覆盖 include/trace/events/mmflags.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.9029105Z [+] 覆盖 include/trace/hooks/mm.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.9050786Z [+] 覆盖 include/trace/hooks/vmscan.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.9125084Z [+] 覆盖 include/uapi/drm/drm_mode.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.9650499Z [+] 覆盖 include/uapi/linux/input.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.9832097Z [+] 覆盖 include/uapi/linux/netfilter_ipv6/ip6t_HL.h
probe	UNKNOWN STEP	2026-09-28T09:46:06.9857191Z [+] 覆盖 include/uapi/linux/android/binder.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.0125845Z [+] 覆盖 include/uapi/linux/netfilter_ipv4/ipt_ecn.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.0144376Z [+] 覆盖 include/uapi/linux/netfilter_ipv4/ipt_ttl.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.0226843Z [+] 覆盖 include/uapi/linux/userfaultfd.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.0242313Z [+] 覆盖 include/uapi/linux/netfilter/xt_TCPMSS.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.1437438Z [+] 覆盖 include/uapi/linux/netfilter/xt_connmark.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.1626323Z [+] 覆盖 include/uapi/linux/netfilter/xt_RATEEST.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.1719947Z [+] 覆盖 include/uapi/linux/netfilter/xt_MARK.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.1735203Z [+] 覆盖 include/uapi/linux/netfilter/xt_DSCP.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.1749194Z [+] 覆盖 include/dt-bindings/input/linux-event-codes.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.1822164Z [+] 覆盖 include/dt-bindings/clock/qcom,dispcc-sm8350.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.1838705Z [+] 覆盖 include/dt-bindings/clock/qcom,dispcc-sm8150.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.1851801Z [+] 覆盖 include/linux/suspend.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.2025779Z [+] 覆盖 include/linux/mm.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.2623376Z [+] 覆盖 include/linux/mmzone.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.2723065Z [+] 覆盖 include/linux/page-flags.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.2742502Z [+] 覆盖 include/linux/cgroup_subsys.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.2922109Z [+] 覆盖 include/linux/sched.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.3019717Z [+] 覆盖 include/linux/workqueue.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.3036868Z [+] 覆盖 include/linux/pageblock-flags.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.3121262Z [+] 覆盖 include/linux/lockdep_types.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.3136124Z [+] 覆盖 include/linux/fdtable.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.3222165Z [+] 覆盖 include/linux/lockdep.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.3234200Z [+] 覆盖 include/linux/fs.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.3922832Z [+] 覆盖 include/linux/task_io_accounting.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.3941576Z [+] 覆盖 include/linux/blk_types.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.4218185Z [+] 覆盖 include/linux/file.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.4235048Z [+] 覆盖 include/linux/slub_def.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.4323272Z [+] 覆盖 include/linux/mm_types.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.4335363Z [+] 覆盖 include/linux/local_lock.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.4419460Z [+] 覆盖 include/linux/pgsize_migration.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.4434944Z [+] 覆盖 include/linux/local_lock_internal.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.4448945Z [+] 覆盖 include/linux/blk-mq.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.4524689Z [+] 覆盖 include/linux/dma-buf.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.5219076Z [+] 覆盖 include/linux/hid.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.5240957Z [+] 覆盖 include/linux/gunyah.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.5256881Z [+] 覆盖 include/net/sock.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.5518184Z [+] 覆盖 include/net/af_unix.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.5536187Z [+] 覆盖 kernel/fork.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.5615539Z [+] 覆盖 kernel/cgroup/cgroup.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.5718168Z [+] 覆盖 kernel/Makefile
probe	UNKNOWN STEP	2026-09-28T09:46:07.5734365Z [+] 覆盖 kernel/.gitignore
probe	UNKNOWN STEP	2026-09-28T09:46:07.5818235Z [+] 覆盖 kernel/sched/sched.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.5834293Z [+] 覆盖 kernel/futex/futex.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.6022041Z [+] 覆盖 kernel/futex/requeue.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6520612Z [+] 覆盖 kernel/locking/rtmutex_api.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6538581Z [+] 覆盖 kernel/locking/lockdep.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6553936Z [+] 覆盖 kernel/locking/rtmutex.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6617575Z [+] 覆盖 kernel/locking/spinlock.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6633051Z [+] 覆盖 kernel/time/posix-cpu-timers.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6714738Z [+] 覆盖 kernel/signal.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6730789Z [+] 覆盖 kernel/power/process.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6816663Z [+] 覆盖 kernel/power/suspend.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.6833468Z [+] 覆盖 kernel/power/power.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.7016881Z [+] 覆盖 kernel/power/hibernate.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.7032786Z [+] 覆盖 kernel/power/user.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.7214912Z [+] 覆盖 kernel/power/main.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.7230639Z [+] 覆盖 kernel/exit.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.7315104Z [+] 覆盖 android/abi_gki_aarch64_mtk
probe	UNKNOWN STEP	2026-09-28T09:46:07.7336877Z [+] 覆盖 android/abi_gki_aarch64_pixel
probe	UNKNOWN STEP	2026-09-28T09:46:07.7419050Z [+] 覆盖 android/abi_gki_aarch64_vivo
probe	UNKNOWN STEP	2026-09-28T09:46:07.8424124Z [+] 覆盖 android/abi_gki_aarch64.stg
probe	UNKNOWN STEP	2026-09-28T09:46:07.8615593Z [+] 覆盖 android/abi_gki_aarch64_qcom
probe	UNKNOWN STEP	2026-09-28T09:46:07.8633522Z [+] 覆盖 android/abi_gki_aarch64.stg.allowed_breaks
probe	UNKNOWN STEP	2026-09-28T09:46:07.8714297Z [+] 覆盖 scripts/dummy-tools/objcopy
probe	UNKNOWN STEP	2026-09-28T09:46:07.8728746Z [+] 覆盖 scripts/dummy-tools/nm
probe	UNKNOWN STEP	2026-09-28T09:46:07.8814851Z [+] 覆盖 drivers/base/power/wakeup.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.8832514Z [+] 覆盖 drivers/md/dm-bow.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.8917570Z [+] 覆盖 drivers/hid/wacom_wac.h
probe	UNKNOWN STEP	2026-09-28T09:46:07.9009945Z [+] 覆盖 drivers/hid/hid-vivaldi-common.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9025173Z [+] 覆盖 drivers/hid/hid-primax.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9115834Z [+] 覆盖 drivers/hid/hid-core.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9130210Z [+] 覆盖 drivers/hid/wacom_wac.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9411006Z [+] 覆盖 drivers/hid/hid-multitouch.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9429244Z [+] 覆盖 drivers/hid/hid-gfrm.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9514727Z [+] 覆盖 drivers/hid/hid-logitech-dj.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9612434Z [+] 覆盖 drivers/hid/wacom_sys.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9628863Z [+] 覆盖 drivers/hid/hid-logitech-hidpp.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9639835Z [+] 覆盖 drivers/hid/hid-magicmouse.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9708755Z [+] 覆盖 drivers/virtio/virtio_input.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9913782Z [+] 覆盖 drivers/usb/gadget/function/f_uvc.c
probe	UNKNOWN STEP	2026-09-28T09:46:07.9929029Z [+] 覆盖 drivers/usb/gadget/function/uvc.h
probe	UNKNOWN STEP	2026-09-28T09:46:08.0012556Z [+] 覆盖 drivers/usb/gadget/function/uvc_v4l2.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.0028420Z [+] 覆盖 drivers/usb/gadget/function/f_accessory.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.0112417Z [+] 覆盖 drivers/usb/gadget/configfs.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.0129060Z [+] 覆盖 drivers/staging/greybus/hid.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.0144504Z [+] 覆盖 drivers/android/binder_internal.h
probe	UNKNOWN STEP	2026-09-28T09:46:08.0421584Z [+] 覆盖 drivers/android/vendor_hooks.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.0817285Z [+] 覆盖 drivers/android/binder.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.0834454Z [+] 覆盖 drivers/android/dbitmap.h
probe	UNKNOWN STEP	2026-09-28T09:46:08.0848011Z [+] 覆盖 drivers/virt/gunyah/rsc_mgr.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.0913558Z [+] 覆盖 drivers/dma-buf/dma-buf.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.0930211Z [+] 覆盖 fs/fuse/backing.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1109858Z [+] 覆盖 fs/fuse/dev.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1127126Z [+] 覆盖 fs/fuse/inode.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1209027Z [+] 覆盖 fs/f2fs/super.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1224344Z [+] 覆盖 fs/f2fs/file.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1408641Z [+] 覆盖 fs/f2fs/node.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1427212Z [+] 覆盖 fs/eventpoll.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1515974Z [+] 覆盖 fs/proc/base.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1527287Z [+] 覆盖 fs/file.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1541876Z [+] 覆盖 fs/exec.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1610906Z [+] 覆盖 mm/huge_memory.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1625556Z [+] 覆盖 mm/page_idle.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1639924Z [+] 覆盖 mm/page_alloc.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.1706430Z [+] 覆盖 mm/pgsize_migration.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2410726Z [+] 覆盖 mm/mmap.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2614652Z [+] 覆盖 mm/vmstat.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2629692Z [+] 覆盖 mm/memory.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2708269Z [+] 覆盖 mm/vmscan.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2725075Z [+] 覆盖 mm/filemap.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2812265Z [+] 覆盖 mm/damon/paddr.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2827390Z [+] 覆盖 mm/userfaultfd.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2907300Z [+] 覆盖 mm/rmap.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.2922188Z [+] 覆盖 net/tipc/msg.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.3309281Z [+] 覆盖 net/ipv4/udp_offload.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.3404918Z [+] 覆盖 net/ipv4/ip_output.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.3420799Z [+] 覆盖 net/ipv4/esp4.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.3506914Z [+] 覆盖 net/bluetooth/rfcomm/sock.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.3521921Z [+] 覆盖 net/bluetooth/sco.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.3607407Z [+] 覆盖 net/ipv6/exthdrs.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.3622293Z [+] 覆盖 net/ipv6/esp6.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4106639Z [+] 覆盖 net/core/gro.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4124661Z [+] 覆盖 net/core/skbuff.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4139282Z [+] 覆盖 net/nfc/llcp_core.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4305266Z [+] 覆盖 net/nfc/llcp_sock.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4346231Z [+] 覆盖 net/l2tp/l2tp_netlink.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4362291Z [+] 覆盖 net/l2tp/l2tp_ip6.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4409228Z [+] 覆盖 net/l2tp/l2tp_core.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4428949Z [+] 覆盖 net/l2tp/l2tp_eth.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4905705Z [+] 覆盖 net/l2tp/l2tp_debugfs.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.4928473Z [+] 覆盖 net/l2tp/l2tp_core.h
probe	UNKNOWN STEP	2026-09-28T09:46:08.5104712Z [+] 覆盖 net/l2tp/l2tp_ip.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.5120931Z [+] 覆盖 net/l2tp/l2tp_ppp.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.5204695Z [+] 覆盖 net/unix/af_unix.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.5222520Z [+] 覆盖 net/unix/garbage.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.5607694Z [+] 覆盖 net/netfilter/xt_HL.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.5805851Z [+] 覆盖 net/netfilter/xt_DSCP.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.5908324Z [+] 覆盖 net/netfilter/xt_tcpmss.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.5925316Z [+] 覆盖 net/netfilter/xt_RATEEST.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.5939475Z [+] 覆盖 net/netfilter/xt_quota2.c
probe	UNKNOWN STEP	2026-09-28T09:46:08.6004495Z [+] 覆盖 block/elevator.h
probe	UNKNOWN STEP	2026-09-28T09:46:08.6005151Z 共应用 171 个头文件补丁
probe	UNKNOWN STEP	2026-09-28T09:46:08.6034560Z ##[group]Run set -uo pipefail
probe	UNKNOWN STEP	2026-09-28T09:46:08.6034816Z ^[[36;1mset -uo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6035069Z ^[[36;1msed -i 's/check_defconfig//' ./common/build.config.gki^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6035465Z ^[[36;1msed -i '/name = "kernel_aarch64",/a\    check_defconfig = "disabled",' common/BUILD.bazel^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6035798Z ^[[36;1mok=0^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6035960Z ^[[36;1mfor i in 1 2 3 4; do^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6036165Z ^[[36;1m  echo "===== Bazel 构建 第 $i 次 ====="^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6036498Z ^[[36;1m  if tools/bazel build --config=fast --disk_cache=/home/runner/.cache/bazel \^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6036882Z ^[[36;1m       //common:kernel_aarch64/Image > /tmp/bazel.log 2>&1; then^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6037149Z ^[[36;1m    ok=1; break^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6037321Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6037516Z ^[[36;1m  echo "----- 真实 error 行（最多 40 条）-----"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6038087Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6038573Z ^[[36;1m  echo "----- tail 40 -----"^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6038790Z ^[[36;1m  tail -40 /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6039185Z ^[[36;1m  python3 "$GITHUB_WORKSPACE/.github/tools/bazel_module_outs.py" /tmp/bazel.log common/BUILD.bazel || break^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6039561Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6039743Z ^[[36;1m[ "$ok" = "1" ] || { echo "构建失败"; exit 1; }^[[0m
probe	UNKNOWN STEP	2026-09-28T09:46:08.6094045Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-28T09:46:08.6094248Z env:
probe	UNKNOWN STEP	2026-09-28T09:46:08.6094487Z   KERNEL_SOURCE_COMMIT: 489c6def208fb01674c02d18df10bfe0bbaa4d66
probe	UNKNOWN STEP	2026-09-28T09:46:08.6094761Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T09:46:08.6803924Z ===== Bazel 构建 第 1 次 =====
probe	UNKNOWN STEP	2026-09-28T09:56:00.4559818Z ----- 真实 error 行（最多 40 条）-----
probe	UNKNOWN STEP	2026-09-28T09:56:00.4577667Z 25:arch/arm64/configs/gki_defconfig:4:warning: unexpected data: ﻿#
probe	UNKNOWN STEP	2026-09-28T09:56:00.4579017Z 42:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:39:14: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4580371Z 48:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:40:7: error: use of undeclared identifier 'XT_CONNMARK_SET'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4581803Z 51:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:42:29: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4583084Z 57:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:42:45: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4584226Z 63:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:43:11: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4585604Z 69:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:43:26: error: use of undeclared identifier 'D_SHIFT_RIGHT'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4587037Z 72:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:44:20: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4589026Z 78:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:46:20: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4590366Z 84:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:53:7: error: use of undeclared identifier 'XT_CONNMARK_SAVE'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4591807Z 87:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:54:37: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4593504Z 93:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:55:11: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4594894Z 99:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:55:26: error: use of undeclared identifier 'D_SHIFT_RIGHT'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4596230Z 102:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:56:27: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4597626Z 108:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:58:27: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4599102Z 114:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:60:41: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4600423Z 120:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:67:7: error: use of undeclared identifier 'XT_CONNMARK_RESTORE'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4601928Z 123:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:68:47: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4603297Z 129:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:69:11: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4604580Z 135:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:69:26: error: use of undeclared identifier 'D_SHIFT_RIGHT'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4605453Z 138:fatal error: too many errors emitted, stopping now [-ferror-limit=]
probe	UNKNOWN STEP	2026-09-28T09:56:00.4606306Z 140:make[4]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:250: net/netfilter/xt_connmark.o] Error 1
probe	UNKNOWN STEP	2026-09-28T09:56:00.4607677Z 141:make[3]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: net/netfilter] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4608799Z 143:make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: net] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4609838Z 145:make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:2068: .] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4610687Z 146:make: *** [Makefile:256: __sub-make] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4611253Z ----- tail 40 -----
probe	UNKNOWN STEP	2026-09-28T09:56:00.4611861Z                                                     ^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4612990Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:60:41: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4614030Z                 newmark = (READ_ONCE(ct->mark) & ~info->ctmask) ^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4614639Z                                                   ~~~~^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4615655Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:27:53: note: forward declaration of 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4616790Z connmark_tg_shift(struct sk_buff *skb, const struct xt_connmark_tginfo2 *info)
probe	UNKNOWN STEP	2026-09-28T09:56:00.4617456Z                                                     ^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4618385Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:67:7: error: use of undeclared identifier 'XT_CONNMARK_RESTORE'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4619406Z         case XT_CONNMARK_RESTORE:
probe	UNKNOWN STEP	2026-09-28T09:56:00.4619844Z              ^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4620761Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:68:47: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4638122Z                 new_targetmark = (READ_ONCE(ct->mark) & info->ctmask);
probe	UNKNOWN STEP	2026-09-28T09:56:00.4638655Z                                                         ~~~~^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4639731Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:27:53: note: forward declaration of 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4640720Z connmark_tg_shift(struct sk_buff *skb, const struct xt_connmark_tginfo2 *info)
probe	UNKNOWN STEP	2026-09-28T09:56:00.4641228Z                                                     ^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4642271Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:69:11: error: incomplete definition of type 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4643194Z                 if (info->shift_dir == D_SHIFT_RIGHT)
probe	UNKNOWN STEP	2026-09-28T09:56:00.4643546Z                     ~~~~^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4644328Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:27:53: note: forward declaration of 'struct xt_connmark_tginfo2'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4645325Z connmark_tg_shift(struct sk_buff *skb, const struct xt_connmark_tginfo2 *info)
probe	UNKNOWN STEP	2026-09-28T09:56:00.4645830Z                                                     ^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4646616Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/net/netfilter/xt_connmark.c:69:26: error: use of undeclared identifier 'D_SHIFT_RIGHT'
probe	UNKNOWN STEP	2026-09-28T09:56:00.4647471Z                 if (info->shift_dir == D_SHIFT_RIGHT)
probe	UNKNOWN STEP	2026-09-28T09:56:00.4647825Z                                        ^
probe	UNKNOWN STEP	2026-09-28T09:56:00.4648255Z fatal error: too many errors emitted, stopping now [-ferror-limit=]
probe	UNKNOWN STEP	2026-09-28T09:56:00.4648709Z 1 warning and 20 errors generated.
probe	UNKNOWN STEP	2026-09-28T09:56:00.4649464Z make[4]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:250: net/netfilter/xt_connmark.o] Error 1
probe	UNKNOWN STEP	2026-09-28T09:56:00.4650575Z make[3]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: net/netfilter] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4651654Z make[3]: *** Waiting for unfinished jobs....
probe	UNKNOWN STEP	2026-09-28T09:56:00.4652327Z make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: net] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4653020Z make[2]: *** Waiting for unfinished jobs....
probe	UNKNOWN STEP	2026-09-28T09:56:00.4653634Z make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:2068: .] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4654231Z make: *** [Makefile:256: __sub-make] Error 2
probe	UNKNOWN STEP	2026-09-28T09:56:00.4654573Z [276 / 278] checking cached actions
probe	UNKNOWN STEP	2026-09-28T09:56:00.4654925Z Target //common:kernel_aarch64/Image failed to build
probe	UNKNOWN STEP	2026-09-28T09:56:00.4655423Z Use --verbose_failures to see the command lines of failed build steps.
probe	UNKNOWN STEP	2026-09-28T09:56:00.4655949Z INFO: Elapsed time: 591.599s, Critical Path: 571.40s
probe	UNKNOWN STEP	2026-09-28T09:56:00.4656457Z INFO: 276 processes: 265 internal, 1 local, 10 processwrapper-sandbox.
probe	UNKNOWN STEP	2026-09-28T09:56:00.4656948Z ERROR: Build did NOT complete successfully
probe	UNKNOWN STEP	2026-09-28T09:56:00.4764127Z 没有解析到缺失模块
probe	UNKNOWN STEP	2026-09-28T09:56:00.4793400Z 构建失败
probe	UNKNOWN STEP	2026-09-28T09:56:00.4812399Z ##[error]Process completed with exit code 1.
probe	UNKNOWN STEP	2026-09-28T09:56:00.4881241Z ##[group]Run actions/upload-artifact@v4
probe	UNKNOWN STEP	2026-09-28T09:56:00.4881693Z with:
probe	UNKNOWN STEP	2026-09-28T09:56:00.4881920Z   name: bazel-log
probe	UNKNOWN STEP	2026-09-28T09:56:00.4882168Z   path: /tmp/bazel.log
probe	UNKNOWN STEP	2026-09-28T09:56:00.4882441Z   if-no-files-found: ignore
probe	UNKNOWN STEP	2026-09-28T09:56:00.4882650Z   compression-level: 6
probe	UNKNOWN STEP	2026-09-28T09:56:00.4882819Z   overwrite: false
probe	UNKNOWN STEP	2026-09-28T09:56:00.4882992Z   include-hidden-files: false
probe	UNKNOWN STEP	2026-09-28T09:56:00.4883186Z env:
probe	UNKNOWN STEP	2026-09-28T09:56:00.4883399Z   KERNEL_SOURCE_COMMIT: 489c6def208fb01674c02d18df10bfe0bbaa4d66
probe	UNKNOWN STEP	2026-09-28T09:56:00.4883702Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-28T09:56:00.9436369Z (node:116207) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
probe	UNKNOWN STEP	2026-09-28T09:56:00.9436947Z (Use `node --trace-deprecation ...` to show where the warning was created)
probe	UNKNOWN STEP	2026-09-28T09:56:00.9476751Z With the provided path, there will be 1 file uploaded
probe	UNKNOWN STEP	2026-09-28T09:56:00.9483822Z Artifact name is valid!
probe	UNKNOWN STEP	2026-09-28T09:56:00.9495508Z Root directory input is valid!
probe	UNKNOWN STEP	2026-09-28T09:56:01.1726753Z Beginning upload of artifact content to blob storage
probe	UNKNOWN STEP	2026-09-28T09:56:01.1902545Z (node:116207) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
probe	UNKNOWN STEP	2026-09-28T09:56:01.2180701Z Uploaded bytes 1883
probe	UNKNOWN STEP	2026-09-28T09:56:01.2319558Z Finished uploading artifact content to blob storage!
probe	UNKNOWN STEP	2026-09-28T09:56:01.2320293Z SHA256 digest of uploaded artifact zip is 0614f689108f33c3bb9a0c93190f2d94dbd253ce8a73b4af58b1f4a1689338c4
probe	UNKNOWN STEP	2026-09-28T09:56:01.2322080Z Finalizing artifact upload
probe	UNKNOWN STEP	2026-09-28T09:56:01.4233097Z Artifact bazel-log.zip successfully finalized. Artifact ID 10962577585
probe	UNKNOWN STEP	2026-09-28T09:56:01.4233828Z Artifact bazel-log has been successfully uploaded! Final size is 1883 bytes. Artifact ID is 10962577585
probe	UNKNOWN STEP	2026-09-28T09:56:01.4234703Z Artifact download URL: https://github.com/glboxed-max/GKI_KernelSU_SUSFS/actions/runs/36405188758/artifacts/10962577585
probe	UNKNOWN STEP	2026-09-28T09:56:01.4420400Z Post job cleanup.
probe	UNKNOWN STEP	2026-09-28T09:56:01.5125877Z [command]/usr/bin/git version
probe	UNKNOWN STEP	2026-09-28T09:56:01.5165098Z git version 2.55.0
probe	UNKNOWN STEP	2026-09-28T09:56:01.5194978Z Temporarily overriding HOME='/home/runner/work/_temp/17878a56-488a-47a3-9d3d-3e9c7855f203' before making global git config changes
probe	UNKNOWN STEP	2026-09-28T09:56:01.5195988Z Adding repository directory to the temporary git global config as a safe directory
probe	UNKNOWN STEP	2026-09-28T09:56:01.5199552Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS
probe	UNKNOWN STEP	2026-09-28T09:56:01.5230174Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
probe	UNKNOWN STEP	2026-09-28T09:56:01.5258672Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
probe	UNKNOWN STEP	2026-09-28T09:56:01.5485268Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
probe	UNKNOWN STEP	2026-09-28T09:56:01.5515311Z http.https://github.com/.extraheader
probe	UNKNOWN STEP	2026-09-28T09:56:01.5524542Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
probe	UNKNOWN STEP	2026-09-28T09:56:01.5556097Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
probe	UNKNOWN STEP	2026-09-28T09:56:01.5760830Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
probe	UNKNOWN STEP	2026-09-28T09:56:01.5794636Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
probe	UNKNOWN STEP	2026-09-28T09:56:01.6132958Z Cleaning up orphan processes
probe	UNKNOWN STEP	2026-09-28T09:56:01.6471300Z Terminate orphan process: pid (3055) (java.lang=ALL-UNNAMED)
probe	UNKNOWN STEP	2026-09-28T09:56:01.6490523Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```
