<!-- Improved compatibility of back to top link: See: https://github.com//Reounaka/8200Dev_Project/pull/73 -->
<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[https://github.com/Reounaka/8200Dev_Project]">
    <img src="https://github.com/Reounaka/8200Dev_Project/blob/main/static/group_22_010.png" alt="Logo" width="1000" height="200">
  </a>

<h3 align="center">8200dev Attendance Project</h3>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="left">
This project comes to solve the need for daily monitoring of the students’ attendance in the course. He does this by analyzing the csv files that are produced through the webex application and produces a report on the student’s attendance status.
  
  
The report execution process is:
- Downloading Excel files.
- Analysis of the files using Python.
- Producing an Excel report on the student's attendance status.
- Displaying the report using the flask application and  mysql to store the data. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![python][python.js]][python-url]
* [![flask][flask.js]][flask-url]
* [![mysql][mysql.js]][mysql-url]
* [![docker][docker.js]][docker-url]
* [![Jenkins][Jenkins.js]][Jenkins-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

  

### Prerequisites

In order to run the application without problems you will need to use docker.
  
If Docker is not installed on your computer, you can download and install it through the following link:https://www.docker.com
  
  * For mac run this command on terminal
  ```sh
brew cask install docker
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Reounaka/8200Dev_Project
   ```
2. You will need a ".env" file in order to use the app.
   
   Create a file in the project repo, Name it ".env" and fill it up according to this template. 
  
   ```env
    HOSTNAME = < Host machine IP >
    SFTP_USERNAME = < Host machine user > 
    SFTP_PASSWORD =  < Host machine password > 
    MYSQL_USER =  < User for mysql client > 
    MYSQL_PASSWORD = < Password for mysql client >
    MYSQL_DATABASE = < Database name for mysql client >
    MYSQL_ROOT_PASSWORD = < Root password for mysql client >
   ```
   *Host machine = The computer where the csv files are downloaded from.
  
3. run the application using docker
   ```sh
   docker-composer up --build
   ```
   *Make sure that the docker machine is running.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
  
  app installation video: 
  
https://user-images.githubusercontent.com/105148680/194262232-2176dcc2-c3cb-4468-9aa1-1f94d3112d86.mov

    
  app running video:

https://user-images.githubusercontent.com/105148680/194262951-fce8271a-c3be-4726-badd-738f00f65ed9.mov



<p align="right">(<a href="#readme-top">back to top</a>)</p>

  
<!-- CI/CD -->
## CI/CD
  This is a simple demo on the usage of Jenkins, Docker Build, and Container Registry (DockerHub), Git and GitHub to build a CI/CD pipeline.
  Here’s a diagram that summarizes the workflow:
  
  <div align="center">
  <a href="[https://github.com/Reounaka/8200Dev_Project]">
    <img src="https://github.com/Reounaka/8200Dev_Project/blob/main/static/Screenshot%202022-12-05%20at%2013.09.49.png" alt="Logo" width="1000" height="400">
  </a>
    
 <div align="left">
    
1.A developer pushes the source code to GitHub, which lends itself as the Version Control System.
    
2.GitHub triggers a post-commit hook to Jenkins Build.
    
3.Jenkins Build creates the container image and pushes it to DockerHub Registry.
    
4.Jenkins "Test Slave" pull the image and runs it to test the website .
    
5.After getting OK from the user, Jenkins deploy the new features to the webiste on "Production's Slave".

<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!
 1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Reouven Nakache - reounaka@gmail.com  
  
 [![linkedin][linkedin.shield]][linkedin-url]      [![github][github.shield]][github-url]
  
  
Project Link: https://github.com/Reounaka/8200Dev_Project
  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python.js]: https://img.shields.io/badge/PYTHON-000000?style=for-the-badge&logo=python&logoColor=blue
[python-url]: https://www.python.org
[flask.js]: https://img.shields.io/badge/flask-critical?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[mysql.js]: https://img.shields.io/badge/mysql-yellow?style=for-the-badge&logo=mysql&logoColor=white
[mysql-url]: https://www.mysql.com
[docker.js]: https://shields.io/badge/docker-blue?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com
[linkedin-url]: https://www.linkedin.com/in/reouven/
[linkedin.shield]:https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[github-url]: https://github.com/Reounaka/
[github.shield]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[Jenkins.js]: https://shields.io/badge/jenkins-orange?style=for-the-badge&logo=jenkins&logoColor=black
[Jenkins-url]: https://www.jenkins.io/

