from flask import Flask, render_template
# flask --app data_server run
from flask import Flask
from flask import request
import json

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
@app.route('/index') 
def home():
    f = open("data/broad.json", "r")
    data = json.load(f)
    f.close()

    countries = list(data.keys())
    requested_data = {}
    for country in countries:
        requested_data[country] = data[country]

    manFill, queensFill, brookFill, siFill, bronxFill = "", "", "", "", ""

    if 0 <= float(data["Manhattan"]) < 16:
        manFill = "#3cee00"
    elif 20 <= float(data["Manhattan"]) < 22:
        manFill = "#c6ee00"
    elif 25 <= float(data["Manhattan"]) < 26:
        manFill = "#eeb300"
    elif 25 <= float(data["Manhattan"]) < 27:
        manFill = "#ee5300"
    elif 25 <= float(data["Manhattan"]) < 31:
        manFill = "#ee0000"

    if 0 <= float(data["Queens"]) < 16:
        queensFill = "#3cee00"
    elif 20 <= float(data["Queens"]) < 22:
        queensFill = "#c6ee00"
    elif 25 <= float(data["Queens"]) < 26:
        queensFill = "#eeb300"
    elif 25 <= float(data["Queens"]) < 27:
        queensFill = "#ee5300"
    elif 25 <= float(data["Queens"]) < 31:
        queensFill = "#ee0000"

    if 0 <= float(data["Brooklyn"]) < 16:
        brookFill = "#3cee00"
    elif 20 <= float(data["Brooklyn"]) < 22:
        brookFill = "#c6ee00"
    elif 25 <= float(data["Brooklyn"]) < 26:
        brookFill = "#eeb300"
    elif 25 <= float(data["Brooklyn"]) < 27:
        brookFill = "#ee5300"
    elif 25 <= float(data["Brooklyn"]) < 31:
        brookFill = "#ee0000"

    if 0 <= float(data["Staten Island"]) < 16:
        siFill = "#3cee00"
    elif 20 <= float(data["Staten Island"]) < 22:
        siFill = "#c6ee00"
    elif 25 <= float(data["Staten Island"]) < 26:
        siFill = "#eeb300"
    elif 25 <= float(data["Staten Island"]) < 27:
        siFill = "#ee5300"
    elif 25 <= float(data["Statden Islan"]) < 31:
        siFill = "#ee0000"

    if 0 <= float(data["Bronx"]) < 16:
        bronxFill = "#3cee00"
    elif 20 <= float(data["Bronx"]) < 22:
        bronxFill = "#c6ee00"
    elif 25 <= float(data["Bronx"]) < 26:
        bronxFill = "#eeb300"
    elif 25 <= float(data["Bronx"]) < 27:
        bronxFill = "#ee5300"
    elif 25 <= float(data["Bronx"]) < 31:
        bronxFill = "#ee0000"



    sorted_boroughs = sorted(data.items(), key=lambda x: float(x[1]), reverse=True)

    firstBor, firstData = sorted_boroughs[0]
    secondBor, secondData = sorted_boroughs[1]
    thirdBor, thirdData = sorted_boroughs[2]
    fourthBor, fourthData = sorted_boroughs[3]
    fifthBor, fifthData = sorted_boroughs[4]

    formatted_text = f"{firstBor} has the highest obesity rates in New York City with {firstData}% of its population being obese. {secondBor} has the second highest obesity rate with {secondData}% being obese. {thirdBor} has the median obesity with its obesity rate at {thirdData}%. {fourthBor} has the second lowest obesity with its obesity rate being {fourthData}%. {fifthBor} has the lowest rate of obesity with only an {fifthData}% obesity population rate."

    return render_template('index.html', data=requested_data, manFill=manFill, queensFill=queensFill, brookFill=brookFill, siFill=siFill, bronxFill=bronxFill, formatted_text=formatted_text)











@app.route('/about')
def about():
    return render_template('about.html')







@app.route('/queens')
def queens():
    f = open("data/specific.json", "r")
    data = json.load(f)
    f.close()

    x_offset = 100
    x_scale = 800 / (2020 - 2003)  
    y_offset = 450
    y_scale = 400 / 40 

    boroughs = {
        "Manhattan": [],
        "Bronx": [],
        "Queens": [],
        "Brooklyn": [],
        "Staten_Island": []
    }

    for borough, points_list in boroughs.items():
        for year, value in sorted(data.get(borough, {}).items()):
            x = x_offset + (int(year) - 2003) * (x_scale-5)
            y = y_offset - (float(value) * y_scale)
            points_list.append(f"{x},{y}")

    ManhattanP = " ".join(boroughs["Manhattan"])
    BronxP = " ".join(boroughs["Bronx"])
    QueensP = " ".join(boroughs["Queens"])
    BrooklynP = " ".join(boroughs["Brooklyn"])
    StatenP = " ".join(boroughs["Staten_Island"])




