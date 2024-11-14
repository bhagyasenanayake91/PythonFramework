pipeline {
   // agent { docker { image 'mcr.microsoft.com/playwright/python:v1.47.0-noble' } }
   agent { dockerfile true }
   stages {
      stage('e2e-tests') {
         steps {
            // sh 'pip install -r requirements.txt'
            sh 'pytest'
         }
      }
   }
}