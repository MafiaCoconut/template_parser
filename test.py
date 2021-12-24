import json


data = {}
list_games = ['GTA5', 'League']
for game in list_games:
    data[game] = []
    for i in range(5):
        video = {
            "channel name": "name",
            "video title": "title",
            "number of viewers": "151",
            "url": "https://www.youtube.com/watch?v=4CtMYbAkU80"
        }
        data[game].append(video)

print(data)


with open('data/test.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)



