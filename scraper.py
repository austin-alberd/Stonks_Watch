import requests, bs4


# This is the format that the code should follow when it is put into the function AAPL:NASDAQ

def get_stock_price(code):
    try:
        #pull hte HTML file and put it into Beautiful Soup
        res = requests.get(f'https://google.com/finance/quote/{code}')
        res.raise_for_status()
        stockInfo = bs4.BeautifulSoup(res.text, 'html.parser')
        #Search for the div that the price is stored in
        price = stockInfo.select(".rPF6Lc > .ln0Gqe > div > div > span >div >div ")
        #Clean up the output and strip the HTML tags
        raw_dat= str(price[0])
        clean_1 =raw_dat.split('>')
        raw_dat_2 = str(clean_1[1])
        clean_final = raw_dat_2.split('<')
        raw_dat_3=str(clean_final[0])
        final = raw_dat_3.split('$')
        return final[1]
    except:
        #Only prints if something messes up and thats bad!
        print("OH NO! An error occoured please check all of your inputs and make sure they are in the correct format.")


