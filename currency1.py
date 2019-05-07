import requests

def main():
    res = requests.get("https://api.fixer.io/latest?base=USD&symbols=EUR")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["EUR"]
    print("1 USD is equal to {} EUR".format(rate))

if __name__ == "__main__":
    main()
