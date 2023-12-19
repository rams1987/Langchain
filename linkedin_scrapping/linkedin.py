import os
import requests


def scrap_linkedin_profile(linkedin_profile_url):
    gist_response = requests.get(
        "https://gist.githubusercontent.com/rams1987/cc2ab893fb048dde8924152a24c47bb2/raw/cf5cfb92decfc487b5850a58793755f8a727f247/linkedin-profile.json"
    )

    data = gist_response.json()
    return data


scrap_linkedin_profile(
    "https://gist.githubusercontent.com/rams1987/cc2ab893fb048dde8924152a24c47bb2/raw/cf5cfb92decfc487b5850a58793755f8a727f247/linkedin-profile.json"
)
