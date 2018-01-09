# RESTful-Geocodes
A RESTful geocoding API implemented in Python. When prompted with a location name this API returns the latitude and 
longitude coordinates of the location in a serialized json structure.

## Python Dependencies To Run The Service
- [Flask (A Python web development microframework)](http://flask.pocoo.org/) 
- [json (For serializing data)](https://docs.python.org/2/library/json.html)

## Usage
### Running The Service
After the necessary dependencies have been installed, the service can be run from the commandline. 
The main program `geocodes.py` takes two arguments `host_name` and `port_number`.
The service can be run as follows:

`$ python geocodes.py [host_name] [port_number]`

The arguments are important when attempting to access the service API later.
As an example try running the service as follows:

`$ python geocodes.py 0.0.0.0 5000`

This will run the geocodes service on the localhost at port 5000.

### Using The Service
Once the service is up and running, there are several modes to query the geocodes.
An example with using [curl](https://curl.haxx.se/) in the terminal and programmatically
in Python are presented here.

#### with curl in the Terminal
Given the host name and port number used above, the following command attempts to get
the geocodes of a location.

`curl -X GET -i http://0.0.0.0:5000/geocodes/v1/{location_name}`

Here, `{location_name}` is a place holder to be replaced with the actual name of
the location of interest

#### with urllib2 and json in Python

`urllib2` is part of the python standard library and can be used to open URL's.
As the response from this API is serialized in the JSON format, the `json` library
is used to interpret the results of the API call. The following snippet demonstrates
how to obtain the latitude and longitude information of `Boston MA`


```python
import urllib2, json
response = urllib2.urlopen("http://0.0.0.0:5000/geocodes/v1/Boston+MA")
results = json.load(response)
if  results["status"] == "Result Found":
    print (results["location_name"] + " is at latitude: " + str(results["latitude"])
     + ", longitude " + str(results["longitude"]))
else:
    print (results["location_name"] + " was not found")

```

The `urllib2` library is used to access the API endpoint `/geocodes/v1/` the parameter
`Boston+MA` indicates the location of interest.

### Expected Behavior
On successfully connecting to the geocoding endpoint, a serialized 
`json` object is returned. The `status` key demonstrates whether or not
the queried location was successfully found. The string `Result Found` means
that the location was successfully found and the latitude and longitude information is available.
On the contrary, the string `Not Found` depicts that
the location queried was not found.

Upon success i.e. `status: Result Found`, the keys `latitude` and `longitude` map to the
latitude and longitude information of the location respectively. In addition,
the `location_name` key maps to a verbose version of the original query string.
Precisely, it outputs the original query string and additionally, the name of the
location's name that the geo-coordinates corresponds to. This is relevant when the 
original search string is, possibly, a mispelled location.

