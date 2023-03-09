{{
  config(
    materialized='table',
    unique_key='index'
  )
}}

WITH {{ var('pages')[1] }} AS (
  SELECT
    *
  FROM {{ ref(var('pages')[0]) }}
)

SELECT *
FROM {{ var('pages')[1] }}
