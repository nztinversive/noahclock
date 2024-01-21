from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def countdown():
    # Set the countdown date
    countdown_date = datetime(2076, 1, 18)
    # Get the current time
    now = datetime.now()
    # Calculate the time left until the countdown date
    time_left = countdown_date - now

    # Calculate months and days
    months, days = divmod(time_left.days, 30)
    
    # Calculate hours, minutes, and seconds
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Pass the time left to the template
    return render_template('countdown.html', months=months, days=days, hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    app.run(debug=True)
