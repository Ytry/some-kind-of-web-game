from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)

# route to website homepage / category page
@app.route('/')
def showLanding():

    return render_template('landing_page.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
