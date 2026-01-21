import requests

BASE_URL = "http://127.0.0.1:8080"
IMAGE_URL = "https://media.istockphoto.com/id/814423752/uk/%D1%84%D0%BE%D1%82%D0%BE/%D0%BE%D0%BA%D0%BE-%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%96-%D0%B7-%D0%B1%D0%B0%D1%80%D0%B2%D0%B8%D1%81%D1%82%D0%B8%D0%BC-%D1%85%D1%83%D0%B4%D0%BE%D0%B6%D0%BD%D1%96%D0%BC-%D0%BC%D0%B0%D0%BA%D1%96%D1%8F%D0%B6%D0%B5%D0%BC-%D0%BA%D1%80%D1%83%D0%BF%D0%BD%D0%B8%D0%BC-%D0%BF%D0%BB%D0%B0%D0%BD%D0%BE%D0%BC.jpg?s=1024x1024&w=is&k=20&c=OWdPj-_3hyq_TrJQrlydUDbSsZ63pL_XVK3dYcgNqt4="

LOCAL_FILE = "black_eye.jpg"

img = requests.get(IMAGE_URL).content
with open(LOCAL_FILE, "wb") as f:
    f.write(img)

with open(LOCAL_FILE, "rb") as f:
    files_to_upload = {"image": f}
    request_post = requests.post(f"{BASE_URL}/upload", files=files_to_upload)

print("POST:", request_post.status_code, request_post.json())

image_url = request_post.json()["image_url"]
filename = image_url.split("/")[-1]

headers = {"Content-Type": "text"}
request_get = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
print("GET:", request_get.status_code, request_get.json())

request_del = requests.delete(f"{BASE_URL}/delete/{filename}")
print("DELETE:", request_del.status_code, request_del.json())
=======


def upload_get_delete(image_url: str, local_file: str):
    img = requests.get(image_url).content
    with open(local_file, "wb") as f:
        f.write(img)

    with open(local_file, "rb") as f:
        files_to_upload = {"image": f}
        request_post = requests.post(f"{BASE_URL}/upload", files=files_to_upload)

    print("POST:", request_post.status_code, request_post.json())

    image_url = request_post.json()["image_url"]
    filename = image_url.split("/")[-1]

    headers = {"Content-Type": "text"}
    request_get = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
    print("GET:", request_get.status_code, request_get.json())

    request_del = requests.delete(f"{BASE_URL}/delete/{filename}")
    print("DELETE:", request_del.status_code, request_del.json())


upload_get_delete(IMAGE_URL, "black_eye.jpg")

