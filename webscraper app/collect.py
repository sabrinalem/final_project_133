import spotipy
import config
import pandas as pd
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.SPOTIPY_CLIENT_ID,
                                                           client_secret=config.SPOTIPY_CLIENT_SECRET))

                                                
import_data = pd.read_csv("data/master/combine.csv")
master_data = import_data.copy()
master_data['search'] = master_data['SongName'] + ", " + master_data['ArtistName']

master_data['search'].to_csv('search.csv')
search = master_data['search'].to_list()

def aft(x):
    result = sp.search(q = x, type= "track")
    if len(result['tracks']['items'])>0:
        track_id = result['tracks']['items'][0]['id']
        aft = sp.audio_features(track_id)
        if aft == []:
            aft =""
        else:
            aft = aft[0]
    else:
        aft = ""
    return aft

## DANCEABILITY ##
# danceability_0_1000 = []
# for n in search[:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         danceability_0_1000.append((n, None))
#         print(n)
#     else:
#         danceability_0_1000.append((n, aft(n)['danceability']))
#         print(n)

# make sure to save and store values
# danceability_0_1000_df = pd.DataFrame(danceability_0_1000)
# danceability_0_1000_df.to_csv('aft_danceability.csv')
##################
# danceability_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         danceability_1001_2001.append((n, None))
#         print(n)
#     else:
#         danceability_1001_2001.append((n, aft(n)['danceability']))
#         print(n)

# make sure to save and store values
# danceability_1001_2001_df = pd.DataFrame(danceability_1001_2001)
# danceability_1001_2001_df.to_csv('aft_danceability1.csv')
# ###################
# danceability_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         danceability_2001_3001.append((n,None))
#         print(n)
#     else:
#         danceability_2001_3001.append((n, aft(n)['danceability']))
#         print(n)

# make sure to save and store values
# danceability_2001_3001_df = pd.DataFrame(danceability_2001_3001)
# danceability_2001_3001_df.to_csv('aft_danceability2.csv')
# ###################
# danceability_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         danceability_3001_4001.append((n,None))
#         print(n)
#     else:
#         danceability_3001_4001.append((n, aft(n)['danceability']))
#         print(n)

# make sure to save and store values
# danceability_3001_4001_df = pd.DataFrame(danceability_3001_4001)
# danceability_3001_4001_df.to_csv('aft_danceability3.csv')
# ###################
# danceability_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         danceability_4001_5001.append((n, None))
#         print(n)
#     else:
#         danceability_4001_5001.append((n, aft(n)['danceability']))
#         print(n)

# make sure to save and store values
# danceability_4001_5001_df = pd.DataFrame(danceability_4001_5001)
# danceability_4001_5001_df.to_csv('aft_danceability4.csv')
###################
# danceability_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         danceability_5001_end.append((n, None))
#         print(n)
#     else:
#         danceability_5001_end.append((n, aft(n)['danceability']))
#         print(n)

# # make sure to save and store values
# danceability_5001_end_df = pd.DataFrame(danceability_5001_end)
# danceability_5001_end_df.to_csv('aft_danceability5.csv')


## ENERGY ##
# energy_0_1000 = []
# for n in search[0:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         energy_0_1000.append((n, None))
#         print(n)
#     else:
#         energy_0_1000.append((n, aft(n)['energy']))
#         print(n)

# # make sure to save and store values
# energy_0_1000_df = pd.DataFrame(energy_0_1000)
# energy_0_1000_df.to_csv('aft_energy.csv')
##################
# energy_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         energy_1001_2001.append((n,None))
#         print(n)
#     else:
#         energy_1001_2001.append((n, aft(n)['energy']))
#         print(n)

# # make sure to save and store values
# energy_1001_2001_df = pd.DataFrame(energy_1001_2001)
# energy_1001_2001_df.to_csv('aft_energy1.csv')
# ###################
# energy_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         energy_2001_3001.append((n,None))
#         print(n)
#     else:
#         energy_2001_3001.append((n, aft(n)['energy']))
#         print(n)

# make sure to save and store values
# energy_2001_3001_df = pd.DataFrame(energy_2001_3001)
# energy_2001_3001_df.to_csv('aft_energy2.csv')
###################
# energy_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         energy_3001_4001.append((n,None))
#         print(n)
#     else:
#         energy_3001_4001.append((n, aft(n)['energy']))
#         print(n)

