DROP TABLE TABLE census_data.revisions;

CREATE TABLE census_data.revisions
(
	id serial not null,
    dbkey text,
    audityear text,
    geninfo text,
    geninfo_explain text,
    federalawards text,
    federalawards_explain text,
    notestosefa text,
    notestosefa_explain text,
    auditinfo text,
    auditinfo_explain text,
    findings text,
    findings_explain text,
    findingstext text,
    findingstext_explain text,
    cap text,
    cap_explain text,
    other text,
    other_explain text,
    elecrptrevisionid text,
	CONSTRAINT pk_import_revisions PRIMARY KEY ("id")
);

ALTER TABLE census_data.revisions OWNER TO facdata;