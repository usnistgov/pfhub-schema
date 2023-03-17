# Auto generated from pfhub_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-17T17:09:04
# Schema: pfhub_schema
#
# id: https://w3id.org/usnistgov/pfhub-schema
# description: Schema for Phase-field Simulation and Benchmark Results schema in LinkML.
# license: https://www.nist.gov/open/license

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
version = "0.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
SRAO = CurieNamespace('SRAO', 'http://www.fairsharing.org/ontology/subject/SRAO_')
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
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = PFHUB


# Types

# Class references
class BenchmarkResultId(URIorCURIE):
    pass


class BenchmarkProblemId(URIorCURIE):
    pass


class ContributorId(URIorCURIE):
    pass


class FileName(extended_str):
    pass


class CsvFileName(FileName):
    pass


class DataFileName(FileName):
    pass


class VisualizationFileName(FileName):
    pass


class SoftwareUrl(URIorCURIE):
    pass


class SourceCodeUrl(URIorCURIE):
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
    benchmark: Optional[Union[dict, "BenchmarkProblem"]] = None
    contributors: Optional[Union[Dict[Union[str, ContributorId], Union[dict, "Contributor"]], List[Union[dict, "Contributor"]]]] = empty_dict()
    date_created: Optional[Union[str, XSDDate]] = None
    framework: Optional[Union[Dict[Union[str, SoftwareUrl], Union[dict, "Software"]], List[Union[dict, "Software"]]]] = empty_dict()
    implementation: Optional[Union[dict, "SourceCode"]] = None
    results: Optional[Union[dict, "Results"]] = None
    summary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchmarkResultId):
            self.id = BenchmarkResultId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.benchmark is not None and not isinstance(self.benchmark, BenchmarkProblem):
            self.benchmark = BenchmarkProblem(**as_dict(self.benchmark))

        self._normalize_inlined_as_list(slot_name="contributors", slot_type=Contributor, key_name="id", keyed=True)

        if self.date_created is not None and not isinstance(self.date_created, XSDDate):
            self.date_created = XSDDate(self.date_created)

        self._normalize_inlined_as_list(slot_name="framework", slot_type=Software, key_name="url", keyed=True)

        if self.implementation is not None and not isinstance(self.implementation, SourceCode):
            self.implementation = SourceCode(**as_dict(self.implementation))

        if self.results is not None and not isinstance(self.results, Results):
            self.results = Results(**as_dict(self.results))

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        super().__post_init__(**kwargs)


@dataclass
class BenchmarkProblem(YAMLRoot):
    """
    Information about the specific Benchmark solved.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.BenchmarkProblem
    class_class_curie: ClassVar[str] = "pfhub:BenchmarkProblem"
    class_name: ClassVar[str] = "BenchmarkProblem"
    class_model_uri: ClassVar[URIRef] = PFHUB.BenchmarkProblem

    id: Union[str, BenchmarkProblemId] = None
    name: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchmarkProblemId):
            self.id = BenchmarkProblemId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

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

    architecture: Optional[str] = None
    cores: Optional[int] = None
    nodes: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.architecture is not None and not isinstance(self.architecture, str):
            self.architecture = str(self.architecture)

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

    name: Union[str, FileName] = None
    format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FileName):
            self.name = FileName(self.name)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass
class CsvFile(File):
    """
    Comma-separated values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.CsvFile
    class_class_curie: ClassVar[str] = "pfhub:CsvFile"
    class_name: ClassVar[str] = "CsvFile"
    class_model_uri: ClassVar[URIRef] = PFHUB.CsvFile

    name: Union[str, CsvFileName] = None
    columns: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CsvFileName):
            self.name = CsvFileName(self.name)

        if not isinstance(self.columns, list):
            self.columns = [self.columns] if self.columns is not None else []
        self.columns = [v if isinstance(v, str) else str(v) for v in self.columns]

        super().__post_init__(**kwargs)


