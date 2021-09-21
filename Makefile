install_dev_requirements:
	pip install -r requirements_dev.txt

install_requirements:
	pip install -r requirements.txt

formatting:
	safety check
	isort .
	black .
	flake8 .

generate_documentation:
	pdoc --html --output-dir docs --force . 

open_documentation:
	open docs/ShortestDistancePolygonToLine/index.html


run_shortest_dist_path:
	python3 main.py

docker_build:
	docker build . -t iamgauravsatija/shortest_distance_polygon_to_line

docker_run:
	docker run --name shortest_distance_polygon_to_line iamgauravsatija/shortest_distance_polygon_to_line

docker_push:
	docker push iamgauravsatija/shortest_distance_polygon_to_line
