#!/usr/bin/env python3

import os
import config

print('[ Base setup ]')

if input('|-- Install xorg, alsa? ') == 'y':
    os.system('pacman -Sq --noconfirm xorg alsa-utils')
    os.system('alsactl; alsactl store')

if input('|-- Install nvidia video support? ') == 'y':
    os.system('pacman -Sq --noconfirm nvidia nvidia-utils')

if input('|-- Install intel video support? ') == 'y':
    os.system('pacman -Sq --noconfirm xf86-video-intel')

if input('|-- Install synaptics support? ') == 'y':
    os.system('pacman -Sq --noconfirm xf86-input-synaptics')

if input('|-- Add sound fix for Asus X55Sv? ') == 'y':
    open('/etc/modprobe.d/modprobe.conf','a').write('\noptions snd-hda-intel model=lenovo-ms7195-dig\n\n')

if input('|-- Add "archlinuxfr" server? ') == 'y':
    open('/etc/pacman.conf','a').write('\n[archlinuxfr]\nServer = http://repo.archlinux.fr/i686\n')

if input('|-- Install yaourt? ') == 'y':
    os.system('pacman -Syy && pacman -S yaourt')

if input('|-- Install packer? ') == 'y':
    os.system('yaourt -S packer')

if input('|-- Install pacman-color? ') == 'y':
    os.system('packer -S make gcc && packer -S pacman-color')

if input('|-- Add new user? ') == 'y':
    username = input('|    \'-- new user name: ')
    os.system('useradd -m -s /bin/bash '+username)
    os.system('passwd '+username)
    os.system('gpasswd -a '+username+' optical')
    os.system('gpasswd -a '+username+' users')
    os.system('gpasswd -a '+username+' audio')
    os.system('gpasswd -a '+username+' wheel')
    os.system('gpasswd -a '+username+' power')
    os.system('gpasswd -a '+username+' video')

if input('\'-- Install sudo? ') == 'y':
    username = 'angel'
    os.system('pacman -S sudo')
    open('/etc/sudoers','a').write('\n'+username+'   ALL=(ALL) ALL'+'\n'+username+'   ALL= NOPASSWD: /usr/bin/cpufreq-set'+'\n'+username+'   ALL= NOPASSWD: /sbin/reboot'+'\n'+username+'   ALL= NOPASSWD: /sbin/poweroff'+'\n'+username+'   ALL= NOPASSWD: /sbin/hdparm'+'\n'+username+'  ALL= NOPASSWD: /sbin/shutdown'+'\n'+username+'   ALL= NOPASSWD: /sbin/halt\n\n')

print('')



























