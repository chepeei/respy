#!/usr/bin/env python3

setdir = '/z/Backup/restore/settings/'
homedir = '/home/a'
settings = [
    '.icons',               homedir+'/.icons',\
    '.mc',                  homedir+'/.mc',\
    '.mpd',                 homedir+'/.mpd',\
    'terminal',             homedir+'/.config/Terminal',\
    'deadbeef',             homedir+'/.config/deadbeef',\
    'conky',                homedir+'/.config/conky',\
    '.irssi',               homedir+'/.irssi',\
    '.mozilla',             homedir+'/.mozilla',\
    '.vimeratorrc',         homedir+'/.vimperatorrc',\
    '.zshrc',               homedir+'/.zshrc',\
    'vim/.vimrc',           homedir+'/.vimrc', 'vim/.vim', '/home/angel/.vim',\
    'vim/vimwiki',          homedir+'/vimwiki',\
    'openbox',              homedir+'/.config/openbox', '.themes', '/home/angel/.themes',\
    'tint2',                homedir+'/.config/tint2',\
    'vlc',                  homedir+'/.config/vlc',\
    'pcmanfm',              homedir+'/.config/pcmanfm','libfm', '/home/angel/.config/libfm',\
    '.fonts',               homedir+'/.fonts',\
    'tilda/config_0',       homedir+'/.tilda/config_0',\
    'bash/.bash_profile',   homedir+'/.bash_profile', 'bash/.bashrc', '/home/angel/.bashrc',\
    'gtk/.gtk-bookmarks',   homedir+'/.gtk-bookmarks', 'gtk/.gtkrc-2.0', '/home/angel/.gtkrc-2.0', 'gtk/.gtkrc-2.0-kde', '/home/angel/.gtkrc-2.0-kde',
    'gtk/.gtkrc-2.0.mine',  homedir+'/.gtkrc-2.0.mine',\
    'bin',                  homedir+'/bin',\
    '.xinitrc',             homedir+'/.xinitrc', '.xsession', '/home/angel/.xsession',\
    '.pythonstartup',       homedir+'/.pythonstartup',\
    '.Xdefaults',           homedir+'/.Xdefaults',\
    'gtg',                  homedir+'/.local/share/gtg',\
    #list += ['../../.mozilla', '/home/angel/.mozilla',\
]

packets = [\
# Base
    'hal','gamin','terminal','gksu','sudo','screen','grc',\
    'tar','unrar','unzip','ntfsprogs','htop','zip','gzip','bzip2','dosfstools',\
    'gvfs','gnome-menus',\
    'xlockmore',\
    #gvfs-smb gvfs-obexftp gvfs-afc
# Appearance
    'gtk-candido-engine','xcursor-vanilla-dmz',\
# Dev
    'automake','patch','gcc',\
# System utils
    'ntfs-3g','gparted',\
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
    'django','sqliteman',\
    'python2','python3',\
    'ctags','gvim',\
# Notebook
    'acpi','acpid','laptop-mode-tools','cpufrequtils',\
# Fix
    # fix firefox association problems
    'libgnome',\
]
