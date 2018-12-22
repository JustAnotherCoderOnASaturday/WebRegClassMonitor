# WebRegClassMonitor

Couldn't get into a class that you badly needed?
Don't want to waste an entire quarter taking GE'S?
Frustrated that emailing the Advisors won't help solve your problem?

Well Heres a program that will monitor the website and message you if there is an update.
  or do all the scraping work for you so you can build your email/message/call system.

--=== Requirements ===--
Selenium, 
BeautifulSoup4, 
time
--===     XXXXX    ===--

The program I created was build such that you would 
  first enter the department (ex. COMPSCI, I&C SCI, PSYCH)
  Then the Course ID (ex. 36110)
  Then the wait time per check (ex. 360 aka will wait 360 seconds before the next check)
  
The program will constantly check the website every X seconds on whether
  the specified course is open. If the course is not open, it will pause before 
  checking again. If the course is finally open, the program will message through
  the console that the course is available.
  
  
  
This program was developed with Object Orient Programming so it can be flexible and further developed
  to directly email/call/message, rather than just print in the console.  
  
  ---==== Excruciating Details =====---
  Implemented in Course.py, is the class courseTitle(dept, courseID, waitTime=60).
    in which it stores those 3 instances provided in the parameter
 
 There are 3 Functions that are used:
  def checkCourseAvailability(self):
      This function will take the raw html and check using BeautifulSoup's parsing ability
      whether or not the course ID is "OPEN", or available to enroll in.
      
      It does so by iterating through the School Website's Terribly Designed HTML
      table (<tr>). By iterating through it, the function will check whether or not the
      <tr> tag contains the course ID and then it will check whether the course is open or not.
      
      return True if Course is Open else False
  
  def pauseTime(self):
      This function will put the program to sleep for the given amount of time
      This feature was included because the purpose of this program would be used to constantly 
        check whether the course is available, such that the course would have its own wait time propery.
      The user will be able to determine how often they want the Monitor program to update.
      
      program.sleep(int time)
      
  def _getRawHtml(self):
      The problem with the WebReg's Website is that they require the users to submit a "fillout" form
        before being able to check whether the course is open or not. Unfortunately, the program
        will not be able to retrieve the proper page source code as a result.
        The only way the program is able to check is to first manually select the department and
        then select "Display Web Results".
        
      As a solution, this function utilizes the Selenium library to both Open the Website, 
        select the Department, and then to subtmit the form.
        
      Having completed the steps, the program will finally be able to retrieve the proper page source code.
      
      return raw html SourceCode

