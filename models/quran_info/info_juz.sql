{{
  config(
    materialized='table',
    unique_key='index'
  )
}}

WITH {{ var('juzs')[1] }} AS (
  SELECT
    *
  FROM {{ ref(var('juzs')[0]) }}
)

SELECT *
FROM {{ var('juzs')[1] }}
