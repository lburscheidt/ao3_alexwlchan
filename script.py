from ao3 import AO3
api = AO3()

with open('/home/max/Desktop/Alexwlchan ao3/2025 AO3 ids.txt') as f:
    lines = f.read().splitlines()

    for line in lines:
        work = api.work(id=line)
        try:    
            print(work.json())
        except Exception:
            print("Error on " + str(work.id))
#        >>> work.json()
#'{"rating": ["Teen And Up Audiences"], "fandoms": ["Anthropomorfic - Fandom"], "characters": ["Pinboard", "Delicious - Character", "Diigo - Character"], "language": "English", "additional_tags": ["crackfic", "Meta", "so very not my usual thing"], "warnings": [], "id": "258626", "stats": {"hits": 43037, "words": 605, "bookmarks": 99, "comments": 122, "published": "2011-09-29", "kudos": 1238}, "author": "ambyr", "category": ["F/M"], "title": "The Morning After", "relationship": ["Pinboard/Fandom"], "summary": "<p>Delicious just can\'t understand why it\'s the shy, quiet ones who get all the girls.</p>"}'