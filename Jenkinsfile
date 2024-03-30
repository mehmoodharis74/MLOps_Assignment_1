pipeline {
agent any
tools {
maven 'maven'
}
stages{
stage('checkout'){
steps{
checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/mehmoodharis74/MLOps_Assignment_1.git']]])
sh "mvn clean install"
}
}
stage('Build Docker'){
steps{
script{
sh 'docker build -t mehmoodharis74/MLOps_Assignment_1 .'
}
}
}
stage('Push Docker Image'){
steps{
script{
withCredentials([string(credentialsId: 'mehmoodharis74')]) {
sh ‘docker login -u mehmoodharis74 -p dockerhub098’
sh ‘docker push mehmoodharis74/MLOps_Assignment_1’
}
}
}
}
}
}
