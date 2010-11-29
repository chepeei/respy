#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = True

import os
import config

debug = False
setdir = config.setdir
settings = config.settings
iter_settings = iter(settings)


print('[ Backup and restore settings - config dir: '+config.setdir+']')

def makebu(src,dst,setdir):
    if os.path.isfile(src):
        if len(dst.split('/')) > 1:
            if not os.path.exists('/'.join((setdir+dst).split('/')[:-1])):
                if sh('mkdir -pv "'+'/'.join((setdir+dst).split('/')[:-1])+'"') == 0:
                    print('        > mkdir: ok')
    if sh('mv "'+src+'" "'+setdir+dst+'"') == 0:
        print('        > mv: ok')
    if sh('ln -s "'+setdir+dst+'" "'+src+'"') == 0:
        print('        > ln: ok')





def sh(cmd):
    if debug:
        print('        > debug > '+cmd)
        return 0
    else:
        return os.system(cmd)

while True:
    try:
        dst = next(iter_settings)
        src = next(iter_settings)
    except StopIteration:
        break

    print('|-- Backup '+src+'  -->  '+dst+'')

    if os.path.exists(src):
        if os.path.islink(src):
            print('|    \'-- src is link')
            if setdir+dst == os.path.realpath(src):
                print('|        \'-- src linked to backup')
            else:
                print('|        \'-- src linked to '+os.path.realpath(src))
        else:
            if os.path.exists(setdir+dst):
                print('|    \'-- restore from backup? or make new backup?')
                ans = input('      [r]estore, [n]ew or skip? ')
                if 'n' in ans:
                    sh('rm -Riv "'+setdir+dst+'"')
                    makebu(src,dst,setdir)
                elif 'r' in ans:
                    sh('rm -Riv "'+src+'"')
                    if sh('ln -s "'+setdir+dst+'" "'+src+'"') == 0:
                        print('|        \'-- ln: ok')
            else:
                print('|    \'-- make new backup')
                makebu(src,dst,setdir)
            input()
    else:
        print('|    \'-- src is not exist')
        if os.path.exists(setdir+dst):
            print('|        \'-- backup exist')
            #print('|        \'-- ln "'+setdir+dst+'" "'+src+'"')
            #FIXME: nujno sozdavat papku, naprimere */.config/Terminal
            sh('mkdir -pv "'+'/'.join((src).split('/')[:-1])+'"')
            if sh('ln -s "'+setdir+dst+'" "'+src+'"') == 0:
                print('|            \'-- ln: ok')
        else:
            print('|        \'-- backup is not exist')
            #if sh('ln -s "'+setdir+dst+'" "'+src+'"') == 0:
            #    print('|            \'-- ln: ok')
        input('|')

    print('|')
print('\'-- End')
