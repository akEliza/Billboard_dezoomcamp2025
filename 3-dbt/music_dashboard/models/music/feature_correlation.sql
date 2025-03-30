-- models/music/feature_correlation.sql

SELECT
    CORR(Lyrics_Sentiment, Streams) AS corr_lyrics_streams,
    CORR(TikTok_Virality, Streams) AS corr_tiktok_streams,
    CORR(Danceability, Streams) AS corr_danceability_streams,
    CORR(Acousticness, Streams) AS corr_acousticness_streams,
    CORR(Energy, Streams) AS corr_energy_streams
FROM {{ source('demo_dataset', 'music_table') }}
