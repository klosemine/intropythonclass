from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import itemgetter

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    url = "https://www.sgcarmart.com/new_cars/index.php"
    cars = []   # empty list

    # 1. input
    try:
        page = urlopen(url)   # 1. open the connection
        print("Connected Successfully to SGCarMart")
        # 2. Get the bs4 parser to parse the page
        soup = BeautifulSoup(page, 'html.parser')
        # <div class="limittwolines">Mercedes</div>

        # raw_html_data is a list of html tags
        raw_car_data = soup.findAll('div', {"class": "limittwolines"})
        raw_price_data = soup.findAll('div', {"class": "font_black"})
        # cars = ["mercedes", "bmw", "kia avante"]
        # cars = [ ["mercedes", "$150,000"], ["BMW", "$170,888"] ]
        for index in range(len(raw_car_data)):
            car_name = raw_car_data[index].text
            car_price = raw_price_data[index].text

            # conversion price (text) to number
            car_price = car_price.replace("$", "")
            car_price = car_price.replace(",", "")
            car_price = float(car_price)

            # build a list
            car_data = [car_name, car_price]  # [ "Mercedes", 150000.0]
            cars.append(car_data)   # append car_data list to cars list
            # cars is now a list of lists


    except Exception as exception:
        print(exception)

    # 2. processing
    cars.sort(key=itemgetter(1), reverse=True)


    # 3. output
    for index, car in enumerate(cars):
        car_name = car[0]   # 'CUPRA Formentor'
        car_price = car[1]   # 167890
        print("{:2}) {} costs ${:,.0f}".format(index+1, car_name, car_price))


main()