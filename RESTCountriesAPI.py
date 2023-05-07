import requests
import csv

# make a request to the Rest Countries API to retrieve data on all countries
response = requests.get("https://restcountries.com/v2/all")

# parse the response JSON data
countries_data = response.json()

# create a list to hold the country data
country_list = []

# iterate over the countries and extract all available data for each one
for country in countries_data:
    name = country['name']
    alpha_code_2 = country['alpha2Code']
    alpha_code_3 = country['alpha3Code']
    capital = country['capital'] if 'capital' in country else None
    region = country['region'] if 'region' in country else None
    subregion = country['subregion'] if 'subregion' in country else None
    population = country['population'] if 'population' in country else None
    area = country['area'] if 'area' in country else None
    timezones = country['timezones'] if 'timezones' in country else None
    currencies = [currency['name'] for currency in country['currencies']] if 'currencies' in country else None
    languages = [language['name'] for language in country['languages']] if 'languages' in country else None
    borders = country['borders'] if 'borders' in country else None
    flag = country['flag'] if 'flag' in country else None
    
    # append the data to the country list
    country_list.append([name, alpha_code_2, alpha_code_3, capital, region, subregion,
                         population, area, timezones, currencies, languages, borders, flag])

# write the country data to a CSV file
with open('rest_countries_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Alpha-2 Code', 'Alpha-3 Code', 'Capital', 'Region',
                     'Subregion', 'Population', 'Area', 'Timezones', 'Currencies',
                     'Languages', 'Borders', 'Flag'])
    writer.writerows(country_list)

print(f"{len(country_list)} countries data saved to rest_countries_data.csv")
