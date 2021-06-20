with cte_dedup as(
SELECT t1."date"
    ,t1."rank"
    ,t1.song
    ,t1.artist
    ,row_number() over(partition by t1.artist, t1.song order by
t1.artist,t1.song, t1."date") as dedup_song
    ,row_number() over(partition by t1.artist order by t1.artist,
t1."date") as dedup_artist
FROM PUBLIC."Billboard" AS t1 order by t1.artist , t1."date"
)
select t1."date"
    ,t1."rank"
    ,t1.artist
    ,t1.song
from cte_dedup as t1
where t1.artist like '%' and t1.dedup_song = 1 --and t1.dedup_artist = 1 ;
create table tb_first_song as(
with cte_dedup as(
SELECT t1."date"
    ,t1."rank"
    ,t1.song
    ,t1.artist
    ,row_number() over(partition by t1.artist, t1.song order by
t1.artist,t1.song, t1."date") as dedup_song
    ,row_number() over(partition by t1.artist order by t1.artist,
t1."date") as dedup_artist
FROM PUBLIC."Billboard" AS t1 order by t1.artist , t1."date"
)
select t1."date"
    ,t1."rank"
    ,t1.artist
    ,t1.song
from cte_dedup as t1
where t1.artist like '%AC/DC' or t1.artist like '%Elvis%' and t1.dedup_song = 1
--and t1.dedup_artist = 1
)
;
drop table tb_first_song;
select * from tb_first_song;
create view vw_song as(
select * from tb_first_song
);
insert into tb_first_song (
with cte_dedup as(
SELECT t1."date"
    ,t1."rank"
    ,t1.song
    ,t1.artist
    ,row_number() over(partition by t1.artist, t1.song order by t1.artist,t1.song, t1."date") as dedup_song
    ,row_number() over(partition by t1.artist order by t1.artist,
t1."date") as dedup_artist
FROM PUBLIC."Billboard" AS t1 order by t1.artist , t1."date"
)
select t1."date"
    ,t1."rank"
    ,t1.artist
    ,t1.song
from cte_dedup as t1
where t1.artist like '%Elvis%' and t1.dedup_song = 1
--and t1.dedup_artist = 1
)
select * from vw_song;
create or replace view vw_song as(
select * from tb_first_song as t1 where  t1.artist  like '%AC/DC'
);