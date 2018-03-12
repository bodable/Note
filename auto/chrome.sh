#!/bin/sh
#chrome

sudo add-apt-repository ppa:a-v-shkop/chromium
sudo apt-get update
echo y|sudo apt-get install chromium-browser