#micro summary

    borough_stats = {}
    for borough, points_list in boroughs.items():
        data_points = data.get(borough, {})
        values = [float(value) for value in data_points.values() if value]

        if values:
            average = sum(values) / len(values)
            maximum = max(values)
            minimum = min(values)
            increase = 'an increase' if values[-1] > values[0] else 'a decrease'

            borough_stats[borough] = {
                'average': average,
                'maximum': maximum,
                'minimum': minimum,
                'increase': increase
            }

    formatted_texts = {}
    for borough, stats in borough_stats.items():
        formatted_texts[borough] = (
            f"As seen in the graph, the trends of obesity in {borough.replace('_', ' ')} over the years 2003-2020 are highlighted above. "
            f"{borough.replace('_', ' ')} has an average obesity rate of {stats['average']:.2f}. Over the past 18 years, the maximum obesity rate reached {stats['maximum']}, "
            f"with the minimum obesity rate being {stats['minimum']}. Over this time, there was {stats['increase']} in obesity within {borough.replace('_', ' ')}."
        )

    return render_template('queens.html', BronxP=BronxP, QueensP=QueensP, BrooklynP=BrooklynP, StatenP=StatenP, ManhattanP=ManhattanP, formatted_texts=formatted_texts)




@app.route('/si')
def staten_island():
    f = open("data/specific.json", "r")
    data = json.load(f)
    f.close()

    x_offset = 100
    x_scale = 800 / (2020 - 2003) 
    y_offset = 450
    y_scale = 400 / 40  

    boroughs = {
        "Manhattan": [],
        "Bronx": [],
        "Queens": [],
        "Brooklyn": [],
        "Staten_Island": []
    }

    for borough, points_list in boroughs.items():
        for year, value in sorted(data.get(borough, {}).items()):
            x = x_offset + (int(year) - 2003) * (x_scale-5)
            y = y_offset - (float(value) * y_scale)
            points_list.append(f"{x},{y}")

    ManhattanP = " ".join(boroughs["Manhattan"])
    BronxP = " ".join(boroughs["Bronx"])
    QueensP = " ".join(boroughs["Queens"])
    BrooklynP = " ".join(boroughs["Brooklyn"])
    StatenP = " ".join(boroughs["Staten_Island"])

#micro summary


    borough_stats = {}
    for borough, points_list in boroughs.items():
        data_points = data.get(borough, {})
        values = [float(value) for value in data_points.values() if value]

        if values:
            average = sum(values) / len(values)
            maximum = max(values)
            minimum = min(values)
            increase = 'an increase' if values[-1] > values[0] else 'a decrease'

            borough_stats[borough] = {
                'average': average,
                'maximum': maximum,
                'minimum': minimum,
                'increase': increase
            }

    formatted_texts = {}
    for borough, stats in borough_stats.items():
        formatted_texts[borough] = (
            f"As seen in the graph, the trends of obesity in {borough.replace('_', ' ')} over the years 2003-2020 are highlighted above. "
            f"{borough.replace('_', ' ')} has an average obesity rate of {stats['average']:.2f}. Over the past 18 years, the maximum obesity rate reached {stats['maximum']}%, "
            f"with the minimum obesity rate being {stats['minimum']}%. Over this time, there was an increase in obesity within {borough.replace('_', ' ')}."
        )

    return render_template('si.html', BronxP=BronxP, QueensP=QueensP, BrooklynP=BrooklynP, StatenP=StatenP, ManhattanP=ManhattanP, formatted_texts=formatted_texts)



@app.route('/manhattan')
def manhattan():
    f = open("data/specific.json", "r")
    data = json.load(f)
    f.close()

    x_offset = 100
    x_scale = 800 / (2020 - 2003)  
    y_offset = 450
    y_scale = 400 / 40  

    boroughs = {
        "Manhattan": [],
        "Bronx": [],
        "Queens": [],
        "Brooklyn": [],
        "Staten_Island": []
    }

    for borough, points_list in boroughs.items():
        for year, value in sorted(data.get(borough, {}).items()):
            x = x_offset + (int(year) - 2003) * (x_scale-5)
            y = y_offset - (float(value) * y_scale)
            points_list.append(f"{x},{y}")

    ManhattanP = " ".join(boroughs["Manhattan"])
    BronxP = " ".join(boroughs["Bronx"])
    QueensP = " ".join(boroughs["Queens"])
    BrooklynP = " ".join(boroughs["Brooklyn"])
    StatenP = " ".join(boroughs["Staten_Island"])

#micro summary


    borough_stats = {}
    for borough, points_list in boroughs.items():
        data_points = data.get(borough, {})
        values = [float(value) for value in data_points.values() if value]

        if values:
            average = sum(values) / len(values)
            maximum = max(values)
            minimum = min(values)
            increase = 'an increase' if values[-1] > values[0] else 'a decrease'

            borough_stats[borough] = {
                'average': average,
                'maximum': maximum,
                'minimum': minimum,
                'increase': increase
            }

    formatted_texts = {}
    for borough, stats in borough_stats.items():
        formatted_texts[borough] = (
            f"As seen in the graph, the trends of obesity in {borough.replace('_', ' ')} over the years 2003-2020 are highlighted above. "
            f"{borough.replace('_', ' ')} has an average obesity rate of {stats['average']:.2f}. Over the past 18 years, the maximum obesity rate reached {stats['maximum']}%, "
            f"with the minimum obesity rate being {stats['minimum']}%. Over this time, there was an increase in obesity within {borough.replace('_', ' ')}."
        )

    return render_template('manhattan.html', BronxP=BronxP, QueensP=QueensP, BrooklynP=BrooklynP, StatenP=StatenP, ManhattanP=ManhattanP, formatted_texts=formatted_texts)



