# Use official Python image
FROM python:3.12.5

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "app.py"]
