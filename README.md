# PFHub Schema

Phase-field simulation and benchmark schema in LinkML.

## Website

[pages.nist.gov/pfhub-schema](pfhub-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [pfhub_schema](src/pfhub_schema)
    * [schema](src/pfhub_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/pfhub_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

Use the `make` command to generate project artefacts:

* `make all` to make everything
* `make deploy` to deploy the website

### Examples of Use

Some examples of LinkML in use are available from their
[documentation][linkml-in-use].

### Linter

You can check that the [`pfhub_schema.yaml`][pfhub-schema-yaml]
conforms to the LinkML specification using the `linkml-lint` tool:

``` shell
linkml-lint src/pfhub_schema/schema/pfhub_schema.yaml
```

which is what happens when you

``` shell
make lint
```

### Validator

You can check that the example
[`BenchmarkResult-001.yaml`][pfhub-benchmark-result] conforms to the
PFHub schema using the `linkml-validate` tool:

``` shell
linkml-validate -s src/pfhub_schema/schema/pfhub_schema.yaml examples/BenchmarkResult-001.yaml
```

## Credits

This project was made with the [LinkML cookiecutter][linkml-cruft].
It is maintained by

- Trevor Keller ([@tkphd]), NIST

<!-- authors -->
[@tkphd]: https://github.com/tkphd

<!-- files -->
[pfhub-schema-yaml]: src/pfhub-yaml/schema/pfhub-schema.yaml
[pfhub-benchmark-result]: examples/BenchmarkResult-001.yaml

<!-- links -->
[linkml-in-use]: https://linkml.io/linkml/examples.html
[linkml-cruft]: https://github.com/linkml/linkml-project-cookiecutter
[pfhub-schema]: https://pages.nist.gov/pfhub-schema
