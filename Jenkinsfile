pipeline {
    agent any 
    environment {
    DOCKERHUB_CREDENTIALS = credentials('reounaka-dockerhub')
    }
    stages { 
        stage('SCM Checkout') {
            steps {  
                git 'https://github.com/Reounaka/8200Dev_Project.git'
            }
        }

        stage('Build docker image') {
            steps {  
                sh 'docker build -t ylmt/flaskapp:$BUILD_NUMBER .'
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh 'docker push reounaka/8200dev_project:$BUILD_NUMBER'
            }
        }
}
post {
        always {
            sh 'docker logout'
        }
    }
}