# # make sure to save and store values
# energy_3001_4001_df = pd.DataFrame(energy_3001_4001)
# energy_3001_4001_df.to_csv('aft_energy3.csv')
###################
# energy_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         energy_4001_5001.append((n,None))
#         print(n)
#     else:
#         energy_4001_5001.append((n, aft(n)['energy']))
#         print(n)

# # make sure to save and store values
# energy_4001_5001_df = pd.DataFrame(energy_4001_5001)
# energy_4001_5001_df.to_csv('aft_energy4.csv')
###################
# energy_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         energy_5001_end.append(None)
#         print(n)
#     else:
#         energy_5001_end.append((n, aft(n)['energy']))
#         print(n)

# # make sure to save and store values
# energy_5001_end_df = pd.DataFrame(energy_5001_end)
# energy_5001_end_df.to_csv('aft_energy5.csv')


## LOUDNESS ##
# loudness_0_1000 = []
# for n in search[0:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         loudness_0_1000.append((n,None))
#         print(n)
#     else:
#         loudness_0_1000.append((n, aft(n)['loudness']))
#         print(n)

# # make sure to save and store values
# loudness_0_1000_df = pd.DataFrame(loudness_0_1000)
# loudness_0_1000_df.to_csv('aft_loudness.csv')
##################
# loudness_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         loudness_1001_2001.append((n, None))
#         print(n)
#     else:
#         loudness_1001_2001.append((n, aft(n)['loudness']))
#         print(n)

# # make sure to save and store values
# loudness_1001_2001_df = pd.DataFrame(loudness_1001_2001)
# loudness_1001_2001_df.to_csv('aft_loudness1.csv')
###################
# loudness_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         loudness_2001_3001.append((n,None))
#         print(n)
#     else:
#         loudness_2001_3001.append((n, aft(n)['loudness']))
#         print(n)

# # make sure to save and store values
# loudness_2001_3001_df = pd.DataFrame(loudness_2001_3001)
# loudness_2001_3001_df.to_csv('aft_loudness2.csv')
####################
# loudness_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         loudness_3001_4001.append((n,None))
#         print(n)
#     else:
#         loudness_3001_4001.append((n, aft(n)['loudness']))
#         print(n)

# # make sure to save and store values
# loudness_3001_4001_df = pd.DataFrame(loudness_3001_4001)
# loudness_3001_4001_df.to_csv('aft_loudness3.csv')
###################
# loudness_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         loudness_4001_5001.append((n,None))
#         print(n)
#     else:
#         loudness_4001_5001.append((n, aft(n)['loudness']))
#         print(n)

# # make sure to save and store values
# loudness_4001_5001_df = pd.DataFrame(loudness_4001_5001)
# loudness_4001_5001_df.to_csv('aft_loudness4.csv')

# ###################
# loudness_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         loudness_5001_end.append((n,None))
#         print(n)
#     else:
#         loudness_5001_end.append((n, aft(n)['loudness']))
#         print(n)

# # make sure to save and store values
# loudness_5001_end_df = pd.DataFrame(loudness_5001_end)
# loudness_5001_end_df.to_csv('aft_loudness5.csv')



## SPEECHINESS ##
# speechiness_0_1000 = []
# for n in search[0:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         speechiness_0_1000.append((n,None))
#         print(n)
#     else:
#         speechiness_0_1000.append((n,aft(n)['speechiness']))
#         print(n)

# # make sure to save and store values
# speechiness_0_1000_df = pd.DataFrame(speechiness_0_1000)
# speechiness_0_1000_df.to_csv('aft_speechiness.csv')
##################
# speechiness_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         speechiness_1001_2001.append((n,None))
#         print(n)
#     else:
#         speechiness_1001_2001.append((n,aft(n)['speechiness']))
#         print(n)

# # make sure to save and store values
# speechiness_1001_2001_df = pd.DataFrame(speechiness_1001_2001)
# speechiness_1001_2001_df.to_csv('aft_speechiness1.csv')
# ###################
# speechiness_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         speechiness_2001_3001.append((n,None))
#         print(n)
#     else:
#         speechiness_2001_3001.append((n,aft(n)['speechiness']))
#         print(n)

