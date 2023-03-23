## Add your own custom Makefile targets here

validate:
	$(RUN) linkml-validate -s $(SOURCE_SCHEMA_PATH) --target-class BenchmarkResult src/data/examples/BenchmarkResult-001.yaml
	$(RUN) linkml-validate -s $(SOURCE_SCHEMA_PATH) --target-class BenchmarkResult src/data/examples/moose_1a_ia.yaml
