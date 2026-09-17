pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t atm-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --name atm-container atm-app'
            }
        }
    }
}