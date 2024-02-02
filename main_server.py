from flask import Flask, render_template
from data_importer import generate_both
import os

app = Flask(__name__)

img = os.path.join('static', 'img')

def init_kwargs():
    kwargs = dict()
    kwargs["Сбербанк (SBER)"] = os.path.join(img, 'sber.png')
    kwargs["Лукойл (LKOH)"] = os.path.join(img, 'lukoil.png')
    kwargs["Газпром (GAZP)"] = os.path.join(img, 'gazprom.png')
    kwargs["Новатэк (NVTK)"] = os.path.join(img, 'novatek.png')
    kwargs["Роснефть (ROSN)"] = os.path.join(img, 'rosneft.png')
    kwargs["Алроса (ALRS)"] = os.path.join(img, 'alrosa.png')
    kwargs["ВТБ (VTBR)"] = os.path.join(img, 'vtb.png')
    kwargs["Яндекс (YNDX)"] = os.path.join(img, 'yandex.png')
    kwargs["МТС (MTSS)"] = os.path.join(img, 'mts.png')
    kwargs["Магнит (MGNT)"] = os.path.join(img, 'magnit.png')
    kwargs["X5_Retail_group (FIVE)"] = os.path.join(img, 'X5.png')
    kwargs["Северсталь (CHMF)"] = os.path.join(img, 'sever.png')
    kwargs["Сургутнефтегаз (SNSGS)"] = os.path.join(img, 'surgut.png')
    kwargs["Татнефть (NTATN)"] = os.path.join(img, 'tatneft.png')
    kwargs["Норильский_Никель (GMKN)"] = os.path.join(img, 'nornikel.svg')
    kwargs["Apple (AAPL)"] = os.path.join(img, 'apple.jpg')
    kwargs["Goldman_Sachs_Group (GS)"] = os.path.join(img, 'gold.png')
    kwargs["Visa (V)"] = os.path.join(img, 'visa.webp')
    kwargs["Pfizer (PFE)"] = os.path.join(img, 'pfizer.jpg')
    kwargs["Texas_Instruments (TXN)"] = os.path.join(img, 'texas.png')
    # 
    kwargs["SBER"] = "Сбербанк"
    kwargs["LKOH"] = "Лукойл"
    kwargs["GAZP"] = "Газпром"
    kwargs["NVTK"] = "Новатэк"
    kwargs["ROSN"] = "Роснефть"
    kwargs["ALRS"] = "Алроса"
    kwargs["VTBR"] = "ВТБ"
    kwargs["YNDX"] = "Яндекс"
    kwargs["MTSS"] = "МТС"
    kwargs["MGNT"] = "Магнит"
    kwargs["FIVE"] = "X5 Retail Group"
    kwargs["CHMF"] = "Северсталь"
    kwargs["SNSGS"] = "Сургутнефтегаз"
    kwargs["NTATN"] = "Татнефть"
    kwargs["GMKN"] = "Норильский Никель"
    kwargs["AAPL"] = "Apple"
    kwargs["GS"] = "Goldman Sachs Group"
    kwargs["V"] = "Visa"
    kwargs["PFE"] = "Pfizer"
    kwargs["TXN"] = "Texas Instruments"
    return kwargs

@app.route("/")
def home_page():
    kwargs = init_kwargs()
    #
    filename = "list_of_comp" + ".txt"
    f = open(filename)
    companies = f.read()
    f.close()
    comp = companies.split("\n")
    stock = []
    for i in range(15):
        sym = comp[i]
        para = dict()
        para["name"] = sym
        s = ""
        for i in range(-2, -len(sym), -1):
            if (sym[i] == '('):
                break
            s += sym[i]
        s = s[::-1]
        para["ticker"] = s
        para["fil"] = kwargs.get(sym, os.path.join(img, 'sber.png'))
        para["link"] = "/companyMOEX/" + para["ticker"]
        stock.append(para)
    for i in range(15, 20):
        sym = comp[i]
        para = dict()
        para["name"] = sym
        s = ""
        for i in range(-2, -len(sym), -1):
            if (sym[i] == '('):
                break
            s += sym[i]
        s = s[::-1]
        para["ticker"] = s
        para["fil"] = kwargs.get(sym, os.path.join(img, 'sber.png'))
        para["link"] = "/companyNYSE/" + para["ticker"]
        stock.append(para)
    kwargs["stock"] = stock
    kwargs["logo"] = os.path.join(img, 'Lemming.png')
    kwargs["acc"] = os.path.join(img, "Account.png")
    #
    return render_template("main_page.html", **kwargs)

@app.route("/companyMOEX/<id>")
def user(id):
    kwargs = init_kwargs()
    generate_both(id)
    f = open(id + ".txt", 'r')
    data = f.readlines()
    f.close()
    for i in range(1, len(data)):
        sym = data[i].split(" ")
    kwargs["args"] = ["DATA", "OPEN", "CLOSE", "LOW", "HIGH", "VALUE", "QUANTITY"]
    kwargs["name"] = kwargs[id]
    kwargs["id"] = id
    kwargs["graph"] = "SBER.png"
    kwargs["logo"] = os.path.join(img, 'Lemming.png')
    kwargs["acc"] = os.path.join(img, "Account.png")
    # kwargs["image"] = kwargs.get(kwargs[kwargs[]], os.path.join(img, 'sber.png'))
    return render_template('stock.html', **kwargs)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")