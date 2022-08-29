pipeline {
    agent any 
    // {
    //     docker {
    //         image "aresgowar/aresdockercrawl:1.0"
    //     }
        
    // }

    stages {
        stage('Build') {
            steps {
                withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/') {
                    sh label: '', script: 'docker build -t aresgowar:dockercrawl:2.0 .'
                    sh label: '', script: 'docker push aresgowar:dockercrawl:2.0'
                }
            }
        }
        stage('Build') {
            steps {
                sh """
                    python --version
                    python crawl.py
                """
            }
        }
    }
}
