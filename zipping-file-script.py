import os
import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), path))

with zipfile.ZipFile('stripe-lambda-layer.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir('nodejs', zipf)
