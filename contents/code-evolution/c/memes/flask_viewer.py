import os

from flask import Flask
from flask.helpers import url_for

from memes.conf import PATH, IMG
from memes.lib import populate_image_folder, fetch_image_paths


app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), IMG.FOLDER)
)


SKELETON = """
<!DOCTYPE html><html lang="de"><head><meta charset="utf-8">
<title>Super Meme Viewer</title></head><body>
<div style="text-align=center;">%s</div></body></html>
"""


@app.route('/')
def memes():
    out = []
    for path in fetch_image_paths(PATH.CACHE, IMG.EXT):
        url = url_for('static', filename=os.path.basename(path))
        out.append('<p><img src="%s" width="400px"></p>' % (url))
    return SKELETON % ('\n'.join(out))


def main():
    populate_image_folder(PATH.CACHE, IMG.EXT, maxImages=25)
    app.run(debug=True)


if __name__ == '__main__':
    main()
