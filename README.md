# PFHub Schema

Phase-field simulation and benchmark schema in LinkML.

## Website

[https://pages.nist.gov/pfhub-schema](https://pages.nist.gov/pfhub-schema)

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

## Credits

This project was made with the
[LinkML cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
