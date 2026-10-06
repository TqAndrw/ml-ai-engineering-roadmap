.PHONY: setup run clean

setup:
	bash scripts/setup.sh

run: output/error_users.txt

output/error_users.txt: data/app.log
	bash scripts/run.sh

clean:
	rm -rf output
