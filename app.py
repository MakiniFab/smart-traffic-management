from flask import Flask, render_template
from detect_cars import detect_cars
from traffic_signal import control_traffic_signal

app = Flask(__name__)

@app.route('/')
def home():
    # Detect cars from a sample image
    car_count_lane1 = detect_cars('static/traffic.jpg')
    car_count_lane2 = car_count_lane1 // 2  # Simulating lane 2 with fewer cars

    # Determine signal control based on car count
    signal_status = control_traffic_signal(car_count_lane1, car_count_lane2)

    # Pass data to the web template
    traffic_data = {
        'lane1_cars': car_count_lane1,
        'lane2_cars': car_count_lane2,
        'signal_status': signal_status
    }

    return render_template('index.html', data=traffic_data)

if __name__ == '__main__':
    app.run(debug=True)