# # make sure to save and store values
# speechiness_2001_3001_df = pd.DataFrame(speechiness_2001_3001)
# speechiness_2001_3001_df.to_csv('aft_speechiness2.csv')
###################
# speechiness_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         speechiness_3001_4001.append((n,None))
#         print(n)
#     else:
#         speechiness_3001_4001.append((n,aft(n)['speechiness']))
#         print(n)

# # make sure to save and store values
# speechiness_3001_4001_df = pd.DataFrame(speechiness_3001_4001)
# speechiness_3001_4001_df.to_csv('aft_speechiness3.csv')
# ###################
# speechiness_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         speechiness_4001_5001.append((n,None))
#         print(n)
#     else:
#         speechiness_4001_5001.append((n,aft(n)['speechiness']))
#         print(n)

# # make sure to save and store values
# speechiness_4001_5001_df = pd.DataFrame(speechiness_4001_5001)
# speechiness_4001_5001_df.to_csv('aft_speechiness4.csv')
###################
# speechiness_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         speechiness_5001_end.append((n,None))
#         print(n)
#     else:
#         speechiness_5001_end.append((n,aft(n)['speechiness']))
#         print(n)

# # make sure to save and store values
# speechiness_5001_end_df = pd.DataFrame(speechiness_5001_end)
# speechiness_5001_end_df.to_csv('aft_speechiness5.csv')


## ACOUSTICNESS ##
# acousticness_0_1000 = []
# for n in search[0:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         acousticness_0_1000.append(n,None)
#         print(n)
#     else:
#         acousticness_0_1000.append((n, aft(n)['acousticness']))
#         print(n)

# # make sure to save and store values
# acousticness_0_1000_df = pd.DataFrame(acousticness_0_1000)
# acousticness_0_1000_df.to_csv('aft_acousticness.csv')
##################
# acousticness_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         acousticness_1001_2001.append(n,None)
#         print(n)
#     else:
#         acousticness_1001_2001.append((n, aft(n)['acousticness']))
#         print(n)

# # make sure to save and store values
# acousticness_1001_2001_df = pd.DataFrame(acousticness_1001_2001)
# acousticness_1001_2001_df.to_csv('aft_acousticness1.csv')
###################
# acousticness_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         acousticness_2001_3001.append(n, NOne)
#         print(n)
#     else:
#         acousticness_2001_3001.append((n, aft(n)['acousticness']))
#         print(n)

# # make sure to save and store values
# acousticness_2001_3001_df = pd.DataFrame(acousticness_2001_3001)
# acousticness_2001_3001_df.to_csv('aft_acousticness2.csv')
# ###################
# acousticness_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         acousticness_3001_4001.append((n, None))
#         print(n)
#     else:
#         acousticness_3001_4001.append((n, aft(n)['acousticness']))
#         print(n)

# # make sure to save and store values
# acousticness_3001_4001_df = pd.DataFrame(acousticness_3001_4001)
# acousticness_3001_4001_df.to_csv('aft_acousticness3.csv')
###################
# acousticness_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         acousticness_4001_5001.append(n,None)
#         print(n)
#     else:
#         acousticness_4001_5001.append((n, aft(n)['acousticness']))
#         print(n)

# # make sure to save and store values
# acousticness_4001_5001_df = pd.DataFrame(acousticness_4001_5001)
# acousticness_4001_5001_df.to_csv('aft_acousticness4.csv')
###################
# acousticness_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         acousticness_5001_end.append((n, None))
#         print(n)
#     else:
#         acousticness_5001_end.append((n,aft(n)['acousticness']))
#         print(n)

# # make sure to save and store values
# acousticness_5001_end_df = pd.DataFrame(acousticness_5001_end)
# acousticness_5001_end_df.to_csv('aft_acousticness5.csv')



## INSTRUMENTALNESS ##
# instrumentalness_0_1000 = []
# for n in search[0:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         instrumentalness_0_1000.append((n, None))
#         print(n)
#     else:
#         instrumentalness_0_1000.append((n, aft(n)['instrumentalness']))
#         print(n)

# # make sure to save and store values
# instrumentalness_0_1000_df = pd.DataFrame(instrumentalness_0_1000)
# instrumentalness_0_1000_df.to_csv('aft_instrumentalness.csv')
##################
# instrumentalness_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         instrumentalness_1001_2001.append((n,None))
#         print(n)
#     else:
#         instrumentalness_1001_2001.append((n, aft(n)['instrumentalness']))
#         print(n)

