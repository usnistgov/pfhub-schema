# Auto generated from pfhub_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-14T18:54:33
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
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BITBUCKET = CurieNamespace('bitbucket', 'https://bitbucket.org/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
GITHUB = CurieNamespace('github', 'https://github.com/')
GITLAB = CurieNamespace('gitlab', 'https://gitlab.com/')
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


class FileId(URIorCURIE):
    pass


class SoftwareId(URIorCURIE):
    pass


class SourceCodeId(URIorCURIE):
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
    name: Optional[str] = None
    contributors: Optional[Union[Dict[Union[str, ContributorId], Union[dict, "Contributor"]], List[Union[dict, "Contributor"]]]] = empty_dict()
    benchmark: Optional[Union[str, BenchmarkId]] = None
    framework: Optional[Union[Dict[Union[str, SoftwareId], Union[dict, "Software"]], List[Union[dict, "Software"]]]] = empty_dict()
    implementation: Optional[Union[str, SourceCodeId]] = None
    results: Optional[Union[dict, "Results"]] = None
    summary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchmarkResultId):
            self.id = BenchmarkResultId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="contributors", slot_type=Contributor, key_name="id", keyed=True)

        if self.benchmark is not None and not isinstance(self.benchmark, BenchmarkId):
            self.benchmark = BenchmarkId(self.benchmark)

        self._normalize_inlined_as_list(slot_name="framework", slot_type=Software, key_name="id", keyed=True)

        if self.implementation is not None and not isinstance(self.implementation, SourceCodeId):
            self.implementation = SourceCodeId(self.implementation)

        if self.results is not None and not isinstance(self.results, Results):
            self.results = Results(**as_dict(self.results))

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

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
    name: Optional[str] = None
    number: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchmarkId):
            self.id = BenchmarkId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.number is not None and not isinstance(self.number, str):
            self.number = str(self.number)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class ComputeResource(YAMLRoot):
    """
    Summary of the hardware used to execute the simulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.softwareRequirements
    class_class_curie: ClassVar[str] = "schema:softwareRequirements"
    class_name: ClassVar[str] = "ComputeResource"
    class_model_uri: ClassVar[URIRef] = PFHUB.ComputeResource

    architecture: Optional[Union[Union[dict, "ComputeResource"], List[Union[dict, "ComputeResource"]]]] = empty_list()
    cores: Optional[int] = None
    nodes: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.architecture, list):
            self.architecture = [self.architecture] if self.architecture is not None else []
        self.architecture = [v if isinstance(v, ComputeResource) else ComputeResource(**as_dict(v)) for v in self.architecture]

        if self.cores is not None and not isinstance(self.cores, int):
            self.cores = int(self.cores)

        if self.nodes is not None and not isinstance(self.nodes, int):
            self.nodes = int(self.nodes)

        super().__post_init__(**kwargs)


@dataclass
class Contributor(YAMLRoot):
    """
    Someone who contributed to this solution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Person
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Contributor"
    class_model_uri: ClassVar[URIRef] = PFHUB.Contributor

    id: Union[str, ContributorId] = None
    name: Optional[str] = None
    handle: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    affiliation: Optional[Union[str, List[str]]] = empty_list()
    email: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContributorId):
            self.id = ContributorId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.handle, list):
            self.handle = [self.handle] if self.handle is not None else []
        self.handle = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.handle]

        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, str) else str(v) for v in self.affiliation]

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        super().__post_init__(**kwargs)


