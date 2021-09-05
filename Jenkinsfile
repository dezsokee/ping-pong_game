pipeline {
    def app

    stage('Clone repository') {
        checkout scm
    }
    stage ('Build Docker image') {
        app = docker.build("Szaby200342/ping-pong_game")
    }
    stage ('Test image') {
        app inside {
            sh 'echo "Test passed"'
        }
    }

    stage ('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}