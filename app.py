from flask import Flask, render_template
import pandas as pd
import numpy as np
import io
import base64
from flask import Response
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/histogram')
def histogram():
    # Generate fake data
    data = np.random.normal(size=1000)
    df = pd.DataFrame({'data': data})

    # Create histogram plot
    fig, ax = plt.subplots()
    ax.hist(df['data'], bins=30)

    # Encode plot as base64 string
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    buffer = b''.join(img)
    encoded = base64.b64encode(buffer).decode('utf-8')
    
    return render_template('index.html', histogram=encoded)

@app.route('/scatterplot')
def scatterplot():
    # Generate fake data
    data = np.random.normal(size=(1000, 2))
    df = pd.DataFrame({'x': data[:, 0], 'y': data[:, 1]})

    # Create scatterplot
    fig, ax = plt.subplots()
    ax.scatter(df['x'], df['y'])

    # Encode plot as base64 string
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    buffer = b''.join(img)
    encoded = base64.b64encode(buffer).decode('utf-8')
    
    return render_template('index.html', scatterplot=encoded)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
