

CREATE TABLE "ComputeResource" (
	architecture TEXT, 
	cores INTEGER, 
	nodes INTEGER, 
	PRIMARY KEY (architecture, cores, nodes)
);

CREATE TABLE "CsvFile" (
	name TEXT NOT NULL, 
	format VARCHAR(3), 
	PRIMARY KEY (name)
);

CREATE TABLE "DataFile" (
	name TEXT NOT NULL, 
	format TEXT, 
	PRIMARY KEY (name)
);

CREATE TABLE "Results" (
	csv_data TEXT, 
	raw_data TEXT, 
	viz_data TEXT, 
	hardware TEXT, 
	memory_in_kb INTEGER, 
	time_in_s INTEGER, 
	PRIMARY KEY (csv_data, raw_data, viz_data, hardware, memory_in_kb, time_in_s)
);

CREATE TABLE "SourceCode" (
	url TEXT NOT NULL, 
	name TEXT, 
	"commit" TEXT, 
	PRIMARY KEY (url)
);

CREATE TABLE "Tarball" (
	name TEXT NOT NULL, 
	format VARCHAR(6), 
	PRIMARY KEY (name)
);

CREATE TABLE "VisualizationFile" (
	name TEXT NOT NULL, 
	format TEXT, 
	PRIMARY KEY (name)
);

CREATE TABLE "BenchmarkResult" (
	id TEXT NOT NULL, 
	benchmark_problem VARCHAR(2) NOT NULL, 
	benchmark_version INTEGER NOT NULL, 
	date_created DATE, 
	implementation TEXT, 
	results TEXT, 
	summary TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(implementation) REFERENCES "SourceCode" (url)
);

CREATE TABLE "CsvFile_columns" (
	backref_id TEXT, 
	columns TEXT, 
	PRIMARY KEY (backref_id, columns), 
	FOREIGN KEY(backref_id) REFERENCES "CsvFile" (name)
);

CREATE TABLE "Contributor" (
	id TEXT NOT NULL, 
	name TEXT, 
	email TEXT, 
	"BenchmarkResult_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("BenchmarkResult_id") REFERENCES "BenchmarkResult" (id)
);

CREATE TABLE "Software" (
	url TEXT NOT NULL, 
	name TEXT, 
	"commit" TEXT, 
	download TEXT, 
	version TEXT, 
	"BenchmarkResult_id" TEXT, 
	PRIMARY KEY (url), 
	FOREIGN KEY("BenchmarkResult_id") REFERENCES "BenchmarkResult" (id)
);

CREATE TABLE "Contributor_handle" (
	backref_id TEXT, 
	handle TEXT, 
	PRIMARY KEY (backref_id, handle), 
	FOREIGN KEY(backref_id) REFERENCES "Contributor" (id)
);

CREATE TABLE "Contributor_affiliation" (
	backref_id TEXT, 
	affiliation TEXT, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES "Contributor" (id)
);
