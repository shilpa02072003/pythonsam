pipeline {
    agent any

    stages {
        stage('python') {
            steps {
                sh 'mhello.py'
            }
        }
    }
}
