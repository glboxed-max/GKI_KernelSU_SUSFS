#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 Kleaf 报错里解析「built but not copied」的模块，
把它们并进 common/BUILD.bazel 的 kernel_aarch64 的 module_implicit_outs（幂等）。
用法: bazel_module_outs.py <日志> <BUILD.bazel>
"""
import re
import sys

log_path, bazel_path = sys.argv[1], sys.argv[2]
log = open(log_path, encoding='utf-8', errors='replace').read()

mods = []
start = log.find('built but not copied')
if start >= 0:
    seg = log[start:]
    end = seg.find('Alternatively')
    if end >= 0:
        seg = seg[:end]
    mods = re.findall(r'"([A-Za-z0-9_\-/\.]+\.ko)"', seg)
mods = sorted(set(mods))
if not mods:
    print('没有解析到缺失模块')
    sys.exit(1)

text = open(bazel_path, encoding='utf-8').read()

# 先把我之前误加的 "module_outs": [...] 块删掉（Kleaf 不接受该键）
text = re.sub(r'\n\s*"module_outs":\s*\[.*?\],', '', text, flags=re.S)

m = re.search(r'("kernel_aarch64":\s*\{)(.*?)(\n\s*\},\n\s*"kernel_aarch64_16k")', text, re.S)
if not m:
    print('找不到 kernel_aarch64 目标块')
    sys.exit(1)
body = m.group(2)

existing = set()
mm = re.search(r'"module_implicit_outs":\s*get_gki_modules_list\("arm64"\)\s*\+\s*\[(.*?)\]', body, re.S)
if mm:
    existing = set(re.findall(r'"([^"]+)"', mm.group(1)))

new_all = sorted(existing | set(mods))
extra = ' + [\n' + ''.join('            "%s",\n' % x for x in new_all) + '        ]'
if mm:
    body_new = body[:mm.start()] + '"module_implicit_outs": get_gki_modules_list("arm64")' + extra + body[mm.end():]
else:
    bm = re.search(r'"module_implicit_outs":\s*get_gki_modules_list\("arm64"\),', body)
    if not bm:
        print('找不到 module_implicit_outs')
        sys.exit(1)
    body_new = body[:bm.start()] + '"module_implicit_outs": get_gki_modules_list("arm64")' + extra + ',' + body[bm.end():]

text = text[:m.start(2)] + body_new + text[m.end(2):]
open(bazel_path, 'w', encoding='utf-8', newline='\n').write(text)
print('已并入 module_implicit_outs 共 %d 个（新增 %d）' % (len(new_all), len(set(mods) - existing)))
