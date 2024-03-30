pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'mehmoodharis74/MLOps_Assignment_1'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE_NAME ."
                }
            }
        }

        stage('Login Dockerhub and Push Docker Image') {
    steps {
        script {
            sh "echo 'dockerhub098' | docker login -u 'mehmoodharis74' --password-stdin"

            sh "docker push $DOCKER_IMAGE_NAME"
        }
    }
}
    }
    
    post {
        always {
            // Clean up Docker images
            sh 'docker system prune -af'
        }
        success {
            echo 'Pipeline Success'
            mail bcc: '', 
                 body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", 
                 cc: '', 
                 charset: 'UTF-8', 
                 from: '', 
                 mimeType: 'text/html', 
                 replyTo: '', 
                 subject: "Success CI: Project name -> ${env.JOB_NAME}", 
                 to: "mehmoodharis74@gmail.com"
        }
        failure {
            echo 'Pipeline Failed'
            mail bcc: '', 
                 body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", 
                 cc: '', 
                 charset: 'UTF-8', 
                 from: '', 
                 mimeType: 'text/html', 
                 replyTo: '', 
                 subject: "ERROR CI: Project name -> ${env.JOB_NAME}", 
                 to: "mehmoodharis74@gmail.com"
        }
    }
}
