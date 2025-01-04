# Music Recommendation System

 ![VideoPreview](https://github.com/user-attachments/assets/ba096b66-738d-4fdd-b30d-0e278a1c0383)

A personalized music recommendation system that combines state-of-the-art machine learning with Spotify API integration. This project uses Python for model development, Streamlit for a user-friendly web interface, and Docker for containerization and deployment.

---

## Features

- **Personalized Recommendations**: Tailored music suggestions based on user preferences and song metadata.
- **Machine Learning Model**: Robust and continuously learning recommendation engine.
- **Streamlit Frontend**: Clean, intuitive interface for seamless user interaction.
- **Spotify Integration**: Direct playback, search, and sharing of recommended tracks.
- **Containerization**: Ensures consistent performance, scalability, and portability.
- **Dataset**: Uses a curated dataset from Kaggle for diverse and accurate suggestions.

---

## How It Works

1. **User Song Selection**: Start by selecting a song you like.
2. **Data Collection**: The system gathers metadata and your listening history.
3. **Feature Engineering**: Key features are extracted to train the model.
4. **Model Training**: Machine learning algorithms are used to train the recommendation engine.
5. **Recommendations**: A curated list of 5 songs is presented based on your preferences.

---

## Technical Details

- **Backend**: Python
- **Frontend**: Streamlit
- **API Integration**: Spotify API for album covers, direct links, and track playback.
- **Containerization**: Docker for deployment and cross-platform compatibility.

---

## Installation

Install Commands
   ```bash
   git clone https://github.com/your-username/music-recommendation-system.git
   pip install -r requirements.txt
   //make sure you run model_training.ipynb 
   docker compose up --build
   
