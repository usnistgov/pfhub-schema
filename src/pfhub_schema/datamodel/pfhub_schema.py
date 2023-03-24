# Auto generated from pfhub_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-24T14:26:12
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
from linkml_runtime.linkml_model.types import Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = "0.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PFHUB = CurieNamespace('pfhub', 'https://w3id.org/usnistgov/pfhub-schema/')
DEFAULT_ = PFHUB


# Types

# Class references
class BenchmarkResultId(URIorCURIE):
    pass


class ContributorId(URIorCURIE):
    pass


class FileName(extended_str):
    pass


class ArchiveDataName(FileName):
    pass


class FieldDataName(FileName):
    pass


class TimeSeriesDataName(FileName):
    pass


class ImageDataName(FileName):
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
    benchmark_problem: Union[str, "ValidBenchmarkProblem"] = None
    benchmark_version: int = None
    contributors: Optional[Union[Dict[Union[str, ContributorId], Union[dict, "Contributor"]], List[Union[dict, "Contributor"]]]] = empty_dict()
    date_created: Optional[Union[str, XSDDate]] = None
    framework: Optional[Union[Dict[Union[str, SoftwareUrl], Union[dict, "Software"]], List[Union[dict, "Software"]]]] = empty_dict()
    implementation: Optional[Union[dict, "SourceCode"]] = None
    results: Optional[Union[dict, "Results"]] = None
    schema: Optional[Union[dict, "SourceCode"]] = None
    summary: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchmarkResultId):
            self.id = BenchmarkResultId(self.id)

        if self._is_empty(self.benchmark_problem):
            self.MissingRequiredField("benchmark_problem")
        if not isinstance(self.benchmark_problem, ValidBenchmarkProblem):
            self.benchmark_problem = ValidBenchmarkProblem(self.benchmark_problem)

        if self._is_empty(self.benchmark_version):
            self.MissingRequiredField("benchmark_version")
        if not isinstance(self.benchmark_version, int):
            self.benchmark_version = int(self.benchmark_version)

        self._normalize_inlined_as_list(slot_name="contributors", slot_type=Contributor, key_name="id", keyed=True)

        if self.date_created is not None and not isinstance(self.date_created, XSDDate):
            self.date_created = XSDDate(self.date_created)

        self._normalize_inlined_as_list(slot_name="framework", slot_type=Software, key_name="url", keyed=True)

        if self.implementation is not None and not isinstance(self.implementation, SourceCode):
            self.implementation = SourceCode(**as_dict(self.implementation))

        if self.results is not None and not isinstance(self.results, Results):
            self.results = Results(**as_dict(self.results))

        if self.schema is not None and not isinstance(self.schema, SourceCode):
            self.schema = SourceCode(**as_dict(self.schema))

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        super().__post_init__(**kwargs)


