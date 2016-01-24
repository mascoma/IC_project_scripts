from pymysql import connect, err, sys, cursors
import pandas as pd
def main():
    outputdir = '/Users/Xin/Desktop/IC_project/output/Jan202016/ICC_DS2_1_unmapped_taxa.csv'
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
    sql = 'SELECT reads_name, taxa FROM reads_assignment.ICC_assignment WHERE reads_name IN (SELECT SUBSTRING(reads_name,2) FROM DS2_ICC_comparison.ICC_DS2_1_unmapped_fa);'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
#     for line in data:
#         print(line)
#       print(line, file = outputfile, end = '')
    df = pd.DataFrame(data)
    for i in range(0, len(df['reads_name'])):
        print(df['reads_name'][i]+ "," + df['taxa'][i], file = outputfile, end = '\n')
if __name__ == "__main__": main() 