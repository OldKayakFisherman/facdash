CREATE SCHEMA census_data;
CREATE SCHEMA gsa_data;
CREATE SCHEMA fac_reports;


-- Census Data

DROP TABLE census_data.agencies;

CREATE TABLE census_data.agencies
(
	id serial not null,
	audityear varchar(4),
	dbkey varchar(10),
	ein varchar(9),
	agency varchar(200),
	CONSTRAINT pk_import_agencies PRIMARY KEY ("id")
);

ALTER TABLE census_data.agencies OWNER TO facdata;


DROP TABLE census_data.captext;

CREATE TABLE census_data.captext
(
	id serial not null,
	seq_number text,
	dbkey text,
	audityear text,
	findingrefnums text,
	text text,
	chartstables text,
	CONSTRAINT pk_import_captext PRIMARY KEY ("id")
);

ALTER TABLE census_data.captext OWNER TO facdata;

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

DROP TABLE census_data.cpas;

CREATE TABLE census_data.cpas
(
	id serial not null,
	dbkey varchar(10),
	audityear varchar(4),
	cpafirmname varchar(70),
	cpaein varchar(9),
	cpastreet1 varchar(50),
	cpacity varchar(30),
	cpastate varchar(2),
	cpazipcode varchar(9),
	cpacontact varchar(50),
	cpatitle varchar(40),
	cpaphone varchar(10),
	cpafax varchar(10),
	cpaemail varchar(60),
	CONSTRAINT pk_import_cpas PRIMARY KEY ("id")
);

ALTER TABLE census_data.cpas OWNER TO facdata;

DROP TABLE census_data.duns;

CREATE TABLE census_data.duns
(
	id serial not null,
	audityear varchar(4),
	dbkey varchar(10),
	duns varchar(9),
	dunseqnum varchar(4),
	CONSTRAINT pk_import_duns PRIMARY KEY ("id")
);

ALTER TABLE census_data.duns OWNER TO facdata;

DROP TABLE census_data.eins;

CREATE TABLE census_data.eins
(
	id serial not null,
	audityear varchar(4),
	dbkey varchar(10),
	ein varchar(9),
	einseqnum varchar(4),
	CONSTRAINT pk_import_eins PRIMARY KEY ("id")
);

ALTER TABLE census_data.eins OWNER TO facdata;


CREATE TABLE census_data.findings
(
	id serial not null,
	dbkey varchar(10),
	audityear varchar(4),
	elecauditsid varchar(10),
	elecauditfindingsid varchar(10),
	findingsrefnums varchar(100),
	typerequirement varchar(16),
	modifiedopinion varchar(1),
	othernoncompliance varchar(1),
	materialweakness varchar(1),
	significantdeficiency varchar(1),
	otherfindings varchar(1),
	qcosts varchar(1),
	repeatfinding varchar(1),
	priorfindingrefnums varchar(100),
	CONSTRAINT pk_import_findings PRIMARY KEY ("id")
);

ALTER TABLE census_data.findings OWNER TO facdata;

DROP TABLE census_data.findingstext;

CREATE TABLE census_data.findingstext
(
	id serial not null,
	seq_number text,
	dbkey text,
	audityear text,
	findingrefnums text,
	text text,
	chartstables text,
	CONSTRAINT pk_import_findingstext PRIMARY KEY ("id")
);

ALTER TABLE census_data.findingstext OWNER TO facdata;

DROP TABLE census_data.general;

