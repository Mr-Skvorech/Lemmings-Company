from flask import Flask, render_template
from data_importer import generate_both
from PIL import Image
import os

app = Flask(__name__)

img = os.path.join('./static', 'img')

def init_kwargs():
    kwargs = dict()
    kwargs["Сбербанк (SBER)"] = os.path.join(img, 'sberr.png')
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
    kwargs["Сургутнефтегаз (SNGS)"] = os.path.join(img, 'surgut.png')
    kwargs["Татнефть (TATN)"] = os.path.join(img, 'tatneft.png')
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
    kwargs["SNGS"] = "Сургутнефтегаз"
    kwargs["TATN"] = "Татнефть"
    kwargs["GMKN"] = "Норильский Никель"
    kwargs["AAPL"] = "Apple"
    kwargs["GS"] = "Goldman Sachs Group"
    kwargs["V"] = "Visa"
    kwargs["PFE"] = "Pfizer"
    kwargs["TXN"] = "Texas Instruments"
    #
    kwargs["text_SBER"] = "ПАО Сбербанк является лидером в сфере банковских услуг в России и одним из лидеров среди международных финансовых компаний. Ведущим акционером банка является Министерство финансов РФ. Оно владеет около 52% акций. Остальные 48% находятся в свободном обращении на рынке ценных бумаг. Сбербанк имеет сильные позиции среди конкурентов. Компания работает в более 80 субъектов РФ. В ее структуру входят 11 региональных банков и более 14 тысяч подразделений. Компания является самым дорогим брендом в РФ. Широкий выбор банковских услуг и развитие экосистемы делают Сбербанк желанным партнером для многих компаний."
    kwargs["text_LKOH"] = "ПАО «ЛУКОЙЛ» – нефтяная компания из России, которая занимается добычей, переработкой и продажей нефти. Годовая выручка составляет около 8 трлн рублей. На долю корпорации приходится 1% доказанных мировых запасов нефти и 2% от всемирной добычи. Продукция поставляется в около 100 странах мира. Лукойл позиционирует себя как один из лидеров в области нефтедобычи. У компании внушительные показатели успеха и высокая прибыль. Партнерство с другими предприятиями позволяет добиться хороших результатов и показывать положительную динамику развития. В список партнеров в рамках проектов на территории РФ входят ConocoPhillips и Башнефть. ЛУКОЙЛ разрабатывает месторождения в более 30 странах. Руководство корпорации и менеджеры являются владельцами большой части акций. Согласно рыночной капитализации Лукойл находится на третьем месте среди других компаний с таким же видом деятельности как добыча и переработка нефти. Номинальным держателем акций холдинга является Банк Нью-Йорка, который хранит и ведет учет 61,78% ценных бумаг компании."
    kwargs["text_GAZP"] = "ПАО «Газпром» – глобальная энергетическая компания. Основные направления деятельности – геологоразведка, добыча, транспортировка, хранение, переработка и реализация газа, газового конденсата и нефти, реализация газа в качестве моторного топлива, а также производство и сбыт тепло- и электроэнергии. Компания располагает самыми богатыми в мире запасами природного газа. Его доля в мировых запасах газа составляет 16%, в российских – 71%. На внутреннем рынке «Газпром» реализует свыше половины продаваемого газа. Кроме того, компания поставляет газ в более чем 30 стран ближнего и дальнего зарубежья. Компания входит в четверку крупнейших производителей нефти в Российской Федерации. «Газпром» также владеет крупными генерирующими активами на территории России (16% от общей установленной мощности российской энергосистемы). Кроме того, компания занимает первое место в России по производству тепловой энергии. «Газпром» имеет наименьший углеродный след продукции среди крупнейших нефтегазовых компаний."
    kwargs["text_NVTK"] = "Независимая компания-холдинг НОВАТЭК – крупнейший добытчик и поставщик природного газа в РФ. Организация ведёт разведывательные работы, переработку добытого газа и жидких углеводородов, а также их реализацией на внутреннем и внешнем рынках. Деятельность свою она осуществляет через совместные и дочерние предприятия. Основана компания была в 1994 году в городе Новокуйбышевске, главный штаб её расположен в Ямало-Ненецком округе, где и находятся основные 45 месторождений и лицензионных участков, в городе Тарко-Сале, где находится также принадлежащий НОВАТЭКу завод по переработке нестабильного газа. Компания поставляет газ в 35 регионов РФ и обеспечивает этим 1/5 часть спроса. НОВАТЭК не ограничивается добычей топлива в исследованных местах, она ведёт геологоразведочные работы в новых районах с перспективой на будущее. Уставной капитал холдинга равен 303,6 миллионов рублей, ежегодная выручка около 800 миллиардов рублей. Занимает 6-е место в мире по глобальной добыче газа и 3-е по запасам топлива. В штате холдинга состоят около 7000 специалистов высокой квалификации, а работа в НОВАТЭК – отличная возможность для карьерного роста."
    kwargs["text_ROSN"] = "ПАО Нефтяная компания Роснефть один из лидеров нефтедобычи в России. Она занимает третье место в рейтинге по размеру выручки, которая составляет около 8 трлн рублей. Роснефть выполняет несколько видов деятельности, от разведки и добычи до сбыта и реализации. Продажа продукции делается в стране и за ее пределами. Основные направления добычи и переработки – это нефть и газ. Главным акционером является государство. Ему принадлежит 40,4% акций, еще 18,93% и 19,75% являются активом компаний QH Oil Investments LLC и BP. Сегодня Роснефть крупнейшая публичная корпорация в нефтегазовой отрасли. По добыче газа котируются на втором месте после Газпрома. Компания имеет доли в европейских обрабатывающих компаниях. Также у нее много зависимых и дочерних предприятий. Акции Роснефть (ROSN) торгуются на Лондонской и Московской фондовых биржах, а также на площадках ММВБ и РТС, где они включены в котировальный список Первого уровня. Также идет торговля депозитарными расписками (GDR). Первичное размещение акций (IPO) состоялось в 2006-ом году."
    kwargs["text_ALRS"] = "ПАО АК «АЛРОСА» — российская горнорудная компания с государственным участием. Лидер по добыче алмазов в мире. Основные работы по поиску месторождений полезных ископаемых и их подготовке к использованию проходят в Якутии и Архангельской области."
    kwargs["text_VTBR"] = "ПАО «Банк ВТБ» и его дочерние компании являются поставщиками банковских продуктов и услуг. Банк получает большую часть дохода внутри страны. Самым большим источником доходов банка являются розничный банковский бизнес, который предлагает такие продукты как кредитные карты, ссуды, депозиты и лизинговые услуги. Сегмент корпоративного/инвестиционного банкинга является следующим по величине и предлагает такие услуги, как коммерческое кредитование, торговля ценными бумагами, деривативы, брокерские операции, корпоративные финансы, управление активами и финансовый консалтинг."
    kwargs["text_YNDX"] = "Yandex N.V. PLC — транснациональная компания в отрасли информационных технологий. Владеет системой поиска в интернете, интернет-порталом и веб-службами в нескольких странах. Наиболее заметное положение занимает на рынках России, Белоруссии и Казахстана. Значительную часть дохода Яндекс получает от продажи рекламы. Технологии Яндекса позволяют размещать рекламу на десктопных и мобильных устройствах и таргетировать её на нужную аудиторию."
    kwargs["text_MTSS"] = "ПАО «Мобильные ТелеСистемы» оказывает услуги мобильной, фиксированной и цифровой связи. Компания предлагает беспроводной доступ в Интернет, фиксированную голосовую связь, широкополосный доступ и платное телевидение. Бизнес компании диверсифицирован, экосистема увеличивается. В России доля абонентов около 80млн. Более 50% акций МТС принадлежит АФК системе."
    kwargs["text_MGNT"] = "ПАО «Магнит» — российская компания, управляющая сетью розничных магазинов, с головным офисом в Краснодаре. Одна из ведущих розничных сетей по торговле продуктами питания в России. Логистическая сеть Магнита — одна из крупнейших в Европе, и имеет распределительные центры в разных уголках страны."
    kwargs["text_FIVE"] = "X5 Group — крупная российская продуктовая розничная сеть. Под управлением находятся такие магазины как Пятёрочка, Перекрёсток, Много лосося, а также цифровые бизнесы: Перекрёсток.Впрок, 5post и службы логистики."
    kwargs["text_CHMF"] = "ПАО «Северсталь» – российская вертикально-интегрированная сталелитейная и горнодобывающая компания. Владеет активами в России, а также в Украине, Латвии, Польше, Италии, Либерии. Компания состоит из дивизионов «Северсталь Российская Сталь» и «Северсталь Ресурс». Выпускает горячекатаный и холоднокатаный стальной прокат, гнутые профили и трубы, сортовой прокат и т. п. Компании принадлежит Череповецкий металлургический комбинат в России. Горнорудный сегмент «Северстали» представлен в России двумя горно-обогатительными комбинатами (ГОК): «Карельский окатыш» и «Олкон». Они ежегодно выпускают 15 млн. т. железорудного концентрата. Также в состав «Северстали» входит угольные компании «Воркутауголь» (республика Коми) и PBS Coals (США), а также ряд перспективных горнодобывающих лицензий в развивающихся странах. «Северсталь» остается мировым лидером отрасли по эффективности. Она показывает высочайшую рентабельность по EBITDA среди сталелитейных компаний и генерирует положительный свободный денежный поток на протяжении всего цикла."
    kwargs["text_SNGS"] = "ПАО «Сургутнефтегаз»  - одна из крупнейших частных нефтяных компаний России. Она объединила в своей структуре научно-проектные, геолого-разведочные, буровые, добывающие подразделения, нефте- и газоперерабатывающие, сбытовые предприятия. При этом компания стоит дешевле, чем объем наличных денег на ее счетах."
    kwargs["text_TATN"] = "ПАО Татнефть – один из крупнейших в энергетическом комплексе РФ холдингов, находящийся в республике Татарстан и относящийся к вертикально-интегрированным компаниям. В состав холдинга входят: газодобывающие, нефтеперерабатывающие и нефтедобывающие, нефтехимические предприятия, банки, страховые компании и т.д. Деятельность Татнефти заключается в разведке, открытии, обустройстве нефтедобывающих скважин, непосредственно самой добычи нефти и её реализации через свои каналы, а кроме того, в выпуске вулканизированных шин, труб с полимерным покрытием, синтетических автомасел и многого другого. Помимо нефти ПАО также занимается и добычей газа. Ежегодно Татнефтью из недр извлекается около 250 тонн нефти, 900 кубометров газа, и выработка ежегодно растёт. Но даже при таких темпах добычи, полезных ископаемых хватит ещё не менее чем на 30 лет. Компания обладает развитой сетью АЗС по всей стране и за рубежом в странах СНГ, а также владеет пакетом акций нескольких нефтехимических заводов.  Уставной капитал ПАО Татнефть составляет почти 2,5 миллиона рублей, а общее число его акций – 1,5 миллиона. Среднегодовая выручка Татнефти составляет порядка триллиона рублей."
    kwargs["text_GMKN"] = "Горно-металлургическая компания Норильский никель управляет несколькими предприятиями, которые добывают и производят цветные и драгоценные металлы. Компания также добывает уголь, антрацит, известняк, гипс и др. Норникель – лидер металлургической промышленности России и один из главных производителей драгоценных и цветных металлов в мире. Также компания занимается сбытом собственной продукции и поставляет её в более 30 стран. Кроме того, Норникель имеет серьёзные энергетические и газовые активы. Основная добыча ресурсов происходит на полуострове Таймыр. После чего сырьё передаётся предприятиям для первичной, вторичной и окончательной переработок. Норникель владеет активами и ведёт работы на Кольском полуострове, в Забайкальском крае. А за границей – в Финляндии, ЮАР и Австралии. Штаб-квартира компании находится в Москве."
    kwargs["text_AAPL"] = "Apple Inc. - американская компания, производитель персональных и планшетных компьютеров, аудиоплееров, телефонов, программного обеспечения. Одна из первых стала создавать персональные компьютеры и современные операционные системы. У компании очень грамотный маркетинг, который в паре с инновационными технологиями и узнаваемому дизайну сформировали культовый бренд. APPLE - первая американская компания, чья капитализация превысила 1 трлн долларов США. Это произошло во время торгов акциями компании в 2018 году. В январе 2022 года Apple стала первой компанией в мире, рыночная капитализация которой достигла 3 триллионов долларов США."
    kwargs["text_GS"] = "Goldman Sachs Group, Inc. занимается глобальным инвестиционным банкингом, ценными бумагами и управлением инвестициями, предоставляя финансовые услуги. Компания работает в следующих бизнес-сегментах: инвестиционный банкинг, глобальные рынки, управление активами и управление потребителями и капиталом. Сегмент инвестиционного банкинга обслуживает клиентов государственного и частного секторов по всему миру и предоставляет финансовые консультационные услуги, помогает компаниям привлекать капитал для укрепления и развития своего бизнеса и предоставляет финансирование корпоративным клиентам. Сегмент глобальных рынков обслуживает своих клиентов, которые покупают и продают финансовые продукты, финансируют и управляют рисками. Сегмент управления активами предоставляет инвестиционные услуги, чтобы помочь клиентам сохранить и приумножить свои финансовые активы. Сегмент Consumer &amp; Wealth Management помогает клиентам достичь их индивидуальных финансовых целей, предоставляя консультационные услуги по благосостоянию и банковские услуги. Компания была основана Маркусом Голдманом в 1869 году, ее штаб-квартира находится в Нью-Йорке, штат Нью-Йорк."
    kwargs["text_V"] = "Visa, Inc. занимается предоставлением услуг цифровых платежей. Компания также способствует глобальной торговле за счет передачи ценностей и информации между глобальной сетью потребителей, продавцов, финансовых учреждений, предприятий, стратегических партнеров и государственных структур. Компания предлагает дебетовую карту, кредитную карту, предоплаченные продукты, коммерческие платежные решения и глобальные банкоматы. Компания была основана Ди Хоком в 1958 году, ее штаб-квартира находится в Сан-Франциско, Калифорния."
    kwargs["text_PFE"] = "Pfizer Inc. — одна из крупнейших в мире фармацевтических компаний с годовым объемом продаж около 50 миллиардов долларов (без учета продаж вакцины против COVID-19). Хотя исторически компания продавала многие виды товаров медицинского назначения и химикатов, сейчас на рецептурные лекарства и вакцины приходится большая часть продаж."
    kwargs["text_TXN"] = "Texas Instruments Incorporated занимается разработкой и производством полупроводниковых решений для аналоговых и цифровых встраиваемых систем и обработки приложений. Компания работает через следующие сегменты: аналоговая и встроенная обработка. Полупроводники аналогового сегмента изменяют реальные сигналы, такие как звук, температура, давление или изображения, путем их кондиционирования, усиления и часто преобразования в поток цифровых данных, которые могут обрабатываться другими полупроводниками, такими как встроенные процессоры. Сегмент Embedded Processing предназначен для решения конкретных задач и может быть оптимизирован для различных комбинаций производительности, мощности и стоимости в зависимости от приложения. Компания была основана Сесилом Х. Грином, Патриком Юджином Хаггерти, Джоном Эриком Джонссоном и Юджином Макдермоттом в 1930 году, и ее штаб-квартира находится в Далласе, штат Техас."
    return kwargs

