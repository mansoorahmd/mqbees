{{
  config(
    materialized='table',
    unique_key='index'
  )
}}

WITH {{ var('rukus')[1] }} AS (
  SELECT
    *
  FROM {{ ref(var('rukus')[0]) }}
)

SELECT *
FROM {{ var('rukus')[1] }}
