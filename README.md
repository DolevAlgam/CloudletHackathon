# CloudletHackathon
Full Application Version Control

Welcome, in this repository we will save all the code for the demo.<br>
Although the benefits of saving multiple services on one repository, we are all working simultaneously - that means problems can occur.
To avoid such problems we need to follow two guidelines.
  * Communication - everyone should know what your are working on, you should ask if any one is working on something before accessing that code.
  
  * Format - there is a simple yet important format that describes the way we save and organize our code. You are welcome to criticize and offer new ways of work, but you must follow the format the team has decided on.
  
## Code Foramt

- Main Repo
    - Service Name
      - Dockerfile (That builds the images of the service)
      - "app" Directory (That will contain all the code)
        - Your Code
    - Service Name
      - Dockerfile
      - app
        - Code
        
## Service Spec
Followed below will be details about each Service.
Will talk aboout the general idea, app architecture, APIs and whatever you feel relevant.

### SecurityCamera

### Car
The Car will be made from two IOT devices phsically connected, a Car Base, Motor, Wheels, and a Car Camera.

#### CarBase

#### CarCamera

### Alarm

## APIs
Here we will document all API our services use to talk to each other.<br>
example url: http://car:8000/forward

### Car
#### CarBase
##### Simple Remote APIs
* forward - start moving forward
* backward - start moving backwards
* stop - stop the car
* right - turn right
* left - turn left
##### Scenarios APIs
* scenario1 - initialize scenario1
* scenario2/sectionA - initialize scan of sectionA
* scenario2/sectionB - initialize scan of sectionB
#### CarCamera - Jetson
* scan - initialize weapon detection -- returns string "attack" or "back"

### Alarm
* on - start alarm
* off - stop alarm
