FROM mcr.microsoft.com/devcontainers/python:3.11

# NVIDIA CUDA támogatás (csak ha GPU-t használsz)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Torch telepítése GPU támogatással (aktuális verzió + CUDA 12.x)
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt