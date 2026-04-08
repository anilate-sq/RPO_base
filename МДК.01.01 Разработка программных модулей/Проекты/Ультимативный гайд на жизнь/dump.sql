-- Создание ENUM

-- Статусы гайдов
create type guide_status as enum('черновик', 'актуальный', 'архивный');
-- Типы проблем
create type problem_type as enum('срочная', 'регулярная', 'длительная');
-- Статусы проблем
create type problem_status as enum('активная', 'разрешенная', 'отозванная');
-- Категории навыков
create type skill_category as enum('жизненные', 'профессиональные', 'здоровье', 'финансовые', 'социальные');

-- Создание таблиц

-- Пользователи
create table users(
	id serial primary key,
	username varchar(45) not null unique,
	email varchar(245) not null unique,
	password_hash varchar(245) not null,
	avatar_url varchar(500),
	level int not null default 1,
	experience int not null default 0,
	experience_to_next_level int not null default 100,
	balance decimal(10, 2) not null default 0.00,
	energy int not null default 100 check (energy between 0 and 100),
	stress_level int not null default 0 check (stress_level between 0 and 100),
	created_at timestamp with time zone default current_timestamp,
	updated_at timestamp with time zone default current_timestamp,
	is_active boolean not null default true
);

-- Индексы для таблицы `users`
create index idx_users_username on users(username);
create index idx_users_level on users(level);

-- Разделы гайдов
create table sections(
	id serial primary key,
	title varchar(45) not null,
	description text,
	icon varchar(50),
	color varchar(7),
	sort_order int not null default 0,
	created_at timestamp with time zone default current_timestamp,
	updated_at timestamp with time zone default current_timestamp,
	author int references users(id) on delete set null
);

-- Индексы для таблицы `sections`
create index idx_sections_sort_order on sections(sort_order);

-- Гайды
create table guides(
	id serial primary key,
	section_id int references sections(id) on delete cascade,
	title varchar(245) not null,
	short_description varchar(500),
	content jsonb not null,
	status guide_status not null default 'черновик',
	read_time int,
	difficulty varchar(20),
	tags text[],
	views_count int default 0,
	likes_count int default 0,
	xp_reward int not null default 10,
	skill_points jsonb,
	created_at timestamp with time zone default current_timestamp,
	updated_at timestamp with time zone default current_timestamp,
	author int references users(id) on delete set null
);

-- Индексы для таблицы `guides`
create index idx_guides_section_id on guides(section_id);
create index idx_guides_status on guides(status);
create index idx_guides_tags on guides USING GIN(tags); -- FULLTEXT INDEX

-- Навыки
create table skills(
	id serial primary key,
	name varchar(45) not null,
	description text,
	category skill_category not null,
	icon varchar(50),
	max_level int not null default 10,
	created_at timestamp with time zone default current_timestamp
);

-- Индексы для таблицы `skills`
create index idx_skills_category on skills(category);

-- Навыки конкретного пользователя
create table user_skills(
	id serial primary key,
	user_id int not null references users(id) on delete cascade,
	skill_id int not null references skills(id) on delete cascade,
	level int not null default 1 check (level >= 1),
	experience int not null default 0,
	experience_to_next_level int not null default 100,
	created_at timestamp with time zone default current_timestamp,
	updated_at timestamp with time zone default current_timestamp,
	UNIQUE(user_id, skill_id)

);

-- Индексы для таблицы `user_skills`
create index idx_user_skills_user_id on user_skills(user_id);
create index idx_user_skills_skill_id on user_skills(skill_id);

-- Проблемы
create table problems(
	id serial primary key,
	user_id int references users(id) on delete cascade,
	title varchar(100) not null,
	description text,
	problem_type problem_type not null default 'регулярная',
	status problem_status not null default 'активная',
	priority int not null default 5 check(priority between 1 and 5),
	stress_impact int default 10,
	energy_impact int default -5,
	balance_impact decimal(10,2) default 0.00,
	created_at timestamp with time zone default current_timestamp,
	updated_at timestamp with time zone default current_timestamp,
	resolved_at timestamp with time zone
);