@dataclass
class File(YAMLRoot):
    """
    A generic electronic information container.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.DigitalDocument
    class_class_curie: ClassVar[str] = "schema:DigitalDocument"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = PFHUB.File

    id: Union[str, FileId] = None
    name: Optional[str] = None
    columns: Optional[Union[str, List[str]]] = empty_list()
    format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileId):
            self.id = FileId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.columns, list):
            self.columns = [self.columns] if self.columns is not None else []
        self.columns = [v if isinstance(v, str) else str(v) for v in self.columns]

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass
class Results(YAMLRoot):
    """
    Runtime information and output from a simulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Dataset
    class_class_curie: ClassVar[str] = "schema:Dataset"
    class_name: ClassVar[str] = "Results"
    class_model_uri: ClassVar[URIRef] = PFHUB.Results

    data_table: Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]] = empty_dict()
    data_raw: Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]] = empty_dict()
    data_visualization: Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]] = empty_dict()
    hardware: Optional[Union[Union[dict, ComputeResource], List[Union[dict, ComputeResource]]]] = empty_list()
    memory_in_KB: Optional[int] = None
    time_in_s: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.data_table):
            self.MissingRequiredField("data_table")
        self._normalize_inlined_as_list(slot_name="data_table", slot_type=File, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_raw", slot_type=File, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_visualization", slot_type=File, key_name="id", keyed=True)

        if not isinstance(self.hardware, list):
            self.hardware = [self.hardware] if self.hardware is not None else []
        self.hardware = [v if isinstance(v, ComputeResource) else ComputeResource(**as_dict(v)) for v in self.hardware]

        if self.memory_in_KB is not None and not isinstance(self.memory_in_KB, int):
            self.memory_in_KB = int(self.memory_in_KB)

        if self.time_in_s is not None and not isinstance(self.time_in_s, int):
            self.time_in_s = int(self.time_in_s)

        super().__post_init__(**kwargs)


@dataclass
class Software(YAMLRoot):
    """
    A software product, download, or repository.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.SoftwareApplication
    class_class_curie: ClassVar[str] = "schema:SoftwareApplication"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = PFHUB.Software

    id: Union[str, SoftwareId] = None
    name: Optional[str] = None
    download: Optional[Union[str, URIorCURIE]] = None
    repository: Optional[Union[str, URIorCURIE]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.download is not None and not isinstance(self.download, URIorCURIE):
            self.download = URIorCURIE(self.download)

        if self.repository is not None and not isinstance(self.repository, URIorCURIE):
            self.repository = URIorCURIE(self.repository)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class SourceCode(YAMLRoot):
    """
    Link to the authors' implementation of the benchmark problem.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.SoftwareSourceCode
    class_class_curie: ClassVar[str] = "schema:SoftwareSourceCode"
    class_name: ClassVar[str] = "SourceCode"
    class_model_uri: ClassVar[URIRef] = PFHUB.SourceCode

    id: Union[str, SourceCodeId] = None
    name: Optional[str] = None
    repository: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SourceCodeId):
            self.id = SourceCodeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.repository is not None and not isinstance(self.repository, URIorCURIE):
            self.repository = URIorCURIE(self.repository)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=PFHUB.id, domain=None, range=URIRef)

slots.affiliation = Slot(uri=PFHUB.affiliation, name="affiliation", curie=PFHUB.curie('affiliation'),
                   model_uri=PFHUB.affiliation, domain=None, range=Optional[Union[str, List[str]]])

slots.architecture = Slot(uri=PFHUB.architecture, name="architecture", curie=PFHUB.curie('architecture'),
                   model_uri=PFHUB.architecture, domain=None, range=Optional[Union[Union[dict, ComputeResource], List[Union[dict, ComputeResource]]]])

slots.benchmark = Slot(uri=PFHUB.benchmark, name="benchmark", curie=PFHUB.curie('benchmark'),
                   model_uri=PFHUB.benchmark, domain=None, range=Optional[Union[str, BenchmarkId]])

