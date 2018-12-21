#!/bin/sh
echo "安装python3.6 https://www.cnblogs.com/esin/p/7073119.html"

echo y|sudo apt-get install software-properties-common
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6




