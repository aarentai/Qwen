conda activate qwen
conda env export --no-builds > environment.yml
cd /mnt/efs/hcdai/projects/Qwen
# create a Dockerfile
docker build -t superfresh-retriever .
# Save the Docker image to a tar file
docker save -o superfresh-retriever.tar superfresh-retriever