# # make sure to save and store values
# instrumentalness_1001_2001_df = pd.DataFrame(instrumentalness_1001_2001)
# instrumentalness_1001_2001_df.to_csv('aft_instrumentalness1.csv')
# ###################
# instrumentalness_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         instrumentalness_2001_3001.append((n,None))
#         print(n)
#     else:
#         instrumentalness_2001_3001.append((n, aft(n)['instrumentalness']))
#         print(n)

# # make sure to save and store values
# instrumentalness_2001_3001_df = pd.DataFrame(instrumentalness_2001_3001)
# instrumentalness_2001_3001_df.to_csv('aft_instrumentalness2.csv')
# ###################
# instrumentalness_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         instrumentalness_3001_4001.append((n, None))
#         print(n)
#     else:
#         instrumentalness_3001_4001.append((n, aft(n)['instrumentalness']))
#         print(n)

# # make sure to save and store values
# instrumentalness_3001_4001_df = pd.DataFrame(instrumentalness_3001_4001)
# instrumentalness_3001_4001_df.to_csv('aft_instrumentalness3.csv')

# ###################
# instrumentalness_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         instrumentalness_4001_5001.append((n,None))
#         print(n)
#     else:
#         instrumentalness_4001_5001.append((n, aft(n)['instrumentalness']))
#         print(n)

# # make sure to save and store values
# instrumentalness_4001_5001_df = pd.DataFrame(instrumentalness_4001_5001)
# instrumentalness_4001_5001_df.to_csv('aft_instrumentalness4.csv')
# ###################
# instrumentalness_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         instrumentalness_5001_end.append((n,None))
#         print(n)
#     else:
#         instrumentalness_5001_end.append((n, aft(n)['instrumentalness']))
#         print(n)

# # make sure to save and store values
# instrumentalness_5001_end_df = pd.DataFrame(instrumentalness_5001_end)
# instrumentalness_5001_end_df.to_csv('aft_instrumentalness5.csv')


## LIVENESS ##
# liveness_0_1000 = []
# for n in search[0:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         liveness_0_1000.append((n,None))
#         print(n)
#     else:
#         liveness_0_1000.append((n, aft(n)['liveness']))
#         print(n)

# # make sure to save and store values
# liveness_0_1000_df = pd.DataFrame(liveness_0_1000)
# liveness_0_1000_df.to_csv('aft_liveness.csv')
##################
# liveness_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         liveness_1001_2001.append((n,None))
#         print(n)
#     else:
#         liveness_1001_2001.append((n, aft(n)['liveness']))
#         print(n)

# # make sure to save and store values
# liveness_1001_2001_df = pd.DataFrame(liveness_1001_2001)
# liveness_1001_2001_df.to_csv('aft_liveness1.csv')
# ###################
# liveness_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         liveness_2001_3001.append((n,None))
#         print(n)
#     else:
#         liveness_2001_3001.append((n, aft(n)['liveness']))
#         print(n)

# # make sure to save and store values
# liveness_2001_3001_df = pd.DataFrame(liveness_2001_3001)
# liveness_2001_3001_df.to_csv('aft_liveness2.csv')

###################
# liveness_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         liveness_3001_4001.append((n,None))
#         print(n)
#     else:
#         liveness_3001_4001.append((n, aft(n)['liveness']))
#         print(n)

# # make sure to save and store values
# liveness_3001_4001_df = pd.DataFrame(liveness_3001_4001)
# liveness_3001_4001_df.to_csv('aft_liveness3.csv')

###################
# liveness_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         liveness_4001_5001.append((n,None))
#         print(n)
#     else:
#         liveness_4001_5001.append((n, aft(n)['liveness']))
#         print(n)

# # make sure to save and store values
# liveness_4001_5001_df = pd.DataFrame(liveness_4001_5001)
# liveness_4001_5001_df.to_csv('aft_liveness4.csv')


# ###################
# liveness_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         liveness_5001_end.append((n,None))
#         print(n)
#     else:
#         liveness_5001_end.append(aft(n)['liveness'])
#         print(n)

