import argparse
import mysql.connector

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print (args.accumulate(args.integers))


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nikita_test",
  passwd="nikita_test"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO nikita_test_1.new_table (name) values ('NIKITA') ")
mydb.commit()