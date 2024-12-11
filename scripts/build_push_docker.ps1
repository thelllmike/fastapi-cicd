# List of services
$services = @("patient-service", "appointment-service", "notification-service")

# Docker Hub username
$dockerUsername = "thellmike"

# Loop through each service
foreach ($service in $services) {
    Write-Host "Building Docker image for $service..."
    docker build -t "$service:latest" ".\$service"

    Write-Host "Tagging Docker image for $service..."
    docker tag "$service:latest" "$dockerUsername/$service:latest"

    Write-Host "Pushing Docker image for $service..."
    docker push "$dockerUsername/$service:latest"

    Write-Host "$service Docker image build and push completed!"
}

Write-Host "All Docker images have been built and pushed successfully."
