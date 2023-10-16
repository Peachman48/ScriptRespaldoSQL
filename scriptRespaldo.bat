set anio=%date:~6,4%
set mes=%date:~3,2%
set dia=%date:~0,2%
set nombre_db="--all-databases"
set nombre=db-%dia%-%mes%-%anio%.sql

mysqldump -u root -p123 %nombre_db% > C:\Respaldos_sql\%nombre%

