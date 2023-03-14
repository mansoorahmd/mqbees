-- model: quran_uthmani
WITH sqlite_data AS (
  SELECT ROW_NUMBER() OVER (ORDER BY SurahNumber,AyahNumber) - 1 as _index, *
  FROM {{ source('quran_sqlite_source', 'sc_loaded_quran-uthmani') }}
)
SELECT *
FROM sqlite_data;