-- https://www.hackerrank.com/challenges/revising-the-select-query/problem

select
  *
from
  city
where
  population > 100000
  and countrycode = 'USA'

-- https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
select
  name
from
  city
where
  population > 120000
  and countrycode = 'USA'

-- https://www.hackerrank.com/challenges/asian-population/problem

select
  sum(city.population)
from
  city
  inner join country on city.countrycode = country.code
where
  country.continent = 'Asia'

-- The PADS
-- https://www.hackerrank.com/challenges/the-pads/problem

select
  concat(name, '(', left(occupation, 1), ')')
from
  occupations
order by
  name;

select
  concat(
    'There are a total of ',
    count(*),
    ' ',
    lower(occupation),
    's.'
  )
from
  occupations
group by
  occupation
order by
  count(*),
  occupation;

-- SQL Project Planning
-- https://www.hackerrank.com/challenges/sql-projects/problem

SET
  sql_mode = '';
SELECT
  Start_Date,
  End_Date
FROM
  (
    SELECT
      Start_Date
    FROM
      Projects
    WHERE
      Start_Date NOT IN (
        SELECT
          End_Date
        FROM
          Projects
      )
  ) a,
  (
    SELECT
      End_Date
    FROM
      Projects
    WHERE
      End_Date NOT IN (
        SELECT
          Start_Date
        FROM
          Projects
      )
  ) b
WHERE
  Start_Date < End_Date
GROUP BY
  Start_Date
ORDER BY
  DATEDIFF(End_Date, Start_Date),
  Start_Date

-- https://www.hackerrank.com/challenges/weather-observation-station-18/problem

select
  round(
    abs(min(lat_n) - max(lat_n)) + abs(min(long_w) - max(long_w)),
    4
  )
from
  station

-- https://www.hackerrank.com/challenges/symmetric-pairs/problem

select
  f1.x,
  f1.y
from
  functions f1
  join functions f2
where
  f1.y = f2.x
  and f1.x = f2.y
  and f1.x < f1.y

union

select
  x,
  y
from
  functions
where
  x = y
group by
  x,
  y
having
  count(*) > 1
order by
  x;
