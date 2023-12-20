import requests
import json
import time

# actual request that gets a nitro token
url = "https://api.discord.gx.games/v1/direct-fulfillment"
headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
}
jsonData = {
    "partnerUserId": "5628ad5b72e62a856449c45423c863106a4c8ebc491a7657315dd57635ee6ed7"
}
def main():
    while True:
        print("How many Discord Nitro links do you want?" + "\n")
        print("Enter a whole number above 0.")
        num = input()
        try:
            val = int(num)
            if val < 1:
                print("Enter a whole number above 0.")
        except ValueError:
            print("Enter a whole number above 0.")
            continue
        print("How long do you want to wait in between each Nitro link?")
        print("This reduces the chance of rate limit, which blocks you from getting more links.")
        print("Recommended: 1")
        wait = input()
        try:
            waitTime = float(wait)
            if waitTime < 0:
                print("Enter a positive number.")
            break
        except ValueError:
            print("Enter a positive number.")
    print("WARNING! If you get an error, you might have been ratelimited. Just run it again.")
    for i in range(val):
        request = requests.post(url=url, json = jsonData, headers = headers)
        # stores the token
        tokenText = json.loads(request.text)

        token = tokenText["token"]

        tokenUrl = "https://discord.com/billing/partner-promotions/1180231712274387115/" + token
        # writes it to a file
        txt = open("tokens.txt", "a")
        txt.write("\n" + str(tokenUrl) + "\n")
        txt.close()
        time.sleep(waitTime)
    print("Check 'token.txt'!")
main()