pipeline {
    agent any

    stages {
        stage('SCM') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[ url: 'https://github.com/Grokr-gyanendra/House_api.git']])
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('house')
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def workspaceUnixPath = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    bat "docker run -v ${workspaceUnixPath}:${workspaceUnixPath} -w ${workspaceUnixPath} house python index.py"
                }
            }
        }
        stage('Session Timeout') {
            steps {
                timeout(time: 10, unit: 'SECONDS') {
                    script {
                        echo "Session created. Timing out after 10 seconds..."
                        sleep(time: 10, unit: 'SECONDS')
                    }
                }
            }
        }
    }
}