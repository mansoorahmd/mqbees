-- model: quran_simple_min
WITH sqlite_data AS (
  SELECT ROW_NUMBER() OVER (ORDER BY SurahNumber,AyahNumber) - 1 as _index,ROW_NUMBER() OVER (ORDER BY SurahNumber,AyahNumber) as _globalAyah, *
  FROM {{ source('quran_sqlite_source', 'sc_loaded_quran-simple-min') }}
)

SELECT *
FROM sqlite_data;