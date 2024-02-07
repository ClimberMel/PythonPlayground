

import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read().decode("utf-8")  # Read and decode the response bytes
    courses = json.loads(data) 
    courselist = []         #course data list
    ct = ()                 #course tuple
    
    # Parse the JSON string
    for course in courses:
        #print(course["fullName"])
        if course["enabled"] == True:
            ct = (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
            courselist.append(ct)
    print(courselist)

def retrieve_course(course_name: str):
    stats = {}
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"
    my_request = urllib.request.urlopen(url)
    data = my_request.read().decode("utf-8")  # Read and decode the response bytes
    singlecourse = json.loads(data)
    #print(singlecourse)
    weeks = len(singlecourse)

    #print(singlecourse["students"])
    stList = []
    for week in singlecourse:
        stList.append[singlecourse["students"]]
        print(week)
    #print("students: ", max(stList))







#retrieve_all()

retrieve_course("docker2019")