slots.columns = Slot(uri=PFHUB.columns, name="columns", curie=PFHUB.curie('columns'),
                   model_uri=PFHUB.columns, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^\S+'))

slots.contributors = Slot(uri=SCHEMA.contributor, name="contributors", curie=SCHEMA.curie('contributor'),
                   model_uri=PFHUB.contributors, domain=None, range=Optional[Union[Dict[Union[str, ContributorId], Union[dict, Contributor]], List[Union[dict, Contributor]]]])

slots.cores = Slot(uri=NCIT.C64194, name="cores", curie=NCIT.curie('C64194'),
                   model_uri=PFHUB.cores, domain=None, range=Optional[int])

slots.date = Slot(uri=SCHEMA.datePublished, name="date", curie=SCHEMA.curie('datePublished'),
                   model_uri=PFHUB.date, domain=None, range=Optional[Union[str, XSDDate]])

slots.download = Slot(uri=SCHEMA.downloadUrl, name="download", curie=SCHEMA.curie('downloadUrl'),
                   model_uri=PFHUB.download, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=PFHUB.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.data_raw = Slot(uri=PFHUB.data_raw, name="data_raw", curie=PFHUB.curie('data_raw'),
                   model_uri=PFHUB.data_raw, domain=None, range=Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]])

slots.data_table = Slot(uri=PFHUB.data_table, name="data_table", curie=PFHUB.curie('data_table'),
                   model_uri=PFHUB.data_table, domain=None, range=Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]])

slots.data_visualization = Slot(uri=PFHUB.data_visualization, name="data_visualization", curie=PFHUB.curie('data_visualization'),
                   model_uri=PFHUB.data_visualization, domain=None, range=Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]])

slots.format = Slot(uri=SCHEMA.encodingFormat, name="format", curie=SCHEMA.curie('encodingFormat'),
                   model_uri=PFHUB.format, domain=None, range=Optional[str])

slots.framework = Slot(uri=SCHEMA.SoftwareApplication, name="framework", curie=SCHEMA.curie('SoftwareApplication'),
                   model_uri=PFHUB.framework, domain=None, range=Optional[Union[Dict[Union[str, SoftwareId], Union[dict, Software]], List[Union[dict, Software]]]])

slots.handle = Slot(uri=SCHEMA.identifier, name="handle", curie=SCHEMA.curie('identifier'),
                   model_uri=PFHUB.handle, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.hardware = Slot(uri=PFHUB.hardware, name="hardware", curie=PFHUB.curie('hardware'),
                   model_uri=PFHUB.hardware, domain=None, range=Optional[Union[Union[dict, ComputeResource], List[Union[dict, ComputeResource]]]])

slots.implementation = Slot(uri=PFHUB.implementation, name="implementation", curie=PFHUB.curie('implementation'),
                   model_uri=PFHUB.implementation, domain=None, range=Optional[Union[str, SourceCodeId]])

slots.memory_in_KB = Slot(uri=PFHUB.memory_in_KB, name="memory_in_KB", curie=PFHUB.curie('memory_in_KB'),
                   model_uri=PFHUB.memory_in_KB, domain=None, range=Optional[int])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=PFHUB.name, domain=None, range=Optional[str])

slots.nodes = Slot(uri=NCIT.C18132, name="nodes", curie=NCIT.curie('C18132'),
                   model_uri=PFHUB.nodes, domain=None, range=Optional[int])

slots.number = Slot(uri=SCHEMA.identifier, name="number", curie=SCHEMA.curie('identifier'),
                   model_uri=PFHUB.number, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\a\d'))

slots.repository = Slot(uri=SCHEMA.codeRepository, name="repository", curie=SCHEMA.curie('codeRepository'),
                   model_uri=PFHUB.repository, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.results = Slot(uri=PFHUB.results, name="results", curie=PFHUB.curie('results'),
                   model_uri=PFHUB.results, domain=None, range=Optional[Union[dict, Results]])

slots.summary = Slot(uri=SCHEMA.abstract, name="summary", curie=SCHEMA.curie('abstract'),
                   model_uri=PFHUB.summary, domain=None, range=Optional[str])

slots.version = Slot(uri=SCHEMA.softwareVersion, name="version", curie=SCHEMA.curie('softwareVersion'),
                   model_uri=PFHUB.version, domain=None, range=Optional[str])

slots.time_in_s = Slot(uri=SCHEMA.Number, name="time_in_s", curie=SCHEMA.curie('Number'),
                   model_uri=PFHUB.time_in_s, domain=None, range=Optional[int])