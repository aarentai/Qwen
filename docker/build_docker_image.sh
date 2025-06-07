conda activate qwen
cd /mnt/efs/hcdai/projects/Qwen
conda env export --no-builds > environment.yml
# create a Dockerfile
docker build -t qwen .
# Save the Docker image to a tar file
docker save -o qwen.tar qwen
# Or Push the Docker image to Docker Hub
# Make sure you have logged in to Docker Hub using `docker login`
docker login
# Tag the Docker image
# Replace 'aarentai' with your Docker Hub username
# and 'qwen' with the name of your Docker image
# If you want to push the image with a specific tag, replace 'latest' with your desired tag
docker tag qwen:latest aarentai/qwen:latest
# Push the Docker image to Docker Hub
docker push aarentai/qwen:latest