CREATE DATABASE patient_ms_db;

CREATE TABLE patients (
 p_id int NOT NULL,
 p_name varchar(25) NOT NULL,
 p_age int NOT NULL,
 p_address varchar(100) NOT NULL,
 PRIMARY KEY (p_id)
);

CREATE TABLE appointments (
 a_no int NOT NULL,
 a_type varchar(50) NOT NULL,
 a_timing datetime NOT NULL,
 p_id int NOT NULL,
 
 PRIMARY KEY (a_no),
 foreign key(p_id) references patients(p_id)
);

CREATE TABLE employees (
 e_id int NOT NULL,
 e_name varchar(25) NOT NULL,
 e_age int NOT NULL,
 p_id int NOT NULL,
 
 PRIMARY KEY (e_id),
 foreign key(p_id) references patients(p_id)
);

CREATE TABLE doctor (
 e_id int(11) NOT NULL,
 specialization varchar(50) NOT NULL,
 p_id int not null,
 
 FOREIGN KEY (e_id) REFERENCES employees (e_id),
 foreign key(p_id) references patients(p_id)
); 

CREATE TABLE hospital (
 h_regno int(11) NOT NULL,
 h_name varchar(50) NOT NULL,
 h_address varchar(100) NOT NULL,
 h_contact int(10) NOT NULL,
 h_type varchar(50) NOT NULL,
 p_id int not null,
 
 PRIMARY KEY (h_regno),
 foreign key(p_id) references patients(p_id)
);

CREATE TABLE insurance (
 p_no int NOT NULL,
 p_type varchar(50) NOT NULL,
 amt float NOT NULL,
 coverage float NOT NULL,
 p_id int not null,
 
 PRIMARY KEY (p_no),
 foreign key(p_id) references patients(p_id)
);

CREATE TABLE medicine (
 m_code int NOT NULL,
 m_name varchar(100) NOT NULL,
 m_dosage decimal(10,0) NOT NULL,
 m_type varchar(50) NOT NULL,
 p_id int not null,
 
 PRIMARY KEY (m_code),
 foreign key(p_id) references patients(p_id)
);

CREATE TABLE nurse (
 e_id int NOT NULL,
 qualifications varchar(50) NOT NULL,
 p_id int not null,
 
 FOREIGN KEY (e_id) REFERENCES employees (e_id),
 foreign key(p_id) references patients(p_id)
) ;

CREATE TABLE payments (
 recipt_no int NOT NULL,
 p_methods varchar(50) NOT NULL,
 p_amt float NOT NULL,
 installments int NOT NULL,
 p_id int not null,
 
 PRIMARY KEY (recipt_no),
 foreign key(p_id) references patients(p_id)
);

CREATE TABLE reports (
 r_no int NOT NULL,
 r_type varchar(50) NOT NULL,
 r_date date NOT NULL,
 no_of_reports int NOT NULL,
 p_id int not null,
 
 PRIMARY KEY (r_no),
 foreign key(p_id) references patients(p_id)
);

CREATE TABLE ward (
 w_no int NOT NULL,
 w_type varchar(50) NOT NULL,
 w_location varchar(100) NOT NULL,
 p_id int not null,
 
 PRIMARY KEY (w_no),
 foreign key(p_id) references patients(p_id)
);