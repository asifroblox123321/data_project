from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
@app.route('/index') 
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/queens')
def queens():
    return render_template('queens.html')

@app.route('/si')
def staten_island():
    return render_template('si.html')

@app.route('/manhattan')
def manhattan():
    return render_template('manhattan.html')

@app.route('/brooklyn')
def brooklyn():
    return render_template('brooklyn.html')

@app.route('/bronx')
def bronx():
    return render_template('bronx.html')

def print_url():
    print("Server is running. Access the home page at http://127.0.0.1:5000/index")
    print("Access other pages at http://127.0.0.1:5000/about, /queens, /si, /manhattan, /brooklyn, /bronx")

if __name__ == '__main__':
    print_url()
    app.run(debug=True)  
