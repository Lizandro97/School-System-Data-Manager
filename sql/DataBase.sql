--EJECUTAR PARA CREAR LA BD
CREATE DATABASE BDFyA;


use BDFyA

--EJECUTAR PRIMERA TABLA
CREATE TABLE Estudiante(
IdEstudiante int primary key not null,
Nombre varchar(30) not null,
Apellido varchar(30) not null,
Dirección varchar(50) not null,
Telefono varchar(9) not null,
DNI int not null,
Ciudad varchar(9) not null,
Correo varchar(20) not null
)
GO

INSERT INTO Estudiante (IdEstudiante, Nombre, Apellido, Dirección, Telefono, DNI, Ciudad, Correo)
VALUES (001, 'juan', 'Chipana', '24 de octubre', 925751266, 71657437, 'Ilo', 'wilias@gmaiol.com')


CREATE TABLE Curso(
Nombre_Curso int primary key not null,
Tipo varchar(30) not null,
Grado varchar(50) not null,
Codigo int not null,
HoraSemana int not null,
Creditos INTEGER DEFAULT 0,
)

INSERT INTO Curso (IdCurso, Nombre_Curso, Tipo, Grado, Codigo, HoraSemana, Creditos)
values(001, 'Algebra', 'Numeros', 'Quinto grado', 2017147889, 7, 3)
