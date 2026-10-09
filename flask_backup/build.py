import os
from flask_frozen import Freezer
from app import app

# Add a route for celestia
@app.route('/celestia.html')
def celestia():
    from flask import render_template
    from app import SITE
    return render_template('celestia.html', site=SITE)

app.config['FREEZER_DESTINATION'] = 'dist'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print("Static site generated in 'dist' directory.")
