from pymysql import connect, err, sys, cursors
import pandas as pd
import csv
def main():
    outputdir = '/Users/Xin/Desktop/IC_project/output/Jan282016/ICC_virus_assignment.csv'
    outputfile = open(outputdir, 'w')
    conn = connect(host = '', 
               port = 3306,
               user = 'xchen',
               passwd = '008');
      
    cursor = conn.cursor( cursors.DictCursor );
#     sql = 'CREATE DATABASE IF NOT EXISTS rpoB_reads_assignment'
#     cursor.execute(sql)
    #sql = 'USE rpoB_reads_assignment'
    #cursor.execute(sql)
    #sql = 'SELECT reads_name, sequence FROM reads_trimmed_merged.DS2_1_trimmed_merged_fa WHERE id < 100 AND SUBSTRING(reads_name, 2) NOT IN (SELECT reads_name from reads_assignment.DS2_1_assignment);'
    inputdir1 = '/Users/Xin/Desktop/IC_project/output/Jan282016/ICC_virus_count.csv'
    with open(inputdir1, 'r') as inputfile:
        f = csv.DictReader(inputfile, delimiter =",", fieldnames=['taxa','count'])
        for row in f:
            taxa = row['taxa']
            sql = 'SELECT reads_name, taxa FROM reads_assignment.ICC_assignment WHERE taxa =' + "'" + taxa + "';"
            cursor.execute(sql)
            data = cursor.fetchall()
            if not data:
                sql = 'SELECT reads_name, taxa FROM reads_assignment.ICC_assignment WHERE taxa LIKE' + "'%" + taxa + "%';"
                cursor.execute(sql)
                data = cursor.fetchall()
            df = pd.DataFrame(data)
            for i in range(0, len(df['reads_name'])):
                print(df['reads_name'][i]+ "," + df['taxa'][i], file = outputfile, end = '\n')
 
        cursor.close()
        conn.close()
#     for line in data:
#         print(line)
#       print(line, file = outputfile, end = '')
 
if __name__ == "__main__": main() 