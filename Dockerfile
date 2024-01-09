FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy script to the container
COPY config.py .
COPY cfunctions.py .
COPY mongodb.py .
COPY app.py .
COPY loopimg.py .
COPY loopchat.py .

# Install Flask
RUN pip install flask
RUN pip install flask-cors
RUN pip install openai
RUN pip install pymongo
#RUN pip install gunicorn

# Set default command to execute the script
CMD ["python", "./app.py"]
#CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
