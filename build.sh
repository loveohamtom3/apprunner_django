#!/usr/bin/env bash
echo build start
sudo yum install -y mysql-devel
pip install -r requirements.txt
echo build end