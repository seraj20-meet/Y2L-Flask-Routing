from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price,picture_link,desc)
Product_object = Product(
	name=name,
	price= price,
	picture_link= picture_link,
	desc=description)
	session.add(product_object)
	session.commit()

def delete_product(their_name):
   """
   Delete all students with a
   certain name from the database.
   """
   session.query().filter_by(
       name=their_name).first().delete()
   session.commit()

def update_lab_status(name, price,picture_link,desc):
   """
   Update a student in the database, with
   whether or not they have finished the lab
   """
   product = session.query(Product).filter_by(
       name=name).first()
   product.name = name
   prodict.price= price
   prod.pic_link = picture_link
   prod.dexc = desc

   session.commit()


def query_all():
   """
   Print all the students
   in the database.
   """
   Productssss = session.query(
      Product).all()
   return Products


print(query_all())

def query_by_name(their_name):
   """
   Find the first student
   in the database, by their name
   """
   Product1 = session.query(
       Product).filter_by(
       name=their_name).first()
   return Product1

