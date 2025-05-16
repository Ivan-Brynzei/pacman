.PHONY: test lint ci

test:
	pytest --html=reports/test_report.html --self-contained-html

lint:
	flake8 . --format=html --htmldir=reports/lint_report

ci: test lint
