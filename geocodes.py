import json
import urllib2
import sys
from flask import Flask, request


''' Initialize flask app '''
app = Flask(__name__)

''' Information for using the HERE maps API '''
hereAppID = "vMH4VH5NId6d7nsjJ2XG"
hereAppCode = "lwkqrQqcBGAil5yV2Ls16w"
hereGeocodingURL = "https://geocoder.api.here.com/6.2/geocode.json?app_id=%s&app_code=%s&searchtext=" % \
                       (hereAppID, hereAppCode)


def serialize(input_dictionary):
    """
        Returns a json structure without escaping non-ASCII charaters. For more info see:
        https://docs.python.org/2/library/json.html
    """
    return json.dumps(input_dictionary, ensure_ascii=False, indent=4, separators=(',', ': ')).encode('utf8')


# Add a basic endpoint to test connection
@app.route('/geocodes/v1/', methods=["GET"])
def basicFunction():
    if request.method == "GET":
        return json.dumps({"status": "Connected",
                           "message": "Successfully connected to geocodes"})


# Add the geocode endpoint
@app.route('/geocodes/v1/<string:location_string>', methods=["GET"])
def geocodesFunction(location_string):
    if request.method == "GET":
        ''' Try finding the lat,lng coordinates with HERE maps '''
        request_url = hereGeocodingURL + location_string
        heremaps_response = urllib2.urlopen(request_url)
        results = json.load(heremaps_response)

        ''' If the location was found by HERE maps '''
        if len(results["Response"]["View"]) > 0:
            ''' Get the location name as found by HERE maps '''
            corrected_location_string = location_string + "(" + results["Response"]\
                                             ["View"][0]["Result"][0]["Location"]["Address"]["Label"] + ")"
            lat = results["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Latitude"]
            lng = results["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Longitude"]
            return serialize({"location_name": corrected_location_string,
                               "status": "Result Found",
                               "latitude": lat,
                               "longitude": lng}) , 200
        else:
            return serialize({"location_name": location_string,
                              "status": "Not Found",
                              "Message": location_string + " was not found by HERE maps"}) , 200


if __name__ == "__main__":

    if len(sys.argv) < 2:
        ''' Prompt for proper usage, obtaining host name and port number '''
        print ("\nUsage: " + sys.argv[0] + " host_name port_number\n")
    else:
        app.run(host=sys.argv[1], port=int(sys.argv[2]))