node {
    def app

    stage ('Clone repository') {
        checkout scm
    }

    stage ('Bulid image') {
        app = docker.build ("szdezsoke2003/ping-pong_game")
    }

    stage ('Test imgage') {
        app.inside {
            sh 'echo "Test passed"'
        }
    }

    stage ('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'c265b68c-616f-4975-b293-1a58321a6ea6') {
            app.push ("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}