@echo off

REM List of services
set services=patient-service appointment-service notification-service

REM Docker Hub username
set dockerUsername=thellmike

for %%s in (%services%) do (
    echo Building Docker image for %%s...
    docker build -t %%s:latest ".\..\%%s"

    echo Tagging Docker image for %%s...
    docker tag %%s:latest %dockerUsername%/%%s:latest

    echo Pushing Docker image for %%s...
    docker push %dockerUsername%/%%s:latest

    echo %%s Docker image build and push completed!
)

echo All Docker images have been built and pushed successfully.
pause
