from src.part2_common_query_caching import client

content = """<?xml version="1.0" encoding="UTF-8" ?>
<schema name="test" version="1.5">
<fields>
   <field name="_yz_id" type="_yz_str" indexed="true" stored="true"
    multiValued="false" required="true" />
   <field name="_yz_ed" type="_yz_str" indexed="true" stored="true"
    multiValued="false" />
   <field name="_yz_pn" type="_yz_str" indexed="true" stored="true"
    multiValued="false" />
   <field name="_yz_fpn" type="_yz_str" indexed="true" stored="true"
    multiValued="false" />
   <field name="_yz_vtag" type="_yz_str" indexed="true" stored="true"
    multiValued="false" />
   <field name="_yz_rk" type="_yz_str" indexed="true" stored="true"
    multiValued="false" />
   <field name="_yz_rb" type="_yz_str" indexed="true" stored="true"
    multiValued="false" />
   <field name="_yz_rt" type="_yz_str" indexed="true" stored="true"
    multiValued="false" />
   <field name="_yz_err" type="_yz_str" indexed="true"
    multiValued="false" />
</fields>
<uniqueKey>_yz_id</uniqueKey>
<types>
    <fieldType name="_yz_str" class="solr.StrField"
     sortMissingLast="true" />
</types>
</schema>"""
schema_name = 'jalapeno'
client.create_search_schema(schema_name, content)

client.get_search_schema('jalapeno')

