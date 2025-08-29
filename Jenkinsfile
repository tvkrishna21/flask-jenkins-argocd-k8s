pipeline {
    
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        
        stage('Checkout'){
           steps {
                git credentialsId: '0819c8c8-4583-4950-bfa5-a23ae01ff226', 
                url: 'https://github.com/tvkrishna21/flask-jenkins-argocd-k8s',
                branch: 'main'
           }
        }
        
        stage('echo'){
            steps {
                script{
                    sh '''
                    echo 'Build number'
                    echo $IMAGE_TAG
                    ls -ltr
                    '''
                }
            }
        }
    }
}
