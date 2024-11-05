# Use a Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script to the container
COPY qr_code_generator.py /app/qr_code_generator.py

# Install required Python packages
RUN pip install qrcode[pil]

# Set environment variables (optional default values)
ENV QR_DATA_URL="https://github.com/ErcihanK" \
    QR_CODE_DIR="/app" \
    QR_CODE_FILENAME="github_qr.png"

# Run the Python script when the container starts
CMD ["python", "/app/qr_code_generator.py"]
