import os
from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv


def search_image(text: str) -> str:
    load_dotenv()
    GCS_DEVELOPER_KEY = os.getenv('GOOGLE_TOKEN')
    GCS_CX = os.getenv('GOOGLE_CX')
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
    _search_params = {
        'q': text,
        'num': 1,
        'safe': 'high',
        'fileType': 'jpg'}
#        'imgType': 'clipart|face|lineart|news|photo',
#        'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
#        'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow',
#        'imgColorType': 'color|gray|mono|trans',
#        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'}
    gis.search(search_params=_search_params)
    return gis.results()[0].get_raw_data()

# this will search and download:
# gis.search(search_params=_search_params, path_to_dir='/path/')

# this will search, download and resize:
# gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# search first, then download and resize afterwards:
# gis.search(search_params=_search_params)
# for image in gis.results():
#    image.download('/path/')
#    image.resize(500, 500)