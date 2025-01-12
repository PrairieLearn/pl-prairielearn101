#! /bin/bash
export PATH=/grade/serverFilesCourse:$PATH
ln -s /usr/lib/llvm-18/lib/libclang.so.1 /usr/lib/libclang.so
python3 /grade/tests/test.py
