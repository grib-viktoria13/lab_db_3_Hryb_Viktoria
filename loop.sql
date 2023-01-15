DO $$
 DECLARE
	test_name artist.name%TYPE;
	test_country artist.country%TYPE;
	test_tcu artist.tcu%TYPE;
	test_year artist.years%TYPE;
     
 BEGIN 
     test_name:= 'Lady Gaga'; 
     test_country:= ''; 
     test_tcu:=159;
     test_year:=2008;
    FOR i in 1 ..5 total LOOP 
   	   INSERT into artist(id, name, country,tcu,years) VALUES(6+i, test_name || i, test_country || i, test_tcu+i, test_year+i);
    END LOOP; 
 END;
$$

