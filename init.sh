#!/bin/bash
#! -*- coding: utf-8 -*-

echo "============================="
echo " Prepare to restore settings"
#echo ""
#echo "Run pppoe-setup..."
#echo ""
#pppoe-setup
#echo ""
#echo "Restore pppoe.conf..."
#sleep 5
#echo ""
#cp /z/a.Backup/Dropbox/settings/a.Archlinux/pppoe.conf /etc/ppp/pppoe.conf
#sleep 5
#echo ""
#echo "Run adsl connection..."
#echo ""
#/etc/rc.d/adsl start
#sleep 5
echo ""
echo "Update packets info..."
echo ""
pacman -Syy
echo ""
echo "Update system..."
echo ""
pacman -Syu
pacman -Syu
echo ""
echo "Now reboot..."
sleep 10
echo ""
reboot
