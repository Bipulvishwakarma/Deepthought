import requests
# from lxml import html

url=input("please enter the URL of the website you want to scrape: ")
# Taking url as input

val=requests.get(url)
# Opening the url (Basically a get request)

# print(val.content)
file = open("Scraped-WebPage.html",'w')
# Open a file in write mode

cal = val.text
# Copying the content from the recieved data

for i in cal:
    try:
        # Try and except block to handle error incase the value to be written is not a string
        file.write(i)
    except:
        print("An exception occurred")