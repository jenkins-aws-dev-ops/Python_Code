pipeline {
    agent { label "runner2" } 
    parameters {
        choice(name: 'Branch',
        choices:'main\nSP_1\nSP_2\n')
        text(name: 'Customers',
        defaultValue: '<Samsung>')
        string(name: 'Install location',
        defaultValue: '/usr/packages/')
    }
    stages {
        stage('Parallel jobs') {
            parallel {
                stage('Build') {
                    agent { label "runner2" }
                    steps {
                        echo "Compiling..."
                        sh 'cmake .'
                        sh 'make'
                    }
                }
                stage ('Coverage') { 
                stages {
                stage('gcov run') {
                    agent { label "runner2" }
                    steps {
                        sh 'hostname'
                        sh './runTests'
                    }
                }
                stage('genHTML report') {
                    agent { label "runner2" }
                    steps {
                        sh 'cd CMakeFiles/runTests.dir; lcov --capture --directory . --output-file coverage.info; genhtml coverage.info --output-directory out'
                        publishHTML target: [
                            allowMissing: false,
                            alwaysLinkToLastBuild: false,
                            keepAll: true,
                            reportDir: 'CMakeFiles/runTests.dir/out',
                            reportFiles: 'index.html',
                            reportName: 'RCov Report'
                        ]
                    }
                }
                }
                }
                stage('Valgrind') {
                    agent { label "runner2" }
                    steps {
                        sh 'valgrind --leak-check=yes ./runTests'
                    }
                }
                
                stage('Build HelloWorld') {
                    agent { label "runner2" }
                    steps {
                        echo "Compiling hello"
                        sh "cd hello; make all"
                    }
                }
                stage('Coverity') {
                    agent { label "runner2" }
                    steps {
                        sh 'hostname'
                        echo "Run Coverity"
                    }
                }
            }
        }
        stage('AdHoc Tests') {
            steps {
                echo "Run AdHoc"
            }
        }
        stage('Full regression') {
            parallel {
                stage('Suite 1') {
                    agent { label "runner2" }
                    steps {
                        echo "Hello ${params.all_choices}"
                        sh '/usr/bin/python3 --version'
                        sh 'hostname'
                    }
                }
                stage('Suite 2') {
                    agent { label "runner2" }
                    steps {
                        sleep 1
                        sh '/usr/bin/python3 testP.py'
                        sh 'hostname'
                    }
                }
                stage('Suite 3') {
                    steps {
                        sleep 1
                        sh '/usr/bin/python3 testP.py'
                    }
                }
            }
        }
        stage('Final QA Test') {
            steps {
                echo "QA Test ${params.branch}"
            }
        }
        stage('Package & Install Test') {
            steps {
                echo "Installation test ${params.branch}"
            }
        }
        stage('Public report') {
            steps {
                echo "Public report ${params.branch}"
                /*
                sh 'mkdir -p /var/lib/jenkins/workspace/Build/coverage'
                publishHTML target: [
                   allowMissing: false,
                    alwaysLinkToLastBuild: false,
                    keepAll: true,
                    reportDir: 'coverage',
                    reportFiles: 'index.html',
                    reportName: 'RCov Report'
                ]
                */
            }
        }
    }
post {
    success {
        echo "The Pipeline success :)"
    }
  }
}
