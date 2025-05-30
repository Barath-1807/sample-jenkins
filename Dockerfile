# Use a base image with X11 support and Tkinter installed
FROM python:3.10-slim

# Install Tkinter and dependencies
RUN apt-get update && \
    apt-get install -y python3-tk x11-apps && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy your script
COPY app.py .

# Set environment to allow GUI forwarding
ENV DISPLAY=:0

# Run the script
CMD ["python", "app.py"]
