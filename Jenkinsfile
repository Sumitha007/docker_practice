pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t atm-app .'
            }
        }

        stage('Remove Old Container') {
            steps {
                bat 'docker rm -f atm-app-container 2>nul || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --name atm-app-container atm-app'
            }
        }
    }
}