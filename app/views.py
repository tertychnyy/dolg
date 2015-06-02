from app import app
import json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/api/events')
def api_events():
    data = {}
    event1 = {'name': 'Поездка в Португалию',
              'id': 1,
              'startdate': '2015-08-04 05:35'}
    event2 = {'name': 'Может в кальянную сходим?',
              'id': 2,
              'startdate': '2015-06-12 20:00'}
    data['data'] = [event1, event2]
    return json.dumps(data)