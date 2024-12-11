#!/bin/bash

# List of services
services=("patient-service" "appointment-service" "notification-service")

# Docker Hub username
docker_username="thellmike"

# Loop through each service
for service in "${services[@]}"; do
  echo "Building Docker image for $service..."
  docker build -t "$service:latest" ./$service

  echo "Tagging Docker image for $service..."
  docker tag "$service:latest" "$docker_username/$service:latest"

  echo "Pushing Docker image for $service..."
  docker push "$docker_username/$service:latest"

  echo "$service Docker image build and push completed!"
done

echo "All Docker images have been built and pushed successfully."
