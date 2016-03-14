from pymysql import connect, err, sys, cursors
import pandas as pd
def main():
    outputdir = '/isi/olga/xin/Halophile_project/output/Feb152016/ICC_Haloarcula.fa'
    outputfile = open(outputdir, 'w')
    conn = connect(host = 'localhost', 
              
               user = 'xchen',
               passwd = 'f0029mc');
      
    cursor = conn.cursor( cursors.DictCursor );
#     sql = 'CREATE DATABASE IF NOT EXISTS rpoB_reads_assignment'
#     cursor.execute(sql)
    sql = 'USE xchen_projects'
    cursor.execute(sql)
    #sql = 'SELECT reads_name, sequence FROM reads_trimmed_merged.DS2_1_trimmed_merged_fa WHERE id < 100 AND SUBSTRING(reads_name, 2) NOT IN (SELECT reads_name from reads_assignment.DS2_1_assignment);'
    sql = 'SELECT reads_name, sequence FROM ICC_trimmed_merged_fa WHERE SUBSTRING(reads_name, 2) IN (SELECT reads_name FROM ICC_reads_taxapath_megan WHERE taxapath LIKE '+"'%" + 'Haloarcula;'+ "%'" +');'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
#     for line in data:
#         print(line)
#       print(line, file = outputfile, end = '')
    print("almost done!")
    df = pd.DataFrame(data)
    for i in range(0, len(df['reads_name'])):
        print >> outputfile, df['reads_name'][i]+ '\t' + df['sequence'][i]
if __name__ == "__main__": main() 
