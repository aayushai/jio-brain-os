
#### Enrich API


BrainEnrich Process (Java) will make a call to Enrich API to get required attributes and entity values.

1. Enrich Process == Brain Process
2. Enrich API by Knowledge Graph

#### Enrich Process Config 

This is handled at BrainOS level hence not in the scope of enrich API code. 

```json
{
  "input_topic": "/jio/aicoe/brainos/retail/user_product_txn",
  "output_topic": "/jio/aicoe/brainos/retail/user_product_enrich_txn",
  "attribute_enrich_config": {
    "/entity/common/person": [
      "location",
      "segment"
    ],
    "/entity/retail/product": [
      "price",
      "discount"
    ]
  },
  "predicate_enrich_config": {
    "/entity/common/person": [
      "study_at",
      "works_at"
    ],
    "/entity/retail/product": [
      "brand"
    ]
  }
}
```

#### Enrich API Request
```json
{
  "attribute": [
    {
      "type": "agriculture_crop",
      "entity_ids": [
        "agriculture_crop/20000064"
      ],
      "attributes": [
        "type",
        "variety"
      ]
    },
    {
      "type": "agriculture_cropseason",
      "entity_ids": [
        "agriculture_cropseason/20000045"
      ],
      "attributes": [
        "season"
      ]
    }
  ],
  "predicate": [
    {
      "type": "agriculture_cropseason",
      "entity_ids": [
        "agriculture_cropseason/20000045"
      ],
      "predicates": [
        "agriculture_cropseason_has_agriculture_cropseasonstage"
      ]
    }
  ]
}
```
#### Enrich API Response
```json
status {
  is_ok: true
  brain_status_instance {
  parameters {
  key: "msg"
  value: "no error"
}
}
}
enrich_attribute_response {
entity_id_attribute {
key: "agriculture_crop"
value {
attribute_value {
key: "agriculture_crop/20000064"
value {
attribute_value {
key: "type"
value {
atomic {
symbolic {
value {
str: "onion"
}
}
}
}
}
attribute_value {
key: "variety"
value {
atomic {
symbolic {
value {
str: "Medium Duration"
}
}
}
}
}
}
}
}
}
entity_id_attribute {
key: "agriculture_cropseason"
value {
attribute_value {
key: "agriculture_cropseason/20000045"
value {
attribute_value {
key: "season"
value {
atomic {
symbolic {
value {
str: "Foundation Pruning"
}
}
}
}
}
}
}
}
}
}
enrich_predicate_response {
subject_predicate {
key: "agriculture_cropseason"
value {
entity_id_predicate {
key: "agriculture_cropseason/20000045"
value {
predicate_value {
key: "agriculture_cropseason_has_agriculture_cropseasonstage"
value {
entity {
entity_type: "agriculture_cropseasonstage"
biz_id {
type: "/bizid/agriculture_cropseasonstage/cropseasonstage_id"
value: "1234567"
}
name {
key: "english"
value {
canonical: "Bud Differentiation"
aliases {
element {
key: ""
value: true
}
}
}
}
attributes {
key: "stage"
value {
atomic {
symbolic {
value {
str: "Bud Differentiation"
}
}
}
}
}
}
}
}
}
}
}
}
}
```