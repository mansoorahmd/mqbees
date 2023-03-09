{{
  config(
    materialized='table',
    unique_key='index'
  )
}}

WITH {{ var('hizbs')[1] }} AS (
  SELECT
    *
  FROM {{ ref(var('hizbs')[0]) }}
)

SELECT *
FROM {{ var('hizbs')[1] }}
