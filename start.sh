#!/data/data/com.termux/files/usr/bin/bash

echo "================================="
echo "🚀 TRADING BOT STARTUP"
echo "================================="

# =================================
# UPDATE TERMUX
# =================================

pkg update -y

# =================================
# INSTALL REQUIRED PACKAGES
# =================================

pkg install python -y
pkg install git -y

# =================================
# UPGRADE PIP
# =================================

pip install --upgrade pip

# =================================
# INSTALL PYTHON LIBRARIES
# =================================

pip install ccxt
pip install pandas
pip install ta
pip install requests

# =================================
# AUTO RESTART LOOP
# =================================

while true
do

    echo "================================="
    echo "🤖 STARTING BOT"
    echo "================================="

    python main.py

    echo "================================="
    echo "❌ BOT CRASHED"
    echo "♻️ RESTARTING IN 5 SECONDS"
    echo "================================="

    sleep 5

done