-- Индексы для таблицы `problems`
create index idx_problems_user_id on problems(user_id);
create index idx_problems_status on problems(status);
create index idx_problems_type on problems(problem_type);
create index idx_problems_priority on problems(priority);

-- Варианты действий
create table actions_options(
	id serial primary key,
	problem_id int not null references problems(id) on delete cascade,
	title varchar(100) not null,
	description text,
	stress_change int default 0,
	energy_change int default 0,
	balance_change decimal(10, 2) default 0.00,
	xp_reward int default 0,
	success_chance int default 100 check(success_chance between 0 and 100),
	sort_order int not null default 0,
	created_at timestamp with time zone default current_timestamp
);

-- Индексы для таблицы `actions_options`
create index idx_actions_options_problem_id on actions_options(problem_id);

-- История проблем
create table user_problem_history(
	id serial primary key,
	user_id int not null references users(id) on delete cascade,
	problem_id int not null references problems(id) on delete cascade,
	action_id int not null references actions_options(id) on delete restrict,
	was_successful boolean not null default true,
	stress_change int,
	energy_change int,
	balance_change decimal(10, 2),
	xp_gained int,
	created_at timestamp with time zone default current_timestamp
);

-- Индексы для таблицы `user_problem_history`
create index idx_user_promblem_history_user_id on user_problem_history(user_id);
create index idx_user_promblem_history_problem_id on user_problem_history(problem_id);
create index idx_user_promblem_history_created_at on user_problem_history(created_at);

-- Прогресс чтения гайда
create table guide_progress(
	id serial primary key,
	user_id int not null references users(id) on delete cascade,
	guide_id int not null references guides(id) on delete cascade,
	status varchar(20) not null default 'не начато',
	progress_percent int not null default 0 check(progress_percent between 0 and 100),
	start_at timestamp with time zone default current_timestamp,
	end_at timestamp with time zone,
	UNIQUE(user_id, guide_id) -- Уникальность
);

-- Индексы для таблицы `guide_progress`
create index idx_guide_progress_user_id on guide_progress(user_id);
create index idx_guide_progress_guide_id on guide_progress(guide_id);
create index idx_guide_progress_status on guide_progress(status);

-- Достижения
create table achievements(
	id serial primary key,
	name varchar(100) not null,
	description text not null,
	icon varchar(50),
	category varchar(50),
	condition_json jsonb not null,
	xp_reward int default 0,
	skill_points jsonb,
	created_at timestamp with time zone default current_timestamp
);

-- Достижения конкретного пользователя
create table user_achievements(
	id serial primary key,
	user_id int not null references users(id) on delete cascade,
	achievement_id int not null references achievements(id) on delete cascade,
	created_at timestamp with time zone default current_timestamp,
	UNIQUE(user_id, achievement_id)
);

-- Индексы для таблицы `user_achievements`
create index idx_user_achievement_user_id on user_achievements(user_id);

-- Статистика пользователя
create table user_stats(
	id serial primary key,
	user_id int not null references users(id) on delete cascade,
	guides_read int not null default 0,
	problems_solved int not null default 0,
	days_active int not null default 0,
	longest_streak int not null default 0,
	current_streak int not null default 0,
	last_activity_date date default current_date,
	updated_at timestamp with time zone default current_timestamp,
	UNIQUE(user_id)
);

-- Индексы для таблицы `user_stats`
create index idx_user_stats_user_id on user_stats(user_id);

-- Триггеры и функции 

-- Функция для обновления поля update_at
create or replace function update_updated_at_column()
returns trigger as $$
begin
	new.updated_at = current_timestamp;
	return new;
end;
$$ language 'plpgsql';

-- Триггеры для вызова функции в разных таблицах
create trigger update_users_update_at before update on users
	for each row execute function update_updated_at_column();

create trigger update_sections_update_at before update on sections
	for each row execute function update_updated_at_column();

create trigger update_guides_update_at before update on guides
	for each row execute function update_updated_at_column();

