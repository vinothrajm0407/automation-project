pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/vinothrajm0407/automation-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"%PYTHON_PATH%\" -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "\"%PYTHON_PATH%\" -m pytest --html=report.html --self-contained-html"
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Automation Test Report'
            ])
        }
    }
}
