

CREATE TABLE "Benchmark" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	version TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "BenchmarkResult" (
	datasets TEXT, 
	PRIMARY KEY (datasets)
);

CREATE TABLE "ComputeResource" (
	architecture TEXT, 
	cores INTEGER, 
	nodes INTEGER, 
	PRIMARY KEY (architecture, cores, nodes)
);

CREATE TABLE "Results" (
	csv_data TEXT NOT NULL, 
	raw_data TEXT, 
	viz_data TEXT, 
	hardware TEXT, 
	memory_in_kb INTEGER, 
	time_in_s INTEGER, 
	PRIMARY KEY (csv_data, raw_data, viz_data, hardware, memory_in_kb, time_in_s)
);

CREATE TABLE "SourceCode" (
	id TEXT NOT NULL, 
	name TEXT, 
	repository TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	name TEXT, 
	benchmark TEXT, 
	date_created DATE, 
	implementation TEXT, 
	results TEXT, 
	summary TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(benchmark) REFERENCES "Benchmark" (id), 
	FOREIGN KEY(implementation) REFERENCES "SourceCode" (id)
);

CREATE TABLE "Contributor" (
	id TEXT NOT NULL, 
	name TEXT, 
	email TEXT, 
	"Dataset_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);

CREATE TABLE "Software" (
	id TEXT NOT NULL, 
	name TEXT, 
	download TEXT, 
	repository TEXT, 
	version TEXT, 
	"Dataset_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
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
