# Use an official Python runtime as a parent image
FROM python:3.11-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT=8000

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update -y && apt-get install -y \
    libpq-dev \
    python3-distutils \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /code/

# Collect static files
RUN python manage.py collectstatic

# Expose port
EXPOSE 8000

# Start server using gunicorn
CMD ["gunicorn", "--bind", ":8000", "winstonsarchive_rev.wsgi:application"]
# CMD ["python", "manage.py", "runserver"]