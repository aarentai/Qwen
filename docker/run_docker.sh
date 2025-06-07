cd /mnt/efs/hcdai/projects/Qwen
# Load the Docker image from the tar file
docker load -i qwen.tar
# If you want to pull the Docker image from Docker Hub instead of loading from a tar file, you can use:
docker pull aarentai/qwen:latest
# See available Docker images
docker images
# Run the Docker container interactively
docker run -it qwen bash
# Exit the Docker container
exit