# # make sure to save and store values
# liveness_5001_end_df = pd.DataFrame(liveness_5001_end)
# liveness_5001_end_df.to_csv('aft_liveness5.csv')



## VALENCE ## 
# valence_0_1000 = []
# for n in search[0:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         valence_0_1000.append((n,None))
#         print(n)
#     else:
#         valence_0_1000.append((n, aft(n)['valence']))
#         print(n)

# # make sure to save and store values
# valence_0_1000_df = pd.DataFrame(valence_0_1000)
# valence_0_1000_df.to_csv('aft_valence.csv')
##################
# valence_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         valence_1001_2001.append((n,None))
#         print(n)
#     else:
#         valence_1001_2001.append((n, aft(n)['valence']))
#         print(n)

# # make sure to save and store values
# valence_1001_2001_df = pd.DataFrame(valence_1001_2001)
# valence_1001_2001_df.to_csv('aft_valence1.csv')
# ###################
# valence_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         valence_2001_3001.append((n,None))
#         print(n)
#     else:
#         valence_2001_3001.append((n, aft(n)['valence']))
#         print(n)

# # make sure to save and store values
# valence_2001_3001_df = pd.DataFrame(valence_2001_3001)
# valence_2001_3001_df.to_csv('aft_valence2.csv')

###################
# valence_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         valence_3001_4001.append((n,None))
#         print(n)
#     else:
#         valence_3001_4001.append((n, aft(n)['valence']))
#         print(n)

# # make sure to save and store values
# valence_3001_4001_df = pd.DataFrame(valence_3001_4001)
# valence_3001_4001_df.to_csv('aft_valence3.csv')

# ###################
# valence_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         valence_4001_5001.append((n,None))
#         print(n)
#     else:
#         valence_4001_5001.append((n, aft(n)['valence']))
#         print(n)

# # make sure to save and store values
# valence_4001_5001_df = pd.DataFrame(valence_4001_5001)
# valence_4001_5001_df.to_csv('aft_valence4.csv')


# ###################
# valence_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         valence_5001_end.append((n,None))
#         print(n)
#     else:
#         valence_5001_end.append((n, aft(n)['valence']))
#         print(n)

# # make sure to save and store values
# valence_5001_end_df = pd.DataFrame(valence_5001_end)
# valence_5001_end_df.to_csv('aft_valence5.csv')
 


## TEMPO ##
# tempo_0_1000 = []
# for n in search[0:1001]:
#     if aft(n) == "" or aft(n) == None: 
#         tempo_0_1000.append((n,None))
#         print(n)
#     else:
#         tempo_0_1000.append((n, aft(n)['tempo']))
#         print(n)

# # make sure to save and store values
# tempo_0_1000_df = pd.DataFrame(tempo_0_1000)
# tempo_0_1000_df.to_csv('aft_tempo.csv')
##################
# tempo_1001_2001 = []
# for n in search[1001:2001]:
#     if aft(n) == "" or aft(n) == None: 
#         tempo_1001_2001.append((n,None))
#         print(n)
#     else:
#         tempo_1001_2001.append((n, aft(n)['tempo']))
#         print(n)

# # make sure to save and store values
# tempo_1001_2001_df = pd.DataFrame(tempo_1001_2001)
# tempo_1001_2001_df.to_csv('aft_tempo1.csv')
# ###################
# tempo_2001_3001 = []
# for n in search[2001:3001]:
#     if aft(n) == "" or aft(n) == None: 
#         tempo_2001_3001.append((n,None))
#         print(n)
#     else:
#         tempo_2001_3001.append((n, aft(n)['tempo']))
#         print(n)

# # make sure to save and store values
# tempo_2001_3001_df = pd.DataFrame(tempo_2001_3001)
# tempo_2001_3001_df.to_csv('aft_tempo2.csv')

# ###################
# tempo_3001_4001 = []
# for n in search[3001:4001]:
#     if aft(n) == "" or aft(n) == None: 
#         tempo_3001_4001.append((n,None))
#         print(n)
#     else:
#         tempo_3001_4001.append((n, aft(n)['tempo']))
#         print(n)

