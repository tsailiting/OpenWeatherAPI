import requests


def get_pet_name():
    """Get Pet Name"""
    """Q. Implement a function to do options from 2~4.
1. Get the JSON response from the URL below, and validate the correct HTTP status(200) by printing code “OK”.
2. https://90c4db3d451c4b8db6070b92436aeb36.api.mockbin.io/
3. Print out Julie’s pet, which is different from John’s (i.e., not the same category of pets)
4. Follow by line #3, Print out it’s name
"""
    response = requests.get(
        "https://90c4db3d451c4b8db6070b92436aeb36.api.mockbin.io/")
    data = response.json()
    return data["PetShop"]["Members"]


def main():
    member_pet = get_pet_name()
    julie_pet = member_pet["Julie"]["Pets"]
    print('Julie: ', julie_pet)
    john_pet = member_pet["John"]["Pets"]
    print('John: ', john_pet)
    for pet in julie_pet:
        if pet not in john_pet:
            print('Julie\'s pet: ', julie_pet["Julie"]["Pets"][pet])


main()
