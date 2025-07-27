# Makefile

MY_VIRTUALENV_DIR := my_virtualenv
PYTHON := $(MY_VIRTUALENV_DIR)/bin/python
PIP := $(MY_VIRTUALENV_DIR)/bin/pip

# Create virtual environment using virtualenv
my_virtualenv:
	virtualenv $(MY_VIRTUALENV_DIR)
	make install

# # Activate virtualenv (prints instructions)
# activate:
# 	@echo "Run: 'source $(MY_VIRTUALENV_DIR)/bin/activate'"

# # Deactivate virtualenv (prints instructions)
# deactivate:
# 	@echo "Run: 'deactivate'"

# Install dependencies (you can expand requirements.txt later)
install: my_virtualenv
	$(PIP) install --upgrade pip
	$(PIP) install pyyaml

# Run main script
run:
	$(PYTHON) main.py

# Run tests
test:
	$(PYTHON) -m unittest test_rules_engine.py

# Clean up
clean:
	rm -rf $(MY_VIRTUALENV_DIR) __pycache__ *.pyc
