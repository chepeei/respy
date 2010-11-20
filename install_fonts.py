#!/usr/bin/env python3

def install():
    import os
    print('[ Fonts install ]')
    packets = ('freetype2','fontconfig','libxft','cairo',)

    for packet in packets:
        print("|-- Install:",packet+'-ubuntu')
        os.system('sudo packer -S --noconfirm '+packet+'-ubuntu')
        os.system('sudo pacman -Rd --noconfirm '+packet)
        os.system('sleep 10')
        os.system('sudo pacman -U --noconfirm /tmp/packerbuild-0/'+packet+'-ubuntu/'+packet+'-ubuntu/'+packet+'-ubuntu*')
    os.system('sudo pacman -Qs ubuntu')
    print ('\'-- End\n')

if __name__ == '__main__':
    install()
