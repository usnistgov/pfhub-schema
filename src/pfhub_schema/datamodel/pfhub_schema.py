# Auto generated from pfhub_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-10T15:58:56
# Schema: pfhub-schema
#
# id: https://w3id.org/usnistgov/pfhub-schema
# description: Phase-field simulation and benchmark schema in LinkML.
# license: NIST

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
IANA_APP = CurieNamespace('iana_app', 'https://www.iana.org/assignments/media-types/application/')
IANA_TEXT = CurieNamespace('iana_text', 'https://www.iana.org/assignments/media-types/text/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ORCID = CurieNamespace('orcid', 'https://orcid.org/')
PFHUB = CurieNamespace('pfhub', 'https://w3id.org/usnistgov/pfhub-schema/')
QUDT = CurieNamespace('qudt', 'http://qudt.org/2.1/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = PFHUB


# Types

# Class references
class BenchmarkResultId(URIorCURIE):
    pass


class BenchmarkId(URIorCURIE):
    pass


class ContributorId(URIorCURIE):
    pass


class ImplementationId(URIorCURIE):
    pass


class FileId(URIorCURIE):
    pass


@dataclass
class BenchmarkResult(YAMLRoot):
    """
    Root and context for this Benchmark Problem solution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.BenchmarkResult
    class_class_curie: ClassVar[str] = "pfhub:BenchmarkResult"
    class_name: ClassVar[str] = "BenchmarkResult"
    class_model_uri: ClassVar[URIRef] = PFHUB.BenchmarkResult

    id: Union[str, BenchmarkResultId] = None
    name: str = None
    contributors: Optional[Union[Dict[Union[str, ContributorId], Union[dict, "Contributor"]], List[Union[dict, "Contributor"]]]] = empty_dict()
    benchmark: Optional[Union[str, BenchmarkId]] = None
    framework: Optional[str] = None
    hardware: Optional[str] = None
    implementation: Optional[Union[str, ImplementationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchmarkResultId):
            self.id = BenchmarkResultId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="contributors", slot_type=Contributor, key_name="id", keyed=True)

        if self.benchmark is not None and not isinstance(self.benchmark, BenchmarkId):
            self.benchmark = BenchmarkId(self.benchmark)

        if self.framework is not None and not isinstance(self.framework, str):
            self.framework = str(self.framework)

        if self.hardware is not None and not isinstance(self.hardware, str):
            self.hardware = str(self.hardware)

        if self.implementation is not None and not isinstance(self.implementation, ImplementationId):
            self.implementation = ImplementationId(self.implementation)

        super().__post_init__(**kwargs)


@dataclass
class Benchmark(YAMLRoot):
    """
    Information about the specific Benchmark solved.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.Benchmark
    class_class_curie: ClassVar[str] = "pfhub:Benchmark"
    class_name: ClassVar[str] = "Benchmark"
    class_model_uri: ClassVar[URIRef] = PFHUB.Benchmark

    id: Union[str, BenchmarkId] = None
    name: str = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchmarkId):
            self.id = BenchmarkId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class Contributor(YAMLRoot):
    """
    Someone who contributed to this solution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.Contributor
    class_class_curie: ClassVar[str] = "pfhub:Contributor"
    class_name: ClassVar[str] = "Contributor"
    class_model_uri: ClassVar[URIRef] = PFHUB.Contributor

    id: Union[str, ContributorId] = None
    name: str = None
    handle: Optional[Union[str, URIorCURIE]] = None
    affiliation: Optional[Union[str, List[str]]] = empty_list()
    email: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContributorId):
            self.id = ContributorId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.handle is not None and not isinstance(self.handle, URIorCURIE):
            self.handle = URIorCURIE(self.handle)

        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, str) else str(v) for v in self.affiliation]

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        super().__post_init__(**kwargs)


@dataclass
class Implementation(YAMLRoot):
    """
    Link to the authors' implementation of the benchmark problem
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.codeRepository
    class_class_curie: ClassVar[str] = "schema:codeRepository"
    class_name: ClassVar[str] = "Implementation"
    class_model_uri: ClassVar[URIRef] = PFHUB.Implementation

    id: Union[str, ImplementationId] = None
    name: str = None
    repository: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImplementationId):
            self.id = ImplementationId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.repository is not None and not isinstance(self.repository, URIorCURIE):
            self.repository = URIorCURIE(self.repository)

        super().__post_init__(**kwargs)


@dataclass
class File(YAMLRoot):
    """
    A generic electronic information container.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.MediaObject
    class_class_curie: ClassVar[str] = "schema:MediaObject"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = PFHUB.File

    id: Union[str, FileId] = None
    name: str = None
    format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileId):
            self.id = FileId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=PFHUB.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=PFHUB.name, domain=None, range=str)

slots.affiliation = Slot(uri=PFHUB.affiliation, name="affiliation", curie=PFHUB.curie('affiliation'),
                   model_uri=PFHUB.affiliation, domain=None, range=Optional[Union[str, List[str]]])

slots.benchmark = Slot(uri=PFHUB.benchmark, name="benchmark", curie=PFHUB.curie('benchmark'),
                   model_uri=PFHUB.benchmark, domain=None, range=Optional[Union[str, BenchmarkId]])

slots.contributors = Slot(uri=SCHEMA.contributor, name="contributors", curie=SCHEMA.curie('contributor'),
                   model_uri=PFHUB.contributors, domain=None, range=Optional[Union[Dict[Union[str, ContributorId], Union[dict, Contributor]], List[Union[dict, Contributor]]]])

slots.date = Slot(uri=SCHEMA.datePublished, name="date", curie=SCHEMA.curie('datePublished'),
                   model_uri=PFHUB.date, domain=None, range=Optional[Union[str, XSDDate]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=PFHUB.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.format = Slot(uri=SCHEMA.encodingFormat, name="format", curie=SCHEMA.curie('encodingFormat'),
                   model_uri=PFHUB.format, domain=None, range=Optional[str])

slots.framework = Slot(uri=SCHEMA.SoftwareApplication, name="framework", curie=SCHEMA.curie('SoftwareApplication'),
                   model_uri=PFHUB.framework, domain=None, range=Optional[str])

slots.handle = Slot(uri=SCHEMA.identifier, name="handle", curie=SCHEMA.curie('identifier'),
                   model_uri=PFHUB.handle, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.hardware = Slot(uri=PFHUB.hardware, name="hardware", curie=PFHUB.curie('hardware'),
                   model_uri=PFHUB.hardware, domain=None, range=Optional[str])

slots.implementation = Slot(uri=PFHUB.implementation, name="implementation", curie=PFHUB.curie('implementation'),
                   model_uri=PFHUB.implementation, domain=None, range=Optional[Union[str, ImplementationId]])

slots.repository = Slot(uri=PFHUB.repository, name="repository", curie=PFHUB.curie('repository'),
                   model_uri=PFHUB.repository, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.summary = Slot(uri=SCHEMA.abstract, name="summary", curie=SCHEMA.curie('abstract'),
                   model_uri=PFHUB.summary, domain=None, range=Optional[str])

slots.version = Slot(uri=PFHUB.version, name="version", curie=PFHUB.curie('version'),
                   model_uri=PFHUB.version, domain=None, range=Optional[str])