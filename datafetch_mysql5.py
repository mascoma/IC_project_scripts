from pymysql import connect, err, sys, cursors
import pandas as pd
def main():
    outputdir = '/isi/olga/xin/Halophile_project/output/Feb262016/DS2_1_ua_bowtie_assigned.txt'
    outputfile = open(outputdir, 'w')
    inputdir = '/isi/olga/xin/Halophile_project/output/Feb252016/DS2_1_ua_mapped.txt'
    df = pd.read_table(inputdir, header = None, names=['reads','gi','ref'], delimiter=" ")
    conn = connect(host = 'localhost', 
               user = 'xchen',
               passwd = 'f0029mc');
      
    cursor = conn.cursor( cursors.DictCursor );
#     sql = 'CREATE DATABASE IF NOT EXISTS rpoB_reads_assignment'
#     cursor.execute(sql)
    sql = 'USE xchen_general'
    cursor.execute(sql)
    #sql = 'SELECT reads_name, sequence FROM reads_trimmed_merged.DS2_1_trimmed_merged_fa WHERE id < 100 AND SUBSTRING(reads_name, 2) NOT IN (SELECT reads_name from reads_assignment.DS2_1_assignment);'
    for a in range(len(df['gi'])):
    	sql = 'SELECT t.* FROM gi_taxaid g INNER JOIN taxa_id_name t ON g.taxaid = t.tax_id WHERE g.gi = ' + str(df['gi'][a]) + ' AND t.name_class LIKE '+ "'" + '%scientific name%' +"';"
    	cursor.execute(sql)
    	data = cursor.fetchall()
	if data:
    		print >> outputfile, str(df['reads'][a]) +'\t' +str(df['gi'][a]) +data[0]["name_txt"]+data[0]["unique_name"]+str(data[0]["tax_id"])
  	else:
		print >> outputfile, str(df['reads'][a]) +'\t' +str(df['gi'][a]) + '\t' + '\t' + '\t '
        print(str(a))
    cursor.close()
    conn.close()
if __name__ == "__main__": main() 
