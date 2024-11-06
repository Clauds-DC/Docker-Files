FROM python:3

# Change DIR -> code/ folder
WORKDIR /code

# Check python and pip version
RUN python --version
RUN pip --version

# Copy all code from local, to inside of image, could be one by one or zipped
COPY ./requirements.txt /code/requirements.txt

# For now,  copy all 
COPY . .

# Check if copied inside docker image to be created
RUN ls -la

# install dependencies
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 8000
# Run app via uvcorn, and no port assigned - default 8000
CMD ["uvicorn", "api_app:app", "--host", "0.0.0.0"]
