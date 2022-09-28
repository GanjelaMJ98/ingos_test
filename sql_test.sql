-- 1)
-- a
select 	region_id,
		max(gender_group.max_salary) - min(gender_group.max_salary) as deff_max,
		max(gender_group.min_salary) - min(gender_group.min_salary) as deff_min
from (
	select 	region_id,
			gender,
			max(salary) as max_salary,
			min(salary) as min_salary
	from staff
	group by region_id, gender
	order by region_id) as gender_group
group by region_id;

-- b
select 	country,
		company_regions, 
		percentile_disc(0.5) within group (order by salary) as perc_0_5,
		percentile_disc(0.6) within group (order by salary) as perc_0_6,
		percentile_disc(0.9) within group (order by salary) as perc_0_9,
		percentile_disc(0.95) within group (order by salary) as perc_0_95
from staff natural join company_regions
group by country, company_regions

-- c
alter table company_divisions alter column company_division set not null;

-- d
create view director_viev as
	select 	company_regions.company_regions,
			company_divisions.department,
			staff.last_name,
			staff.job_title
	from staff
	inner join company_divisions on  company_divisions.department = staff.department
	inner join company_regions on  company_regions.region_id =  staff.region_id
	where lower(job_title)  like '%director%';

-- e
create index idx_staff_job_title1 ON staff (lower(job_title));











-- 2)
select 	CONCAT(left(author_firstname, 1), ' ', author_lastname) as author_name,
		max(book_price),
		min(book_price),
		sum(expensive_book) as count
from (	select *, 	case 
						when book_price < 10 then 0 else 1
					end expensive_book
		from authors 
		inner join books on books.book_author = authors.author_id
		) full_table
group by author_firstname, author_lastname
having  sum(expensive_book) <> 0
order by count desc, max desc, author_lastname asc;