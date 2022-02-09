import random
import requests 

list_images = [f'https://solindek.tech/avatars/avatar{_}.jpg' for _ in range(26)]

Url = random.choice(list_images)

print("Random avatar: " + Url)

Inp = True

while Inp:
    choice = input("Do you want to download it? Y/N >>> ")
    if choice.lower() == 'y':
        Inp = False
        r = requests.get(Url, allow_redirects=True)

        open(Url.replace('https://solindek.tech/avatars/', ''), 'wb').write(r.content)

        print("File has download... Output in " + Url.replace('https://solindek.tech/avatars/', ''))
    elif choice.lower() == 'n':
        Inp = False
        print("So you dont want to download an avatar..")
    else:
        print("Invalid choice...")
        Inp = True
