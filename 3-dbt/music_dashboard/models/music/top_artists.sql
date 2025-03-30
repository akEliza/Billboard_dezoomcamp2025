-- models/music/top_artists.sql

WITH artist_popularity AS (
    SELECT
        Artist,
        SUM(Streams) AS total_streams
    FROM {{ source('demo_dataset', 'music_table') }}
    GROUP BY Artist
),

ranked_artists AS (
    SELECT
        Artist,
        total_streams,
        RANK() OVER (ORDER BY total_streams DESC) AS rank
    FROM artist_popularity
)

SELECT
    Artist,
    total_streams,
    rank
FROM ranked_artists
WHERE rank <= 20  -- 前20艺术家
ORDER BY rank
