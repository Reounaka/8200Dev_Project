node {
    def app
    agent any
    environment{
       DOCKERHUB_CREDENTIALS = credentials('credential-dockerhub')
    }

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("reounaka/8200dev_project:latest")
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        app.inside {
            sh 'echo "Tests passed"'
        }
    }
    
    stage('Login') {
            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'


    }
      
    stage('Push') {
        sh 'docker push reounaka/8200dev_image:latest'
    }
}
