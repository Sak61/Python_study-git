import requests
import pprint

def request():
    
    headers = {'Content-Type': 'audio/flac'}

    params = {'model':'ja-JP_BroadbandModel'}

    #params = (
    #    ('continuous', 'true'), URLにあったけど必要ない？
    #    ('model', 'ja-JP_BroadbandModel'),
    #)

    auth = ('53f2651e-a0f3-4f56-b80b-48be1a01ea3c', 'fwrQj8UqHIZi')

    url = ('https://stream.watsonplatform.net/speech-to-text/api/v1/recognize')

    path = open('/home/fuchigami/Downloads/voice.flac', 'rb').read()

    res = requests.post(url, headers=headers, params=params, data=path,auth=auth)

    pprint.pprint(res.json())

if __name__=="__main__":
    request()