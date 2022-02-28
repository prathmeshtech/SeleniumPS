from itertools import product
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import io

my_url = "https://www.flipkart.com/search?q=earphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {
                               "class": "_13oc-S"})

# filename = "Flipkart_val.csv"
# f = io.open(filename, "w", encoding="utf-8")
# headers = "Earphones-Names,Ratings,Pricing\n"
# f.write(headers)

df = pd.DataFrame(columns=["Product_Name", "Price", "Rating"])

for container in containers:
    product_name = container.div.img["alt"]

    rating_container = container.findAll("div", {"class": "_3LWZlK"})
    rating = rating_container[0].text

    price_container = container.findAll("div", {"class": "_30jeq3"})
    price = price_container[0].text

    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." + rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    df.loc[len(df)] = [product_name, final_price, final_rating]

    # f.write(pricing)
    # final = product_name.replace(",", "|") + "," + rating + "," + price + "\n"
    # f.write(final)
# f.close()

table = pa.Table.from_pandas(df)
pq.write_table(table, 'example_noindex.parquet')
