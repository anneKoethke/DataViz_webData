# -*- coding: utf8 -*-
from bs4 import BeautifulSoup


# alle Transfersaisons: Sommer+Winter, ohne Leihe, ohne VereinsinternerWechsel

saison_array = [
    "06_07",
    "07_08",
    "08_09",
    "09_10",
    "10_11",
    "11_12",
    "12_13",
    "13_14",
    "14_15",
    "15_16",
    "16_17",
    "17_18"
]

gesamt = []
for saison in saison_array:
    print('--- Season: ' + saison + ' ---')

    # print('  --- loading html file ---')
    with open("raw/" + saison + ".html", encoding="utf8") as html_file:
        soup = BeautifulSoup(html_file, 'lxml')


    # print('  --- processing data ---')

    # VEREINSNAMEN pro Saison
    vereinsliste = []

    vereins_div = soup.find('div', class_='wappenleiste-box')
    all_imgs = vereins_div.find_all('img')
    for img in all_imgs:
        vereinsliste.append(img['alt'])




    # TRANSFERBILANZ DER SAISON
    transferbilanz_div = soup.find('div', class_='transferbilanz') # Div mit der Transferbilanz über die gesamte Saison

    heads = transferbilanz_div.find_all('div', class_='headline')  # Abgänge, Zugänge, Gesamtbilanz-Überschrift
    abgaenge = {heads[0].contents[0].strip(': '): heads[0].b.contents[0]}  # ges. Abgänge der Saison
    zugaenge = {heads[1].contents[0].strip(': '): heads[1].b.contents[0]}  # ges. Zugänge der Saison

    texts = transferbilanz_div.find_all('div', class_='text')

    single_span_arr = []

    for content in texts:
        spans_arr = content.find_all('span')
        for span in spans_arr:
            single_span_arr.append(span.contents[0].strip(' €'))
    # zwischenspeicher für den Zusammenhang
    transfer_einnahmen = single_span_arr[0]
    einnahmen_pro_verein = single_span_arr[1]
    einnahmen_pro_spieler = single_span_arr[2]
    transfer_ausgaben = single_span_arr[3]
    ausgaben_pro_verein = single_span_arr[4]
    ausgaben_pro_spieler = single_span_arr[5]
    gesamtbilanz = single_span_arr[6]
    ges_bilanz_pro_verein = single_span_arr[7]
    ges_bilanz_pro_spieler = single_span_arr[8]



    # EINZELNE SPIELER
    
    tbodys = soup.find_all('tbody')
    trs = tbodys[36].find_all('tr') # abgänge
    anzahl_abgaenge = len(trs)
    spieler_abgaenge = []
    for tr in trs:
        for td in (tr.find_all('td')):
            print(td)
            print()

    # SPIELERÄBGÄNGE PRO VEREIN

    # alle Boxes, dann alle imgs

    # SPIELERZUGÄGNE PRO VEREIN
    spieler_zugaenge = []



    # ERGEBNIS

    # alle Daten pro Saison (saison, vereinsliste, Bilanz, einzelne Vereine)
    transferbilanz_saison = {
        'Vereine': vereinsliste,
        'Abgänge': heads[0].b.contents[0],
        'Zugänge': heads[1].b.contents[0],
        'Transfereinnahmen': transfer_einnahmen,
        'Einnahmen pro Verein': einnahmen_pro_verein,
        'Einnahmen pro Spieler': einnahmen_pro_spieler,
        'Transferausgaben': transfer_ausgaben,
        'Ausgaben pro Verein': ausgaben_pro_verein,
        'Ausgaben pro Spieler': ausgaben_pro_spieler,
        'Gesamtbilanz': gesamtbilanz,
        'Gesamtbilanz pro Verein': ges_bilanz_pro_verein,
        'Gesamtbilanz pro Spieler': ges_bilanz_pro_spieler
    }
    # print(transferbilanz_saison) #funzt!
    # print('  --- appending result to list ---')
    gesamt.append( {saison : transferbilanz_saison} )


print('--- result: ---')
# print(gesamt)
# print(gesamt[10]) #16_17