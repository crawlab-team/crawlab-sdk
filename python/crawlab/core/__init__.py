import os

CRAWLAB_ROOT = os.path.join(os.environ.get('HOME'), '.crawlab')
CRAWLAB_TMP = os.path.join(CRAWLAB_ROOT, 'tmp')

if not os.path.exists(CRAWLAB_ROOT):
    os.mkdir(CRAWLAB_ROOT)

if not os.path.exists(CRAWLAB_TMP):
    os.mkdir(CRAWLAB_TMP)
