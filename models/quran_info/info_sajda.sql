{{
  config(
    materialized='table',
    unique_key='index'
  )
}}

WITH {{ var('sajdas')[1] }} AS (
  SELECT
    *
  FROM {{ ref(var('sajdas')[0]) }}
)

SELECT *
FROM {{ var('sajdas')[1] }}
