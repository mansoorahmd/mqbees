{{
  config(
    materialized='table',
    unique_key='index'
  )
}}

WITH {{ var('suras')[1] }} AS (
  SELECT
    *
  FROM {{ ref(var('suras')[0]) }}
)

SELECT *
FROM {{ var('suras')[1] }}
