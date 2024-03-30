pipeline {
    environment {
        registry = "mehmoodharis74/MLOps_Assignment_1:final"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    
    agent any
    
    stages {
        stage('Cloning our Git') {
            steps {
                git 'https://github.com/mehmoodharis74/MLOps_Assignment_1.git'
            }
        }
        
        stage('Building our image') {
            steps {
                script {
                    dockerImage = docker.build(registry + ":$BUILD_NUMBER")
                }
            }
        }
        
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        
        stage('Cleaning up') {
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
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
