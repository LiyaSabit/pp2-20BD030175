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

#first

def single(movies):
    for i in range(len(movies)):
        for key, value in movies[i].items():
            if key == 'imdb':
                if value >= 5.5:
                    print(movies[i].get('name'), "TRUE")
                else:
                    print(movies[i].get('name'), "FALSE")


# single(movies)

#second

def sub(movies):
    n = 1
    for i in range(len(movies)):
        for key, value in movies[i].items():
            if key == 'imdb':
                if value >= 5.5:
                    print(n, ". ", movies[i:i+1], sep='')
                n=n+1

# sub(movies)

#third

def category(movies):
    l = []
    for i in range(len(movies)):
        for key, value in movies[i].items():
            if key == 'category':
                if value not in l:
                    l.append(value)
    for i in range(len(l)):
        print(l[i], ':' , sep='', end='\n')
        for j in range(len(movies)):
            for key, value in movies[j].items():
                if key == 'category':
                    if value == l[i]:
                        print(movies[j].get('name'))
                        
# category(movies)


#fourth

def average(movies):
    sum = 0
    cnt = 0
    for i in range(len(movies)):
        for key, value in movies[i].items():
            if key == 'imdb':
                cnt+=1
                sum+=value        
    print(round(sum/cnt, 1))

# average(movies)

#fifth

def avv(movies):
    l = []
    for i in range(len(movies)):
        for key, value in movies[i].items():
            if key == 'category':
                if value not in l:
                    l.append(value)
    for i in range(len(l)):
        cnt = 0
        sum = 0
        print(l[i], ':' , sep='')
        for j in range(len(movies)):
            for key, value in movies[j].items():
                if key == 'category':
                    if value == l[i]:
                        cnt+=1
                        sum+=movies[j].get('imdb')
        print(round(sum/cnt, 1))

# avv(movies)