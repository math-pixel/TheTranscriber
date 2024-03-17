# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install needed dependencies
RUN apt-get update && apt-get install -y \
    libmagic-dev \
    youtube-dl \
    ffmpeg \ 
    libpulse-mainloop-glib0 \ 
    libxcb-xinerama0

RUN pip install --no-cache-dir youtube-dl
RUN pip install --no-cache-dir -r requirements.txt

# Set the QT_QPA_PLATFORM environment variable to xcb
ENV QT_QPA_PLATFORM=xcb
ENV QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms

# Make port 80 available to the world outside this container
EXPOSE 80


# Run app.py when the container launches
CMD ["python", "main.py"]
