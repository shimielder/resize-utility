# resize-utility
small script on Python, that allow you to make thumbnails with given parameters
start it with console/bash command like
python3 resize.py w- home/username/pictures -d home/username/thumbnails -px 300 -pf _thumb
keys:
-w Directory with images
-d Destination directory (optional, by default script create <current_working_directory-resized> directory)
-px Thumbnail's size (optional, default 150)
-pf Thumbnail's postfix (optional, by default no postfix)