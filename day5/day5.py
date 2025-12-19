"""
tasks = []

tasks.append('Learn Python')
tasks.append('Practise git')
tasks.append('Build project')
tasks.append('Make portfolio')

print('My tasks: ')
for x in tasks:
	print(x)
"""

games = [
	{
		"genre" : "racing",
		"name" : "NFS most wanted",
		"year" : 1923
	},
	{
                "genre" : "fight",
                "name" : "UFC",
                "year" : 2005
        },
	{
                "genre" : "strategy",
                "name" : "Generals",
                "year" : 2000
        },
	{
                "genre" : "racing",
                "name" : "Asetto corsa",
                "year" : "2312"
        },
        {
                "genre" : "fight",
                "name" : "Box",
                "year" : 2005
        },
        {
                "genre" : "strategy",
                "name" : "Generals zero Your",
                "year" : 2000
        }
	]
for game in games :
	if game["genre"] == "racing":
		print(game)

for game in games:
	if game["year"] == 2005:
		print(game)
count = 0
for game in games: 
	count = count + 1
print('total games - ',  count)
