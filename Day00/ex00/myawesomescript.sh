#!/bin/sh

curl -s https://bit.ly/4880Txe | grep -o '<a href=".*">' | cut -d'"' -f2