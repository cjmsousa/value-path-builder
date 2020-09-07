##################################################################################################################
# Release stage
##################################################################################################################
FROM python:3.8 AS release  

#Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copy source code
COPY src/ /app/

#Start the app
CMD ["python", "/app/app.py"] 

##################################################################################################################
# Development stage
##################################################################################################################
FROM python:3.8 AS development

#Copy the content of the relase image
COPY --from=release / /

#Copy tests
COPY tests/unit_tests/ /tests/unit_tests/
COPY tests/integration_tests/ /tests/integration_tests/
COPY tests/endtoend_tests/ /tests/endtoend_tests/

#Install requirements
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

#Start the app
CMD ["python", "/app/app.py"]