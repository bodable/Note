#!/bin.sh

##安装准备
#更新软件列表
sudo apt-get update
#更新软件	
#sudo apt-get upgrade


##前期安装
#vim
echo "atm installing vim" 
echo y|sudo apt-get install vim

#chrome
echo "atm installing chrom"
sh chrome.sh

 




