pipeline {

    agent any
	
    environment {
    DOCKERHUB_CREDENTIALS = credentials('reounaka-dockerhub')
    EMAIL = "reounaka@gmail.com"
    }

    stages { 
        stage('SCM Checkout') {
            steps {  
                  git branch: 'main', url: 'https://github.com/Reounaka/8200Dev_Project.git'      
            }
        }
        stage('Build Image') {
            steps { 
		sh 'echo Starting Image Build'  
                sh 'docker build -t reounaka/8200dev_project:latest .'
            }
        }
        stage('Dockerhub Login') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push Image') {
            steps{
                sh'''
		   docker push reounaka/8200dev_project:latest
		   scp -i Key-amazon.pem /var/lib/jenkins/workspace/$JOB_NAME/docker-compose.yml ec2-user@test:/home/ec2-user
		   scp -i Key-amazon.pem /var/lib/jenkins/workspace/$JOB_NAME/.env ec2-user@test:/home/ec2-user
		  '''
            }
        }

        stage('Echo Test') {
            agent {
                    label 'Test'
                    }
            steps{
                    git branch: 'main', url: 'https://github.com/Reounaka/8200Dev_Project.git'
                    sh ''' 
                    #!/bin/bash
                    docker-compose up -d --build
               
                    sleep 200
                    webserv="http://localhost:5000/" 
                    keyword="Attendance"
                    if curl -s "$webserv" | grep "$keyword"
                    then
                    # if the keyword is in the website
                    echo "SUCCESS - Website is up."
                    else
                    echo "FAILURE - Website is down."
                    fi
                    '''
                }
            post {
                always {
                    sh ''' echo "Cleaning Workspace" && docker-compose down && docker system prune -af'''
                }
                failure{
                    mail to: "reounaka@gmail.com",
                    subject: "jenkins build:${currentBuild.currentResult}: ${env.JOB_NAME}",
                    body: "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nMore Info can be found here at the changelog: ${env.BUILD_URL}"
                }
             } 
        }
        stage('Continue to Deployment?') {
            agent none
            steps{ 
                input ( message: "Should we continue to deployment?", ok:  "Yes, we Should. ")
            }
        }
        stage('Deployment') {
            agent {
                    label 'Deploy'
                    } 
            steps{ 
                git branch: 'main', url: 'https://github.com/Reounaka/8200Dev_Project.git'
                sh '''
                docker-compose up -d --build
                '''
            
            }
        }
    }      
    post {
            always {
                sh 'docker logout'
                }
        }
}
