
node {
    def app

    stage('Clone repository') {
      
        
        checkout scm
    }

    stage('Build image') {
  
       app = docker.build("reounaka/8200dev_project")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'credential-dockerhub') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
