# Base image
FROM python:3.11-slim
#Set a working directory for the container
WORKDIR /app
#Copy all files from the current directory to app directory of the container
COPY . /app
# Install system dependencies required
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
#install python dependencies
RUN pip install --no-cache-dir -r requirements.txt
#Run python scripts sequentially
CMD ["bash", "-c", "python extract_rawdata.py && python load_refine_data.py"]