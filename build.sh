#!/usr/bin/env bash
echo build start
sudo yum install python3-devel
sudo yum install gcc
sudo yum install -y mysql-devel
pip install -r requirements.txt
echo build end