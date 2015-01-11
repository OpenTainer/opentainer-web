.PHONY: docs
docs:
	cd docs && make html

.PHONY: run
run:
	./manage.py runserver

.PHONY: clean
clean:
	find . -name "*.pyc" -type f -delete