@dataclass
class DataFile(File):
    """
    Raw data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.DataFile
    class_class_curie: ClassVar[str] = "pfhub:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = PFHUB.DataFile

    name: Union[str, DataFileName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DataFileName):
            self.name = DataFileName(self.name)

        super().__post_init__(**kwargs)


@dataclass
class VisualizationFile(File):
    """
    Visualization data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.VisualizationFile
    class_class_curie: ClassVar[str] = "pfhub:VisualizationFile"
    class_name: ClassVar[str] = "VisualizationFile"
    class_model_uri: ClassVar[URIRef] = PFHUB.VisualizationFile

    name: Union[str, VisualizationFileName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, VisualizationFileName):
            self.name = VisualizationFileName(self.name)

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

    csv_data: Optional[Union[Dict[Union[str, CsvFileName], Union[dict, CsvFile]], List[Union[dict, CsvFile]]]] = empty_dict()
    raw_data: Optional[Union[Dict[Union[str, DataFileName], Union[dict, DataFile]], List[Union[dict, DataFile]]]] = empty_dict()
    viz_data: Optional[Union[Dict[Union[str, VisualizationFileName], Union[dict, VisualizationFile]], List[Union[dict, VisualizationFile]]]] = empty_dict()
    hardware: Optional[Union[Union[dict, ComputeResource], List[Union[dict, ComputeResource]]]] = empty_list()
    memory_in_kb: Optional[int] = None
    time_in_s: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="csv_data", slot_type=CsvFile, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="raw_data", slot_type=DataFile, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="viz_data", slot_type=VisualizationFile, key_name="name", keyed=True)

        if not isinstance(self.hardware, list):
            self.hardware = [self.hardware] if self.hardware is not None else []
        self.hardware = [v if isinstance(v, ComputeResource) else ComputeResource(**as_dict(v)) for v in self.hardware]

        if self.memory_in_kb is not None and not isinstance(self.memory_in_kb, int):
            self.memory_in_kb = int(self.memory_in_kb)

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

    url: Union[str, SoftwareUrl] = None
    name: Optional[str] = None
    download: Optional[Union[str, URIorCURIE]] = None
    repository: Optional[Union[str, URIorCURIE]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, SoftwareUrl):
            self.url = SoftwareUrl(self.url)

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

    url: Union[str, SourceCodeUrl] = None
    name: Optional[str] = None
    repository: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, SourceCodeUrl):
            self.url = SourceCodeUrl(self.url)

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

slots.architecture = Slot(uri=SRAO['0000258'], name="architecture", curie=SRAO.curie('0000258'),
                   model_uri=PFHUB.architecture, domain=None, range=Optional[str])

