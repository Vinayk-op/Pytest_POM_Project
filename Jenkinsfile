pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Works only when job is configured as "Pipeline script from SCM"
                checkout scm
            }
        }

        stage('Setup Python') {
    steps {
        bat 'python -m venv venv'
        bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
        bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
    }
}

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest --alluredir=Reports/allure-results'
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'Reports/allure-results/**', fingerprint: true
            }
        }
    }
}