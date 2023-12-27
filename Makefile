all: install_req

install_req:
	pip install -r requirements.txt

run:
	python3 src/index.py

clean:
	rm -rf gh_repos/
