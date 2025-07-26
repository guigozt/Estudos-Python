def verificarSite(url):
    import requests

    try:
        requests.get(url)
    except:
        print(f'\033[33mO site {url} não está acessível\033[m')
    else:
        print(f'\033[32mO site {url} está no ar!\033[m')

def main():
    verificarSite('https://www.pudim.com.br/')
main()