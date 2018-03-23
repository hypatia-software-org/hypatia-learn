clean:
	autopep8 -raai hypatia_learn/
	autopep8 -raai resources/
	autopep8 -raai config/
	isort --recursive --atomic --force-adds --apply --quiet hypatia_learn/
	isort --recursive --atomic --force-adds --apply --quiet resources/
	isort --recursive --atomic --force-adds --apply --quiet config/

