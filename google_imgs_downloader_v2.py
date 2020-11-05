import requests
from bs4 import BeautifulSoup

def google_images_download(directory, search, num_of_img):
    
    search_mod = search.upper()
    search_mod = search_mod.split()

    # first page of google images
    url1 = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwipwcKTxOfrAhUUDrkGHZ3kB5kQ_AUoAXoECB8QAw&sfr=gws&sei=g8xeX6WWO4KI5OUP1Ne2sAQ'
    i = 0

    response = requests.get(url1)

    soup = BeautifulSoup(response.text, 'html.parser')

    links_list = []
    repeat_img = []

    table = soup.find_all('table', attrs={'class': 'TxbwNb'})

    for links in table:
        links_list.append(links.a.get('href'))

    links_list = [sites[7:sites.index('&')] for sites in links_list]

    for link in links_list:
        if i == num_of_img:
            break
        url = link
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            images = soup.find_all('img')
            for image in images:
                if i == num_of_img:
                    break
                elif image.get('src') == None or '.svg' in image.get('src'):
                    pass
                elif image.get('src') in repeat_img:
                    pass
                else:
                    search_comp = [i in image.get('src').upper() for i in search_mod]
                    if search_comp.count(True) == len(search_comp) and 'http' in image.get('src'):
                        with open(f'{directory}/{search.lower()}_{i}.png', 'wb') as f:
                            img_response = requests.get(image.get('src'))
                            if img_response.status_code == 200:  # sucess
                                if i == num_of_img:
                                    break
                                else:
                                    #print(link, '-', i)
                                    print(image.get('src'), '-', i)
                                    repeat_img.append(image.get('src'))
                                    f.write(img_response.content)
                                    i += 1
                            else:
                                continue
        except:
            pass

    page = 20
    if i < num_of_img:
        while True:
            links_list = []
            img_list = []
            urln = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&tbm=isch&ei=78xeX5PTGc_Z5OUPrsyA0A0&start={page}&sa=N'
            response = requests.get(urln)
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find_all('table', attrs={'class': 'TxbwNb'})
            for links in table:
                links_list.append(links.a.get('href'))
            links_list = [sites[7:sites.index('&')] for sites in links_list]
            for link in links_list:
                if i == num_of_img:
                    break
                url = link
                try:
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    images = soup.find_all('img')
                    for image in images:
                        if i == num_of_img:
                            break
                        elif image.get('src') == None or '.svg' in image.get('src'):
                            pass
                        elif image.get('src') in repeat_img:
                            pass
                        else:
                            search_comp = [i in image.get('src').upper() for i in search_mod]
                            if search_comp.count(True) == len(search_comp) and 'http' in image.get('src'):
                                with open(f'{directory}/{search.lower()}_{i}.png', 'wb') as f:
                                    img_response = requests.get(image.get('src'))
                                    if img_response.status_code == 200:  # sucess
                                        if i == num_of_img:
                                            break
                                        else:
                                            #print(link, '-', i)
                                            print(image.get('src'), '-', i)
                                            repeat_img.append(image.get('src'))
                                            f.write(img_response.content)
                                            i += 1
                            else:
                                pass
                except:
                    pass

            if i < num_of_img:
                page += 20
            else:
                break
    print('')
    print(f'{i} images were downloaded')
    print('')
if __name__ == '__main__':
    while True:
        print(50*'=')
        print("In which directory do you want to save the images?\ne.g. C:/Users/daniel/Desktop/images \n(you can use \ as well)\nDON'T USE ''")
        print('')
        directory = str(input('Directory: '))
        print('')
        search = str(input('What images do you want to download? '))
        print('')
        num_of_img = int(input('How many images do you want to download? '))
        print('')
        print('Downloading...Check your directory')
        
        google_images_download(directory, search, num_of_img)
        
        exit_question = str(input('Do you want to quit? [Y/N]'))
        if exit_question.upper()[0] == 'Y':
            print('Bye!')
            break
        else:
            continue
