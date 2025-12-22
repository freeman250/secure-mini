#!/bin/bash
set -e

IMAGE_NAME="secureme-mini"
IMAGE_TAG="latest"

echo "Building Docker image ${IMAGE_NAME}:${IMAGE_TAG} from repo root..."
docker build -f infrastructure/Dockerfile -t ${IMAGE_NAME}:${IMAGE_TAG} .

echo "Build done ✅"
docker images | head
