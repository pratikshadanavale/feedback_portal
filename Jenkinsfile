pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/.venv/Scripts/activate"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/pratikshadanavale/feedback_portal.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '.venv\\Scripts\\pytest'
            }
        }

        stage('Run Django Checks') {
            steps {
                bat '.venv\\Scripts\\python manage.py check'
            }
        }

        stage('Echo Jira Ticket') {
            steps {
                echo '🔗 Linked Jira Ticket: SATMS-007 - OOP Enhancement for Feedback Portal'
            }
        }
    }

    post {
        success {
            echo '✅ Build and validation successful. Ready to mark ticket SATMS-007 as "To Deploy".'
        }
        failure {
            echo '❌ Build failed. Investigate before closing Jira ticket.'
        }
    }
}

