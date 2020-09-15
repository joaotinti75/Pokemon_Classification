import requests
from bs4 import BeautifulSoup

search = str(input('Deseja baixar imagens de que? '))
num_of_img = int(input('Quantas imagens você deseja baixar? '))
links_list = []
img_list = []
img_index = 0
page_number = (num_of_img // 20) * 20

url1 = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwipwcKTxOfrAhUUDrkGHZ3kB5kQ_AUoAXoECB8QAw&sfr=gws&sei=g8xeX6WWO4KI5OUP1Ne2sAQ'  
req = requests.get(url1)
soup = BeautifulSoup(req.text, 'html.parser')

for img in soup.find_all('img')[1:]: #getting all the 'img' tag from the html file, excelpt the google icon
    if img_index == num_of_img: 
        break
    else:
        links_list.append(img.get('src'))
        img_index += 1
        
for links in links_list:
    img_list.append(requests.get(links)) #acessing the images page and storing the link in a list

for i, img in enumerate(img_list): #converting the images into byte
    with open(f'C:/Users/joaovitor/Desktop/imagens/{search}_{i}.png', 'wb') as f: #wb = write byte
        f.write(img.content)
        
for pages in range(20, page_number + 20, 20):
    img_list = []
    links_list = []
    
    if img_index == num_of_img:
        break
    else:
        urln = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&tbm=isch&ei=78xeX5PTGc_Z5OUPrsyA0A0&start={pages}&sa=N'
        req = requests.get(urln)
        soup = BeautifulSoup(req.text, 'html.parser')

        for img in soup.find_all('img')[1:]:
            if img_index == num_of_img:
                break
            else:
                links_list.append(img.get('src'))
                img_index += 1
                
        for links in links_list:
            img_list.append(requests.get(links))
            
        for i, img in enumerate(img_list):
            with open(f'C:/Users/joaovitor/Desktop/imagens/{search}_{i + img_index - len(links_list)}.png', 'wb') as f: #wb = write byte
                f.write(img.content)
   
print('pronto')
