import requests
import sys
import base64


def send_raw_image():
    test_image = "/Users/manuel.martin/personal-projects/imagelens/processor/resources/MSRA-TD500/train/IMG_0030.JPG"
    url = "http://localhost:{PORT}/{ENDPOINT}".format(
        PORT=sys.argv[1], ENDPOINT=sys.argv[2])
    files = {'media': open(test_image, 'rb')}
    requests.post(url, files=files)


if __name__ == "__main__":
    send_raw_image()
