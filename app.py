from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
  <head>
    <title>Live Clock</title>
    <style>
      body { background-color: green; color: cyan; font-family: Arial; font-size: 30px; text-align: center; padding-top: 100px; }
    </style>
    <script>
      function updateClock() {
        const now = new Date();
        const time = now.toLocaleTimeString('en-GB'); // 24-hour format
        const date = now.toLocaleDateString('en-GB'); // dd-mm-yyyy
        document.getElementById('clock').innerHTML = time + "
" + date;
      }

      setInterval(updateClock, 1000); // Update every second
      window.onload = updateClock;
    </script>
  </head>
  <body>
    <div id="clock"></div>
  </body>
</html>
"""

@app.route('/')
def clock():
    return render_template_string(TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
