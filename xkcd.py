import requests
import sys
import os

xkcd_url = "https://xkcd.com/info.0.json"


def get_xkcd_json():
    # Make the request.
    response = requests.get(xkcd_url)

    # Get the JSON data from the response object.
    return response.json()


def download_image(image_url, file_name):
    with open(file_name, 'wb') as handle:
        response = requests.get(image_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


# This will totally depend upon the type of OS
def open_image(image_uri):
    platform = get_platform()

    if platform == "OS X":
        os.system('open ' + image_uri)
        pass
    elif platform == "Linux":
        pass
    elif platform == "Windows":
        pass


# This is a helper function to determine the type of OS this script is running on.
def get_platform():
    # Creating a dictionary with the most common responses.
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }

    # If the platform is not in the above dictionary, return it as usual.
    if sys.platform not in platforms:
        return sys.platform

    # If the platform is in the above dictionary, return a friendly os  string.
    return platforms[sys.platform]


# Specifying location for downloaded XKCD images.
# If XKCD_IMAGES_FOLDER is not set, store the images in Pictures folder in user home.
def get_xkcd_download_folder():
    try:
        xkcd_images_folder = os.environ['XKCD_IMAGES_FOLDER']
    except:
        xkcd_images_folder = os.environ['HOME'] + '/Pictures/xkcd/'

    return xkcd_images_folder


def main():
    # Get the JSON from the xkcd website
    xkcd_json = get_xkcd_json()

    # Extract the image url and file name with which the image should be saved.
    image_url = xkcd_json['img']

    file_name = xkcd_json['safe_title'].replace(" ", "") + ".png"

    # Generally, from observation, the file downloaded will be a png.
    # Removing the spaces in the title.
    file_uri = get_xkcd_download_folder() + file_name

    download_image(image_url, file_uri)

    open_image(file_uri)

    print("RAN TO COMPLETION!")


if __name__ == '__main__':
    main()