# # make sure to save and store values
# tempo_3001_4001_df = pd.DataFrame(tempo_3001_4001)
# tempo_3001_4001_df.to_csv('aft_tempo3.csv')
###################
# tempo_4001_5001 = []
# for n in search[4001:5001]:
#     if aft(n) == "" or aft(n) == None: 
#         tempo_4001_5001.append((n,None))
#         print(n)
#     else:
#         tempo_4001_5001.append((n, aft(n)['tempo']))
#         print(n)

# # make sure to save and store values
# tempo_4001_5001_df = pd.DataFrame(tempo_4001_5001)
# tempo_4001_5001_df.to_csv('aft_tempo4.csv')
###################
# tempo_5001_end = []
# for n in search[5001:]:
#     if aft(n) == "" or aft(n) == None: 
#         tempo_5001_end.append((n,None))
#         print(n)
#     else:
#         tempo_5001_end.append(aft(n)['tempo'])
#         print(n)

# # make sure to save and store values
# tempo_4001_5001_df = pd.DataFrame(tempo_5001_end)
# tempo_4001_5001_df.to_csv('aft_tempo5.csv')

######################################  APPEND AND MERGE  ################################################  
# acousticness = pd.read_csv('data/master/audioft/aft_acousticness.csv')
# acousticness_1 = pd.read_csv('data/master/audioft/aft_acousticness1.csv')
# acousticness_2 = pd.read_csv('data/master/audioft/aft_acousticness2.csv')
# acousticness_3 = pd.read_csv('data/master/audioft/aft_acousticness3.csv')
# acousticness_4 = pd.read_csv('data/master/audioft/aft_acousticness4.csv')
# acousticness_5 = pd.read_csv('data/master/audioft/aft_acousticness5.csv')

# acousticness_aft = acousticness.append(
#     [acousticness_1,acousticness_2,acousticness_3,acousticness_4,acousticness_5])
# acousticness_aft = acousticness_aft[["1"]]

# danceability = pd.read_csv('data/master/audioft/aft_danceability.csv')
# danceability_1 = pd.read_csv('data/master/audioft/aft_danceability1.csv')
# danceability_2 = pd.read_csv('data/master/audioft/aft_danceability2.csv')
# danceability_3 = pd.read_csv('data/master/audioft/aft_danceability3.csv')
# danceability_4 = pd.read_csv('data/master/audioft/aft_danceability4.csv')
# danceability_5 = pd.read_csv('data/master/audioft/aft_danceability5.csv')

# danceability_aft = danceability.append(
#     [danceability_1,danceability_2,danceability_3,danceability_4,danceability_5])
# danceability_aft = danceability_aft[["1"]]


# energy = pd.read_csv('data/master/audioft/aft_energy.csv')
# energy_1 = pd.read_csv('data/master/audioft/aft_energy1.csv')
# energy_2 = pd.read_csv('data/master/audioft/aft_energy2.csv')
# energy_3 = pd.read_csv('data/master/audioft/aft_energy3.csv')
# energy_4 = pd.read_csv('data/master/audioft/aft_energy4.csv')
# energy_5 = pd.read_csv('data/master/audioft/aft_energy5.csv')

# energy_aft = energy.append(
#     [energy_1,energy_2,energy_3,energy_4,energy_5])
# energy_aft = energy_aft[["1"]]


# instrumentalness = pd.read_csv('data/master/audioft/aft_instrumentalness.csv')
# instrumentalness_1 = pd.read_csv('data/master/audioft/aft_instrumentalness1.csv')
# instrumentalness_2 = pd.read_csv('data/master/audioft/aft_instrumentalness2.csv')
# instrumentalness_3 = pd.read_csv('data/master/audioft/aft_instrumentalness3.csv')
# instrumentalness_4 = pd.read_csv('data/master/audioft/aft_instrumentalness4.csv')
# instrumentalness_5 = pd.read_csv('data/master/audioft/aft_instrumentalness5.csv')

# instrumentalness_aft = instrumentalness.append(
#     [instrumentalness_1,instrumentalness_2,instrumentalness_3,instrumentalness_4,instrumentalness_5])
# instrumentalness_aft = instrumentalness_aft[["1"]]


# liveness = pd.read_csv('data/master/audioft/aft_liveness.csv')
# liveness_1 = pd.read_csv('data/master/audioft/aft_liveness1.csv')
# liveness_2 = pd.read_csv('data/master/audioft/aft_liveness2.csv')
# liveness_3 = pd.read_csv('data/master/audioft/aft_liveness3.csv')
# liveness_4 = pd.read_csv('data/master/audioft/aft_liveness4.csv')
# liveness_5 = pd.read_csv('data/master/audioft/aft_liveness5.csv')

