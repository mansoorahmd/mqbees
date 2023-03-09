{% macro extract_suras_meta() %}
WITH xml_data AS (
  SELECT XMLPARSE(DOCUMENT '{{ref('seeds/suras_meta.xml')}}') AS xml
),
sura_nodes AS (
  SELECT unnest(xpath('/suras/sura', xml)) AS sura_node
  FROM xml_data
),
suras_meta AS (
  SELECT
    (xpath('@index', sura_node))[1]::text AS index,
    (xpath('@ayas', sura_node))[1]::text AS ayas,
    (xpath('@start', sura_node))[1]::text AS start,
    (xpath('@name', sura_node))[1]::text AS name,
    (xpath('@tname', sura_node))[1]::text AS tname,
    (xpath('@ename', sura_node))[1]::text AS ename,
    (xpath('@type', sura_node))[1]::text AS type,
    (xpath('@order', sura_node))[1]::text AS order,
    (xpath('@rukus', sura_node))[1]::text AS rukus
  FROM sura_nodes
)
SELECT * FROM suras_meta
{% endmacro %}
