'''
This file contains the entity and predicate schemas without 
the attributes filled in, so that the attributes
can be filled based on user input
'''

entity_schema = {
  "message": "Schema Validation Failed",
  "level": "strict",
  "rule": {
    "type": "object",
    "properties": {
      "entityType": {
        "type": "string"
      },
      "bizId": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string"
            },
            "value": {
              "type": "string"
            }
          },
          "required": [
            "type",
            "value"
          ]
        }
      },
      "name": {
        "type": "object",
        "properties": {
          "language": {
            "type": "object",
            "properties": {
              "canonical": {
                "type": "string"
              },
              "aliases": {
                "type": "object",
                "properties": {
                  "element": {
                    "type": "object",
                    "properties": {
                      "alias": {
                        "type": "boolean"
                      }
                    }
                  }
                },
                "required": [
                  "element"
                ]
              }
            },
            "required": [
              "canonical",
              "aliases"
            ]
          }
        }
      },
      "attributes": {
        "type": "object",
        "properties": {
          "segment": {
            "type": "object",
            "properties": {
              "symbolic": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "value": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "unit",
                  "value"
                ]
              }
            },
            "required": [
              "symbolic"
            ]
          },
          "title": {
            "type": "object",
            "properties": {
              "symbolic": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "value": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "unit",
                  "value"
                ]
              }
            },
            "required": [
              "symbolic"
            ]
          }
        },
        "required": [
        ]
      }
    },
    "required": [
      "entityType",
      "name"
    ]
  }
}

predicate_schema = {
  "message": "Schema validation failed",
  "level": "strict",
  "rule": {
    "type": "object",
    "properties": {
      "predicateName": {
        "type": "string"
      },
      "attributes": {
        "type": "object",
        "properties": {
        },
        "required": [

        ]
      }
    },
    "required":[
      "predicateName"
    ]
  }
}
