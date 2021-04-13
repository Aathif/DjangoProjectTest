pipeline {
    agent any

    stages {
        stage('Source') {
            steps {
                echo 'Cloning git repo'
                git branch: 'main', poll: false, url: 'https://github.com/Aathif/DjangoProjectTest'
            }
        }
        stage('Build') {
            steps {
                echo 'Starting build Process'
                sh """virtualenv -p python3 myenv
                && ls
                && source myenv/bin/activate"""
                sh 'pip install requirements.txt'
                sh 'python manage.py migrate'
                sh 'python manage.py runserver &'
                echo "Build Scuccessful"
                
            }
        }
    }
}
