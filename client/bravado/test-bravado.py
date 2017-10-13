# Setup - virtualenv (Python 2 or 3)
# $ virtualenv -p /PATH/TO/PYTHON venv
# $ source venv/bin/activate
# $ pip install bravado
# $ python test-bravado.py

from bravado.client import SwaggerClient

server_swagger_url = 'https://endotypes.renci.org/v1/swagger.json'

# defaults to github_swagger, but should be changed to local_swagger if doing development work
client = SwaggerClient.from_url(
    server_swagger_url
)

endotypes_result = client.endotypes.endotypes_post(input={
  "date_of_birth": "2017-10-12",
  "model_type": "M0",
  "race": "1",
  "sex": "M",
  "visits": [
    {
      "exposure": {
        "exposure_type": "pm25",
        "units": "ugm3",
        "value": 33.3
      },
      "icd_codes": "ICD9:V12,ICD9:E002",
      "lat": "20",
      "lon": "20",
      "time": "2017-10-12T21:12:29.451Z",
      "visit_type": "INPATIENT"
    }
  ]
}).result()
print(endotypes_result)
