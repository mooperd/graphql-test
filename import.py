import csv # give python csv superpowers

with open(r"uk-towns-sample.csv") as csvfile:
    reader = csv.DictReader(csvfile)

from sqlalchemy import Integer, Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Country is currently the "parent" of everything. It is the "root".
class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class County(Base):
    __tablename__ = 'county'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # We define the relationship between Country and County here.
    country = relation("Country", backref="country")
    country_id = Column(Integer, ForeignKey('country.id'))

# Town is a child of County
class Town(Base):
    __tablename__ = 'town'
    id = Column(Integer, primary_key=True)
    county = Column(String)
    country_name = Column(String)
    name = Column(String)
    grid_reference = Column(String)
    easting = Column(Integer)
    northing = Column(Integer)
    latitude = Column(String)
    longitude = Column(String)
    elevation = Column(Integer)
    postcode_sector = Column(String)
    local_government_area = Column(String)
    nuts_region = Column(String)
    town_type = Column(String)
    # We define the relationship between Country and County here.
    county = relation("County", backref="county")
    county_id = Column(Integer, ForeignKey('county.id'))


# A bunch of stuff to make the connection to the database work.
def dbconnect():
    engine = create_engine('postgres://postgres:postgrespassword@localhost:5432/postgres')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


''' Above here defines the DB'''
''' Below here adds data to the DB '''

def addTown(session, town_input):
    # Try and get the Country from the database. If error (Except) add to the database.
    try: 
        county = session.query(County).filter(County.name == town_input["county"]).one()
    except:
        try:
            country = session.query(Country).filter(Country.name == town_input["country"]).one()
        except:
            country = Country()
            country.name = town_input["country"]
        county = County()
        county.name = town_input["county"]
        county.country = country
        session.add(county)

    town = Town()
    # Add attributes
    town.name = town_input["name"]
    town.grid_reference = town_input["grid_reference"]
    town.easting = town_input["easting"]
    town.northing = town_input["northing"]
    town.latitude = town_input["latitude"]
    town.longitude = town_input["longitude"]
    town.elevation = town_input["elevation"]
    town.postcode_sector = town_input["postcode_sector"]
    town.local_government_area = town_input["local_government_area"]
    town.nuts_region = town_input["nuts_region"]
    town.town_type = town_input["town_type"]
    # add the country (parent) to the town (child)
    town.county = county
    session.add(town)
    session.commit()


with open(r"uk-towns-sample.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    session = dbconnect()
    for i in reader:
        addTown(session, i)