#!/data/data/com.termux/files/usr/bin/bash

echo "================================="
echo "🚀 TRADING BOT STARTING"
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
pkg install clang -y
pkg install rust -y
pkg install libffi -y
pkg install openssl -y

# =================================
# UPGRADE PIP TO STABLE
# =================================

pip install --upgrade pip setuptools wheel

# =================================
# INSTALL REQUIREMENTS
# =================================

pip install -r requirements.txt

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