slots.columns = Slot(uri=PFHUB.columns, name="columns", curie=PFHUB.curie('columns'),
                   model_uri=PFHUB.columns, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^\S+'))

slots.cores = Slot(uri=NCIT.C64194, name="cores", curie=NCIT.curie('C64194'),
                   model_uri=PFHUB.cores, domain=None, range=Optional[int])

slots.date_created = Slot(uri=SCHEMA.dateCreated, name="date_created", curie=SCHEMA.curie('dateCreated'),
                   model_uri=PFHUB.date_created, domain=None, range=Optional[Union[str, XSDDate]])

slots.download = Slot(uri=SCHEMA.downloadUrl, name="download", curie=SCHEMA.curie('downloadUrl'),
                   model_uri=PFHUB.download, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=PFHUB.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.format = Slot(uri=SCHEMA.encodingFormat, name="format", curie=SCHEMA.curie('encodingFormat'),
                   model_uri=PFHUB.format, domain=None, range=Optional[str])

slots.handle = Slot(uri=SCHEMA.member, name="handle", curie=SCHEMA.curie('member'),
                   model_uri=PFHUB.handle, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.memory_in_kb = Slot(uri=PFHUB.memory_in_kb, name="memory_in_kb", curie=PFHUB.curie('memory_in_kb'),
                   model_uri=PFHUB.memory_in_kb, domain=None, range=Optional[int])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=PFHUB.name, domain=None, range=Optional[str])

slots.nodes = Slot(uri=NCIT.C18132, name="nodes", curie=NCIT.curie('C18132'),
                   model_uri=PFHUB.nodes, domain=None, range=Optional[int])

slots.repository = Slot(uri=SCHEMA.codeRepository, name="repository", curie=SCHEMA.curie('codeRepository'),
                   model_uri=PFHUB.repository, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.summary = Slot(uri=SCHEMA.abstract, name="summary", curie=SCHEMA.curie('abstract'),
                   model_uri=PFHUB.summary, domain=None, range=Optional[str])

slots.version = Slot(uri=SCHEMA.softwareVersion, name="version", curie=SCHEMA.curie('softwareVersion'),
                   model_uri=PFHUB.version, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\d+\.]+'))

slots.time_in_s = Slot(uri=SCHEMA.Number, name="time_in_s", curie=SCHEMA.curie('Number'),
                   model_uri=PFHUB.time_in_s, domain=None, range=Optional[int])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=PFHUB.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.benchmark = Slot(uri=PFHUB.benchmark, name="benchmark", curie=PFHUB.curie('benchmark'),
                   model_uri=PFHUB.benchmark, domain=None, range=Optional[Union[dict, BenchmarkProblem]])

slots.contributors = Slot(uri=SCHEMA.contributor, name="contributors", curie=SCHEMA.curie('contributor'),
                   model_uri=PFHUB.contributors, domain=None, range=Optional[Union[Dict[Union[str, ContributorId], Union[dict, Contributor]], List[Union[dict, Contributor]]]])

slots.framework = Slot(uri=SCHEMA.SoftwareApplication, name="framework", curie=SCHEMA.curie('SoftwareApplication'),
                   model_uri=PFHUB.framework, domain=None, range=Optional[Union[Dict[Union[str, SoftwareUrl], Union[dict, Software]], List[Union[dict, Software]]]])

slots.hardware = Slot(uri=PFHUB.hardware, name="hardware", curie=PFHUB.curie('hardware'),
                   model_uri=PFHUB.hardware, domain=None, range=Optional[Union[Union[dict, ComputeResource], List[Union[dict, ComputeResource]]]])

slots.implementation = Slot(uri=PFHUB.implementation, name="implementation", curie=PFHUB.curie('implementation'),
                   model_uri=PFHUB.implementation, domain=None, range=Optional[Union[dict, SourceCode]])

slots.results = Slot(uri=PFHUB.results, name="results", curie=PFHUB.curie('results'),
                   model_uri=PFHUB.results, domain=None, range=Optional[Union[dict, Results]])

slots.csv_data = Slot(uri=PFHUB.csv_data, name="csv_data", curie=PFHUB.curie('csv_data'),
                   model_uri=PFHUB.csv_data, domain=None, range=Optional[Union[Dict[Union[str, CsvFileName], Union[dict, CsvFile]], List[Union[dict, CsvFile]]]])

slots.raw_data = Slot(uri=PFHUB.raw_data, name="raw_data", curie=PFHUB.curie('raw_data'),
                   model_uri=PFHUB.raw_data, domain=None, range=Optional[Union[Dict[Union[str, DataFileName], Union[dict, DataFile]], List[Union[dict, DataFile]]]])

slots.viz_data = Slot(uri=PFHUB.viz_data, name="viz_data", curie=PFHUB.curie('viz_data'),
                   model_uri=PFHUB.viz_data, domain=None, range=Optional[Union[Dict[Union[str, VisualizationFileName], Union[dict, VisualizationFile]], List[Union[dict, VisualizationFile]]]])

slots.File_name = Slot(uri=SCHEMA.name, name="File_name", curie=SCHEMA.curie('name'),
                   model_uri=PFHUB.File_name, domain=File, range=Union[str, FileName])

slots.Software_url = Slot(uri=SCHEMA.url, name="Software_url", curie=SCHEMA.curie('url'),
                   model_uri=PFHUB.Software_url, domain=Software, range=Union[str, SoftwareUrl])

slots.SourceCode_url = Slot(uri=SCHEMA.url, name="SourceCode_url", curie=SCHEMA.curie('url'),
                   model_uri=PFHUB.SourceCode_url, domain=SourceCode, range=Union[str, SourceCodeUrl])