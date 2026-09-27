# 最近失败的 CRC Probe 运行 36327026403

## 元信息
```
name=CRC Probe (原厂 config ABI 对齐验证)
sha=cf000090a33a6cfbdfc3a6018c329d11e31a2a58
conclusion=failure
created=2026-09-27T14:44:44Z
updated=2026-09-27T15:04:04Z
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
probe	UNKNOWN STEP	2026-09-27T14:47:37.3972530Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-27T15:04:00.1046177Z 29:arch/arm64/configs/gki_defconfig:4:warning: unexpected data: ﻿#
probe	UNKNOWN STEP	2026-09-27T15:04:00.1048290Z 50:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:344:13: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1052301Z 57:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:560:21: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1055015Z 64:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:561:16: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1056566Z 71:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:562:48: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1057932Z 78:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:2822:22: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1059085Z 86:make[4]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:250: drivers/hid/wacom_sys.o] Error 1
probe	UNKNOWN STEP	2026-09-27T15:04:00.1059990Z 87:make[3]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: drivers/hid] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1061100Z 89:make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: drivers] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1061866Z 90:make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:2068: .] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1062373Z 91:make: *** [Makefile:256: __sub-make] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1071636Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:561:16: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1077868Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:562:48: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1085405Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:2822:22: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1101812Z make[4]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:250: drivers/hid/wacom_sys.o] Error 1
probe	UNKNOWN STEP	2026-09-27T15:04:00.1103347Z make[3]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: drivers/hid] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1105273Z make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: drivers] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1106597Z make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:2068: .] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1107542Z make: *** [Makefile:256: __sub-make] Error 2
```

