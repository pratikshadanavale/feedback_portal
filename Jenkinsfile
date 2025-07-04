pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
        PYTHON = 'python'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git credentialsId: 'github-creds-pratiksha', url: 'https://github.com/pratikshadanavale/feedback_portal.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "${tool 'Python3.12'}\\python.exe -m venv %VENV_DIR%"
                bat "%VENV_DIR%\\Scripts\\pip install -r requirements.txt"
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat "%VENV_DIR%\\Scripts\\python manage.py test"
            }
        }

        stage('Run Django Checks') {
            steps {
                bat "%VENV_DIR%\\Scripts\\python manage.py check"
            }
        }

        stage('Echo Jira Ticket') {
            steps {
                echo '🔗 Linked Jira Ticket: SATMS-007 - OOP Enhancement for Feedback Portal'
            }
        }
    }
        stage('Simulate Deployment') {
            steps {
                bat 'run_gunicorn.bat'
                echo '🚀 Deployment simulated using Gunicorn.'
            }
        }

        stage('Deploy Application') {
            steps {
                echo '🚀 Simulating deployment using run_gunicorn.bat'
                bat 'run_gunicorn.bat'
        }
    }
    post {
        success {
            echo '✅ Build & simulated deployment successful. Ticket SATMS-009 ready for production.'
        }
        failure {
            echo '❌ Build or deployment failed. Investigate before closing Jira ticket.'
        }
    }
}

