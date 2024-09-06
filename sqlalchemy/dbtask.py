from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql import func

DATABASE_URL = "postgresql+psycopg2://postgres:QwErT131096@localhost/sklad"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    EmployeeID = Column(Integer, primary_key=True)
    LastName = Column(String)
    FirstName = Column(String)
    MiddleName = Column(String)
    Position = Column(String)
    Address = Column(String)
    HomePhone = Column(String)
    BirthDate = Column(Date)

class Client(Base):
    __tablename__ = 'clients'
    ClientID = Column(Integer, primary_key=True)
    FullName = Column(String)
    Address = Column(String)
    Phone = Column(String)

class Supplier(Base):
    __tablename__ = 'suppliers'
    SupplierID = Column(Integer, primary_key=True)
    SupplierName = Column(String)
    SupplierRep = Column(String)
    ContactPhone = Column(String)
    Address = Column(String)

class Product(Base):
    __tablename__ = 'products'
    ProductID = Column(Integer, primary_key=True)
    SupplyID = Column(Integer, ForeignKey('supplies.SupplyID'))
    ProductName = Column(String)
    TechnicalSpecs = Column(String)
    Description = Column(String)
    Image = Column(String)
    PurchasePrice = Column(Float)
    InStock = Column(Integer)
    Quantity = Column(Integer)
    SalePrice = Column(Float)

class Order(Base):
    __tablename__ = 'orders'
    OrderID = Column(Integer, primary_key=True)
    EmployeeID = Column(Integer, ForeignKey('employees.EmployeeID'))
    ProductID = Column(Integer, ForeignKey('products.ProductID'))
    PlacementDate = Column(Date)
    CompletionDate = Column(Date)
    ClientID = Column(Integer, ForeignKey('clients.ClientID'))

class Supply(Base):
    __tablename__ = 'supplies'
    SupplyID = Column(Integer, primary_key=True)
    SupplierID = Column(Integer, ForeignKey('suppliers.SupplierID'))
    SupplyDate = Column(Date)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employees = [
    Employee(LastName='Ivanov', FirstName='Ivan', MiddleName='Demianovich', Position='Head Manager', Address='Moscow', HomePhone='+7973435454', BirthDate='1990-01-01'),
    Employee(LastName='Petrov', FirstName='Daniil', MiddleName='Innokentievich', Position='Service Manager', Address='Skolkovo', HomePhone='+7987654321', BirthDate='1992-05-15'),
    Employee(LastName='Stupka', FirstName='Bogdan', MiddleName='Tikhonovich', Position='PR Manager', Address='Kommunarka', HomePhone='+7968148842', BirthDate='1985-02-10'),
    Employee(LastName='Zukerman', FirstName='Ishmael', MiddleName='Ionovich', Position='Finance Director', Address='Moscow', HomePhone='+7939133710', BirthDate='1969-07-25'),
    Employee(LastName='Malyaev', FirstName='Salamat', MiddleName='Ilgizovich', Position='Warehouse keeper', Address='Moscow', HomePhone='+7999505143', BirthDate='1993-05-17'),
]

clients = [
    Client(FullName='Sidorov S.S.', Address='Kazan', Phone='+79999991123'),
    Client(FullName='Kuznetsov K.K.', Address='Nizhny Novgorod', Phone='+79314234234'),
    Client(FullName='Zubrov V.S.', Address='Krasnoyarsk', Phone='88005553535'),
    Client(FullName='Volgin Y.D.', Address='Moscow', Phone='+79834031022'),
    Client(FullName='Daniliuk A.A.', Address='Vladivostok', Phone='+79991234554'),
]

suppliers = [
    Supplier(SupplierName='Zaloopka and Co', SupplierRep='Andreev A.A.', ContactPhone='1112223333', Address='Moscow'),
    Supplier(SupplierName='Daipo Eba Lou', SupplierRep='Hyosaki M.', ContactPhone='14881337228', Address='Tokyo'),
    # Add 3 more suppliers
]

products = [
    Product(SupplyID=1, ProductName='Product1', TechnicalSpecs='Specs1', Description='Description1', Image='image1.png', PurchasePrice=100.50, InStock=10, Quantity=5, SalePrice=150.75),
    Product(SupplyID=2, ProductName='Product2', TechnicalSpecs='Specs2', Description='Description2', Image='image2.png', PurchasePrice=200.75, InStock=20, Quantity=10, SalePrice=250.00),
    # Add 3 more products
]

session.add_all(employees + clients + suppliers + products)
session.commit()

results = session.query(Order, Client, Product).join(Client, Order.ClientID == Client.ClientID).join(Product, Order.ProductID == Product.ProductID).all()
for result in results:
    print(result)

session.query(Client).filter(Client.ClientID == 1).update({Client.Address: 'Updated Address'})
session.commit()

filtered_clients = session.query(Client).filter(Client.Address == 'Kazan').order_by(Client.FullName).all()
for client in filtered_clients:
    print(client)

avg_cost = session.query(func.avg(Product.SalePrice)).scalar()
print(f'Average product sale price: {avg_cost}')

session.query(Supplier).filter(Supplier.SupplierID <= 2).delete()
session.commit()

remaining_suppliers = session.query(Supplier).all()
for supplier in remaining_suppliers:
    print(supplier)
