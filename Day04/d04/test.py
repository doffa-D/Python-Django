import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Target URL
base_url = "https://ma.oraimo.com"

# Send an HTTP request to the website
response = requests.get(base_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the anchor tags (links) in the page
    all_links = soup.find_all('a')

    # Store existing links in a set
    existing_links = set()

    # Load existing links from a file (if available)
    try:
        with open('existing_links.txt', 'r') as file:
            existing_links.update(line.strip() for line in file)
    except FileNotFoundError:
        pass

    # Extract and print new URLs
    new_links = set()
    for link in all_links:
        # Combine the base URL with the relative URL using urljoin
        full_url = urljoin(base_url, link.get('href'))
        new_links.add(full_url)
        if full_url not in existing_links:
            print(f"New Link: {full_url}")

    # Update existing links file
    with open('existing_links.txt', 'w') as file:
        file.write('\n'.join(new_links.union(existing_links)))

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


# import requests
# from concurrent.futures import ThreadPoolExecutor

# i = 0

# def spin():
#     global i
#     spin_url = "https://ma.oraimo.com/new-year/spin-to-win/luck.php?site=ma"
#     coupon_url = "https://ma.oraimo.com/rest/FR/V1/guest-carts/48nUmliswqcUrPGgMWFWI1ggut1Gdhwj/coupons/"

#     with ThreadPoolExecutor() as executor:
#         while True:
#             res = requests.get(spin_url, headers={
#                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
#                 "Accept": "*/*",
#                 "Accept-Language": "en-GB,en;q=0.5",
#                 "X-Requested-With": "XMLHttpRequest",
#                 "Sec-Fetch-Dest": "empty",
#                 "Sec-Fetch-Mode": "cors",
#                 "Sec-Fetch-Site": "same-origin",
#                 "Referer": "https://ma.oraimo.com/new-year/spin-to-win/",
#             })

#             json_data = res.json()
#             code = json_data.get("data", {}).get("code")

#             if code is not None:
#                 i += 1
#                 coupon_code_url = f"{coupon_url}{code}"
#                 future = executor.submit(requests.put, coupon_code_url, headers={
#                     "accept": "*/*",
#                     "accept-language": "ar-MA,ar;q=0.9,fr-MA;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
#                     "cache-control": "no-cache",
#                     "content-type": "application/json",
#                     "pragma": "no-cache",
#                     "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
#                     "sec-ch-ua-mobile": "?0",
#                     "sec-ch-ua-platform": "\"macOS\"",
#                     "sec-fetch-dest": "empty",
#                     "sec-fetch-mode": "cors",
#                     "sec-fetch-site": "same-origin",
#                     "x-requested-with": "XMLHttpRequest",
#                     "Referer": "https://ma.oraimo.com/checkout/",
#                     "Referrer-Policy": "strict-origin-when-cross-origin",
#                 })
#                 future.add_done_callback(lambda f: process_response(f.result(), json_data))

# def process_response(response, spin_data):
#     with open("res.txt", "a") as file:
#         file.write(f"From spin : {response.json()} : {response.status_code} | {spin_data} \n")

# if __name__ == "__main__":
#     spin()