# liveness_aft = liveness.append(
#     [liveness_1,liveness_2,liveness_3,liveness_4,liveness_5])
# liveness_aft = liveness_aft[["1"]]


# loudness = pd.read_csv('data/master/audioft/aft_loudness.csv')
# loudness_1 = pd.read_csv('data/master/audioft/aft_loudness1.csv')
# loudness_2 = pd.read_csv('data/master/audioft/aft_loudness2.csv')
# loudness_3 = pd.read_csv('data/master/audioft/aft_loudness3.csv')
# loudness_4 = pd.read_csv('data/master/audioft/aft_loudness4.csv')
# loudness_5 = pd.read_csv('data/master/audioft/aft_loudness5.csv')

# loudness_aft = loudness.append(
#     [loudness_1,loudness_2,loudness_3,loudness_4,loudness_5])
# loudness_aft = loudness_aft[["1"]]


# speechiness = pd.read_csv('data/master/audioft/aft_speechiness.csv')
# speechiness_1 = pd.read_csv('data/master/audioft/aft_speechiness1.csv')
# speechiness_2 = pd.read_csv('data/master/audioft/aft_speechiness2.csv')
# speechiness_3 = pd.read_csv('data/master/audioft/aft_speechiness3.csv')
# speechiness_4 = pd.read_csv('data/master/audioft/aft_speechiness4.csv')
# speechiness_5 = pd.read_csv('data/master/audioft/aft_speechiness5.csv')

# speechiness_aft = speechiness.append(
#     [speechiness_1,speechiness_2,speechiness_3,speechiness_4,speechiness_5])
# speechiness_aft = speechiness_aft[["1"]]


# tempo = pd.read_csv('data/master/audioft/aft_tempo.csv')
# tempo_1 = pd.read_csv('data/master/audioft/aft_tempo1.csv')
# tempo_2 = pd.read_csv('data/master/audioft/aft_tempo2.csv')
# tempo_3 = pd.read_csv('data/master/audioft/aft_tempo3.csv')
# tempo_4 = pd.read_csv('data/master/audioft/aft_tempo4.csv')
# tempo_5 = pd.read_csv('data/master/audioft/aft_tempo5.csv')

# tempo_aft = tempo.append(
#     [tempo_1,tempo_2,tempo_3,tempo_4,tempo_5])
# tempo_aft = tempo_aft[["1"]]


# valence = pd.read_csv('data/master/audioft/aft_valence.csv')
# valence_1 = pd.read_csv('data/master/audioft/aft_valence1.csv')
# valence_2 = pd.read_csv('data/master/audioft/aft_valence2.csv')
# valence_3 = pd.read_csv('data/master/audioft/aft_valence3.csv')
# valence_4 = pd.read_csv('data/master/audioft/aft_valence4.csv')
# valence_5 = pd.read_csv('data/master/audioft/aft_valence5.csv')

# valence_aft = valence.append(
#     [valence_1,valence_2,valence_3,valence_4,valence_5])
# valence_aft = valence_aft[["1"]]

# aft_df = acousticness_aft.rename(columns={"1":"acousticness"})
# aft_df['danceability'] = danceability_aft
# aft_df['energy'] = energy_aft
# aft_df['instrumentalness'] = instrumentalness_aft
# aft_df['liveness'] = liveness_aft
# aft_df['loudness'] = loudness_aft
# aft_df['speechiness'] = speechiness_aft
# aft_df['tempo'] = tempo_aft
# aft_df['valence'] = valence_aft

# aft_df = aft_df.reset_index()
# df1 = pd.read_csv('data/master/combine.csv')
# df1 = df1[["Position", "SongName", "ArtistName", "ReleaseYear", "Win"]].reset_index()

# data =  pd. merge(df1, aft_df, left_index=True, right_index=True)
# data.to_csv('data.csv')

# manually checked and inserted any missing data using excel
# REMOVED 15 rows of data manually due to missing audio feature data

## FINAL DATA SET ##
master_df = pd.read_csv('data/master/master_data.csv')