## 失败步骤完整日志
```
probe	UNKNOWN STEP	2026-09-27T14:44:53.4518267Z hint:
probe	UNKNOWN STEP	2026-09-27T14:44:53.4518907Z hint: Disable this message with "git config set advice.defaultBranchName false"
probe	UNKNOWN STEP	2026-09-27T14:44:53.4525571Z Initialized empty Git repository in /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/.git/
probe	UNKNOWN STEP	2026-09-27T14:44:53.4537771Z [command]/usr/bin/git remote add origin https://github.com/glboxed-max/GKI_KernelSU_SUSFS
probe	UNKNOWN STEP	2026-09-27T14:44:53.4599658Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:44:53.4601436Z ##[group]Disabling automatic garbage collection
probe	UNKNOWN STEP	2026-09-27T14:44:53.4607852Z [command]/usr/bin/git config --local gc.auto 0
probe	UNKNOWN STEP	2026-09-27T14:44:53.4663784Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:44:53.4664725Z ##[group]Setting up auth
probe	UNKNOWN STEP	2026-09-27T14:44:53.4666685Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
probe	UNKNOWN STEP	2026-09-27T14:44:53.4705620Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
probe	UNKNOWN STEP	2026-09-27T14:44:53.5138652Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
probe	UNKNOWN STEP	2026-09-27T14:44:53.5176547Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
probe	UNKNOWN STEP	2026-09-27T14:44:53.5415311Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
probe	UNKNOWN STEP	2026-09-27T14:44:53.5456712Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
probe	UNKNOWN STEP	2026-09-27T14:44:53.5691424Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
probe	UNKNOWN STEP	2026-09-27T14:44:53.5734957Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:44:53.5736025Z ##[group]Fetching the repository
probe	UNKNOWN STEP	2026-09-27T14:44:53.5744997Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +cf000090a33a6cfbdfc3a6018c329d11e31a2a58:refs/remotes/origin/main
probe	UNKNOWN STEP	2026-09-27T14:44:54.3559203Z From https://github.com/glboxed-max/GKI_KernelSU_SUSFS
probe	UNKNOWN STEP	2026-09-27T14:44:54.3562983Z  * [new ref]         cf000090a33a6cfbdfc3a6018c329d11e31a2a58 -> origin/main
probe	UNKNOWN STEP	2026-09-27T14:44:54.3569899Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:44:54.3572525Z ##[group]Determining the checkout info
probe	UNKNOWN STEP	2026-09-27T14:44:54.3575368Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:44:54.3576764Z [command]/usr/bin/git sparse-checkout disable
probe	UNKNOWN STEP	2026-09-27T14:44:54.3636601Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
probe	UNKNOWN STEP	2026-09-27T14:44:54.3674047Z ##[group]Checking out the ref
probe	UNKNOWN STEP	2026-09-27T14:44:54.3679034Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
probe	UNKNOWN STEP	2026-09-27T14:44:54.3951757Z Switched to a new branch 'main'
probe	UNKNOWN STEP	2026-09-27T14:44:54.3956466Z branch 'main' set up to track 'origin/main'.
probe	UNKNOWN STEP	2026-09-27T14:44:54.3965925Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:44:54.4014215Z [command]/usr/bin/git log -1 --format=%H
probe	UNKNOWN STEP	2026-09-27T14:44:54.4042801Z cf000090a33a6cfbdfc3a6018c329d11e31a2a58
probe	UNKNOWN STEP	2026-09-27T14:44:54.4315868Z ##[group]Run sudo rm -rf /usr/share/dotnet /opt/ghc /usr/local/lib/android/sdk /usr/local/share/boost \
probe	UNKNOWN STEP	2026-09-27T14:44:54.4319021Z ^[[36;1msudo rm -rf /usr/share/dotnet /opt/ghc /usr/local/lib/android/sdk /usr/local/share/boost \^[[0m
probe	UNKNOWN STEP	2026-09-27T14:44:54.4322008Z ^[[36;1m            /opt/hostedtoolcache/CodeQL "$AGENT_TOOLSDIRECTORY" 2>/dev/null || true^[[0m
probe	UNKNOWN STEP	2026-09-27T14:44:54.4324205Z ^[[36;1mdf -h /^[[0m
probe	UNKNOWN STEP	2026-09-27T14:44:54.4642916Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-27T14:44:54.4644271Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:46:19.2038338Z Filesystem      Size  Used Avail Use% Mounted on
probe	UNKNOWN STEP	2026-09-27T14:46:19.2039126Z /dev/root       145G   37G  108G  26% /
probe	UNKNOWN STEP	2026-09-27T14:46:19.2084610Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-27T14:46:19.2084956Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.2085433Z ^[[36;1mmkdir -p "$GITHUB_WORKSPACE/git-repo" "$GITHUB_WORKSPACE/kernel" "$GITHUB_WORKSPACE/AnyKernel3"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.2086186Z ^[[36;1mcurl -sSL https://storage.googleapis.com/git-repo-downloads/repo -o "$GITHUB_WORKSPACE/git-repo/repo"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.2086781Z ^[[36;1mchmod +x "$GITHUB_WORKSPACE/git-repo/repo"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.2087152Z ^[[36;1mecho "$GITHUB_WORKSPACE/git-repo" >> "$GITHUB_PATH"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.2155174Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-27T14:46:19.2155508Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:46:19.3201030Z Prepare all required actions
probe	UNKNOWN STEP	2026-09-27T14:46:19.3393391Z ##[group]Run ./.github/actions/download-kernel
probe	UNKNOWN STEP	2026-09-27T14:46:19.3393730Z with:
probe	UNKNOWN STEP	2026-09-27T14:46:19.3393936Z   android_version: android14
probe	UNKNOWN STEP	2026-09-27T14:46:19.3394179Z   kernel_version: 6.1
probe	UNKNOWN STEP	2026-09-27T14:46:19.3394445Z   version: android14-6.1
probe	UNKNOWN STEP	2026-09-27T14:46:19.3394685Z   os_patch_level: 2025-09
probe	UNKNOWN STEP	2026-09-27T14:46:19.3394914Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:46:19.3451916Z ##[start-action display=Initialize and Sync Kernel Repository;id=__self.sync]
probe	UNKNOWN STEP	2026-09-27T14:46:19.3500393Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-27T14:46:19.3500983Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3501221Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3501564Z ^[[36;1m# Derive android and kernel from combined version when available^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3501956Z ^[[36;1mVERSION="android14-6.1"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3502271Z ^[[36;1mANDROID_PART=$(echo "$VERSION" | cut -d- -f1)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3502674Z ^[[36;1mKERNEL_PART=$(echo "$VERSION" | cut -d- -f2)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3503074Z ^[[36;1mFORMATTED_BRANCH="${ANDROID_PART}-${KERNEL_PART}-2025-09"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3503417Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3503608Z ^[[36;1minit_repo() {^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3503834Z ^[[36;1m  local depth="$1"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3504073Z ^[[36;1m  local depth_flag=""^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3504326Z ^[[36;1m  if [ "$depth" != "0" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3504607Z ^[[36;1m    depth_flag="--depth=${depth}"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3504876Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3505525Z ^[[36;1m  repo init -u https://android.googlesource.com/kernel/manifest -b common-${FORMATTED_BRANCH} ${depth_flag} || { echo "ERROR: repo init failed" >&2; return 1; }^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3506622Z ^[[36;1m  REMOTE_BRANCH=$(git ls-remote https://android.googlesource.com/kernel/common ${FORMATTED_BRANCH}) || { echo "ERROR: git ls-remote failed" >&2; return 1; }^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3507354Z ^[[36;1m  DEFAULT_MANIFEST_PATH=.repo/manifests/default.xml^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3507817Z ^[[36;1m  DEPRECATED=false^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3508306Z ^[[36;1m  if grep -q deprecated <<< "$REMOTE_BRANCH"; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3509158Z ^[[36;1m    sed -i "s/\"${FORMATTED_BRANCH}\"/\"deprecated\/${FORMATTED_BRANCH}\"/g" "$DEFAULT_MANIFEST_PATH"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3509783Z ^[[36;1m    echo "[!] Note: Branch ${FORMATTED_BRANCH} is considered deprecated."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3510192Z ^[[36;1m    DEPRECATED=true^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3510452Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3510876Z ^[[36;1m  echo "deprecated=$DEPRECATED" >> $GITHUB_OUTPUT^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3511300Z ^[[36;1m  # Google retires old monthly heads entirely (neither live nor^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3511768Z ^[[36;1m  # deprecated/); the manifest still pins common to the dead^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3512224Z ^[[36;1m  # branch. Fall back to the latest immutable release tag so the^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3512645Z ^[[36;1m  # build keeps working. Tags are never deleted.^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3512984Z ^[[36;1m  TAG_FALLBACK=""^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3513528Z ^[[36;1m  if [ "$DEPRECATED" = "false" ] && [ -z "$REMOTE_BRANCH" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3514587Z ^[[36;1m    LATEST_TAG=$(git ls-remote https://android.googlesource.com/kernel/common "refs/tags/${FORMATTED_BRANCH}_r*" 2>/dev/null | awk '{print $2}' | grep -v '\^{}$' | sed 's|refs/tags/||' | awk -F'_r' '{print $NF+0, $0}' | sort -n | tail -n 1 | cut -d' ' -f2- || true)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3515915Z ^[[36;1m    if [ -n "$LATEST_TAG" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3516666Z ^[[36;1m      echo "[!] Note: Branch ${FORMATTED_BRANCH} head missing upstream; using tag ${LATEST_TAG}."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3517849Z ^[[36;1m      sed -i "/path=\"common\"/ s/revision=\"${FORMATTED_BRANCH}\"/revision=\"${LATEST_TAG}\"/" "$DEFAULT_MANIFEST_PATH"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3518747Z ^[[36;1m      TAG_FALLBACK="$LATEST_TAG"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3519188Z ^[[36;1m    else^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3520233Z ^[[36;1m      echo "WARNING: no head or tag found for ${FORMATTED_BRANCH}; sync will likely fail." >&2^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3521397Z ^[[36;1m    fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3521744Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3522087Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3522616Z ^[[36;1m  # 有些月份 AOSP 的 manifest 直接把 common 钉成 `_rNN` 发布 tag（而不是分支）。^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3523060Z ^[[36;1m  # 这种情况下 refs/heads/<rev> 不存在，必须允许按 tag 拉取；否则 repo 会 fetch^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3523533Z ^[[36;1m  # refs/heads/androidXX-YY-YYYY-MM_rNN 并报 "couldn't find remote ref"。^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3523938Z ^[[36;1m  MANIFEST_TAG=""^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3524537Z ^[[36;1m  MANIFEST_COMMON_REV="$(grep -E 'path="common"' "$DEFAULT_MANIFEST_PATH" 2>/dev/null | grep -oE 'revision="[^"]+"' | head -n1 | cut -d'"' -f2 || true)"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3525242Z ^[[36;1m  if [[ "$MANIFEST_COMMON_REV" =~ _r[0-9]+$ ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3525587Z ^[[36;1m    MANIFEST_TAG="$MANIFEST_COMMON_REV"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3526018Z ^[[36;1m    echo "[!] manifest pins common to release tag '${MANIFEST_TAG}'; 将允许 tag 拉取。"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3526448Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3526718Z ^[[36;1m  echo "tag_fallback=$TAG_FALLBACK" >> $GITHUB_OUTPUT^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3527121Z ^[[36;1m  echo "manifest_tag=$MANIFEST_TAG" >> $GITHUB_OUTPUT^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3527434Z ^[[36;1m}^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3527619Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3527813Z ^[[36;1mMAX_RETRIES=3^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3528044Z ^[[36;1mRETRY_DELAY_SHORT=15^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3528288Z ^[[36;1mSYNC_TIMEOUT="15m"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3528522Z ^[[36;1mattempt=1^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3528852Z ^[[36;1m# Always shallow: the build only needs the branch tip. Deeper retries^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3529350Z ^[[36;1m# just download more data into a strained runner (slower + more disk).^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3529741Z ^[[36;1mDEPTHS=(1 1 1)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3529963Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3530159Z ^[[36;1mclean_workspace() {^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3530416Z ^[[36;1m  echo "Disk before cleanup:"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3530910Z ^[[36;1m  df -h "$PWD" | tail -n +2 || true^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3531326Z ^[[36;1m  # Remove repo metadata AND any half-checked-out project dirs from the^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3531842Z ^[[36;1m  # previous attempt. Deleting only .repo leaves stale checkouts behind^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3532371Z ^[[36;1m  # and every later sync fails with "Checking out local projects failed".^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3532831Z ^[[36;1m  find "$PWD" -mindepth 1 -maxdepth 1 -exec rm -rf {} +^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3533184Z ^[[36;1m  echo "Disk after cleanup:"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3533467Z ^[[36;1m  df -h "$PWD" | tail -n +2 || true^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3533736Z ^[[36;1m}^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3533916Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3534136Z ^[[36;1mwhile [ $attempt -le $MAX_RETRIES ]; do^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3534470Z ^[[36;1m  CURRENT_DEPTH="${DEPTHS[$((attempt-1))]}"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3535108Z ^[[36;1m  echo "Attempt $attempt/$MAX_RETRIES: initialize and sync kernel repository (depth=${CURRENT_DEPTH}, sync timeout $SYNC_TIMEOUT)..."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3535979Z ^[[36;1m  df -h "$PWD" | tail -n +2 || true^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3536283Z ^[[36;1m  if init_repo "$CURRENT_DEPTH"; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3536650Z ^[[36;1m    # 默认最小浅克隆；若本次需要按 tag 拉取（tag fallback 或 manifest 用 _rNN tag），^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3537090Z ^[[36;1m    # 则去掉 -c/--current-branch 与 --no-tags，确保 repo 能取到 tag。^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3537598Z ^[[36;1m    SYNC_ARGS=(-c --current-branch --no-clone-bundle --no-tags --jobs-checkout=4 -j4)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3538118Z ^[[36;1m    if [ -n "$TAG_FALLBACK" ] || [ -n "${MANIFEST_TAG:-}" ]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3538532Z ^[[36;1m      SYNC_ARGS=(--no-clone-bundle --jobs-checkout=4 -j4)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3538860Z ^[[36;1m    fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3539139Z ^[[36;1m    if timeout $SYNC_TIMEOUT repo sync "${SYNC_ARGS[@]}"; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3539653Z ^[[36;1m      echo "Kernel repository initialization and sync succeeded on attempt $attempt."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3540219Z ^[[36;1m      break^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3540435Z ^[[36;1m    else^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3540769Z ^[[36;1m      rc=$?^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3540989Z ^[[36;1m      if [ $rc -eq 124 ]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3541322Z ^[[36;1m        echo "repo sync timed out after $SYNC_TIMEOUT."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3541641Z ^[[36;1m      else^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3541906Z ^[[36;1m        echo "repo sync failed with exit code $rc."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3542478Z ^[[36;1m      fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3542828Z ^[[36;1m    fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3543154Z ^[[36;1m  else^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3543487Z ^[[36;1m    rc=$?^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3544047Z ^[[36;1m    echo "repo init or branch preflight failed with exit code $rc."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3544763Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3545122Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3545503Z ^[[36;1m  if [ $attempt -lt $MAX_RETRIES ]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3546271Z ^[[36;1m    echo "Cleaning workspace and retrying after ${RETRY_DELAY_SHORT}s..."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3546930Z ^[[36;1m    clean_workspace || true^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3547209Z ^[[36;1m    sleep $RETRY_DELAY_SHORT^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3547461Z ^[[36;1m  else^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3547709Z ^[[36;1m    echo "All $MAX_RETRIES attempts failed." >&2^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3548016Z ^[[36;1m    exit $rc^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3548219Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3548429Z ^[[36;1m  attempt=$((attempt+1))^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3548678Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-27T14:46:19.3624087Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
probe	UNKNOWN STEP	2026-09-27T14:46:19.3624468Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:46:19.3754429Z Attempt 1/3: initialize and sync kernel repository (depth=1, sync timeout 15m)...
probe	UNKNOWN STEP	2026-09-27T14:46:19.3772267Z /dev/root       145G   37G  108G  26% /
probe	UNKNOWN STEP	2026-09-27T14:46:22.1433109Z 
probe	UNKNOWN STEP	2026-09-27T14:46:22.1433958Z repo has been initialized in /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel
probe	UNKNOWN STEP	2026-09-27T14:47:37.2025936Z Finalizing sync state...
probe	UNKNOWN STEP	2026-09-27T14:47:37.2026711Z repo sync has finished successfully.
probe	UNKNOWN STEP	2026-09-27T14:47:37.2305647Z Kernel repository initialization and sync succeeded on attempt 1.
probe	UNKNOWN STEP	2026-09-27T14:47:37.2339034Z ##[end-action id=__self.sync;outcome=success;conclusion=success;duration_ms=77888]
probe	UNKNOWN STEP	2026-09-27T14:47:37.2344984Z ##[start-action display=Capture Kernel Common Commit Metadata;id=__self.__run]
probe	UNKNOWN STEP	2026-09-27T14:47:37.2366862Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-27T14:47:37.2367170Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2367397Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2367596Z ^[[36;1mif [[ ! -d common ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2368006Z ^[[36;1m  echo "WARNING: common folder not found; skipping commit metadata capture."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2368415Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2368608Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2368788Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2368969Z ^[[36;1mcd common^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2369165Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2369361Z ^[[36;1mif [[ ! -d .git ]]; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2369796Z ^[[36;1m  echo "WARNING: common is not a git checkout; skipping commit metadata capture."^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2370397Z ^[[36;1m  exit 0^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2370836Z ^[[36;1mfi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2371067Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2371296Z ^[[36;1mCOMMIT_DATE=$(git log -1 --format=%cI)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2371623Z ^[[36;1mCOMMIT_MSG=$(git log -1 --format=%s)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2371934Z ^[[36;1mCOMMIT_SHA=$(git rev-parse HEAD)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2372208Z ^[[36;1m^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2372478Z ^[[36;1mecho "KERNEL_SOURCE_COMMIT=$COMMIT_SHA" >> "$GITHUB_ENV"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2372880Z ^[[36;1mecho "Kernel common commit date: $COMMIT_DATE"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2373239Z ^[[36;1mecho "Kernel common commit msg: $COMMIT_MSG"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2373594Z ^[[36;1mecho "Kernel common commit SHA: $COMMIT_SHA"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2438171Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
probe	UNKNOWN STEP	2026-09-27T14:47:37.2438613Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:47:37.2592534Z Kernel common commit date: 2026-09-24T21:53:04Z
probe	UNKNOWN STEP	2026-09-27T14:47:37.2593879Z Kernel common commit msg: ANDROID: netfilter: xt_quota2: fix UAF in q2_get_counter error path
probe	UNKNOWN STEP	2026-09-27T14:47:37.2594841Z Kernel common commit SHA: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-27T14:47:37.2609756Z ##[end-action id=__self.__run;outcome=success;conclusion=success;duration_ms=26]
probe	UNKNOWN STEP	2026-09-27T14:47:37.2682633Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-27T14:47:37.2682997Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2683356Z ^[[36;1mcp "$GITHUB_WORKSPACE/.github/config/vivo_pd2339_a16_defconfig" \^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2683861Z ^[[36;1m   "$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2684485Z ^[[36;1mecho "配置行数: $(grep -c . "$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig")"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2749290Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-27T14:47:37.2749572Z env:
probe	UNKNOWN STEP	2026-09-27T14:47:37.2749873Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-27T14:47:37.2750240Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:47:37.2875176Z 配置行数: 8766
probe	UNKNOWN STEP	2026-09-27T14:47:37.2931279Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-27T14:47:37.2931662Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2932040Z ^[[36;1mD="$GITHUB_WORKSPACE/kernel/common/arch/arm64/configs/gki_defconfig"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2932551Z ^[[36;1msed -i 's/^CONFIG_WERROR=y/# CONFIG_WERROR is not set/' "$D"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2933039Z ^[[36;1mgrep -q '^\(# \)\?CONFIG_WERROR' "$D" || echo '# CONFIG_WERROR is not set' >> "$D"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2933457Z ^[[36;1mgrep -n 'CONFIG_WERROR' "$D"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.2997861Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-27T14:47:37.2998149Z env:
probe	UNKNOWN STEP	2026-09-27T14:47:37.2998438Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-27T14:47:37.2998795Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:47:37.3148565Z 27:# CONFIG_WERROR is not set
probe	UNKNOWN STEP	2026-09-27T14:47:37.3184382Z ##[group]Run set -euo pipefail
probe	UNKNOWN STEP	2026-09-27T14:47:37.3184731Z ^[[36;1mset -euo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3185021Z ^[[36;1mSRC="$GITHUB_WORKSPACE/.github/patches/abi"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3185380Z ^[[36;1mcd "$GITHUB_WORKSPACE/kernel/common"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3185666Z ^[[36;1mn=0^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3185875Z ^[[36;1mwhile IFS= read -r f; do^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3186144Z ^[[36;1m  rel="${f#$SRC/}"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3186381Z ^[[36;1m  cp "$f" "$rel"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3186610Z ^[[36;1m  echo "[+] 覆盖 $rel"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3186843Z ^[[36;1m  n=$((n+1))^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3187069Z ^[[36;1mdone < <(find "$SRC" -type f)^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3187339Z ^[[36;1mecho "共应用 $n 个头文件补丁"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3251366Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-27T14:47:37.3251659Z env:
probe	UNKNOWN STEP	2026-09-27T14:47:37.3251959Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-27T14:47:37.3252331Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:47:37.3378436Z [+] 覆盖 include/trace/events/mmflags.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3395281Z [+] 覆盖 include/uapi/linux/android/binder.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3412639Z [+] 覆盖 include/linux/mm.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3448725Z [+] 覆盖 include/linux/mmzone.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3465853Z [+] 覆盖 include/linux/page-flags.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3482799Z [+] 覆盖 include/linux/cgroup_subsys.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3499252Z [+] 覆盖 include/linux/sched.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3515631Z [+] 覆盖 include/linux/skbuff.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3531761Z [+] 覆盖 include/linux/workqueue.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3547675Z [+] 覆盖 include/linux/pageblock-flags.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3563862Z [+] 覆盖 include/linux/fs.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3580073Z [+] 覆盖 include/linux/pagemap.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3597054Z [+] 覆盖 include/linux/task_io_accounting.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3613737Z [+] 覆盖 include/linux/blk_types.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3629311Z [+] 覆盖 include/linux/slub_def.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3645424Z [+] 覆盖 include/linux/mm_types.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3662351Z [+] 覆盖 include/linux/blk-mq.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3679782Z [+] 覆盖 include/net/sock.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3697652Z [+] 覆盖 kernel/cgroup/cgroup.c
probe	UNKNOWN STEP	2026-09-27T14:47:37.3714642Z [+] 覆盖 kernel/kthread.c
probe	UNKNOWN STEP	2026-09-27T14:47:37.3731066Z [+] 覆盖 kernel/sched/sched.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3748036Z [+] 覆盖 kernel/futex/futex.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3765551Z [+] 覆盖 drivers/md/dm-core.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3781439Z [+] 覆盖 drivers/hid/wacom_wac.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3798235Z [+] 覆盖 drivers/staging/android/ashmem.c
probe	UNKNOWN STEP	2026-09-27T14:47:37.3815373Z [+] 覆盖 drivers/android/binder_internal.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3832241Z [+] 覆盖 fs/f2fs/f2fs.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3848971Z [+] 覆盖 mm/slub.c
probe	UNKNOWN STEP	2026-09-27T14:47:37.3867130Z [+] 覆盖 mm/page_alloc.c
probe	UNKNOWN STEP	2026-09-27T14:47:37.3883652Z [+] 覆盖 mm/slab.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3899847Z [+] 覆盖 mm/vmstat.c
probe	UNKNOWN STEP	2026-09-27T14:47:37.3916510Z [+] 覆盖 mm/vmscan.c
probe	UNKNOWN STEP	2026-09-27T14:47:37.3932538Z [+] 覆盖 block/elevator.h
probe	UNKNOWN STEP	2026-09-27T14:47:37.3933034Z 共应用 33 个头文件补丁
probe	UNKNOWN STEP	2026-09-27T14:47:37.3967506Z ##[group]Run set -uo pipefail
probe	UNKNOWN STEP	2026-09-27T14:47:37.3967847Z ^[[36;1mset -uo pipefail^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3968170Z ^[[36;1msed -i 's/check_defconfig//' ./common/build.config.gki^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3968703Z ^[[36;1msed -i '/name = "kernel_aarch64",/a\    check_defconfig = "disabled",' common/BUILD.bazel^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3969180Z ^[[36;1mok=0^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3969387Z ^[[36;1mfor i in 1 2 3 4; do^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3969651Z ^[[36;1m  echo "===== Bazel 构建 第 $i 次 ====="^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3970090Z ^[[36;1m  if tools/bazel build --config=fast --disk_cache=/home/runner/.cache/bazel \^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3970599Z ^[[36;1m       //common:kernel_aarch64/Image > /tmp/bazel.log 2>&1; then^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3971314Z ^[[36;1m    ok=1; break^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3971540Z ^[[36;1m  fi^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3971781Z ^[[36;1m  echo "----- 真实 error 行（最多 40 条）-----"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3972530Z ^[[36;1m  grep -n -m 40 -E "error:|Error [0-9]|fatal error|BUILD_BUG_ON|No such file or directory|undeclared|note: expanded from macro|expected" /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3973199Z ^[[36;1m  echo "----- tail 40 -----"^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3973483Z ^[[36;1m  tail -40 /tmp/bazel.log || true^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3974017Z ^[[36;1m  python3 "$GITHUB_WORKSPACE/.github/tools/bazel_module_outs.py" /tmp/bazel.log common/BUILD.bazel || break^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3974537Z ^[[36;1mdone^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.3974762Z ^[[36;1m[ "$ok" = "1" ] || { echo "构建失败"; exit 1; }^[[0m
probe	UNKNOWN STEP	2026-09-27T14:47:37.4039455Z shell: /usr/bin/bash -e {0}
probe	UNKNOWN STEP	2026-09-27T14:47:37.4039748Z env:
probe	UNKNOWN STEP	2026-09-27T14:47:37.4040036Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-27T14:47:37.4040401Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T14:47:37.4163361Z ===== Bazel 构建 第 1 次 =====
probe	UNKNOWN STEP	2026-09-27T15:04:00.1022331Z ----- 真实 error 行（最多 40 条）-----
probe	UNKNOWN STEP	2026-09-27T15:04:00.1046177Z 29:arch/arm64/configs/gki_defconfig:4:warning: unexpected data: ﻿#
probe	UNKNOWN STEP	2026-09-27T15:04:00.1048290Z 50:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:344:13: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1052301Z 57:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:560:21: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1055015Z 64:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:561:16: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1056566Z 71:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:562:48: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1057932Z 78:/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:2822:22: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1059085Z 86:make[4]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:250: drivers/hid/wacom_sys.o] Error 1
probe	UNKNOWN STEP	2026-09-27T15:04:00.1059990Z 87:make[3]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: drivers/hid] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1061100Z 89:make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: drivers] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1061866Z 90:make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:2068: .] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1062373Z 91:make: *** [Makefile:256: __sub-make] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1062675Z ----- tail 40 -----
probe	UNKNOWN STEP	2026-09-27T15:04:00.1065602Z         if (r && hid_data->inputmode_field_index >= 0 &&
probe	UNKNOWN STEP	2026-09-27T15:04:00.1066639Z                            ^~~~~~~~~~~~~~~~~~~~~
probe	UNKNOWN STEP	2026-09-27T15:04:00.1067246Z                            inputmode_index
probe	UNKNOWN STEP	2026-09-27T15:04:00.1068279Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_wac.h:299:8: note: 'inputmode_index' declared here
probe	UNKNOWN STEP	2026-09-27T15:04:00.1069469Z         __s16 inputmode_index;  /* InputMode HID feature index in the report */
probe	UNKNOWN STEP	2026-09-27T15:04:00.1070103Z               ^
probe	UNKNOWN STEP	2026-09-27T15:04:00.1071636Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:561:16: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1072945Z             hid_data->inputmode_field_index < r->maxfield) {
probe	UNKNOWN STEP	2026-09-27T15:04:00.1073458Z                       ^~~~~~~~~~~~~~~~~~~~~
probe	UNKNOWN STEP	2026-09-27T15:04:00.1073870Z                       inputmode_index
probe	UNKNOWN STEP	2026-09-27T15:04:00.1074793Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_wac.h:299:8: note: 'inputmode_index' declared here
probe	UNKNOWN STEP	2026-09-27T15:04:00.1075943Z         __s16 inputmode_index;  /* InputMode HID feature index in the report */
probe	UNKNOWN STEP	2026-09-27T15:04:00.1076651Z               ^
probe	UNKNOWN STEP	2026-09-27T15:04:00.1077868Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:562:48: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1079400Z                 struct hid_field *field = r->field[hid_data->inputmode_field_index];
probe	UNKNOWN STEP	2026-09-27T15:04:00.1080121Z                                                              ^~~~~~~~~~~~~~~~~~~~~
probe	UNKNOWN STEP	2026-09-27T15:04:00.1081060Z                                                              inputmode_index
probe	UNKNOWN STEP	2026-09-27T15:04:00.1082175Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_wac.h:299:8: note: 'inputmode_index' declared here
probe	UNKNOWN STEP	2026-09-27T15:04:00.1083448Z         __s16 inputmode_index;  /* InputMode HID feature index in the report */
probe	UNKNOWN STEP	2026-09-27T15:04:00.1084121Z               ^
probe	UNKNOWN STEP	2026-09-27T15:04:00.1085405Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_sys.c:2822:22: error: no member named 'inputmode_field_index' in 'struct hid_data'; did you mean 'inputmode_index'?
probe	UNKNOWN STEP	2026-09-27T15:04:00.1086930Z         wacom_wac->hid_data.inputmode_field_index = -1;
probe	UNKNOWN STEP	2026-09-27T15:04:00.1087792Z                             ^~~~~~~~~~~~~~~~~~~~~
probe	UNKNOWN STEP	2026-09-27T15:04:00.1088265Z                             inputmode_index
probe	UNKNOWN STEP	2026-09-27T15:04:00.1089299Z /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/drivers/hid/wacom_wac.h:299:8: note: 'inputmode_index' declared here
probe	UNKNOWN STEP	2026-09-27T15:04:00.1090547Z         __s16 inputmode_index;  /* InputMode HID feature index in the report */
probe	UNKNOWN STEP	2026-09-27T15:04:00.1100166Z               ^
probe	UNKNOWN STEP	2026-09-27T15:04:00.1100523Z 5 errors generated.
probe	UNKNOWN STEP	2026-09-27T15:04:00.1101812Z make[4]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:250: drivers/hid/wacom_sys.o] Error 1
probe	UNKNOWN STEP	2026-09-27T15:04:00.1103347Z make[3]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: drivers/hid] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1104308Z make[3]: *** Waiting for unfinished jobs....
probe	UNKNOWN STEP	2026-09-27T15:04:00.1105273Z make[2]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/scripts/Makefile.build:503: drivers] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1106597Z make[1]: *** [/home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS/kernel/common/Makefile:2068: .] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1107542Z make: *** [Makefile:256: __sub-make] Error 2
probe	UNKNOWN STEP	2026-09-27T15:04:00.1108096Z Target //common:kernel_aarch64/Image failed to build
probe	UNKNOWN STEP	2026-09-27T15:04:00.1108794Z Use --verbose_failures to see the command lines of failed build steps.
probe	UNKNOWN STEP	2026-09-27T15:04:00.1109426Z [276 / 278] checking cached actions
probe	UNKNOWN STEP	2026-09-27T15:04:00.1109928Z INFO: Elapsed time: 982.488s, Critical Path: 956.11s
probe	UNKNOWN STEP	2026-09-27T15:04:00.1111167Z INFO: 276 processes: 265 internal, 1 local, 10 processwrapper-sandbox.
probe	UNKNOWN STEP	2026-09-27T15:04:00.1111880Z ERROR: Build did NOT complete successfully
probe	UNKNOWN STEP	2026-09-27T15:04:00.1297535Z 没有解析到缺失模块
probe	UNKNOWN STEP	2026-09-27T15:04:00.1339200Z 构建失败
probe	UNKNOWN STEP	2026-09-27T15:04:00.1357817Z ##[error]Process completed with exit code 1.
probe	UNKNOWN STEP	2026-09-27T15:04:00.1500928Z ##[group]Run actions/upload-artifact@v4
probe	UNKNOWN STEP	2026-09-27T15:04:00.1501286Z with:
probe	UNKNOWN STEP	2026-09-27T15:04:00.1501482Z   name: bazel-log
probe	UNKNOWN STEP	2026-09-27T15:04:00.1501694Z   path: /tmp/bazel.log
probe	UNKNOWN STEP	2026-09-27T15:04:00.1501924Z   if-no-files-found: ignore
probe	UNKNOWN STEP	2026-09-27T15:04:00.1502161Z   compression-level: 6
probe	UNKNOWN STEP	2026-09-27T15:04:00.1502381Z   overwrite: false
probe	UNKNOWN STEP	2026-09-27T15:04:00.1502590Z   include-hidden-files: false
probe	UNKNOWN STEP	2026-09-27T15:04:00.1502816Z env:
probe	UNKNOWN STEP	2026-09-27T15:04:00.1503070Z   KERNEL_SOURCE_COMMIT: 885bb3fe06d567751d15e7a7ba02e8ccc5dac01e
probe	UNKNOWN STEP	2026-09-27T15:04:00.1503415Z ##[endgroup]
probe	UNKNOWN STEP	2026-09-27T15:04:00.5452855Z (node:124989) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
probe	UNKNOWN STEP	2026-09-27T15:04:00.5453711Z (Use `node --trace-deprecation ...` to show where the warning was created)
probe	UNKNOWN STEP	2026-09-27T15:04:00.5510855Z With the provided path, there will be 1 file uploaded
probe	UNKNOWN STEP	2026-09-27T15:04:00.5531406Z Artifact name is valid!
probe	UNKNOWN STEP	2026-09-27T15:04:00.5533651Z Root directory input is valid!
probe	UNKNOWN STEP	2026-09-27T15:04:00.8733374Z Beginning upload of artifact content to blob storage
probe	UNKNOWN STEP	2026-09-27T15:04:00.8987335Z (node:124989) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
probe	UNKNOWN STEP	2026-09-27T15:04:01.0667594Z Uploaded bytes 1622
probe	UNKNOWN STEP	2026-09-27T15:04:01.1181518Z Finished uploading artifact content to blob storage!
probe	UNKNOWN STEP	2026-09-27T15:04:01.1182742Z SHA256 digest of uploaded artifact zip is 1b40c7bae34a33d43f02b85801e6499ff46b99acb39417d52661538d83bc3d55
probe	UNKNOWN STEP	2026-09-27T15:04:01.1184017Z Finalizing artifact upload
probe	UNKNOWN STEP	2026-09-27T15:04:01.3440386Z Artifact bazel-log.zip successfully finalized. Artifact ID 10934513034
probe	UNKNOWN STEP	2026-09-27T15:04:01.3442056Z Artifact bazel-log has been successfully uploaded! Final size is 1622 bytes. Artifact ID is 10934513034
probe	UNKNOWN STEP	2026-09-27T15:04:01.3451915Z Artifact download URL: https://github.com/glboxed-max/GKI_KernelSU_SUSFS/actions/runs/36327026403/artifacts/10934513034
probe	UNKNOWN STEP	2026-09-27T15:04:01.3674991Z Post job cleanup.
probe	UNKNOWN STEP	2026-09-27T15:04:01.4622211Z [command]/usr/bin/git version
probe	UNKNOWN STEP	2026-09-27T15:04:01.4709831Z git version 2.55.0
probe	UNKNOWN STEP	2026-09-27T15:04:01.4753100Z Temporarily overriding HOME='/home/runner/work/_temp/64f5727a-a5c8-46f3-adc3-a7e8b07d90e5' before making global git config changes
probe	UNKNOWN STEP	2026-09-27T15:04:01.4754574Z Adding repository directory to the temporary git global config as a safe directory
probe	UNKNOWN STEP	2026-09-27T15:04:01.4760121Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/GKI_KernelSU_SUSFS/GKI_KernelSU_SUSFS
probe	UNKNOWN STEP	2026-09-27T15:04:01.4810904Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
probe	UNKNOWN STEP	2026-09-27T15:04:01.4857158Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
probe	UNKNOWN STEP	2026-09-27T15:04:01.5175212Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
probe	UNKNOWN STEP	2026-09-27T15:04:01.5205080Z http.https://github.com/.extraheader
probe	UNKNOWN STEP	2026-09-27T15:04:01.5218661Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
probe	UNKNOWN STEP	2026-09-27T15:04:01.5261402Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
probe	UNKNOWN STEP	2026-09-27T15:04:01.5526862Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
probe	UNKNOWN STEP	2026-09-27T15:04:01.5572778Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
probe	UNKNOWN STEP	2026-09-27T15:04:01.6005473Z Cleaning up orphan processes
probe	UNKNOWN STEP	2026-09-27T15:04:01.6414251Z Terminate orphan process: pid (3192) (java.lang=ALL-UNNAMED)
probe	UNKNOWN STEP	2026-09-27T15:04:01.6474934Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```
