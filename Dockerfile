FROM continuumio/miniconda3

# Set the working directory inside the container
WORKDIR /app

# Copy the environment file
COPY environment.yml .

# Create the conda environment
RUN conda env create -f environment.yml

# Copy the rest of the code
COPY . .

# Activate environment and run script
SHELL ["conda", "run", "-n", "qwen", "/bin/bash", "-c"]