create trigger update_problems_update_at before update on problems
	for each row execute function update_updated_at_column();

create trigger update_user_skills_update_at before update on user_skills
	for each row execute function update_updated_at_column();


-- Заполнение тестовыми данными
insert into users(username, email, password_hash, level, experience, balance, energy, stress_level)
values ('Студент 1', 'student1@gmail.com', '123', 5, 350, -3000.00, 75, 35),
('Студент 2', 'student2@gmail.com', '123', 3, 150, 1500.00, 95, 15),
('Студент 3', 'student3@gmail.com', '123', 7, 550, 50.00, 25, 85);


insert into sections(title, description, color, sort_order) values
('Быт', 'Выживание в бытовой жизни', '#ef76ae', 1),
('Финансы', 'Смерть в нищите', '#76efb7', 2),
('Учеба', 'Чертовы проекты', '#75bcf0', 3),
('Работа', 'Хлопковые поля', '#f0a975', 4),
('Менталка', 'Минус рассудок', '#bd3131', 5);

insert into skills(name, description, category, max_level) values
('Готовка', 'Смерть от голода', 'жизненные', 10),
('Бюджетирование', 'Финансовая грамотность', 'финансовые', 10),
('Тайм-менеджмент', 'Планирование времени', 'профессиональные', 10),
('Коммуникация', 'Общаться с людьми', 'социальные', 10),
('Стрессоустойчивость', 'Не гореть', 'здоровье', 10),
('Уборка', 'Порядок', 'жизненные', 10),
('Поиск информации', 'Гуглить', 'профессиональные', 10),
('Мотивация', 'Нужно поднять', 'профессиональные', 10),
('Пассивный заработок', 'Нужно копить', 'финансовые', 10),
('Целая спина', 'Боль в спине', 'здоровье', 10);

insert into guides(section_id, title, short_description, content, status, read_time, difficulty, tags, xp_reward, skill_points)
SELECT 
	s.id,
	'Как приготовить еду и не травануться',
	'Базовые принципы выживания на кухне',
	'{"blocks": [{"type": "text", "content": "Шаг 1. Купи продукты"}, {"type": "text", "content": "Шаг 2. Помой продукты"}, {"type": "text", "content": "Шаг 3. Приготовь еду"}]}',
	'актуальный',
	5,
	'легкая',
	ARRAY['еда', 'новичок', 'быт'],
	25,
	'{"life": 5}'::jsonb
	FROM sections s where title = 'Быт';

insert into problems(user_id, title, description, problem_type, status, priority, stress_impact, energy_impact, balance_impact)
select
	u.id,
	'Нужно закупиться едой',
	'В холодильнике пустота, а жрать хочется',
	'срочная',
	'активная',
	4,
	15,
	-10,
	-550.00
	FROM users u where u.username = 'Студент 1';

insert into actions_options(problem_id, title, description, stress_change, energy_change, balance_change, xp_reward, success_chance)
select
	p.id,
	'Заказать доставку',
	'Быстро, дорого, но круто',
	-10,
	5,
	-1200,
	5,
	100
from problems p where p.title = 'Нужно закупиться едой';

insert into actions_options(problem_id, title, description, stress_change, energy_change, balance_change, xp_reward, success_chance)
select
	p.id,
	'Просить у родителей',
	'Смириться с поражением',
	-5,
	0,
	5000,
	1,
	60
from problems p where p.title = 'Нужно закупиться едой';

insert into achievements (name, description, category, condition_json, xp_reward) values
('Первые шаги', 'Прочитать первый гайд', 'начинающий', '{"guides_read": 1}', 50),
('Финансовый гроссмейстер', 'Выйти в плюс по балансу', 'финансовый магнат', '{"balance_positive": true}', 100),
('Опытный выживальщик', 'Решить 10 проблем', 'выживальщик', '{"problems_solved": 10}', 150),
('Дзем мастер', 'Снизить стресс до 0', 'здоровье', '{"stress_zero": true}', 200);