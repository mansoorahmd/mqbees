-- model: quran_simple_clean
WITH sqlite_data AS (
  SELECT ROW_NUMBER() OVER (ORDER BY SurahNumber,AyahNumber) - 1 as _index, *
  FROM {{ source('quran_sqlite_source', 'sc_loaded_quran-simple-clean') }}
)
SELECT *
FROM sqlite_data;

