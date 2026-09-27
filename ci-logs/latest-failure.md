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
probe	UNKNOWN STEP	2026-09-26T23:14:14.9693233Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:15:04.4395557Z 26:arch/arm64/configs/gki_defconfig:4:warning: unexpected data: ﻿#
probe	UNKNOWN STEP	2026-09-26T23:15:04.4397063Z 45:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/mm_types.h:559:1: error: extraneous closing brace ('}')
probe	UNKNOWN STEP	2026-09-26T23:15:04.4453044Z 1137:make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:118: arch/arm64/kernel/asm-offsets.s] Error 1
probe	UNKNOWN STEP	2026-09-26T23:15:04.4453927Z 1138:make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:1369: prepare0] Error 2
probe	UNKNOWN STEP	2026-09-26T23:15:04.4476595Z make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:118: arch/arm64/kernel/asm-offsets.s] Error 1
probe	UNKNOWN STEP	2026-09-26T23:15:04.4477452Z make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:1369: prepare0] Error 2
probe	UNKNOWN STEP	2026-09-26T23:15:04.4478516Z make: *** [Makefile:256: __sub-make] Error 2
```

## 失败步骤完整日志
```
probe	UNKNOWN STEP	2026-09-26T23:10:45.0635600Z From https://github.com/glboxed-max/GKI_KernelSU_SUSFS
probe	UNKNOWN STEP	2026-09-26T23:10:45.0638709Z  * [new ref]         4195a579f4fcb77754cdbd4a122202adb18a3ed7 -> origin/main
probe	UNKNOWN STEP	2026-09-26T23:10:45.0643461Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:10:45.0645668Z ##[group]Determining the checkout info
probe	UNKNOWN STEP	2026-09-26T23:10:45.0648689Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:10:45.0650133Z [command]/usr/bin/git sparse-checkout disable
probe	UNKNOWN STEP	2026-09-26T23:10:45.0705661Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
probe	UNKNOWN STEP	2026-09-26T23:10:45.0740606Z ##[group]Checking out the ref
probe	UNKNOWN STEP	2026-09-26T23:10:45.0744850Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
probe	UNKNOWN STEP	2026-09-26T23:10:45.0974630Z Switched to a new branch 'main'
probe	UNKNOWN STEP	2026-09-26T23:10:45.0980615Z branch 'main' set up to track 'origin/main'.
probe	UNKNOWN STEP	2026-09-26T23:10:45.0986838Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:10:45.1029607Z [command]/usr/bin/git log -1 --format=%H
probe	UNKNOWN STEP	2026-09-26T23:10:45.1055898Z 4195a579f4fcb77754cdbd4a122202adb18a3ed7
probe	UNKNOWN STEP	2026-09-26T23:10:45.1321282Z ##[group]Run sudo rm -rf /usr/share/dotnet /opt/ghc /usr/local/lib/android/sdk /usr/local/share/boost \
probe	UNKNOWN STEP	2026-09-26T23:10:45.1324442Z ^[[36;1msudo rm -rf /usr/share/dotnet /opt/ghc /usr/local/lib/android/sdk /usr/local/share/boost \^[[0m
probe	UNKNOWN STEP	2026-09-26T23:10:45.1327349Z ^[[36;1m            /opt/hostedtoolcache/CodeQL "$AGENT_TOOLSDIRECTORY" 2>/dev/null || true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:10:45.1329772Z ^[[36;1mdf -h /^[[0m
probe	UNKNOWN STEP	2026-09-26T23:10:45.1681405Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-26T23:10:45.1682623Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:13:06.6015824Z Filesystem      Size  Used Avail Use% Mounted on
probe	UNKNOWN STEP	2026-09-26T23:13:06.6016298Z /dev/root       145G   37G  108G  26% /
probe	UNKNOWN STEP	2026-09-26T23:13:06.6062723Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-26T23:13:06.6063090Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.6063558Z ^[[36;1mmkdir -p "$GITHUB_WORKSPACE/git-repo" "$GITHUB_WORKSPACE/kernel" "$GITHUB_WORKSPACE/AnyKernel3"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.6064335Z ^[[36;1mcurl -sSL https://storage.googleapis.com/git-repo-downloads/repo -o "$GITHUB_WORKSPACE/git-repo/repo"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.6064903Z ^[[36;1mchmod +x "$GITHUB_WORKSPACE/git-repo/repo"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.6065267Z ^[[36;1mecho "$GITHUB_WORKSPACE/git-repo" >> "$GITHUB_PATH"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.6131295Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-26T23:13:06.6131595Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:13:06.7157285Z Prepare all required actions
probe	UNKNOWN STEP	2026-09-26T23:13:06.7339204Z ##[group]Run ./.github/actions/download-kernel
probe	UNKNOWN STEP	2026-09-26T23:13:06.7339539Z with:
probe	UNKNOWN STEP	2026-09-26T23:13:06.7339752Z   android_version: android14
probe	UNKNOWN STEP	2026-09-26T23:13:06.7340003Z   kernel_version: 6.1
probe	UNKNOWN STEP	2026-09-26T23:13:06.7340255Z   version: android14-6.1
probe	UNKNOWN STEP	2026-09-26T23:13:06.7340488Z   os_patch_level: 2025-09
probe	UNKNOWN STEP	2026-09-26T23:13:06.7340713Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:13:06.7396095Z ##[start-action display=Initialize and Sync Kernel Repository;id=__self.sync]
probe	UNKNOWN STEP	2026-09-26T23:13:06.7443321Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-26T23:13:06.7443702Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7443937Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7444260Z ^[[36;1m# Derive android and kernel from combined version when available^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7444660Z ^[[36;1mVERSION="android14-6.1"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7444971Z ^[[36;1mANDROID_PART=$(echo "$VERSION" | cut -d- -f1)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7445368Z ^[[36;1mKERNEL_PART=$(echo "$VERSION" | cut -d- -f2)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7445769Z ^[[36;1mFORMATTED_BRANCH="${ANDROID_PART}-${KERNEL_PART}-2025-09"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7446117Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7446310Z ^[[36;1minit_repo() {^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7446538Z ^[[36;1m  local depth="$1"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7446783Z ^[[36;1m  local depth_flag=""^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7447039Z ^[[36;1m  if [ "$depth" != "0" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7447319Z ^[[36;1m    depth_flag="--depth=${depth}"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7447587Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7448447Z ^[[36;1m  repo init -u https://android.googlesource.com/kernel/manifest -b common-${FORMATTED_BRANCH} ${depth_flag} || { echo "ERROR: repo init failed" >&2; return 1; }^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7449540Z ^[[36;1m  REMOTE_BRANCH=$(git ls-remote https://android.googlesource.com/kernel/common ${FORMATTED_BRANCH}) || { echo "ERROR: git ls-remote failed" >&2; return 1; }^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7450271Z ^[[36;1m  DEFAULT_MANIFEST_PATH=.repo/manifests/default.xml^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7450615Z ^[[36;1m  DEPRECATED=false^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7450908Z ^[[36;1m  if grep -q deprecated <<< "$REMOTE_BRANCH"; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7451421Z ^[[36;1m    sed -i "s/\"${FORMATTED_BRANCH}\"/\"deprecated\/${FORMATTED_BRANCH}\"/g" "$DEFAULT_MANIFEST_PATH"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7452006Z ^[[36;1m    echo "[!] Note: Branch ${FORMATTED_BRANCH} is considered deprecated."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7452393Z ^[[36;1m    DEPRECATED=true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7452620Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7452870Z ^[[36;1m  echo "deprecated=$DEPRECATED" >> $GITHUB_OUTPUT^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7453282Z ^[[36;1m  # Google retires old monthly heads entirely (neither live nor^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7453735Z ^[[36;1m  # deprecated/); the manifest still pins common to the dead^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7454179Z ^[[36;1m  # branch. Fall back to the latest immutable release tag so the^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7454585Z ^[[36;1m  # build keeps working. Tags are never deleted.^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7454910Z ^[[36;1m  TAG_FALLBACK=""^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7455413Z ^[[36;1m  if [ "$DEPRECATED" = "false" ] && [ -z "$REMOTE_BRANCH" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7456460Z ^[[36;1m    LATEST_TAG=$(git ls-remote https://android.googlesource.com/kernel/common "refs/tags/${FORMATTED_BRANCH}_r*" 2>/dev/null | awk '{print $2}' | grep -v '\^{}$' | sed 's|refs/tags/||' | awk -F'_r' '{print $NF+0, $0}' | sort -n | tail -n 1 | cut -d' ' -f2- || true)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7457428Z ^[[36;1m    if [ -n "$LATEST_TAG" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7458174Z ^[[36;1m      echo "[!] Note: Branch ${FORMATTED_BRANCH} head missing upstream; using tag ${LATEST_TAG}."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7458904Z ^[[36;1m      sed -i "/path=\"common\"/ s/revision=\"${FORMATTED_BRANCH}\"/revision=\"${LATEST_TAG}\"/" "$DEFAULT_MANIFEST_PATH"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7459456Z ^[[36;1m      TAG_FALLBACK="$LATEST_TAG"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7459725Z ^[[36;1m    else^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7460292Z ^[[36;1m      echo "WARNING: no head or tag found for ${FORMATTED_BRANCH}; sync will likely fail." >&2^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7460750Z ^[[36;1m    fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7460947Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7461140Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7461426Z ^[[36;1m  # 有些月份 AOSP 的 manifest 直接把 common 钉成 `_rNN` 发布 tag（而不是分支）。^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7461862Z ^[[36;1m  # 这种情况下 refs/heads/<rev> 不存在，必须允许按 tag 拉取；否则 repo 会 fetch^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7462339Z ^[[36;1m  # refs/heads/androidXX-YY-YYYY-MM_rNN 并报 "couldn't find remote ref"。^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7462742Z ^[[36;1m  MANIFEST_TAG=""^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7463347Z ^[[36;1m  MANIFEST_COMMON_REV="$(grep -E 'path="common"' "$DEFAULT_MANIFEST_PATH" 2>/dev/null | grep -oE 'revision="[^"]+"' | head -n1 | cut -d'"' -f2 || true)"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7464046Z ^[[36;1m  if [[ "$MANIFEST_COMMON_REV" =~ _r[0-9]+$ ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7464393Z ^[[36;1m    MANIFEST_TAG="$MANIFEST_COMMON_REV"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7464820Z ^[[36;1m    echo "[!] manifest pins common to release tag '${MANIFEST_TAG}'; 将允许 tag 拉取。"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7465251Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7465513Z ^[[36;1m  echo "tag_fallback=$TAG_FALLBACK" >> $GITHUB_OUTPUT^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7465902Z ^[[36;1m  echo "manifest_tag=$MANIFEST_TAG" >> $GITHUB_OUTPUT^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7466214Z ^[[36;1m}^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7466396Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7466584Z ^[[36;1mMAX_RETRIES=3^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7466818Z ^[[36;1mRETRY_DELAY_SHORT=15^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7467061Z ^[[36;1mSYNC_TIMEOUT="15m"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7467294Z ^[[36;1mattempt=1^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7467618Z ^[[36;1m# Always shallow: the build only needs the branch tip. Deeper retries^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7468264Z ^[[36;1m# just download more data into a strained runner (slower + more disk).^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7468656Z ^[[36;1mDEPTHS=(1 1 1)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7468870Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7469059Z ^[[36;1mclean_workspace() {^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7469312Z ^[[36;1m  echo "Disk before cleanup:"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7469609Z ^[[36;1m  df -h "$PWD" | tail -n +2 || true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7470029Z ^[[36;1m  # Remove repo metadata AND any half-checked-out project dirs from the^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7470538Z ^[[36;1m  # previous attempt. Deleting only .repo leaves stale checkouts behind^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7471041Z ^[[36;1m  # and every later sync fails with "Checking out local projects failed".^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7471509Z ^[[36;1m  find "$PWD" -mindepth 1 -maxdepth 1 -exec rm -rf {} +^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7471860Z ^[[36;1m  echo "Disk after cleanup:"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7472151Z ^[[36;1m  df -h "$PWD" | tail -n +2 || true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7472421Z ^[[36;1m}^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7472604Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7472824Z ^[[36;1mwhile [ $attempt -le $MAX_RETRIES ]; do^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7473158Z ^[[36;1m  CURRENT_DEPTH="${DEPTHS[$((attempt-1))]}"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7473788Z ^[[36;1m  echo "Attempt $attempt/$MAX_RETRIES: initialize and sync kernel repository (depth=${CURRENT_DEPTH}, sync timeout $SYNC_TIMEOUT)..."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7474537Z ^[[36;1m  df -h "$PWD" | tail -n +2 || true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7474847Z ^[[36;1m  if init_repo "$CURRENT_DEPTH"; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7475265Z ^[[36;1m    # 默认最小浅克隆；若本次需要按 tag 拉取（tag fallback 或 manifest 用 _rNN tag），^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7475713Z ^[[36;1m    # 则去掉 -c/--current-branch 与 --no-tags，确保 repo 能取到 tag。^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7476225Z ^[[36;1m    SYNC_ARGS=(-c --current-branch --no-clone-bundle --no-tags --jobs-checkout=4 -j4)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7476742Z ^[[36;1m    if [ -n "$TAG_FALLBACK" ] || [ -n "${MANIFEST_TAG:-}" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7477157Z ^[[36;1m      SYNC_ARGS=(--no-clone-bundle --jobs-checkout=4 -j4)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7477485Z ^[[36;1m    fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7478168Z ^[[36;1m    if timeout $SYNC_TIMEOUT repo sync "${SYNC_ARGS[@]}"; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7478696Z ^[[36;1m      echo "Kernel repository initialization and sync succeeded on attempt $attempt."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7479284Z ^[[36;1m      break^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7479512Z ^[[36;1m    else^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7479720Z ^[[36;1m      rc=$?^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7479941Z ^[[36;1m      if [ $rc -eq 124 ]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7480268Z ^[[36;1m        echo "repo sync timed out after $SYNC_TIMEOUT."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7480589Z ^[[36;1m      else^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7480845Z ^[[36;1m        echo "repo sync failed with exit code $rc."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7481154Z ^[[36;1m      fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7481345Z ^[[36;1m    fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7481533Z ^[[36;1m  else^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7481725Z ^[[36;1m    rc=$?^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7482033Z ^[[36;1m    echo "repo init or branch preflight failed with exit code $rc."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7482401Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7482590Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7482807Z ^[[36;1m  if [ $attempt -lt $MAX_RETRIES ]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7483226Z ^[[36;1m    echo "Cleaning workspace and retrying after ${RETRY_DELAY_SHORT}s..."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7483638Z ^[[36;1m    clean_workspace || true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7483916Z ^[[36;1m    sleep $RETRY_DELAY_SHORT^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7484168Z ^[[36;1m  else^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7484418Z ^[[36;1m    echo "All $MAX_RETRIES attempts failed." >&2^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7484728Z ^[[36;1m    exit $rc^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7484938Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7485143Z ^[[36;1m  attempt=$((attempt+1))^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7485386Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-26T23:13:06.7559807Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
probe	UNKNOWN STEP	2026-09-26T23:13:06.7560184Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:13:06.7682479Z Attempt 1/3: initialize and sync kernel repository (depth=1, sync timeout 15m)...
probe	UNKNOWN STEP	2026-09-26T23:13:06.7701242Z /dev/root       145G   37G  108G  26% /
probe	UNKNOWN STEP	2026-09-26T23:13:09.3968647Z 
probe	UNKNOWN STEP	2026-09-26T23:13:09.3969246Z repo has been initialized in /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel
probe	UNKNOWN STEP	2026-09-26T23:14:14.8082729Z Finalizing sync state...
probe	UNKNOWN STEP	2026-09-26T23:14:14.8303308Z repo sync has finished successfully.
probe	UNKNOWN STEP	2026-09-26T23:14:14.8304172Z Kernel repository initialization and sync succeeded on attempt 1.
probe	UNKNOWN STEP	2026-09-26T23:14:14.8333260Z ##[end-action id=__self.sync;outcome=success;conclusion=success;duration_ms=68093]
probe	UNKNOWN STEP	2026-09-26T23:14:14.8338902Z ##[start-action display=Capture Kernel Common Commit Metadata;id=__self.__run]
probe	UNKNOWN STEP	2026-09-26T23:14:14.8359907Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-26T23:14:14.8360206Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8360437Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8360639Z ^[[36;1mif [[ ! -d common ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8361030Z ^[[36;1m  echo "WARNING: common folder not found; skipping commit metadata capture."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8361434Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8361626Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8361814Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8361994Z ^[[36;1mcd common^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8362191Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8362378Z ^[[36;1mif [[ ! -d .git ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8362783Z ^[[36;1m  echo "WARNING: common is not a git checkout; skipping commit metadata capture."^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8363396Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8363592Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8363773Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8363988Z ^[[36;1mCOMMIT_DATE=$(git log -1 --format=%cI)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8364310Z ^[[36;1mCOMMIT_MSG=$(git log -1 --format=%s)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8364629Z ^[[36;1mCOMMIT_SHA=$(git rev-parse HEAD)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8364896Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8365158Z ^[[36;1mecho "KERNEL_SOURCE_COMMIT=$COMMIT_SHA" >> "$GITHUB_ENV"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8365548Z ^[[36;1mecho "Kernel common commit date: $COMMIT_DATE"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8365908Z ^[[36;1mecho "Kernel common commit msg: $COMMIT_MSG"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8366271Z ^[[36;1mecho "Kernel common commit SHA: $COMMIT_SHA"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8431167Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
probe	UNKNOWN STEP	2026-09-26T23:14:14.8431579Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:14:14.8572447Z Kernel common commit date: 2026-09-24T21:53:04Z
probe	UNKNOWN STEP	2026-09-26T23:14:14.8573921Z Kernel common commit msg: ANDROID: netfilter: xt_quota2: fix UAF in q2_get_counter error path
probe	UNKNOWN STEP	2026-09-26T23:14:14.8574899Z Kernel common commit SHA: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-26T23:14:14.8588679Z ##[end-action id=__self.__run;outcome=success;conclusion=success;duration_ms=24]
probe	UNKNOWN STEP	2026-09-26T23:14:14.8658470Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-26T23:14:14.8658848Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8659219Z ^[[36;1mcp "$GITHUB_WORKSPACE/.github/config/vivo_pd2339_a16_defconfig" \^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8659746Z ^[[36;1m   "$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8660340Z ^[[36;1mecho "配置行数: $(grep -c . "$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig")"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8723450Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-26T23:14:14.8723709Z env:
probe	UNKNOWN STEP	2026-09-26T23:14:14.8724001Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-26T23:14:14.8724351Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:14:14.8840231Z 配置行数: 8766
probe	UNKNOWN STEP	2026-09-26T23:14:14.8891104Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-26T23:14:14.8891437Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8891807Z ^[[36;1mD="$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8892316Z ^[[36;1msed -i 's/^CONFIG_WERROR=y/# CONFIG_WERROR is not set/' "$D"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8892804Z ^[[36;1mgrep -q '^\(# \)\?CONFIG_WERROR' "$D" || echo '# CONFIG_WERROR is not set' >> "$D"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8893230Z ^[[36;1mgrep -n 'CONFIG_WERROR' "$D"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.8955981Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-26T23:14:14.8956238Z env:
probe	UNKNOWN STEP	2026-09-26T23:14:14.8956518Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-26T23:14:14.8956873Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:14:14.9096163Z 27:# CONFIG_WERROR is not set
probe	UNKNOWN STEP	2026-09-26T23:14:14.9130138Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-26T23:14:14.9130480Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9130776Z ^[[36;1mSRC="$GITHUB_WORKSPACE/.github/patches/abi"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9131132Z ^[[36;1mcd "$GITHUB_WORKSPACE/kernel/common"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9131421Z ^[[36;1mn=0^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9131623Z ^[[36;1mwhile IFS= read -r f; do^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9131878Z ^[[36;1m  rel="${f#$SRC/}"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9132108Z ^[[36;1m  cp "$f" "$rel"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9132334Z ^[[36;1m  echo "[+] 覆盖 $rel"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9132572Z ^[[36;1m  n=$((n+1))^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9132801Z ^[[36;1mdone < <(find "$SRC" -type f)^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9133065Z ^[[36;1mecho "共应用 $n 个头文件补丁"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9193623Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-26T23:14:14.9193885Z env:
probe	UNKNOWN STEP	2026-09-26T23:14:14.9194164Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-26T23:14:14.9194514Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:14:14.9307477Z [+] 覆盖 include/trace/events/mmflags.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9323572Z [+] 覆盖 include/uapi/linux/android/binder.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9340014Z [+] 覆盖 include/linux/mm.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9355437Z [+] 覆盖 include/linux/mmzone.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9371181Z [+] 覆盖 include/linux/page-flags.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9386563Z [+] 覆盖 include/linux/cgroup_subsys.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9402424Z [+] 覆盖 include/linux/sched.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9418239Z [+] 覆盖 include/linux/workqueue.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9433796Z [+] 覆盖 include/linux/pageblock-flags.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9450337Z [+] 覆盖 include/linux/fs.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9465548Z [+] 覆盖 include/linux/task_io_accounting.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9481132Z [+] 覆盖 include/linux/blk_types.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9496597Z [+] 覆盖 include/linux/slub_def.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9513507Z [+] 覆盖 include/linux/mm_types.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9529093Z [+] 覆盖 include/linux/blk-mq.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9544863Z [+] 覆盖 include/net/sock.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9561876Z [+] 覆盖 kernel/cgroup/cgroup.c
probe	UNKNOWN STEP	2026-09-26T23:14:14.9577417Z [+] 覆盖 kernel/sched/sched.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9593736Z [+] 覆盖 kernel/futex/futex.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9609202Z [+] 覆盖 drivers/android/binder_internal.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9625687Z [+] 覆盖 mm/page_alloc.c
probe	UNKNOWN STEP	2026-09-26T23:14:14.9641552Z [+] 覆盖 mm/vmstat.c
probe	UNKNOWN STEP	2026-09-26T23:14:14.9656579Z [+] 覆盖 block/elevator.h
probe	UNKNOWN STEP	2026-09-26T23:14:14.9657092Z 共应用 23 个头文件补丁
probe	UNKNOWN STEP	2026-09-26T23:14:14.9688670Z ##[group]Run set -uo pipefail
probe	UNKNOWN STEP	2026-09-26T23:14:14.9689010Z ^[[36;1mset -uo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9689333Z ^[[36;1msed -i 's/check_defconfig//' ./common/build.config.gki^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9689852Z ^[[36;1msed -i '/name = "kernel_aarch64",/a\    check_defconfig = "disabled",' common/BUILD.bazel^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9690282Z ^[[36;1mok=0^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9690484Z ^[[36;1mfor i in 1 2 3 4; do^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9690743Z ^[[36;1m  echo "===== Bazel 构建 第 $i 次 ====="^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9691178Z ^[[36;1m  if tools/bazel build --config=fast --disk_cache=/home/runner/.cache/bazel \^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9691691Z ^[[36;1m       //common:kernel_aarch64/Image > /tmp/bazel.log 2>&1; then^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9692043Z ^[[36;1m    ok=1; break^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9692267Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9692516Z ^[[36;1m  echo "----- 真实 error 行（最多 40 条）-----"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9693233Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9693895Z ^[[36;1m  echo "----- tail 40 -----"^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9694170Z ^[[36;1m  tail -40 /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9694696Z ^[[36;1m  python3 "$GITHUB_WORKSPACE/.github/tools/bazel_module_outs.py" /tmp/bazel.log common/BUILD.bazel || break^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9695199Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9695418Z ^[[36;1m[ "$ok" = "1" ] || { echo "构建失败"; exit 1; }^[[0m
probe	UNKNOWN STEP	2026-09-26T23:14:14.9759071Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-26T23:14:14.9759331Z env:
probe	UNKNOWN STEP	2026-09-26T23:14:14.9759605Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-26T23:14:14.9759954Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:14:14.9871106Z ===== Bazel 构建 第 1 次 =====
probe	UNKNOWN STEP	2026-09-26T23:15:04.4376766Z ----- 真实 error 行（最多 40 条）-----
probe	UNKNOWN STEP	2026-09-26T23:15:04.4395557Z 26:arch/arm64/configs/gki_defconfig:4:warning: unexpected data: ﻿#
probe	UNKNOWN STEP	2026-09-26T23:15:04.4397063Z 45:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/mm_types.h:559:1: error: extraneous closing brace ('}')
probe	UNKNOWN STEP	2026-09-26T23:15:04.4399361Z 305:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4400992Z 328:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4402153Z 351:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4403269Z 374:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4404362Z 397:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:139:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4405728Z 420:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:140:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4406827Z 443:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4408355Z 466:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4410209Z 489:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:144:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4411861Z 512:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4414205Z 535:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4416022Z 558:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4418105Z 581:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4419710Z 604:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:139:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4421309Z 627:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:140:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4422670Z 650:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4423647Z 673:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4424617Z 696:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:144:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4425562Z 719:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4426517Z 742:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:137:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4427463Z 765:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4428713Z 788:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:138:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4429690Z 811:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:139:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4431111Z 834:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:140:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4432812Z 857:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:8: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4434567Z 880:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:143:24: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4436361Z 903:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:144:3: note: expanded from macro '_SIG_SET_BINOP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4438422Z 926:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:173:27: note: expanded from macro '_SIG_SET_OP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4440448Z 929:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:185:24: note: expanded from macro '_sig_not'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4442200Z 952:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:173:10: note: expanded from macro '_SIG_SET_OP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4443965Z 975:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:174:20: note: expanded from macro '_SIG_SET_OP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4445747Z 978:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:185:24: note: expanded from macro '_sig_not'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4447492Z 1001:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:174:3: note: expanded from macro '_SIG_SET_OP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4449814Z 1024:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:176:27: note: expanded from macro '_SIG_SET_OP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4451062Z 1027:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:185:24: note: expanded from macro '_sig_not'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4452054Z 1050:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:176:10: note: expanded from macro '_SIG_SET_OP'
probe	UNKNOWN STEP	2026-09-26T23:15:04.4453044Z 1137:make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:118: arch/arm64/kernel/asm-offsets.s] Error 1
probe	UNKNOWN STEP	2026-09-26T23:15:04.4453927Z 1138:make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:1369: prepare0] Error 2
probe	UNKNOWN STEP	2026-09-26T23:15:04.4454435Z ----- tail 40 -----
probe	UNKNOWN STEP	2026-09-26T23:15:04.4454888Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/fs.h:33:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4455661Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/percpu-rwsem.h:7:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4456453Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/rcuwait.h:6:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4457228Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/sched/signal.h:6:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4458695Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:241:10: warning: array index 1 is past the end of the array (that has type 'unsigned long[1]') [-Warray-bounds]
probe	UNKNOWN STEP	2026-09-26T23:15:04.4459517Z         case 2: set->sig[1] = 0;
probe	UNKNOWN STEP	2026-09-26T23:15:04.4459756Z                 ^        ~
probe	UNKNOWN STEP	2026-09-26T23:15:04.4460332Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/uapi/asm-generic/signal.h:62:2: note: array 'sig' declared here
probe	UNKNOWN STEP	2026-09-26T23:15:04.4460952Z         unsigned long sig[_NSIG_WORDS];
probe	UNKNOWN STEP	2026-09-26T23:15:04.4461208Z         ^
probe	UNKNOWN STEP	2026-09-26T23:15:04.4461683Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/arch/arm64/kernel/asm-offsets.c:10:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4462491Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/arm_sdei.h:8:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4463264Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/acpi/ghes.h:5:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4463992Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/acpi/apei.h:9:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4464726Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/acpi.h:15:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4465472Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/device.h:32:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4466250Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/device/driver.h:21:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4467173Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/module.h:19:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4468200Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/elf.h:6:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4468970Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/arch/arm64/include/asm/elf.h:141:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4469735Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/fs.h:33:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4470502Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/percpu-rwsem.h:7:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4471297Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/rcuwait.h:6:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4472085Z In file included from /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/sched/signal.h:6:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4473294Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/linux/signal.h:254:10: warning: array index 1 is past the end of the array (that has type 'unsigned long[1]') [-Warray-bounds]
probe	UNKNOWN STEP	2026-09-26T23:15:04.4474100Z         case 2: set->sig[1] = -1;
probe	UNKNOWN STEP	2026-09-26T23:15:04.4474347Z                 ^        ~
probe	UNKNOWN STEP	2026-09-26T23:15:04.4474916Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/include/uapi/asm-generic/signal.h:62:2: note: array 'sig' declared here
probe	UNKNOWN STEP	2026-09-26T23:15:04.4475538Z         unsigned long sig[_NSIG_WORDS];
probe	UNKNOWN STEP	2026-09-26T23:15:04.4475785Z         ^
probe	UNKNOWN STEP	2026-09-26T23:15:04.4475975Z 49 warnings and 1 error generated.
probe	UNKNOWN STEP	2026-09-26T23:15:04.4476595Z make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:118: arch/arm64/kernel/asm-offsets.s] Error 1
probe	UNKNOWN STEP	2026-09-26T23:15:04.4477452Z make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:1369: prepare0] Error 2
probe	UNKNOWN STEP	2026-09-26T23:15:04.4478217Z make[1]: *** Waiting for unfinished jobs....
probe	UNKNOWN STEP	2026-09-26T23:15:04.4478516Z make: *** [Makefile:256: __sub-make] Error 2
probe	UNKNOWN STEP	2026-09-26T23:15:04.4478833Z Target //common:kernel_aarch64/Image failed to build
probe	UNKNOWN STEP	2026-09-26T23:15:04.4479245Z Use --verbose_failures to see the command lines of failed build steps.
probe	UNKNOWN STEP	2026-09-26T23:15:04.4479647Z INFO: Elapsed time: 49.309s, Critical Path: 22.69s
probe	UNKNOWN STEP	2026-09-26T23:15:04.4480038Z INFO: 276 processes: 265 internal, 1 local, 10 processwrapper-sandbox.
probe	UNKNOWN STEP	2026-09-26T23:15:04.4480418Z ERROR: Build did NOT complete successfully
probe	UNKNOWN STEP	2026-09-26T23:15:04.4654888Z 没有解析到缺失模块
probe	UNKNOWN STEP	2026-09-26T23:15:04.4690797Z 构建失败
probe	UNKNOWN STEP	2026-09-26T23:15:04.4704607Z ##[error]Process completed with exit code 1.
probe	UNKNOWN STEP	2026-09-26T23:15:04.4787129Z ##[group]Run actions/upload-artifact@v4
probe	UNKNOWN STEP	2026-09-26T23:15:04.4787435Z with:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4787624Z   name: bazel-log
probe	UNKNOWN STEP	2026-09-26T23:15:04.4788198Z   path: /tmp/bazel.log
probe	UNKNOWN STEP	2026-09-26T23:15:04.4788458Z   if-no-files-found: ignore
probe	UNKNOWN STEP	2026-09-26T23:15:04.4788703Z   compression-level: 6
probe	UNKNOWN STEP	2026-09-26T23:15:04.4788920Z   overwrite: false
probe	UNKNOWN STEP	2026-09-26T23:15:04.4789132Z   include-hidden-files: false
probe	UNKNOWN STEP	2026-09-26T23:15:04.4789377Z env:
probe	UNKNOWN STEP	2026-09-26T23:15:04.4789637Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-26T23:15:04.4789978Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-26T23:15:04.6459103Z (node:15627) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
probe	UNKNOWN STEP	2026-09-26T23:15:04.6460406Z (Use `node --trace-deprecation ...` to show where the warning was created)
probe	UNKNOWN STEP	2026-09-26T23:15:04.6519168Z With the provided path, there will be 1 file uploaded
probe	UNKNOWN STEP	2026-09-26T23:15:04.6527999Z Artifact name is valid!
probe	UNKNOWN STEP	2026-09-26T23:15:04.6528542Z Root directory input is valid!
probe	UNKNOWN STEP	2026-09-26T23:15:04.9821045Z Beginning upload of artifact content to blob storage
probe	UNKNOWN STEP	2026-09-26T23:15:05.0043096Z (node:15627) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
probe	UNKNOWN STEP	2026-09-26T23:15:05.2217715Z Uploaded bytes 3145
probe	UNKNOWN STEP	2026-09-26T23:15:05.2853788Z Finished uploading artifact content to blob storage!
probe	UNKNOWN STEP	2026-09-26T23:15:05.2854748Z SHA256 digest of uploaded artifact zip is bd2ce16a27818373bb9512cb48e41180540211a96f17394b79582925c58930a8
probe	UNKNOWN STEP	2026-09-26T23:15:05.2855720Z Finalizing artifact upload
probe	UNKNOWN STEP	2026-09-26T23:15:05.5302250Z Artifact bazel-log.zip successfully finalized. Artifact ID 10917773376
probe	UNKNOWN STEP	2026-09-26T23:15:05.5303513Z Artifact bazel-log has been successfully uploaded! Final size is 3145 bytes. Artifact ID is 10917773376
probe	UNKNOWN STEP	2026-09-26T23:15:05.5310746Z Artifact download URL: https://github.com/glboxed-max/GKI_KernelSU_SUSFS/actions/runs/36278613280/artifacts/10917773376
probe	UNKNOWN STEP	2026-09-26T23:15:05.5525439Z Post job cleanup.
probe	UNKNOWN STEP	2026-09-26T23:15:05.6377809Z [command]/usr/bin/git version
probe	UNKNOWN STEP	2026-09-26T23:15:05.6424088Z git version 2.55.0
probe	UNKNOWN STEP	2026-09-26T23:15:05.6468986Z Temporarily overriding HOME='/home/runner/work/_temp/444ba7fd-c7f9-4df5-a379-f5b95792b05b' before making global git config changes
probe	UNKNOWN STEP	2026-09-26T23:15:05.6469990Z Adding repository directory to the temporary git global config as a safe directory
probe	UNKNOWN STEP	2026-09-26T23:15:05.6475012Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS
probe	UNKNOWN STEP	2026-09-26T23:15:05.6514174Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
probe	UNKNOWN STEP	2026-09-26T23:15:05.6549878Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
probe	UNKNOWN STEP	2026-09-26T23:15:05.6826651Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
probe	UNKNOWN STEP	2026-09-26T23:15:05.6871069Z http.https://github.com/.extraheader
probe	UNKNOWN STEP	2026-09-26T23:15:05.6884179Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
probe	UNKNOWN STEP	2026-09-26T23:15:05.6950716Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
probe	UNKNOWN STEP	2026-09-26T23:15:05.7271918Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
probe	UNKNOWN STEP	2026-09-26T23:15:05.7364775Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
probe	UNKNOWN STEP	2026-09-26T23:15:05.7773406Z Cleaning up orphan processes
probe	UNKNOWN STEP	2026-09-26T23:15:05.8125382Z Terminate orphan process: pid (3122) (java.lang=ALL-UNNAMED)
probe	UNKNOWN STEP	2026-09-26T23:15:05.8177298Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```
