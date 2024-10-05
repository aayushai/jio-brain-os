
query = "insert %s into '%s' \
		 LET inserted = NEW \
		 return inserted._id"
#line1: Inserting the entity into the collection
#line2: Creating a variable called inserted to store the newly created entity
#line3: Returning the entity_id of the newly created entity

'''
Sample query:
insert
{
  "entityType": "common_candidate",
  "bizId": [
    {
      "type": "industry/candidate",
      "value": "industry/candidate/SAN"
    }
  ],
  "name": [
    {
      "language": {
        "language": "English",
        "script": "Roman"
      },
      "canonical": "santosh",
      "alias": [
        "santy"
      ]
    }
  ],
  "attributes": {
    "email": {
      "symbolic": {
        "type": "candidate/email",
        "unit": "email/id",
        "value": "email/id/santosh@outlook.com"
      }
    },
    "gender": {
      "symbolic": {
        "type": "candidate/gender",
        "unit": "candidate/gender",
        "value": "candidate/gender/male"
      }
    },
    "linkedin_url": {
      "symbolic": {
        "type": "candidate/linkedin",
        "unit": "candidate/linkedin/url",
        "value": "https://in.linkedin.com/santosh"
      }
    },
    "phone_number": {
      "symbolic": {
        "type": "candidate/phonenumber",
        "unit": "candidate/phonenumber",
        "value": "9246724689"
      }
    
  }
}
}into common_candidate
'''