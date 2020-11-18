# from requests import get
# import urllib.request as request
# import json

# COUNTRY = ['Belgium', 'Denmark']
# main_api = 'https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true'
# response = get(main_api)
# response_text = response.text
# response_json = response.json()

# for row in response_json:
#     print(row['country'])

# for row in response_json:
#     if row['country'] in COUNTRY:
#         print(row['infected'])

# for row in json.loads(responseT):
#     if row['country'] in COUNTRY:
#         print(row['infected'])

# for row in json.loads(response.text):
#     if row['region'] in COUNTRY:
#         rows.append([
#             row['region'],
#             row['infected'],
#             row['lastUpdatedApify']
#         ])

myList = [
	{
		'foo':12,
		'bar':14
	},
	{
		'foo':52,
		'car':641
	},
	{
		'foo':6,
		'tar':84
	}
]
print(type(myList))
for row in myList:
    if row['foo'] == 52:
        print(row.keys())