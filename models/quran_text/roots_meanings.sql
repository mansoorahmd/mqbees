-- model: quran_simple_clean
WITH sqlite_data AS (
  SELECT *
  FROM {{ source('quran_sqlite_source', 'roots_meanings') }}
)
SELECT *
FROM sqlite_data;

