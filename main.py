from flask import Flask, render_template, request
from werkzeug import secure_filename
from cluster import get_dominant
from imageio import imread
import os
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        img = imread(secure_filename(f.filename))
        os.remove(secure_filename(f.filename))
        tot, name, centroids_conc = get_dominant(img)
        return render_template("main.html", after=True, colors=centroids_conc, tot=tot, name=name)
    return render_template("main.html", after=False)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.run(debug = True)
