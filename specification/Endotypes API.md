## NIH Endotypes API

As defined using [OpenAPI 2.0 Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md)

**WORK IN PROGRESS**

[/endotypes]():

- INPUT: in body

```
@description - list of CMAQ exposures
@body

{
	date_of_birth
	​race
	​sex
	visit: [
		​​{
			​time
			zip
			visit_type: [ "INPATIENT" | "OUTPATIENT" | "EMERGENCY" ]
			icd_code
			exposure: [
				​​value
				units
				​​​exposure_type
				time_window
			​]
		}
	...
	]
}
```


- OUTPUT: 
 
``` 
@return
	- {JSON array of objects}

[ 
  ​{
    ​endotype_id          : "E0"
    entotype_description : "..."
    periods : [
      ​{ start_time ... end_time },
      { start_time ... end_time },
      ...
    ]
  }
  ...
]
```