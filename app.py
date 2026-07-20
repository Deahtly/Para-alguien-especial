from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def i(): return render_template('index.html')
app.run(debug=True)