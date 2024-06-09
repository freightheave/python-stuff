#google play music is deprecated donot use this anymore!
import csv
from gmusicapi import Mobileclient

api = Mobileclient()

api.oauth_login(device_id=Mobileclient.FROM_MAC_ADDRESS, oauth_credentials='path_to_OAuth_Token', locale='en_IN')

#   --- CODE TO GET SONGS ---

songs = api.get_all_songs(incremental=False, include_deleted=None, updated_after=None)

with open('songs.csv', 'w', newline='') as file:
    fieldnames = ['title', 'artist','album','albumArtist']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(songs)):
        writer.writerow({'title':songs[i].get('title', 'Blank'), 'artist':songs[i].get('artist', 'Blank'),'album':songs[i].get('album', 'Blank'),'albumArtist':songs[i].get('albumArtist', 'Blank')})

api.logout()
