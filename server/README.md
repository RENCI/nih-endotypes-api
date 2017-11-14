# Swagger Enabled Flask Server

## Local Development

###  <a name="localenv"></a>Local Environment

From the top level of the repository:

```
$ cd server/
$ virtualenv -p /usr/local/bin/python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

**ini/connexion.ini**

Set up the `ini/connexion.ini` file to match your environment. An example file named `ini/connexion.ini.example` has been provided as a template.

```
$ cp ini/connexion.ini.example ini/connexion.ini
```

- Change `/PATH_TO/` to be the actual path to the code.
- If using the docker based database update the `FQDN_OR_IP` to be that of the platform docker is being run from.

	```config
	[connexion]
	server =
	debug = True
	port = 5000
	keyfile =
	certfile =
	
	[sys-path]
	exposures = /PATH_TO/nih-endotypes-api/server/endotypes
	controllers = /PATH_TO/nih-endotypes-api/server/controllers

	```

To run the server, please execute the following:

```
python3 app.py
```

and open your browser to here:

```
http://localhost:5000/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:5000/v1/swagger.json
```

## Docker Development

**TODO**

## Production Deployment

**TODO**
