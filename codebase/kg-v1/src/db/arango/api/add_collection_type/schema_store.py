'''
This file contains the schema body corresponding to each quantity type.
Every attribute must fetch its type of schema from here
'''
schema_store = {

    "atomic": {
        "type": "object",
        "properties": {
            "symbolic": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "object",
                        "properties": {
                            "str": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "str"
                        ]
                    }
                },
                "required": [
                    "value"
                ]
            }
        },
        "required": [
            "symbolic"
        ]
    },

    "symbolic": {
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

    "numeric": {
            "type": "object",
            "properties": {
              "numeric": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "unit"
                ]
              }
            },
            "required": [
              "numeric"
            ]
          },

    "timeseries": {
            "type": "object",
            "properties": {
              "timeseries": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "timeseriesNumericValue": {
                    "type": "number"
                  }
                },
                "required": [
                  "type",
                  "unit",
                  "timeseriesNumericValue"
                ]
              }
            },
            "required": [
              "timeseries"
            ]
          }
}