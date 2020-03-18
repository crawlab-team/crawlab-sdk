import os

if os.name == 'nt':
    home = os.environ.get('HOMEPATH')
else:
    home = os.environ.get('HOME')

CRAWLAB_ROOT = os.path.join(home, '.crawlab')
CRAWLAB_TMP = os.path.join(CRAWLAB_ROOT, 'tmp')

if not os.path.exists(CRAWLAB_ROOT):
    os.mkdir(CRAWLAB_ROOT)

if not os.path.exists(CRAWLAB_TMP):
    os.mkdir(CRAWLAB_TMP)
