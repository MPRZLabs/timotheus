#!/usr/bin/bash
python margen.py > margend.txt
cat "margend.txt" "marchosen.txt" > "markovpredb.txt"
