import urllib2
import json


def testBasicConnection():
    response = urllib2.urlopen("http://localhost:5000/geocodes/v1/")
    results  = json.load(response)
    return True if results["status"] == "Connected" else False


if __name__ == "__main__":
    print ("\nConnection Test Passed!" if testBasicConnection() else "\nConnection Test Failed!")
    print