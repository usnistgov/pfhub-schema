

CREATE TABLE "Benchmark" (
	id TEXT NOT NULL, 
	name TEXT, 
	number TEXT, 
	version TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ComputeResource" (
	architecture TEXT, 
	cores INTEGER, 
	nodes INTEGER, 
	PRIMARY KEY (architecture, cores, nodes)
);

CREATE TABLE "Results" (
	data_raw TEXT, 
	data_table TEXT NOT NULL, 
	data_visualization TEXT, 
	hardware TEXT, 
	"memory_in_KB" INTEGER, 
	time_in_s INTEGER, 
	PRIMARY KEY (data_raw, data_table, data_visualization, hardware, "memory_in_KB", time_in_s)
);

CREATE TABLE "SourceCode" (
	id TEXT NOT NULL, 
	name TEXT, 
	repository TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "BenchmarkResult" (
	id TEXT NOT NULL, 
	name TEXT, 
	benchmark TEXT, 
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
	"BenchmarkResult_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("BenchmarkResult_id") REFERENCES "BenchmarkResult" (id)
);

CREATE TABLE "Software" (
	id TEXT NOT NULL, 
	name TEXT, 
	download TEXT, 
	repository TEXT, 
	version TEXT, 
	"BenchmarkResult_id" TEXT, 
	PRIMARY KEY (id), 
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
