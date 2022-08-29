pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch 'main', url: 'https://github.com/aresgowar/python-crawl-data.git'
            }
        }
        // stage('Docker') {
        //     steps {
        //         withDockerRegistry(credentialsId: 'docker-hub', url: ' https://index.docker.io/v1/') {
        //         }
        //     }
        // }
    }
}