@dataclass
class ComputeResource(YAMLRoot):
    """
    Summary of the hardware used to execute the simulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://schema.org/softwareRequirements")
    class_class_curie: ClassVar[str] = None
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

    class_class_uri: ClassVar[URIRef] = URIRef("https://schema.org/Person")
    class_class_curie: ClassVar[str] = None
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

    class_class_uri: ClassVar[URIRef] = URIRef("https://schema.org/DigitalDocument")
    class_class_curie: ClassVar[str] = None
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
class ArchiveData(File):
    """
    Specialization of a pfhub:File containing a compressed data archive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.ArchiveData
    class_class_curie: ClassVar[str] = "pfhub:ArchiveData"
    class_name: ClassVar[str] = "ArchiveData"
    class_model_uri: ClassVar[URIRef] = PFHUB.ArchiveData

    name: Union[str, ArchiveDataName] = None
    format: Optional[Union[str, "CompressedFiles"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ArchiveDataName):
            self.name = ArchiveDataName(self.name)

        if self.format is not None and not isinstance(self.format, CompressedFiles):
            self.format = CompressedFiles(self.format)

        super().__post_init__(**kwargs)


@dataclass
class FieldData(File):
    """
    Specialization of a pfhub:File representing field variables in a simulation domain using a format appropriate for
    the application.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.FieldData
    class_class_curie: ClassVar[str] = "pfhub:FieldData"
    class_name: ClassVar[str] = "FieldData"
    class_model_uri: ClassVar[URIRef] = PFHUB.FieldData

    name: Union[str, FieldDataName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FieldDataName):
            self.name = FieldDataName(self.name)

        super().__post_init__(**kwargs)


@dataclass
class TimeSeriesData(File):
    """
    Specialization of a pfhub:File representing a time series in plain text using named columns of comma-separated
    values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://en.wikipedia.org/wiki/Comma-separated_values")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "TimeSeriesData"
    class_model_uri: ClassVar[URIRef] = PFHUB.TimeSeriesData

    name: Union[str, TimeSeriesDataName] = None
    columns: Optional[Union[str, List[str]]] = empty_list()
    format: Optional[Union[str, "TabularFiles"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, TimeSeriesDataName):
            self.name = TimeSeriesDataName(self.name)

        if not isinstance(self.columns, list):
            self.columns = [self.columns] if self.columns is not None else []
        self.columns = [v if isinstance(v, str) else str(v) for v in self.columns]

        if self.format is not None and not isinstance(self.format, TabularFiles):
            self.format = TabularFiles(self.format)

        super().__post_init__(**kwargs)


@dataclass
class ImageData(File):
    """
    Specialization of a pfhub:File for images and visualization data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PFHUB.ImageData
    class_class_curie: ClassVar[str] = "pfhub:ImageData"
    class_name: ClassVar[str] = "ImageData"
    class_model_uri: ClassVar[URIRef] = PFHUB.ImageData

    name: Union[str, ImageDataName] = None
    format: Optional[Union[str, "ImageFiles"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ImageDataName):
            self.name = ImageDataName(self.name)

        if self.format is not None and not isinstance(self.format, ImageFiles):
            self.format = ImageFiles(self.format)

        super().__post_init__(**kwargs)


@dataclass
class Results(YAMLRoot):
    """
    Runtime information and output from a simulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://schema.org/Dataset")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Results"
    class_model_uri: ClassVar[URIRef] = PFHUB.Results

    file_archive: Optional[Union[Dict[Union[str, ArchiveDataName], Union[dict, ArchiveData]], List[Union[dict, ArchiveData]]]] = empty_dict()
    file_spatial: Optional[Union[Dict[Union[str, FieldDataName], Union[dict, FieldData]], List[Union[dict, FieldData]]]] = empty_dict()
    file_timeseries: Optional[Union[Dict[Union[str, TimeSeriesDataName], Union[dict, TimeSeriesData]], List[Union[dict, TimeSeriesData]]]] = empty_dict()
    file_visual: Optional[Union[Dict[Union[str, ImageDataName], Union[dict, ImageData]], List[Union[dict, ImageData]]]] = empty_dict()
    fictive_time: Optional[float] = None
    hardware: Optional[Union[Union[dict, ComputeResource], List[Union[dict, ComputeResource]]]] = empty_list()
    memory_in_kb: Optional[int] = None
    time_in_s: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="file_archive", slot_type=ArchiveData, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="file_spatial", slot_type=FieldData, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="file_timeseries", slot_type=TimeSeriesData, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="file_visual", slot_type=ImageData, key_name="name", keyed=True)

        if self.fictive_time is not None and not isinstance(self.fictive_time, float):
            self.fictive_time = float(self.fictive_time)

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://schema.org/SoftwareApplication")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = PFHUB.Software

    url: Union[str, SoftwareUrl] = None
    name: Optional[str] = None
    commit: Optional[str] = None
    download: Optional[Union[str, URIorCURIE]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, SoftwareUrl):
            self.url = SoftwareUrl(self.url)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.commit is not None and not isinstance(self.commit, str):
            self.commit = str(self.commit)

        if self.download is not None and not isinstance(self.download, URIorCURIE):
            self.download = URIorCURIE(self.download)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class SourceCode(YAMLRoot):
    """
    Link to the authors' implementation of the benchmark problem.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://schema.org/SoftwareSourceCode")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SourceCode"
    class_model_uri: ClassVar[URIRef] = PFHUB.SourceCode

    url: Union[str, SourceCodeUrl] = None
    name: Optional[str] = None
    commit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, SourceCodeUrl):
            self.url = SourceCodeUrl(self.url)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.commit is not None and not isinstance(self.commit, str):
            self.commit = str(self.commit)

        super().__post_init__(**kwargs)


# Enumerations
class ValidBenchmarkProblem(EnumDefinitionImpl):
    """
    Known parts of the accepted PFHub Benchmark Problems.
    """
    _defn = EnumDefinition(
        name="ValidBenchmarkProblem",
        description="Known parts of the accepted PFHub Benchmark Problems.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1a",
                PermissibleValue(text="1a",
                                 description="Spinodal decomposition in a square domain with periodic boundaries.") )
        setattr(cls, "1b",
                PermissibleValue(text="1b",
                                 description="Spinodal decomposition in a square domain with no-flux boundaries.") )
        setattr(cls, "1c",
                PermissibleValue(text="1c",
                                 description="Spinodal decomposition in a T-shaped domain with no-flux boundaries.") )
        setattr(cls, "1d",
                PermissibleValue(text="1d",
                                 description="Spinodal decomposition on a closed spherical shell.") )
        setattr(cls, "2a",
                PermissibleValue(text="2a",
                                 description="Ostwald ripening in a square domain with periodic boundaries.") )
        setattr(cls, "2b",
                PermissibleValue(text="2b",
                                 description="Ostwald ripening in a square domain with no-flux boundaries.") )
        setattr(cls, "2c",
                PermissibleValue(text="2c",
                                 description="Ostwald ripening in a T-shaped domain with no-flux boundaries.") )
        setattr(cls, "2d",
                PermissibleValue(text="2d",
                                 description="Ostwald ripening on a closed spherical shell.") )
        setattr(cls, "3a",
                PermissibleValue(text="3a",
                                 description="Dendritic growth in a square domain.") )
        setattr(cls, "4a",
                PermissibleValue(text="4a",
                                 description="Elastic precipitate with radii (20 nm, 20 nm), C₁₁₁₁=250 aJ/nm³, C₁₁₂₂=150 aJ/nm³, C₁₂₁₂=100 aJ/nm³.") )
        setattr(cls, "4b",
                PermissibleValue(text="4b",
                                 description="Elastic precipitate with radii (75 nm, 75 nm), C₁₁₁₁=250 aJ/nm³, C₁₁₂₂=150 aJ/nm³, C₁₂₁₂=100 aJ/nm³.") )
        setattr(cls, "4c",
                PermissibleValue(text="4c",
                                 description="Elastic precipitate with radii (20 nm, 20 nm), C₁₁₁₁=275 aJ/nm³, C₁₁₂₂=165 aJ/nm³, C₁₂₁₂=110 aJ/nm³.") )
        setattr(cls, "4d",
                PermissibleValue(text="4d",
                                 description="Elastic precipitate with radii (75 nm, 75 nm), C₁₁₁₁=275 aJ/nm³, C₁₁₂₂=165 aJ/nm³, C₁₂₁₂=110 aJ/nm³.") )
        setattr(cls, "4e",
                PermissibleValue(text="4e",
                                 description="Elastic precipitate with radii (20/0.9 nm, 0.9*20 nm), C₁₁₁₁=250 aJ/nm³, C₁₁₂₂=150 aJ/nm³, C₁₂₁₂=100 aJ/nm³.") )
        setattr(cls, "4f",
                PermissibleValue(text="4f",
                                 description="Elastic precipitate with radii (75/0.9 nm, 0.9*75 nm), C₁₁₁₁=250 aJ/nm³, C₁₁₂₂=150 aJ/nm³, C₁₂₁₂=100 aJ/nm³.") )
        setattr(cls, "4g",
                PermissibleValue(text="4g",
                                 description="Elastic precipitate with radii (20/0.9 nm, 0.9*20 nm), C₁₁₁₁=275 aJ/nm³, C₁₁₂₂=165 aJ/nm³, C₁₂₁₂=110 aJ/nm³.") )
        setattr(cls, "4h",
                PermissibleValue(text="4h",
                                 description="Elastic precipitate with radii (75/0.9 nm, 0.9*75 nm), C₁₁₁₁=275 aJ/nm³, C₁₁₂₂=165 aJ/nm³, C₁₂₁₂=110 aJ/nm³.") )
        setattr(cls, "5a",
                PermissibleValue(text="5a",
                                 description="Stokes flow in an un-obstructed channel.") )
        setattr(cls, "5b",
                PermissibleValue(text="5b",
                                 description="Stokes flow in a channel with elliptical obstruction.") )
        setattr(cls, "6a",
                PermissibleValue(text="6a",
                                 description="Electrostatics in a square domain.") )
        setattr(cls, "6b",
                PermissibleValue(text="6b",
                                 description="Electrostatics in a domain comprised of a rectangle and half-circle.") )
        setattr(cls, "7a",
                PermissibleValue(text="7a",
                                 description="Method of Manufactured Solutions: order of accuracy test.") )
        setattr(cls, "7b",
                PermissibleValue(text="7b",
                                 description="Method of Manufactured Solutions: performance with fixed error.") )
        setattr(cls, "7c",
                PermissibleValue(text="7c",
                                 description="Method of Manufactured Solutions: increased rate of change.") )
        setattr(cls, "8a",
                PermissibleValue(text="8a",
                                 description="Homogeneous nucleation with a single initial seed.") )
        setattr(cls, "8b",
                PermissibleValue(text="8b",
                                 description="Homogeneous nucleation with multiple initial seeds.") )
        setattr(cls, "8c",
                PermissibleValue(text="8c",
                                 description="Homogeneous nucleation with seeds at random times.") )

class ValidBenchmarkVersion(EnumDefinitionImpl):
    """
    Known versions of the accepted PFHub Benchmark Problems.
    """
    _defn = EnumDefinition(
        name="ValidBenchmarkVersion",
        description="Known versions of the accepted PFHub Benchmark Problems.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="Initial or Hackathon version.") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="Published version.") )

class CompressedFiles(EnumDefinitionImpl):
    """
    Valid compressed archive file extensions.
    """
    bz2 = PermissibleValue(text="bz2",
                             description="Bzip-2 file extension.",
                             meaning=None)
    gz = PermissibleValue(text="gz",
                           description="GZip file extension.",
                           meaning=None)
    tgz = PermissibleValue(text="tgz",
                             description="Shorthand tarball extension.",
                             meaning=None)
    zip = PermissibleValue(text="zip",
                             description="Zip file extension.",
                             meaning=None)

    _defn = EnumDefinition(
        name="CompressedFiles",
        description="Valid compressed archive file extensions.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "7z",
                PermissibleValue(text="7z",
                                 description="7zip file extension.",
                                 meaning=None) )
        setattr(cls, "tar.gz",
                PermissibleValue(text="tar.gz",
                                 description="Gzipped Tar extension.",
                                 meaning=None) )

class DataFiles(EnumDefinitionImpl):
    """
    Valid raw or transformed spatial phase-field data file extensions.
    """
    csv = PermissibleValue(text="csv",
                             description="Comma-separated values.",
                             meaning=None)
    hdf5 = PermissibleValue(text="hdf5",
                               description="Hierarchical HDF5 data.",
                               meaning=None)
    pvti = PermissibleValue(text="pvti",
                               description="Parallel VTK ImageData file.",
                               meaning=None)
    pvtr = PermissibleValue(text="pvtr",
                               description="Parallel VTK RectilinearGrid file.",
                               meaning=None)
    pvts = PermissibleValue(text="pvts",
                               description="Parallel VTK StructuredGrid file.",
                               meaning=None)
    pvtu = PermissibleValue(text="pvtu",
                               description="Parallel VTK UnstructuredGrid file.",
                               meaning=None)
    tsv = PermissibleValue(text="tsv",
                             description="Tab-delimited values.",
                             meaning=None)
    vti = PermissibleValue(text="vti",
                             description="VTK ImageData file.",
                             meaning=None)
    vtr = PermissibleValue(text="vtr",
                             description="VTK RectilinearGrid file.",
                             meaning=None)
    vts = PermissibleValue(text="vts",
                             description="VTK StructuredGrid file.",
                             meaning=None)
    vtu = PermissibleValue(text="vtu",
                             description="VTK UnstructuredGrid file.",
                             meaning=None)
    xdmf = PermissibleValue(text="xdmf",
                               description="XML summary with HDF5 data.",
                               meaning=None)

    _defn = EnumDefinition(
        name="DataFiles",
        description="Valid raw or transformed spatial phase-field data file extensions.",
    )

class ImageFiles(EnumDefinitionImpl):
    """
    Valid image and visualization file extensions.
    """
    png = PermissibleValue(text="png",
                             description="Portable Network Graphics image file format.",
                             meaning=None)
    pvti = PermissibleValue(text="pvti",
                               description="Parallel VTK ImageData file.",
                               meaning=None)
    pvtr = PermissibleValue(text="pvtr",
                               description="Parallel VTK RectilinearGrid file.",
                               meaning=None)
    pvts = PermissibleValue(text="pvts",
                               description="Parallel VTK StructuredGrid file.",
                               meaning=None)
    pvtu = PermissibleValue(text="pvtu",
                               description="Parallel VTK UnstructuredGrid file.",
                               meaning=None)
    tif = PermissibleValue(text="tif",
                             description="Tagged Image File Format file.",
                             meaning=None)
    tsv = PermissibleValue(text="tsv",
                             description="Tab-delimited values.",
                             meaning=None)
    vti = PermissibleValue(text="vti",
                             description="VTK ImageData file.",
                             meaning=None)
    vtr = PermissibleValue(text="vtr",
                             description="VTK RectilinearGrid file.",
                             meaning=None)
    vts = PermissibleValue(text="vts",
                             description="VTK StructuredGrid file.",
                             meaning=None)
    vtu = PermissibleValue(text="vtu",
                             description="VTK UnstructuredGrid file.",
                             meaning=None)

    _defn = EnumDefinition(
        name="ImageFiles",
        description="Valid image and visualization file extensions.",
    )

class TabularFiles(EnumDefinitionImpl):
    """
    Valid tabular file extensions.
    """
    csv = PermissibleValue(text="csv",
                             description="Comma-separated values.",
                             meaning=None)
    tsv = PermissibleValue(text="tsv",
                             description="Tab-delimited values.",
                             meaning=None)

    _defn = EnumDefinition(
        name="TabularFiles",
        description="Valid tabular file extensions.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri="str(uriorcurie)", name="id", curie=None,
                   model_uri=PFHUB.id, domain=None, range=URIRef)

slots.affiliation = Slot(uri=PFHUB.affiliation, name="affiliation", curie=PFHUB.curie('affiliation'),
                   model_uri=PFHUB.affiliation, domain=None, range=Optional[Union[str, List[str]]])

slots.architecture = Slot(uri="str(uriorcurie)", name="architecture", curie=None,
                   model_uri=PFHUB.architecture, domain=None, range=Optional[str])

slots.benchmark_problem = Slot(uri=PFHUB.benchmark_problem, name="benchmark_problem", curie=PFHUB.curie('benchmark_problem'),
                   model_uri=PFHUB.benchmark_problem, domain=None, range=Union[str, "ValidBenchmarkProblem"],
                   pattern=re.compile(r'^\d\a'))

slots.benchmark_version = Slot(uri=PFHUB.benchmark_version, name="benchmark_version", curie=PFHUB.curie('benchmark_version'),
                   model_uri=PFHUB.benchmark_version, domain=None, range=int)

slots.columns = Slot(uri=PFHUB.columns, name="columns", curie=PFHUB.curie('columns'),
                   model_uri=PFHUB.columns, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^\S+'))

slots.commit = Slot(uri="str(uriorcurie)", name="commit", curie=None,
                   model_uri=PFHUB.commit, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+'))

slots.cores = Slot(uri="str(uriorcurie)", name="cores", curie=None,
                   model_uri=PFHUB.cores, domain=None, range=Optional[int])

slots.date_created = Slot(uri="str(uriorcurie)", name="date_created", curie=None,
                   model_uri=PFHUB.date_created, domain=None, range=Optional[Union[str, XSDDate]])

slots.download = Slot(uri="str(uriorcurie)", name="download", curie=None,
                   model_uri=PFHUB.download, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.email = Slot(uri="str(uriorcurie)", name="email", curie=None,
                   model_uri=PFHUB.email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.fictive_time = Slot(uri="str(uriorcurie)", name="fictive_time", curie=None,
                   model_uri=PFHUB.fictive_time, domain=None, range=Optional[float])

slots.format = Slot(uri="str(uriorcurie)", name="format", curie=None,
                   model_uri=PFHUB.format, domain=None, range=Optional[str])

slots.handle = Slot(uri="str(uriorcurie)", name="handle", curie=None,
                   model_uri=PFHUB.handle, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.memory_in_kb = Slot(uri=PFHUB.memory_in_kb, name="memory_in_kb", curie=PFHUB.curie('memory_in_kb'),
                   model_uri=PFHUB.memory_in_kb, domain=None, range=Optional[int])

slots.name = Slot(uri="str(uriorcurie)", name="name", curie=None,
                   model_uri=PFHUB.name, domain=None, range=Optional[str])

slots.nodes = Slot(uri="str(uriorcurie)", name="nodes", curie=None,
                   model_uri=PFHUB.nodes, domain=None, range=Optional[int])

slots.summary = Slot(uri="str(uriorcurie)", name="summary", curie=None,
                   model_uri=PFHUB.summary, domain=None, range=Optional[str])

slots.time_in_s = Slot(uri="str(uriorcurie)", name="time_in_s", curie=None,
                   model_uri=PFHUB.time_in_s, domain=None, range=Optional[int])

slots.url = Slot(uri="str(uriorcurie)", name="url", curie=None,
                   model_uri=PFHUB.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.version = Slot(uri="str(uriorcurie)", name="version", curie=None,
                   model_uri=PFHUB.version, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\d+\.]+'))

slots.contributors = Slot(uri="str(uriorcurie)", name="contributors", curie=None,
                   model_uri=PFHUB.contributors, domain=None, range=Optional[Union[Dict[Union[str, ContributorId], Union[dict, Contributor]], List[Union[dict, Contributor]]]])

slots.file_archive = Slot(uri=PFHUB.file_archive, name="file_archive", curie=PFHUB.curie('file_archive'),
                   model_uri=PFHUB.file_archive, domain=None, range=Optional[Union[Dict[Union[str, ArchiveDataName], Union[dict, ArchiveData]], List[Union[dict, ArchiveData]]]])

slots.file_spatial = Slot(uri=PFHUB.file_spatial, name="file_spatial", curie=PFHUB.curie('file_spatial'),
                   model_uri=PFHUB.file_spatial, domain=None, range=Optional[Union[Dict[Union[str, FieldDataName], Union[dict, FieldData]], List[Union[dict, FieldData]]]])

slots.file_timeseries = Slot(uri=PFHUB.file_timeseries, name="file_timeseries", curie=PFHUB.curie('file_timeseries'),
                   model_uri=PFHUB.file_timeseries, domain=None, range=Optional[Union[Dict[Union[str, TimeSeriesDataName], Union[dict, TimeSeriesData]], List[Union[dict, TimeSeriesData]]]])

slots.file_visual = Slot(uri=PFHUB.file_visual, name="file_visual", curie=PFHUB.curie('file_visual'),
                   model_uri=PFHUB.file_visual, domain=None, range=Optional[Union[Dict[Union[str, ImageDataName], Union[dict, ImageData]], List[Union[dict, ImageData]]]])

slots.framework = Slot(uri="str(uriorcurie)", name="framework", curie=None,
                   model_uri=PFHUB.framework, domain=None, range=Optional[Union[Dict[Union[str, SoftwareUrl], Union[dict, Software]], List[Union[dict, Software]]]])

slots.hardware = Slot(uri=PFHUB.hardware, name="hardware", curie=PFHUB.curie('hardware'),
                   model_uri=PFHUB.hardware, domain=None, range=Optional[Union[Union[dict, ComputeResource], List[Union[dict, ComputeResource]]]])

slots.implementation = Slot(uri=PFHUB.implementation, name="implementation", curie=PFHUB.curie('implementation'),
                   model_uri=PFHUB.implementation, domain=None, range=Optional[Union[dict, SourceCode]])

slots.results = Slot(uri=PFHUB.results, name="results", curie=PFHUB.curie('results'),
                   model_uri=PFHUB.results, domain=None, range=Optional[Union[dict, Results]])

slots.schema = Slot(uri=PFHUB.schema, name="schema", curie=PFHUB.curie('schema'),
                   model_uri=PFHUB.schema, domain=None, range=Optional[Union[dict, SourceCode]])

slots.File_name = Slot(uri="str(uriorcurie)", name="File_name", curie=None,
                   model_uri=PFHUB.File_name, domain=File, range=Union[str, FileName])

slots.ArchiveData_format = Slot(uri="str(uriorcurie)", name="ArchiveData_format", curie=None,
                   model_uri=PFHUB.ArchiveData_format, domain=ArchiveData, range=Optional[Union[str, "CompressedFiles"]])

slots.TimeSeriesData_format = Slot(uri="str(uriorcurie)", name="TimeSeriesData_format", curie=None,
                   model_uri=PFHUB.TimeSeriesData_format, domain=TimeSeriesData, range=Optional[Union[str, "TabularFiles"]])

slots.ImageData_format = Slot(uri="str(uriorcurie)", name="ImageData_format", curie=None,
                   model_uri=PFHUB.ImageData_format, domain=ImageData, range=Optional[Union[str, "ImageFiles"]])

slots.Software_url = Slot(uri="str(uriorcurie)", name="Software_url", curie=None,
                   model_uri=PFHUB.Software_url, domain=Software, range=Union[str, SoftwareUrl])

slots.SourceCode_url = Slot(uri="str(uriorcurie)", name="SourceCode_url", curie=None,
                   model_uri=PFHUB.SourceCode_url, domain=SourceCode, range=Union[str, SourceCodeUrl])