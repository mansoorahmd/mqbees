-- macros/my_macros.sql

{% macro hello_world(role) %}
    {{ log("Running some_macro: " ~ role ~ ", " ~ role) }}
{% endmacro %}
