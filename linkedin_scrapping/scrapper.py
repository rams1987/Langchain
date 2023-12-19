import requests

#
# api_key = 's9u6JEYlDJ3fZjqWl1Le5A'
# headers = {'Authorization': 'Bearer ' + api_key}
# api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
#
# params = {
#     'linkedin_profile_url': 'https://linkedin.com/in/johnrmarty/',
# }
#
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=headers)

gist_response = requests.get(
    "https://gist.githubusercontent.com/rams1987/cc2ab893fb048dde8924152a24c47bb2/raw/cf5cfb92decfc487b5850a58793755f8a727f247/linkedin-profile.json"
)
