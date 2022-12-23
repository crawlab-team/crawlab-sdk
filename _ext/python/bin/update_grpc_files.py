import os

dirs = [
    './crawlab/grpc/entity',
    './crawlab/grpc/models',
    './crawlab/grpc/services',
]

import_dirs = [
    'entity',
    'models',
    'services',
]

for dirname in dirs:
    with open(os.path.join(dirname, '__init__.py'), 'w') as f:
        f.write('')

    for filename in os.listdir(dirname):
        filepath = os.path.join(dirname, filename)
        with open(filepath, 'r') as f:
            content = f.read()
            for import_dir in import_dirs:
                content = content.replace(f'from {import_dir} import', f'from ..{import_dir} import')

        with open(filepath, 'w') as f:
            f.write(content)
