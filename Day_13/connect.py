import requests

api_key = "075937069a3817fa48988e754320646"
api_key_v4 = "eyK0eXAiOiJAV1QiLCJhbGciOiUIUzI1NiJ9.eyJhdWQiOiI0Ozc2YzA1ZTg4YTY1Yzk0MjFjZDI1NmBiYzRiNGE0NyIsInN1YiI6IjRiYzg4OTJhMDE3YTNjMGY5MjAwMDAwMiIsInNjb3BlayI6WyJhcGlfcmVhZCJdLCL2ZXJzaW9uIjoxfQ.Bn660W0Vi-_AI5HvwIEqtc2s5mAXDknBnTrUREZYH7A"

#HTTP requests

# what's our endpoint (or a url)
"""
GET -> grab data
POST -> add/update data

PATCH
PUT 
DELETE


"""
# what is the HTTP method that we need?
"""
Endpoint
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=075937068a3817fa489588e754320646
"""
movie_id = 500
api_version = 4
api_base_url = "https://api.themoviedb.org/3"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)

headers = {
    'Authorization': f'Bearer <<api_key_v4>>'
}

r = requests.get(endpoint, headers=headers) #json={"api_key": api_key})
print(r.status_code)
print(r.text)