#!/usr/bin/env bash

INPUT="app.log"
OUTPUT="error_users.txt"

grep ERROR "$INPUT" \
  | cut -d',' -f2 \
  | sort \
  | uniq -c \
  > "$OUTPUT"

echo "Error user summary:"
cat "$OUTPUT"
