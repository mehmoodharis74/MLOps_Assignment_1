pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t mehmoodharis74/MLOps_Assignment_1 .'

                    // Log in to Docker Hub
                    sh 'docker login -u mehmoodharis74 -p dockerhub098'

                    // Push Docker image to Docker Hub
                    sh 'docker push mehmoodharis74/MLOps_Assignment_1'
                }
            }
        }
    }

    post {
        success {
            echo "Automated testing successful. Docker image built and pushed to Docker Hub."
        }
        failure {
            echo "Automated testing failed. No Docker image pushed to Docker Hub."
        }
    }
}
