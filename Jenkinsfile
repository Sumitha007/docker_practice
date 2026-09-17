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
                bat 'python -m pytest'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python ATM.py'
            }
        }
    }
}