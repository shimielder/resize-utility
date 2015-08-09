# resize-utility
small script on Python, that allow you to make thumbnails with given parameters

# usage
start it with console/bash command like:

for linux:

python3 resize.py w- home/username/pictures -d home/username/thumbnails -px 300 -pf thumb

for windows:

python resize.py w- C:\Users\Admin\Documents\Images -d D:\Site\Preview -px 50 -pf -resized

# keys:

-w Directory with images (if directory contain whitespaces insert it using "")

-d Destination directory (optional, by default script create <current_working_directory-resized> directory)

-px Thumbnail's size (optional, default 150)

-pf Thumbnail's postfix (optional, by default no postfix)

