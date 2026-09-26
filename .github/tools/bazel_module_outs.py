#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 Kleaf 的报错日志里解析「built but not copied」的模块，追加进 common/BUILD.bazel 的
module_outs（幂等）。用法: bazel_module_outs.py <日志> <BUILD.bazel>
"""
import re
import sys

log_path, bazel_path = sys.argv[1], sys.argv[2]
log = open(log_path, encoding='utf-8', errors='replace').read()

mods = re.findall(r'^\s*"([A-Za-z0-9_\-/\.]+\.ko)",\s*$', log, re.M)
# 只保留报错段落里的模块
start = log.find('built but not copied')
if start >= 0:
    seg = log[start:]
    end = seg.find('Alternatively')
    if end >= 0:
        seg = seg[:end]
    mods = re.findall(r'"([A-Za-z0-9_\-/\.]+\.ko)"', seg)
mods = sorted(set(mods))
if not mods:
    print('没有解析到缺失模块，保持原样')
    sys.exit(1)

text = open(bazel_path, encoding='utf-8').read()
m = re.search(r'"kernel_aarch64":\s*\{', text)
if not m:
    print('找不到 kernel_aarch64 目标')
    sys.exit(1)

# 已有的 module_outs
existing = set()
mm = re.search(r'"kernel_aarch64":\s*\{.*?\n(\s*)"module_outs":\s*\[(.*?)\]',
               text, re.S)
if mm:
    existing = set(re.findall(r'"([^"]+)"', mm.group(2)))

new_all = sorted(existing | set(mods))
block = '        "module_outs": [\n' + ''.join('            "%s",\n' % x for x in new_all) + '        ],\n'

if mm:
    text = text[:mm.start()] + block + text[mm.end():]
else:
    # 插到 kernel_aarch64 的 "kmi_symbol_list_strict_mode" 之前
    km = re.search(r'("kernel_aarch64":\s*\{\n)', text)
    text = text[:km.end()] + block + text[km.end():]

open(bazel_path, 'w', encoding='utf-8', newline='\n').write(text)
print('已写入 module_outs 共 %d 个（新增 %d）' % (len(new_all), len(set(mods) - existing)))
