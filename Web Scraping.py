import requests
from bs4 import BeautifulSoup

# Define URL for TripAdvisor search results page
url = 'https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html'

# Send request to URL and get response HTML
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all hotel cards on the page
hotel_cards = soup.find_all('div', {'class': 'ui_container'})

# Loop through each hotel card and extract data
for card in hotel_cards:
    # Extract hotel name
    hotel_name = card.find('a', {'class': 'property_title'}).text.strip()

    # Extract hotel rating
    rating_span = card.find('span', {'class': 'ui_bubble_rating'})
    if rating_span:
        rating = rating_span['alt'].split()[0]
    else:
        rating = None

    # Extract hotel address
    address_span = card.find('span', {'class': 'ui_link'})
    if address_span:
        address = address_span.text.strip()
    else:
        address = None

    # Print hotel data
    print('Hotel Name: {}'.format(hotel_name))
    print('Rating: {}'.format(rating))
    print('Address: {}'.format(address))
    print('--------------------------')