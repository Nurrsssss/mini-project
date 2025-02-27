# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Run Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sales_trading_app.wsgi:application"]
