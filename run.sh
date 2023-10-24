#!/usr/bin/bash

py=""
possible=("python" "python3" "python3.11" "python3.12")
for i in ${possible[@]}; do

    which $i >/dev/null 2>/dev/null
    if [[ $? -eq 0 ]]; then
        py=$i
        break
    fi
done

if [[ "$py" == "" ]]; then
    echo "Python not found on PATH!"
    exit -1
fi

folder=$(dirname "$SCRIPT")
data=$(realpath "$folder/data/unemployment_monthly.csv")

pushd "$folder/src" >/dev/null
$py main.py "$data"
popd >/dev/null