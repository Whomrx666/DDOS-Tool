#!/bin/bash
clear
echo -e "                Installing \033[91mDDOS\033[0mTool,"
echo -e "                Please Wait..."
apt-get -y install python-pip > /dev/null 2>&1
apt-get -y install python3-pip > /dev/null 2>&1
python3 -m pip install --upgrade pip > /dev/null 2>&1
pip install tqdm > /dev/null 2>&1
pip install pyfiglet==0.7 > /dev/null 2>&1
clear
echo -e "\033[92m[*]\033[0m \033[91mDDOS\033[0mTool was installed successfully."
echo -e "\n\nTo run it type '\033[1;4mpython3 DDOS-Tool.py\033[0m'\n\n"
