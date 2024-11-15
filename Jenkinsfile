pipeline {
   // agent { docker { image 'mcr.microsoft.com/playwright/python:v1.48.0-focal' } }
   agent { dockerfile true }
   stages {
      stage('e2e-tests') {
         steps {
            // sh 'pip install -r requirements.txt'
            sh 'pip install playwright'
            sh 'playwright install --with-deps'
            sh 'pytest'
         }
      }
   }
}