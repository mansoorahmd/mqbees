with upstream_python_model as (

    select * from {{ ref('tanzil_quran_text') }}

)
SELECT *
FROM upstream_python_model