CREATE TABLE census_data.general
(
	id serial primary key,
	audityear text,
	dbkey text,
	typeofentity text,
	fyenddate text,
	audittype text,
	periodcovered text,
	numbermonths text,
	ein text,
	multipleeins text,
	einsubcode text,
	duns text,
	multipleduns text,
	auditeename text,
	street1 text,
	street2 text,
	city text,
	state text,
	zipcode text,
	auditeecontact text,
	auditeetitle text,
	auditeephone text,
	auditeefax text,
	auditeeemail text,
	auditeedatesigned text,
	auditeenametitle text,
	cpafirmname text,
	cpastreet1 text,
	cpastreet2 text,
	cpacity text,
	cpastate text,
	cpazipcode text,
	cpacontact text,
	cpatitle text,
	cpaphone text,
	cpafax text,
	cpaemail text,
	cpadatesigned text,
	cog_over text,
	cogagency text,
	oversightagency text,
	typereport_fs text,
	sp_framework text,
	sp_framework_required text,
	typereport_sp_framework text,
	goingconcern text,
	reportablecondition text,
	materialweakness text,
	materialnoncompliance text,
	typereport_mp text,
	dup_reports text,
	dollarthreshold text,
	lowrisk text,
	reportablecondition_mp text,
	materialweakness_mp text,
	qcosts text,
	cyfindings text,
	pyschedule text,
	totfedexpend text,
	datefirewall text,
	previousdatefirewall text,
	reportrequired text,
	multiple_cpas text,
	auditor_ein text,
	facaccepteddate text,
	cpaforeign text,
	cpacountry text,
	entity_type text,
	uei text,
	multipleueis text
);

ALTER TABLE census_data.general OWNER TO facdata;

CREATE TABLE import.incomplete
(
	id serial not null,
	audityear varchar(4),
	dbkey varchar(10),
	ein varchar(9),
	auditeename varchar(70),
	street1 varchar(45),
	street2 varchar(45),
	city varchar(30),
	state varchar(2),
	zipcode varchar(10),
	status varchar(10),
	cogagency varchar(4),
	totfedexpend varchar(12),
	initialdatereceived varchar(10),
	formdate varchar(10),
	componentdate varchar(10),
	CONSTRAINT pk_import_incomplete PRIMARY KEY ("id")
);

ALTER TABLE import.incomplete OWNER TO fac_app;

DROP TABLE census_data.notes;

CREATE TABLE census_data.notes
(
	id serial not null,
	dbkey text,
	audityear text,
    source_id text,
    reportid text,
    version text,
    seq_number  text,
    type_id text,
    note_index text,
    title text,
    content text,
	CONSTRAINT pk_import_notes PRIMARY KEY ("id")
);

ALTER TABLE census_data.notes OWNER TO facdata;

DROP TABLE TABLE census_data.passthrough;

CREATE TABLE census_data.passthrough
(
	id serial not null,
	dbkey text,
	audityear text,
	elecauditsid text,
	passthroughname text,
	passthroughid text,
	CONSTRAINT pk_import_passthrough PRIMARY KEY ("id")
);

ALTER TABLE census_data.passthrough OWNER TO facdata;

DROP TABLE TABLE census_data.passthrough;

CREATE TABLE census_data.passthrough
(
	id serial not null,
	dbkey text,
	audityear text,
	elecauditsid text,
	passthroughname text,
	passthroughid text,
	CONSTRAINT pk_import_passthrough PRIMARY KEY ("id")
);

ALTER TABLE census_data.passthrough OWNER TO facdata;

DROP TABLE TABLE census_data.ueis;

CREATE TABLE census_data.ueis
(
	id serial not null,
    dbkey text,
    audityear text,
    uei text,
    ueiseqnum text,
	CONSTRAINT pk_import_ueis PRIMARY KEY ("id")
);

ALTER TABLE census_data.ueis OWNER TO facdata;

-- gsa data

DROP TABLE gsa_data.awards;

CREATE TABLE gsa_data.awards
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    award_reference text,
    federal_agency_prefix text,
    federal_award_extension text,
    additional_award_identification text,
    federal_program_name text,
    amount_expended text,
    cluster_name text,
    other_cluster_name text,
    state_cluster_name text,
    cluster_total money,
    federal_program_total money,
    is_major bool,
    is_loan bool,
    loan_balance text,
    is_direct bool,
    audit_report_type text,
    findings_count int,
    is_passthrough_award bool,
    passthrough_amount money

);

