-- model: quran_simple_clean
WITH sqlite_data AS (
  SELECT *
  FROM {{ source('quran_sqlite_source', 'morphology') }}
)
SELECT *
FROM sqlite_data;

