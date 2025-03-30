-- models/music/genre_trends.sql

WITH yearly_genre_stats AS (
    SELECT
        Release_Year,
        Genre,
        SUM(Streams) AS total_streams
    FROM {{ source('demo_dataset', 'music_table') }}
    GROUP BY Release_Year, Genre
)

SELECT
    Release_Year,
    Genre,
    total_streams,
    RANK() OVER (PARTITION BY Release_Year ORDER BY total_streams DESC) AS rank
FROM yearly_genre_stats
ORDER BY Release_Year, rank