@app.route("/")
def home_page():
    kwargs = init_kwargs()
    #
    filename = "list_of_comp" + ".txt"
    f = open(filename, encoding="utf-8")
    comp = f.readlines()
    f.close()
    print(*comp)
    stock = []
    for i in range(15):
        sym = comp[i]
        para = dict()
        para["name"] = sym
        s = ""
        for i in range(-3, -len(sym), -1):
            if (sym[i] == '('):
                break
            s += sym[i]
        s = s[::-1]
        print(sym[0:len(sym) - 1])
        para["ticker"] = s
        para["fil"] = kwargs.get(sym[0:len(sym) - 1], os.path.join(img, 'sberr.png'))
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
        print(sym[0:len(sym) - 1])
        para["ticker"] = s
        para["fil"] = kwargs.get(sym[0:len(sym) - 1], os.path.join(img, 'sberr.png'))
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
    f = open(os.path.join('companies', id + ".txt"), 'r', encoding="utf-8")
    data = f.readlines()
    f.close()
    tick = []
    for i in range(1, len(data)):
        sym = data[i].split()
        tick.append(sym)
    kwargs["args"] = ["DATA", "OPEN", "CLOSE", "LOW", "HIGH", "VALUE", "QUANTITY"]
    kwargs["name"] = kwargs[id]
    kwargs["id"] = id
    # kwargs["image"] = os.path.join(img, id + ".png")
    s = 'img/' + id + '.png'
    kwargs["ticker"] = tick
    kwargs["text"] = kwargs["text_" + id]
    file_name = kwargs[kwargs["name"] + " (" + id + ")"]
    im = Image.open(file_name)
    new_file_name = os.path.join(img, 'icon.png')
    im.save(new_file_name, quality=95)
    return render_template('stock.html', **kwargs)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")