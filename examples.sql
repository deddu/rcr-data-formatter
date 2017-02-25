-- cmd + r to run

-- jobs types
select distinct(JobTypeName), `JobTypeInternalDescription` from feb_17;

-- who has been terminated since the beginning of the year
select FullName from feb_17 where TerminatedOn is not Null and TerminatedOn > '2017-01-01'; 

-- who's new after the beginning of the year
select FullName, UserName, `OrganizationName` from feb_17 where `Funding-NSFEarnsBegin/JournalFromDate` is not Null and `Funding-NSFEarnsBegin/JournalFromDate` > '2017-01-01'; 