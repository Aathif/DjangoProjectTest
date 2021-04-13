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
                ls
                . myenv/bin/activate
                pip install requirements.txt
                python manage.py migrate
                python manage.py runserver &"""
                echo "Build Scuccessful"
                
            }
        }
    }
}
