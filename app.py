import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Spotify API credentials
CLIENT_ID = "eee640c4138a45a7a005d82886ce9041"
CLIENT_SECRET = "053059dd4e034968a2b9390106e3bb11"

# Initialize Spotipy client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get song album cover URL
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    result = sp.search(q=search_query, type="track")

    if result and result['tracks']['items']:
        track = result['tracks']['items'][0]
        album_cover_url = track['album']['images'][0]['url']
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

# Function to get Spotify track URL
def get_spotify_track_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    result = sp.search(q=search_query, type="track")

    if result and result['tracks']['items']:
        track = result['tracks']['items'][0]
        track_url = track['external_urls']['spotify']
        return track_url
    else:
        return ""

# Function to recommend songs based on similarity
def recommend(song, num_recommendations):
    idx = music[music['song']==song].index[0]
    distances = similarity[idx]
    sorted_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)
    recommended_music_names=[]
    recommended_music_posters = []
    for i in sorted_indices[1:num_recommendations+1]:
        artist = music.iloc[i[0]].artist
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)
    return recommended_music_names, recommended_music_posters

# Streamlit UI
st.header("Music Recommender")

# Load data
music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Select song from dropdown
music_list = music['song'].values
selected_music = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

# Input number of recommendations
num_recommendations = st.number_input("Number of recommendations", min_value=1, max_value=10, value=5, step=1)

# Button to show recommendations
if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters = recommend(selected_music, num_recommendations)
    cols = st.columns(num_recommendations)
    for i in range(num_recommendations):
        with cols[i]:
            st.text(recommended_music_names[i])
            st.image(recommended_music_posters[i])
            track_url = get_spotify_track_url(recommended_music_names[i], music.iloc[i+1].artist)
            if track_url:
                st.markdown(f"[Listen on Spotify]({track_url})")
            else:
                st.markdown(f"Not Found ")
