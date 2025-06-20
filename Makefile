#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = warhammer-damage-calc
PYTHON_VERSION = 3.12
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

.PHONY: start
start:
	$(PYTHON_INTERPRETER) -m venv .venv
	. .venv/bin/activate && $(PYTHON_INTERPRETER) -m pip install -U pip
	. .venv/bin/activate && $(PYTHON_INTERPRETER) -m pip install -r requirements.txt


.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt


.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +


.PHONY: api_run 
api_run:
	$(PYTHON_INTERPRETER) -m uvicorn src.api:app --reload
	echo "Access the API at: http://localhost:8000/docs"


.PHONY: front_run 
front_run:
	$(PYTHON_INTERPRETER) -m http.server 8080 --directory front


.PHONY: api_docker_requirements
api_docker_requirements:
	pipreqs src --force --savepath src/requirements.in
	echo "uvicorn==0.34.3" >> src/requirements.in


.PHONY: api_docker_build
api_docker_build:
	docker build -f src/Dockerfile -t $(PROJECT_NAME)-api ./src/


.PHONY: front_docker_build
front_docker_build:
	docker build -f front/Dockerfile -t $(PROJECT_NAME)-front ./front


.PHONY: api_docker_run
api_docker_run:
	docker run -d -p 8000:8000 $(PROJECT_NAME)-api
	echo "Access the API at: http://localhost:8000/docs"


.PHONY: front_docker_run
front_docker_run:
	docker run -d -p 8080:8080 $(PROJECT_NAME)-front
	echo "Access the front-end at: http://localhost:8080"


.PHONY: run_test
run_test:
	$(PYTHON_INTERPRETER) -m pytest --cov=src --cov-report=html