import os
import random
from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv


def search_image(text: str) -> str:
    load_dotenv()
    GCS_DEVELOPER_KEY = os.getenv('GOOGLE_TOKEN')
    GCS_CX = os.getenv('GOOGLE_CX')
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX, validate_images=False)
    _search_params = {
        'q': text,
        'num': 10,
        'safe': 'off',
        'fileType': 'jpg',
#        'imgType': 'clipart', 'face', 'lineart', 'news', 'photo',
#        'imgSize': 'LARGE',
#        'imgDominantColor': ('black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow'),
        'imgColorType': 'color'
                    }
    gis.search(search_params=_search_params)
    return random.choice(gis.results()).get_raw_data()

# this will search and download:
# gis.search(search_params=_search_params, path_to_dir='/path/')

# this will search, download and resize:
# gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# search first, then download and resize afterwards:
# gis.search(search_params=_search_params)
# for image in gis.results():
#    image.download('/path/')
#    image.resize(500, 500)