from PushoverSender import PushoverSender
from time import sleep
import datetime
import requests


def main():
    sender = PushoverSender(get_key('user_key.txt'), get_key('api_key.txt'))

    while True:
        time = str(datetime.datetime.now().time())
        time = int(time.replace('.', '').replace(':', ''))
        if time > 90000000000 and time < 220000000000:
            run(sender)
            sleep(9000)


def run(sender):
    # Get data
    print('Getting Data')
    scrape_data('scraped_html.txt',
                'https://vidooly.com/live-stats/T-Series-Vs-PewDiePie')

    # Process data
    print('Processing Data')
    subs = get_subs('scraped_html.txt')
    pewdiepie = subs[0]
    tseries = subs[1]
    difference = pewdiepie - tseries

    # Push message
    print('Sending Message')
    message = ('PewDiePie: ' + str(pewdiepie) + '\nT-Series: ' + str(tseries) +
               '\nDifference: ' + str(difference))

    sender.send(message)
    print('Completed\n')


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


def get_key(filename):
    with open(filename, 'r') as f:
        return f.readline().strip('\n')


main()
