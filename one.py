from urllib.request import urlopen

def oo():
    with urlopen('http://www.google.com') as story:
        for line in story:
            print(line.decode('utf-8'))

if(__name__ == "__main__"):
    oo()
