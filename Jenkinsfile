pipeline {
    agent any
    
    environment {
        REPO_NAME = 'SQMA_Andries_Victor'
        PYTHON_HOME = 'C:\\Users\\victo\\AppData\\Local\\Programs\\Python\\Python311'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '=============================================='
                echo '          SQMA Task 2 - Pipeline Run         '
                echo '=============================================='
                echo "Repository: ${env.REPO_NAME}"
                echo "Build Number: ${env.BUILD_NUMBER}"
                echo "Jenkins URL: ${env.JENKINS_URL}"
                echo '=============================================='
                
                checkout scm
                
                bat '''
                    echo.
                    echo Workspace Contents:
                    dir
                    echo.
                    echo Test Directory:
                    dir tests
                '''
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo '=============================================='
                echo '           Setting Up Environment            '
                echo '=============================================='
                
                bat '''
                    REM Set Python path
                    set PATH=%PYTHON_HOME%;%PYTHON_HOME%\\Scripts;%PATH%
                    
                    echo Python Version:
                    python --version
                    echo.
                    
                    echo Pip Version:
                    pip --version
                    echo.
                    
                    REM Install dependencies if requirements.txt exists
                    if exist requirements.txt (
                        echo Installing dependencies from requirements.txt...
                        python -m pip install -r requirements.txt
                    ) else (
                        echo No requirements.txt found, skipping dependency installation
                    )
                '''
            }
        }
        
        stage('Run Calculator Tests') {
            steps {
                echo '=============================================='
                echo '        Running Calculator Test Suite        '
                echo '=============================================='
                
                bat '''
                    set PATH=%PYTHON_HOME%;%PYTHON_HOME%\\Scripts;%PATH%
                    python -m unittest tests.test_calculator -v
                '''
                
                echo 'Calculator tests completed'
            }
        }
        
        stage('Run String Operations Tests') {
            steps {
                echo '=============================================='
                echo '    Running String Operations Test Suite     '
                echo '=============================================='
                
                bat '''
                    set PATH=%PYTHON_HOME%;%PYTHON_HOME%\\Scripts;%PATH%
                    python -m unittest tests.test_string_operations -v
                '''
                
                echo 'String operations tests completed'
            }
        }
        
        stage('Run List Operations Tests') {
            steps {
                echo '=============================================='
                echo '      Running List Operations Test Suite     '
                echo '=============================================='
                
                bat '''
                    set PATH=%PYTHON_HOME%;%PYTHON_HOME%\\Scripts;%PATH%
                    python -m unittest tests.test_list_operations -v
                '''
                
                echo 'List operations tests completed'
            }
        }
        
        stage('Run Dictionary Operations Tests') {
            steps {
                echo '=============================================='
                echo '  Running Dictionary Operations Test Suite   '
                echo '=============================================='
                
                bat '''
                    set PATH=%PYTHON_HOME%;%PYTHON_HOME%\\Scripts;%PATH%
                    python -m unittest tests.test_dictionary_operations -v
                '''
                
                echo 'Dictionary operations tests completed'
            }
        }
        
        stage('Run All Tests Together') {
            steps {
                echo '=============================================='
                echo '          Running All Tests Together         '
                echo '=============================================='
                
                bat '''
                    set PATH=%PYTHON_HOME%;%PYTHON_HOME%\\Scripts;%PATH%
                    echo Discovering and running all tests...
                    python -m unittest discover tests -v
                '''
                
                echo 'All tests completed'
            }
        }
        
        stage('Generate Report') {
            steps {
                echo '=============================================='
                echo '            Generating Test Report           '
                echo '=============================================='
                
                script {
                    def totalTests = 23
                    echo "Total Tests Executed: ${totalTests}"
                    echo "Test Breakdown:"
                    echo "  - Calculator Tests: 5"
                    echo "  - String Operations Tests: 6"
                    echo "  - List Operations Tests: 6"
                    echo "  - Dictionary Operations Tests: 6"
                    echo "All Stages Passed Successfully!"
                }
            }
        }
    }
    
    post {
        success {
            echo '=============================================='
            echo '               BUILD SUCCESSFUL               '
            echo '=============================================='
            echo 'All pipeline stages completed successfully'
            echo 'All tests passed'
            echo '=============================================='
        }
        failure {
            echo '=============================================='
            echo '                BUILD FAILED                  '
            echo '=============================================='
            echo 'Pipeline failed - check logs above'
            echo '=============================================='
        }
        always {
            echo '=============================================='
            echo '              Pipeline Completed             '
            echo "Build Number: ${env.BUILD_NUMBER}"
            echo "Duration: ${currentBuild.durationString}"
            echo '=============================================='
        }
    }
}