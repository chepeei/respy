#!/usr/bin/env python3

setdir = '/z/Backup/restore/settings/'

settings = [
    '.icons', '/home/angel/.icons',\
    '.mc', '/home/angel/.mc',\
    '.mpd', '/home/angel/.mpd',\
    'terminal', '/home/angel/.config/Terminal',\
    'deadbeef', '/home/angel/.config/deadbeef',\
    'conky', '/home/angel/.config/conky',\
    '.irssi', '/home/angel/.irssi',\
    '.mozilla', '/home/angel/.mozilla',\
    '.vimeratorrc', '/home/angel/.vimperatorrc',\
    '.zshrc', '/home/angel/.zshrc',\
    'vim/.vimrc', '/home/angel/.vimrc', 'vim/.vim', '/home/angel/.vim',\
    'vim/vimwiki', '/home/angel/vimwiki',\
    'openbox', '/home/angel/.config/openbox', '.themes', '/home/angel/.themes',\
    'tint2', '/home/angel/.config/tint2',\
    'vlc', '/home/angel/.config/vlc',\
    'pcmanfm', '/home/angel/.config/pcmanfm','libfm', '/home/angel/.config/libfm',\
    '.fonts', '/home/angel/.fonts',\
    'tilda/config_0', '/home/angel/.tilda/config_0',\
    'bash/.bash_profile', '/home/angel/.bash_profile', 'bash/.bashrc', '/home/angel/.bashrc',\
    'gtk/.gtk-bookmarks', '/home/angel/.gtk-bookmarks', 'gtk/.gtkrc-2.0', '/home/angel/.gtkrc-2.0', 'gtk/.gtkrc-2.0-kde', '/home/angel/.gtkrc-2.0-kde',
    'gtk/.gtkrc-2.0.mine', '/home/angel/.gtkrc-2.0.mine',\
    'bin', '/home/angel/bin',\
    '.xinitrc', '/home/angel/.xinitrc', '.xsession', '/home/angel/.xsession',\
    '.pythonstartup', '/home/angel/.pythonstartup',\
    '.Xdefaults', '/home/angel/.Xdefaults',\
    #list += ['../../.mozilla', '/home/angel/.mozilla',\
    'gtg', '/home/angel/.local/share/gtg',\
]

packets = [\
# Base
    'hal','gamin','terminal','gksu','sudo','screen','grc',\
    'gtk-candido-engine','xcursor-vanilla-dmz',\
    'tar','unrar','unzip','ntfs-3g','ntfsprogs','htop','zip','gzip','bzip2','dosfstools',\
    'gvfs','gnome-menus',\
    'xlockmore',\
    #gvfs-smb gvfs-obexftp gvfs-afc
# Dev
    'automake','patch','gcc',\
# System utils
    'gparted',\
# Openbox
    'lxappearance','obconf','openbox','zsh',\
    'dmenu-xft','tilda','parcellite','xcompmgr','feh','lxtask','tint2','volwheel',\
# Fonts
    'ttf-ms-fonts','ttf-dejavu','ttf-droid','artwiz-fonts','ttf-bitstream-vera',\
# Soft
    'gpicview','evince','file-roller','wine','transmission-gtk','vlc','xfburn','gcalctool',\
    'firefox-branded','flashplugin',\
    'pcmanfm','gigolo-git',\
    'mc',\
# Crypting
    'encfs',\
# Python, vim dev
    'django','ctags','sqliteman',\
    'python','python3',\
    'gvim',\
# Notebook
    'acpi','acpid','laptop-mode-tools','cpufrequtils',\
# Fix
    'libgnome',\ # fix firefox association problems
]



































