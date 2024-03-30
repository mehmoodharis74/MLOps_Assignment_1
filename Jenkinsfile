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
           // mail bcc: '', body: "<br>Project: Project Uploaded Successfully", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "Success CI: Project name", to: "mehmoodharis74@gmail.com";
        }
        failure {
            echo 'Pipeline Failed'
           // mail bcc: '', body: "<br>Project: Project Uploading Failed", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name", to: "mehmoodharis74@gmail.com";
        }
    }
}
