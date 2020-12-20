# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3
#from itemadapter import ItemAdapter


class HospitaldetailsPipeline:
    
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("hospital.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS h_list_tb""")
        self.curr.execute(""" create table h_list_tb(
                    name text,
                    location text,
                    no_of_beds text,
                    hospital_type text
                    )""")
        
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    
    def store_db(self, item):
        self.curr.execute("""insert into h_list_tb values(?,?,?,?)""",
                          (
                             str(item['name']),
                             str(item['location']),
                             str(item['no_of_beds']),
                             str(item['hospital_type'])
                              ))
        self.conn.commit()
    
    
