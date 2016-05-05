### commandly used mysql query


``` mysql
CREATE TABLE IF NOT EXISTS DS2_1_reads_taxapath_megan
(
    reads_name VARCHAR(255) NOT NULL,
    taxapath VARCHAR(1200),
    PRIMARY KEY (reads_name)
    )CHARSET=utf8;
```

``` mysql
CREATE TABLE IF NOT EXISTS DS2_1_reads_taxa 
(
    id INT AUTO_INCREMENT NOT NULL,  
    reads_name VARCHAR(255) NOT NULL,
    taxapath VARCHAR(1200),
    PRIMARY KEY (id),
    FULLTEXT INDEX (reads_name)
    )CHARSET=utf8;
```


```    
CREATE TABLE IF NOT EXISTS DS2_2_reads_taxapath_megan
(
    reads_name VARCHAR(255) NOT NULL,
    taxapath VARCHAR(1200),
    PRIMARY KEY (reads_name)
    )CHARSET=utf8;
```
 
```  
CREATE TABLE IF NOT EXISTS ICC_reads_taxapath_megan
(
    reads_name VARCHAR(255) NOT NULL,
    taxapath VARCHAR(1200),
    PRIMARY KEY (reads_name)
    )CHARSET=utf8;
```

```
CREATE TABLE IF NOT EXISTS gi_taxaid
(
	gi INT NOT NULL,
	taxaid INT ,	
	PRIMARY KEY (gi)
)CHARSET=utf8
```

```	
CREATE TABLE IF NOT EXISTS taxa_id_name
(
	tax_id INT NOT NULL,
	name_txt VARCHAR(200) NOT NULL,
	unique_name VARCHAR(120),
	name_class VARCHAR(255),
	PRIMARY KEY (name_txt, unique_name)
)CHARSET=utf8;
```

```
CREATE TABLE IF NOT EXISTS prot_refseq
(
	prot_id INT, refseq_acc VARCHAR(100), PRIMARY KEY (refseq_acc)
)CHARSET=utf8;
```

```
CREATE TABLE IF NOT EXISTS cognames
(
	COG_id VARCHAR(30),
	fun_class VARCHAR(5),
	COG_annotate VARCHAR(500),
	PRIMARY KEY (COG_id)
)CHARSET=utf8;
```

```
CREATE TABLE IF NOT EXISTS coglist
( 
	domain_id INT,
	genome VARCHAR(200),
	prot_id INT,
	prot_len INT,
	domain_start INT,
	domain_end INT,
	COG_id VARCHAR(30),
	membership_class INT,
	FOREIGN KEY (prot_id) REFERENCES prot_refseq(prot_id),
	
	FOREIGN KEY (COG_id) REFERENCES cognames(COG_id)
)  CHARSET=utf8;
```

```    
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/input/reads_assignment_megan/DS2_1_taxa_path.csv' 
	INTO TABLE DS2_1_reads_taxapath_megan
	COLUMNS TERMINATED BY '\t';  
```  

```
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/input/reads_assignment_megan/DS2_2_taxa_path.csv' 
	INTO TABLE DS2_2_reads_taxapath_megan
	COLUMNS TERMINATED BY '\t';	
```

```	
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/input/reads_assignment_megan/ICC_taxa_path.csv' 
	INTO TABLE ICC_reads_taxapath_megan
	COLUMNS TERMINATED BY '\t';	
```

```
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/db_source/gi_taxid_nucl.dmp'
	INTO TABLE gi_taxaid
	COLUMNS TERMINATED BY '\t';	
```

```
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/db_source/names.dmp'
	INTO TABLE taxa_id_name
	COLUMNS TERMINATED BY '|';
```

```
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/db_source/prot2003-2014.tab' 
	INTO TABLE prot_refseq 
	COLUMNS TERMINATED BY '\t' ;
```

```	
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/db_source/cognames2003-2014.tab'   
	INTO TABLE cognames 
	COLUMNS TERMINATED BY '\t' ;
```

```
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/db_source/cog2003-2014.csv'   
	INTO TABLE coglist
	COLUMNS TERMINATED BY ',' ;
```

```
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/output/Mar072016/ICW_bl_readsassigned.txt' 
	INTO TABLE DS2_1_reads_taxa_megan
	COLUMNS TERMINATED BY '\t'; 
```

```
LOAD DATA LOCAL INFILE '/isi/olga/xin/Halophile_project/output/20160413/DS2_1_assignment_new.csv' 
	INTO TABLE DS2_1_reads_taxa_megan
	COLUMNS TERMINATED BY ','; 
```


```
SELECT reads_name, sequence FROM ICC_trimmed_merged_fa 
	WHERE SUBSTRING(reads_name, 2) 
	IN (SELECT reads_name FROM ICC_reads_taxapath_megan WHERE taxapath LIKE '%Halorubrum;%');
```

```
SELECT * FROM DS2_1_reads_taxapath_megan 
WHERE taxapath LIKE '%Halostagnicola;%';
```

```
SELECT COUNT(*) FROM DS2_1_reads_taxapath_megan 
WHERE taxapath LIKE '%Halonotius sp. J07HN6;%';
```

```	
SELECT t.* FROM gi_taxaid g INNER JOIN taxa_id_name t ON g.taxaid = t.tax_id 
WHERE g.gi = 374428416 AND t.name_class LIKE '%scientific name%';  
```

```
SELECT cn.fun_class FROM cognames cn INNER JOIN coglist cl ON cn.COG_id = cl.COG_id 
INNER JOIN prot_refseq p ON cl.prot_id = p.prot_id 
WHERE p.refseq_acc ='YP_008376373';
```

```
SELECT cn.* FROM cognames cn INNER JOIN coglist cl ON cn.COG_id = cl.COG_id 
WHERE cl.prot_id ='313672230';
```

```
SELECT COUNT(*) 
FROM ICC_umapped_to_DS2_2 AS t1 
CROSS JOIN ICC_read_SEEDS_path_megan AS t2 ON SUBSTRING(t1.reads_name, 2) = t2.reads_name;  
```

``` 
DELETE FROM DS2_2_reads_taxapath_megan WHERE taxapath LIKE '%Not assigned%';
DELETE FROM DS2_2_reads_taxapath_megan WHERE taxapath LIKE '%unclassified sequences%';

DELETE FROM DS2_1_reads_taxa WHERE taxa LIKE '%Not assigned%';
DELETE FROM DS2_1_reads_taxa WHERE taxa LIKE '%unclassified sequences%';
```


sql = 'DROP TABLE  xchen_projects.DS2_1_reads_taxa_megan;'

cursor.execute(sql)

