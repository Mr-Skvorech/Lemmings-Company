from flask import Flask, render_template
from data_importer import generate_both
import os

app = Flask(__name__)

img = os.path.join('static', 'images')

@app.route("/")
def home_page():
    kwargs = dict()
    #
    filename = "list_of_comp" + ".txt"
    file = open(filename)
    companies = file.read()
    comp = companies.split("\n")
    kwargs["stock"] = comp
    kwargs["image"] = os.path.join(img, 'sber.png')
    kwargs["logo"] = os.path.join(img, 'Lemming.png')
    kwargs["acc"] = os.path.join(img, "Account.png")
    #
    return render_template("main_page.html", **kwargs)

@app.route("/company/<name>")
def user(name):
    # file_path_txt = f'companies/{name}.txt';  
    # file_path_png = f'companies/{name}.png';
    # if not(os.path.exists(file_path_txt)):
    #     create_data(name, 2022, 1, 1, 2024, 1, 1, 3)
    # if not(os.path.exists(file_path_png)):
    #     load_graph_to_png(name, name + ".png")
    # file = open(f'companies/{name}.txt', 'r');
    # company = file.readlines()
    # file.close()
    generate_both(name)
    file = open(name + ".txt", 'r')
    data = file.split("\n")
    file.close()
    for i in range(1, len(data)):
        sym = data[i].split(" ")
    kwargs = dict()
    kwargs["args"] = ["DATA", "OPEN", "CLOSE", "LOW", "HIGH", "VALUE", "QUANTITY"]
    kwargs["ticker"] = data[1:]
    kwargs["name"] = name
    kwargs["id"] = name
    kwargs["img"] = name + ".png"
    return render_template('stock.html', **kwargs)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")