@app.route('/brooklyn')
def brooklyn():
    f = open("data/specific.json", "r")
    data = json.load(f)
    f.close()

    x_offset = 100
    x_scale = 800 / (2020 - 2003)  
    y_offset = 450
    y_scale = 400 / 40 

    boroughs = {
        "Manhattan": [],
        "Bronx": [],
        "Queens": [],
        "Brooklyn": [],
        "Staten_Island": []
    }

    for borough, points_list in boroughs.items():
        for year, value in sorted(data.get(borough, {}).items()):
            x = x_offset + (int(year) - 2003) * (x_scale-5)
            y = y_offset - (float(value) * y_scale)
            points_list.append(f"{x},{y}")

    ManhattanP = " ".join(boroughs["Manhattan"])
    BronxP = " ".join(boroughs["Bronx"])
    QueensP = " ".join(boroughs["Queens"])
    BrooklynP = " ".join(boroughs["Brooklyn"])
    StatenP = " ".join(boroughs["Staten_Island"])

#micro summary


    borough_stats = {}
    for borough, points_list in boroughs.items():
        data_points = data.get(borough, {})
        values = [float(value) for value in data_points.values() if value]

        if values:
            average = sum(values) / len(values)
            maximum = max(values)
            minimum = min(values)
            increase = 'an increase' if values[-1] > values[0] else 'a decrease'

            borough_stats[borough] = {
                'average': average,
                'maximum': maximum,
                'minimum': minimum,
                'increase': increase
            }

    formatted_texts = {}
    for borough, stats in borough_stats.items():
        formatted_texts[borough] = (
            f"As seen in the graph, the trends of obesity in {borough.replace('_', ' ')} over the years 2003-2020 are highlighted above. "
            f"{borough.replace('_', ' ')} has an average obesity rate of {stats['average']:.2f}. Over the past 18 years, the maximum obesity rate reached {stats['maximum']}%, "
            f"with the minimum obesity rate being {stats['minimum']}%. Over this time, there was an increase in obesity within {borough.replace('_', ' ')}."
        )

    return render_template('brooklyn.html', BronxP=BronxP, QueensP=QueensP, BrooklynP=BrooklynP, StatenP=StatenP, ManhattanP=ManhattanP, formatted_texts=formatted_texts)



@app.route('/bronx')
def bronx():
    f = open("data/specific.json", "r")
    data = json.load(f)
    f.close()

    x_offset = 100
    x_scale = 800 / (2020 - 2003) 
    y_offset = 450
    y_scale = 400 / 40  

    boroughs = {
        "Manhattan": [],
        "Bronx": [],
        "Queens": [],
        "Brooklyn": [],
        "Staten_Island": []
    }

    for borough, points_list in boroughs.items():
        for year, value in sorted(data.get(borough, {}).items()):
            x = x_offset + (int(year) - 2003) * (x_scale-5)
            y = y_offset - (float(value) * y_scale)
            points_list.append(f"{x},{y}")

    ManhattanP = " ".join(boroughs["Manhattan"])
    BronxP = " ".join(boroughs["Bronx"])
    QueensP = " ".join(boroughs["Queens"])
    BrooklynP = " ".join(boroughs["Brooklyn"])
    StatenP = " ".join(boroughs["Staten_Island"])



    borough_stats = {}
    for borough, points_list in boroughs.items():
        data_points = data.get(borough, {})
        values = [float(value) for value in data_points.values() if value]

        if values:
            average = sum(values) / len(values)
            maximum = max(values)
            minimum = min(values)
            increase = 'an increase' if values[-1] > values[0] else 'a decrease'

            borough_stats[borough] = {
                'average': average,
                'maximum': maximum,
                'minimum': minimum,
                'increase': increase
            }

    formatted_texts = {}
    for borough, stats in borough_stats.items():
        formatted_texts[borough] = (
            f"As seen in the graph, the trends of obesity in {borough.replace('_', ' ')} over the years 2003-2020 are highlighted above. "
            f"{borough.replace('_', ' ')} has an average obesity rate of {stats['average']:.2f}. Over the past 18 years, the maximum obesity rate reached {stats['maximum']}%, "
            f"with the minimum obesity rate being {stats['minimum']}%. Over this time, there was an increase in obesity within {borough.replace('_', ' ')}."
        )

    return render_template('bronx.html', BronxP=BronxP, QueensP=QueensP, BrooklynP=BrooklynP, StatenP=StatenP, ManhattanP=ManhattanP, formatted_texts=formatted_texts)



def print_url():
    print("Server is running. Access the home page at http://127.0.0.1:5000/index")
    print("Access other pages at http://127.0.0.1:5000/about, /queens, /si, /manhattan, /brooklyn, /bronx")




if __name__ == '__main__':
    print_url()
    app.run(debug=True)  
