import urllib2
import json
import string


def testBasicConnection():
    response = urllib2.urlopen("http://localhost:5000/geocodes/v1/")
    results  = json.load(response)
    return True if results["status"] == "Connected" else False

def testGeoCoding(input_string):
    response = urllib2.urlopen("http://localhost:5000/geocodes/v1/"+input_string)
    results = json.load(response)
    if  results["status"] == "Result Found":
        return results["location_name"] , True
    else:
        return input_string, False


if __name__ == "__main__":
    print ("\nConnection Test Passed!" if testBasicConnection() else "\nConnection Test Failed!")
    print

    locations = ["Maputo", "Tokyo", "Rio de Janeiro", "Washington D.C.", "Malmo", "Qatar", "xyz"]
    locations = [string.replace(location, " ", "+") for location in locations]

    n_passed_tests = 0
    for location in locations:
        location_name, success = testGeoCoding(location)
        print (location_name + (" was successfully found "  if success else " was not found"))
        if success: n_passed_tests += 1

    print(str(n_passed_tests) + " tests passed\n" + str(len(locations) - n_passed_tests) + " tests failed")
    print