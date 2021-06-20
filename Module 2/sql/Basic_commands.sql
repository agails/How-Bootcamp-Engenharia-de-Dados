select
       TBB."date"
       , TBB."rank"
       , TBB.song
       , TBB.artist
       , TBB."last-week"
       , TBB."peak-rank"
       , TBB."weeks-on-board"
from
       "Billboard" as TBB
limit 10;

select
       count(TBB.date) as days
from
       "Billboard" as TBB;

select
       max(TBB."date") as max_date
from
       "Billboard" as TBB;

select
       count(*) as lines
from
       "Billboard" as TBB;

select
       TBB."date"
       , TBB."rank"
       , TBB.song
       , TBB.artist
       , TBB."last-week"
       , TBB."peak-rank"
       , TBB."weeks-on-board"
from
       "Billboard" as TBB
where
       TBB."date" = '2021-03-13'

order by 2;

select
       TBB."date"
       , TBB."rank"
       , TBB.song
       , TBB.artist
       , TBB."last-week"
       , TBB."peak-rank"
       , TBB."weeks-on-board"
from
       "Billboard" as TBB
where
       TBB."date" = '2021-03-13'
       and TBB."rank" <= 10;
       
select
       distinct TBB.artist
       , TBB.song
       , MAX(TBB."weeks-on-board") as max_weeks
from
       "Billboard" as TBB
where
       TBB.artist like 'Metallica'
group by
       TBB.song
       , TBB.artist
order by
       3 desc;



