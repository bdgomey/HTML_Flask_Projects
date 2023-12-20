from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cats')
def cats():
  return render_template('cats.html')

@app.route('/dogs')
def dogs():
  return render_template('dogs.html')

@app.route('/training/cats')
def cat_training():
  return render_template('cat_training.html')

@app.route('/training/dogs')
def dog_training():
  return render_template('dog_training.html')

@app.route('/why')
def why():
  return render_template('dogsvcats.html')

if __name__ == '__main__':
  app.run(debug=True)
