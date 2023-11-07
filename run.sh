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
echo "Installing dependencies"
$py -m pip install --upgrade pip &>/dev/null &2>/dev/null # make pip shut up about being out of date
$py -m pip install -r ../requirements.txt &>/dev/null &2>/dev/null
if [[ $? -ne 0 ]]; then
    echo "Failed to install dependencies"
    exit -2
fi
echo Running
$py main.py "$data"
popd >/dev/null