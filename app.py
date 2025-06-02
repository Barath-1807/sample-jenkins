# web_clock.py

from flask import Flask, render_template_string
from time import strftime

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
  <head>
    <title>Live Clock</title>
  #  <meta http-equiv="refresh" content="5">
    <style>
      body { background-color: green; color: cyan; font-family: Arial; font-size: 30px; text-align: center; padding-top: 100px; }
    </style>
  </head>
  <body>
    <div>{{ time }}</div>
  </body>
</html>
"""

@app.route('/')
def clock():
    current_time = strftime("%H:%M:%S<br>%d-%m-%Y")
    return render_template_string(TEMPLATE, time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
