FROM python:3.10.8-slim

# Update repository cache & install libpq + gnu c compiler
RUN apt-get update
RUN apt-get -y install libpq-dev gcc 

# Copy project files over to directory
RUN mkdir -p /api/app
COPY ./app /api/app
COPY ./requirements.txt /api/requirements.txt

# Set workdir to newly copies files
WORKDIR /api

# Install dependencies
RUN python -m pip install -r requirements.txt

# Expose port
EXPOSE 8000

CMD ["uvicorn", "app.main:app"]
