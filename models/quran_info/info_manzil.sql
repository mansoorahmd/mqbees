{{
  config(
    materialized='table',
    unique_key='index'
  )
}}

WITH {{ var('manzils')[1] }} AS (
  SELECT
    *
  FROM {{ ref(var('manzils')[0]) }}
)

SELECT *
FROM {{ var('manzils')[1] }}
