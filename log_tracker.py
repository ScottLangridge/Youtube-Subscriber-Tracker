from time import sleep
import datetime
import requests


def main():
    while True:
        scrape_data('log_html.txt',
                    'https://vidooly.com/live-stats/T-Series-Vs-PewDiePie')
        time = str(datetime.datetime.now().time())
        subs = get_subs('log_html.txt')
        with open('log.txt', 'a+') as log:
            log.write(time + ',' + str(subs[0]) + ',' + str(subs[1]) + '\n')
        sleep(5)


def scrape_data(filename, url):
    data_object = requests.get(url)
    with open(filename, 'w+') as f:
        f.write(data_object.content)


def get_subs(filename):
    with open(filename, 'r') as f:
        html = f.readlines()

    for i in range(len(html)):
        if html[i].strip() == '<h2>PewDiePie</h2>':
            pewdiepie = int(html[i + 1][43:-6])
        if html[i].strip() == '<h2>T-Series</h2>':
            tseries = int(html[i + 1][41: -6])

    return (pewdiepie, tseries)


main()
