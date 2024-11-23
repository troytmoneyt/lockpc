import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Get the list of files and directories in the current directory
    items = os.listdir('.')

    # Separate files and directories
    files = [item for item in items if os.path.isfile(item)]
    directories = [item for item in items if os.path.isdir(item)]

    return render_template('index.html', files=files, directories=directories)

if __name__ == '__main__':
    app.run(debug=True)