ALTER TABLE gsa_data.awards OWNER TO facdata;


DROP TABLE gsa_data.corrective_action_plans;

CREATE TABLE gsa_data.corrective_action_plans
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    finding_ref_number text,
    contains_chart_or_table bool,
    planned_action text
);

ALTER TABLE gsa_data.corrective_action_plans OWNER TO facdata;


DROP TABLE gsa_data.findings;

CREATE TABLE gsa_data.findings
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    award_reference text,
    reference_number text,
    is_material_weakness bool,
    is_modified_opinion bool,
    is_other_findings bool,
    is_other_matters bool,
    prior_finding_ref_numbers text,
    is_questioned_costs bool,
    is_repeat_finding bool,
    is_significant_deficiency bool,
    type_requirement text
);

ALTER TABLE gsa_data.findings OWNER TO facdata;


DROP TABLE gsa_data.findings_text;

CREATE TABLE gsa_data.findings_text
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    finding_ref_number text,
    contains_chart_or_table text,
    finding_text text
);

ALTER TABLE gsa_data.findings_text OWNER TO facdata;


DROP TABLE gsa_data.general;

CREATE TABLE gsa_data.general
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    auditee_certify_name text,
    auditee_certify_title text,
    auditee_contact_name text,
    auditee_email text,
    auditee_name text,
    auditee_phone text,
    auditee_contact_title text,
    auditee_address_line_1 text,
    auditee_city text,
    auditee_state text,
    auditee_ein text,
    auditee_zip text,
    auditor_phone text,
    auditor_state text,
    auditor_city text,
    auditor_contact_title text,
    auditor_address_line_1 text,
    auditor_zip text,
    auditor_country text,
    auditor_contact_name text,
    auditor_email text,
    auditor_firm_name text,
    auditor_foreign_address text,
    auditor_ein text,
    cognizant_agency text,
    oversight_agency text,
    date_created date,
    ready_for_certification_date date,
    auditor_certified_date date,
    auditee_certified_date date,
    submitted_date date,
    fac_accepted_date date,
    fy_end_date date,
    fy_start_date date,
    audit_type text,
    gaap_results text,
    sp_framework_basis text,
    is_sp_framework_required text,
    sp_framework_opinions text,
    is_going_concern_included bool,
    is_internal_control_deficiency_disclosed bool,
    is_internal_control_material_weakness_disclosed bool,
    is_material_noncompliance_disclosed bool,
    dollar_threshold money,
    is_low_risk_auditee bool,
    agencies_with_prior_findings text,
    entity_type text,
    number_months text,
    audit_period_covered text,
    total_amount_expended text,
    type_audit_code text,
    is_public bool,
    data_source text
);

ALTER TABLE gsa_data.general OWNER TO facdata;


DROP TABLE gsa_data.notes_to_sefa;

CREATE TABLE gsa_data.notes_to_sefa
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    title text,
    accounting_policies text,
    is_minimis_rate_used bool,
    rate_explained text,
    contains_chart_or_table bool
);

ALTER TABLE gsa_data.notes_to_sefa OWNER TO facdata;


DROP TABLE gsa_data.passthroughs;

CREATE TABLE gsa_data.passthroughs
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    award_reference text,
    passthrough_id text,
    passthrough_name text
);

ALTER TABLE gsa_data.passthroughs OWNER TO facdata;


DROP TABLE gsa_data.secondary_auditors;

CREATE TABLE gsa_data.secondary_auditors
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    auditor_ein text,
    auditor_name text,
    contact_name text,
    contact_email text,
    contact_phone text,
    address_street text,
    address_city text,
    address_state text,
    address_zipcode text
);

ALTER TABLE gsa_data.secondary_auditors OWNER TO facdata;


DROP TABLE gsa_data.additional_ueis;

CREATE TABLE gsa_data.additional_ueis
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    additional_uei text
);

ALTER TABLE gsa_data.additional_ueis OWNER TO facdata;


