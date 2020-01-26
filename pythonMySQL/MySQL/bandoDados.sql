drop table aluno;

create table alunos(
id_aluno int not null,
id_Nota int,
id_Curso int,
data_nascimento date,
nome varchar(40) not null, 
endereco varchar(255) not null, 
cpf varchar (11) not null, 
primary key(id_aluno),
FOREIGN KEY (id_Nota) REFERENCES notas (id_Notas),
FOREIGN KEY (id_Curso) references cursos (idCurso)); 

create table aluno(
id_aluno int not null,
data_nascimento date,
nome varchar(40) not null, 
endereco varchar(255) not null, 
cpf varchar (11) not null, 
primary key(id_aluno)); 

create table curso(
idCurso int not null, 
nomeCurso varchar(40) not null, 
primary key(idCurso));

create table nota(
	idNotas int not null, 
    descricao varchar(40) not null, 
    nota float not null, 
    primary key(idNotas));
    
    insert into alunos 
    values(DEFAULT, default, default, '1997-03-26',  'Pedro', 'endereço adjfjusfufdsfu', '06444544');
    
    insert into alunos 
    values(DEFAULT, default, default, '1997-03-26',  'Jackson2', 'endereço adjfjusfufdsfu', '06414444544');
    
    insert into cursos
    values('15', 'Ciência da Computação');
    
    insert into aluno
    values(DEFAULT, '1997-03-26',  'Joao', 'endereco Rua 3', 0655654544);
    
    insert into aluno
    values(DEFAULT, '1997-03-26',  'João Pedro', 'esse é meu endereço Rua 3', 0655654544);
    
    insert into alunos 
    values(DEFAULT, 'Jackson3', 'endereco adjfjusfufdsfu', 0641444454, '1997-03-26');
  
    select * from alunos; 
    select * from aluno; 
   