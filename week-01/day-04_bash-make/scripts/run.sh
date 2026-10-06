#!/usr/bin/env bash
set -e

INPUT="data/app.log"
OUTPUT="output/error_users.txt"

if [ ! -f "$INPUT" ]; then
    echo "Missing input: $INPUT"
    exit 1
fi

grep ERROR "$INPUT" \
  | cut -d',' -f2 \
  | sort \
  | uniq -c \
  > "$OUTPUT"

echo "Created $OUTPUT"
