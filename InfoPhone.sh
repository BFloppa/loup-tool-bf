#!/bin/bash

rm -rf PhoneInfoga > /dev/null 2>&1
rm -rf phoneinfoga > /dev/null 2>&1
echo
sleep 1.0
echo -e '\033[1;92m[''\033[0m*''\033[1;92m]''\033[1;92m PhoneInfoga Installing...'
git clone https://github.com/BFloppa/loup-tool-bf > /dev/null 2>&1 && cd PhoneInfo > /dev/null 2>&1 && unzip PhoneInfoga.zip > /dev/null 2>&1 && python3 -m pip install -r requirements.txt > /dev/null 2>&1 && pip2 install colorama > /dev/null 2>&1
rm -rf PhoneInfoga.zip > /dev/null 2>&1
rm -rf InfoPhone.sh > /dev/null 2>&1
chmod +x *
