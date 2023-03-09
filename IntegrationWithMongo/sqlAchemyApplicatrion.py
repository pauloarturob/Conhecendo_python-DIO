import sqlalchemy as sqlA
from sqlalchemy import Column, inspect, select
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__: str = "User_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(45), nullable=False)
    user_id = Column(Integer, ForeignKey("User_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email={self.email})"


print(User.__tablename__)
print(Address.__tablename__)

# Conexão bando de dados
engine = create_engine("sqlite://")

# Criando as classes com tabelas no banco de dados
Base.metadata.create_all(engine)

# investiga o bando de dados
insp = inspect(engine)

print(insp.has_table("User_account"))

print(insp.get_table_names())
print(insp.default_schema_name)

with Session(engine) as session:
    Paulo = User(
        name='Paulo',
        fullname='Artur',
        address=[Address(email='pauloarturob@gmail.com')]
    )

    Stefanie = User(
        name='Stefanie',
        fullname='Artur',
        address=[Address(email='stefaniesdsa@gmail.com'),
                 Address(email='teteartur@gmail.com')]
    )
    # enviando para o banco de dados BD
    session.add_all([Paulo, Stefanie])

    session.commit()

stmt = select(User).where(User.name.in_(['Paulo', 'Stefanie']))
print('Recuperando usuarios a partir de condição de filtragem')
for user in session.scalars(stmt):
    print(user)

stmt1 = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando endereços de email de Stenfanie')
for address in session.scalars(stmt1):
    print(address)
