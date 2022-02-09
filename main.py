import random
import requests 

list_images = [
    'https://solindek.tech/avatars/avatar1.jpg',
    'https://solindek.tech/avatars/avatar10.jpg',
    'https://solindek.tech/avatars/avatar11.jpg',
    'https://solindek.tech/avatars/avatar12.jpg',
    'https://solindek.tech/avatars/avatar13.jpg',
    'https://solindek.tech/avatars/avatar14.jpg',
    'https://solindek.tech/avatars/avatar15.jpg',
    'https://solindek.tech/avatars/avatar16.jpg',
    'https://solindek.tech/avatars/avatar17.jpg',
    'https://solindek.tech/avatars/avatar18.jpg',
    'https://solindek.tech/avatars/avatar19.jpg',
    'https://solindek.tech/avatars/avatar2.jpg',
    'https://solindek.tech/avatars/avatar20.jpg',
    'https://solindek.tech/avatars/avatar21.jpg',
    'https://solindek.tech/avatars/avatar22.jpg',
    'https://solindek.tech/avatars/avatar22.png',
    'https://solindek.tech/avatars/avatar23.jpg',
    'https://solindek.tech/avatars/avatar24.jpg',
    'https://solindek.tech/avatars/avatar25.jpg',
    'https://solindek.tech/avatars/avatar3.jpg',
    'https://solindek.tech/avatars/avatar4.jpg',
    'https://solindek.tech/avatars/avatar5.jpg',
    'https://solindek.tech/avatars/avatar6.jpg',
    'https://solindek.tech/avatars/avatar6.jpg',
    'https://solindek.tech/avatars/avatar7.jpg',
    'https://solindek.tech/avatars/avatar8.jpg',
    'https://solindek.tech/avatars/avatar9.jpg',
]

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
