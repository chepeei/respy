#!/usr/bin/env python3

def install():
    import sys
    sys.dont_write_bytecode = True

    import os
    import config

    print('[ Packets install ]')

    print('-'*50)
    print(config.packets)
    print('-'*50)
    q = input('|-- Install all packets? ')
    if q == 'y':
        os.system("packer -S --noconfirm "+' '.join(config.packets))

    print('\'-- End\n')

install()
