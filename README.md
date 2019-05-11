A)Building Dockerfile:
 
From a terminal, after verifying that docker is running,(note the space before "." at end of this command) type:
  docker build -t class4-homework .


B)Running Image:

After dockerfile is built, run it by (without "." at the end of command)typing:
  docker run class4-homework

Dockerfile will run and execute the csv_reader for home.data file.

Continuous Integration: Is a practice that encourages developers to intergrate their work into a common repository several times a day.This allows for any problems for example in coding, to be detected early and corrected before the project has gone to far ahead. This reduces time going back on a project looking for errors.CI is automated, when code is checked-in it automatically builds it and informs the team member wether it was successful or not.
We can use CI when doing a project as a team, ie when different people are writing code parts for a project.


