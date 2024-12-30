-- inner join
select * from users inner join ratings on users.id=ratings.user_id;

-- left join
select * from users left join ratings on users.id=ratings.user_id;

-- right join
select * from users right join ratings on users.id=ratings.user_id;

-- self join
select * from ratings self join ratings;

-- full join
select * from users left join ratings on users.id=ratings.user_id
union
select * from users right join ratings on users.id=ratings.user_id;

-- cross join
select * from users cross join ratings;



