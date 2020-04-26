# teste se o site pudim está acessível no computador usado
import urllib.request

def connect(host="http://google.com"):
    try:
        urllib.request.urlopen(host)
        return f"\033[32mO site {host.replace('http://', '')} está acessível.\033[m"
    except:
        return f"\033[31mO site {host.replace('http://', '')} NÃO está acessível.\033[m"

print(connect("http://pudim.com.br"))
print(connect("http://google.com.br"))
print(connect("http://youtube.com.br"))
