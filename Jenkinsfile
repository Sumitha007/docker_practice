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
                bat '"C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" ATM.py'
            }
        }
    }
}