movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
import random
def singl():
    a = random.randint(1, 10)
    if movies[a].get("imdb") >= 5.5:
        print("True")
    else:
        print("Else")
    return ""

#2
def imdb():
    a = [p for p in movies if p.get("imdb") >= 5.5]
    for i in a:
        print(i.get("name"))
    return ""

#3
def cat(category):
    a = [p for p in movies]
    for i in a:
        if i.get("category") == category:
            print(i.get("name"))
    return ""

#4
def ave(list):
    p = 0
    k = 0
    for i in list:
        p += int(i.get("imdb"))
        k += 1
    print(p / k)
    return ""

#5
def ave2(category):
    p = 0
    k = 0
    a = [p for p in movies if p.get("category") == category]
    for i in a:
        p += int(i.get("imdb"))
        k += 1
    print(p / k)
    return ""