import requests

url = "https://ma.oraimo.com/rest/FR/V1/guest-carts/coupons/24NY-6%25BWF58YWY"

headers = {
    "accept": "*/*",
    "accept-language": "ar-MA,ar;q=0.9,fr-MA;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "Referer": "https://ma.oraimo.com/checkout/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

response = requests.put(url, headers=headers)

print(response.status_code)
print(response.text)
