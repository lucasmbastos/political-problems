.PHONY: clean

clean:
	find src/ -name "__pycache__" -type d -exec rm -r "{}" \;
	find src/ -name "*.pyc" -type f -exec rm "{}" \;
