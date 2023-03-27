## Add your own custom Makefile targets here
EXAMPLES = examples/BenchmarkResult-001.yaml examples/BenchmarkResult-001.json \
           examples/BenchmarkResult-002.yaml examples/BenchmarkResult-002.json

examples/%.yaml: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C BenchmarkResult $< -o $@
examples/%.json: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C BenchmarkResult $< -o $@

validate: $(EXAMPLES)
	$(RUN) linkml-validate -s $(SOURCE_SCHEMA_PATH) --target-class BenchmarkResult examples/BenchmarkResult-001.yaml
	$(RUN) linkml-validate -s $(SOURCE_SCHEMA_PATH) --target-class BenchmarkResult examples/BenchmarkResult-002.yaml
