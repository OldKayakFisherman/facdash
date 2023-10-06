DROP TABLE census_data.cfdas;

CREATE TABLE census_data.cfdas
(
	id serial not null,
	audityear text,
	dbkey text,
	ein text,
	cfda text,
	awardidentification text,
	rd text,
	federalprogramname text,
	amount text,
	clustername text,
	stateclustername text,
	programtotal text,
	clustertotal text,
	direct text,
	passthroughaward text,
	passthroughamount text,
	majorprogram text,
	typereport_mp text,
	typerequirement text,
	qcosts2 text,
	findings text,
	findingrefnums text,
	arra text,
	loans text,
	loanbalance text,
	findingscount text,
	elecauditsid text,
	otherclustername text,
    cfdaprogramname text,
	CONSTRAINT pk_import_cfdas PRIMARY KEY ("id")	
);

ALTER TABLE census_data.cfdas OWNER TO facdata;
