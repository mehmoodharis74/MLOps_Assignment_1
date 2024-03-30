pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // // Build Docker image
                    // sh 'docker build -t mehmoodharis74/MLOps_Assignment_1 .'

                    // // Log in to Docker Hub
                    // sh 'docker login -u mehmoodharis74 -p dockerhub098'

                    // // Push Docker image to Docker Hub
                    // sh 'docker push mehmoodharis74/MLOps_Assignment_1'
                    echo 'Done'
                }
            }
        }
    }

    post {
        // always {
        //     // Clean up Docker images
        //     sh 'docker system prune -af'
        // }
        success {
            echo 'Pipeline Success'
            mail bcc: '', body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "Success CI: Project name -> ${env.JOB_NAME}", to: "mehmoodharis74@gmail.com";
        }
        failure {
            echo 'Pipeline Failed'
            mail bcc: '', body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "mehmoodharis74@gmail.com";
        }
    }
}
