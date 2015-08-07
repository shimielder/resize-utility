import os
from PIL import Image
from sys import argv, exit

def resizing_images():
    def getopts(argv):
        opts = {}
        while argv:
            if argv[0][0] == '-':
                opts[argv[0]] = argv[1]
                argv = argv[2:]
            else:
                argv = argv[1:]
        if '-w' not in opts:
            print('You must enter working directory!')
            exit([0])

        return opts

    def resizer(opts):
        workpath = opts['-w']
        default_opts = {'-d': '../{}{}/'.format(workpath.split('\\')[-1], '-resized'),
                        '-px': 150,
                        '-pf': ''}

        if '-d' in opts: default_opts['-d'] = opts['-d']
        if '-px' in opts: default_opts['-px'] = int(opts['-px'])
        if '-pf' in opts: default_opts['-pf'] = opts['-pf']
        workpath = opts['-w']
        destination = default_opts['-d']
        picture_size = default_opts['-px']
        postfix = default_opts['-pf']
        try:
            os.chdir(workpath)
            print('Working directory {}'.format(os.getcwd()))
        except OSError:
            print('No such file or directory')
            exit([0])
        try:
            os.mkdir(destination)
            print('Directory {} created'.format(os.getcwd()))
        except OSError:
            pass

        for file in os.listdir():
            try:
                out = Image.open(file)
                sides = out.size
                if sides[0] > sides[1]:
                    original_size = out.crop(
                        ((sides[0] - sides[1]) // 2, 0, sides[0] - (sides[0] - sides[1]) // 2, sides[1]))
                else:
                    original_size = out.crop(
                        (0, (sides[1] - sides[0]) // 2, sides[0], sides[1] - (sides[1] - sides[0]) // 2))
                original_size.thumbnail((picture_size, picture_size))
                original_size.save('{}/{}{}.jpg'.format(destination, file.split('.')[0], postfix), "JPEG")
                print('Image {} converted'.format(file))
            except IOError:
                pass

    opts = getopts(argv)
    resizer(opts)

resizing_images()
