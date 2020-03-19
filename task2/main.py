from bs4 import BeautifulSoup
from requests import get


def main():
    response = get('https://www.gethatch.com/en/')
    bs = BeautifulSoup(response.text, 'html.parser')
    all_holders = bs.find_all(class_="qode_clients clearfix six_columns default qode_clients_separators_disabled")[0]
    for child in all_holders.childGenerator():
        img = child.findChild().findChild().findChild().findChild()
        print(img['src'])


if __name__ == '__main__':
    main()
