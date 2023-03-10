

CREATE TABLE "Benchmark" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	version TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Implementation" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	repository TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "BenchmarkResult" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	benchmark TEXT, 
	framework TEXT, 
	hardware TEXT, 
	implementation TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(benchmark) REFERENCES "Benchmark" (id), 
	FOREIGN KEY(implementation) REFERENCES "Implementation" (id)
);

CREATE TABLE "Contributor" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	handle TEXT, 
	email TEXT, 
	"BenchmarkResult_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("BenchmarkResult_id") REFERENCES "BenchmarkResult" (id)
);

CREATE TABLE "Contributor_affiliation" (
	backref_id TEXT, 
	affiliation TEXT, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES "Contributor" (id)
);
