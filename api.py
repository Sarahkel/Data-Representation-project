import requests, json 

#url = "https://api.github.com/users?since=100"
url = "https://cat-fact.herokuapp.com/facts"
response = requests.get(url)
data = response.json()


#Get the file name for the new file to write
# filename = 'githubusers.json'
# with open(filename, 'w') as f:
#     json.dump(data, f, indent=4)