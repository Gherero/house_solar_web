from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('Здохни сцуко!!!!!')

@app.route('/index')
def index(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
    title = {"text": 'My Title'}
    xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/test')
def test():
    return (render_template('test.html'))

@app.route('/test2')
def test2():
    return (render_template('test2.html'))

@app.route('/test3')
def test3():
    return (render_template('test3.html'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True',port=80)
