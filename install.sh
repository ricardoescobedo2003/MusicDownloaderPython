#!/bin/bash
sudo apt install python3-pip -y
pip3 install plyer
pip3 install pytube
pip3 install tqdm
echo "Dependencias instaladas ahora ejecutamos"
python3 ./main.py