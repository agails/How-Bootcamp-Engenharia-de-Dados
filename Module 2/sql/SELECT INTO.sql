select
    TBB."date",
    TBB."rank",
    TBB.song,
    TBB.artist,
    TBB."last-week",
    TBB."peak-rank",
    TBB."weeks-on-board"
from
    "Billboard" as TBB
limit 10;

select max(TBB."date") as max_date from "Billboard" as TBB limit 10; 

select max(TBB."date") as max_date from "Billboard" as TBB;

select TBB."date" as max_date from "Billboard" as TBB order by "date" desc
limit 1 ;

select
    TBB."date",
    TBB."rank",
    TBB.song,
    TBB.artist,
    TBB."last-week",
    TBB."peak-rank",
    TBB."weeks-on-board"
from
    "Billboard" as TBB
where TBB."date" = '2021-03-13';

select
    TBB."date",
    TBB."rank",
    TBB.song,
    TBB.artist,
    TBB."last-week",
    TBB."peak-rank",
    TBB."weeks-on-board"
from
    "Billboard" as TBB
where TBB."date" = '2021-03-13' and TBB."rank" <= 10;
