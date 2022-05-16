# Feedback on Homework 14

## Hardcode URL of Database in Factory as String

*Almost everyone!*

```python
    def __init__(self):
        engine = create_engine('sqlite:///laptop_store.db', echo=True)
        session = sessionmaker(bind=engine)
        self.__session = session()
```

## Misleading Name for DAO Factory

A descriptive name would be `DaoFactory`, `PersistenceService`, or similar.

These people used the following poor, non-descriptive names for the DAO Factory:

- Bhoken `JasmineRiceSaleDb` - this class is **not** a database
- Chanunya `ArtistSongDao` - this class is **Not** a DAO
- Chatcharawin `WarehouseGPU`
- Krittamate `SportFair`
- Kul `Moto`
- Nabhan `SessionDB`
- Pakapop `FlightBookingDb`
- Panitan `Footballer`
- Panu `Eldenring`
- Pattanan `Brands`
- Peerasu `CoffeeShop` (only thing it does is create DAOs)
- Phakarat `GameOfThronesDB`
- Poomtoom `ShowsDB`
- Raweerat `GroceryStore`
- Sirapop `Genshin`
- Siratee `LottoDB`
- Sirawich `UsCitizen`
- Soravit `CompanyInfo`
- Tanin `CrateDB`
- Tawan `PetCare`
- Thanathip `CarRental`


## Naive DAO Accessor Methods create a new DAO instance each time called

In DAO Factory class there is code like:
```python
class ArtistSongDao:                          # this class is a Factory, NOT a DAO

    def artists(self):
        return ArtistDao(self.__db_session)   # creates new DAO each time

    def songs(self):
        return SongsDao(self.__db_session)    # creates new DAO each time
```

- Bhoken
- Chanunya
- Chatcharain
- Chonchanok
- Jakarin
- Krittamate
- Kul
- Nabhan
- Pakapop
- Panu
- Panuwat
- Pattanan
- Phakarat
- Raweerat
- Siratee
- Sirawich
- Soravit
- Tanin
- Tawan
- Thanathip


## DaoFactory is Singleton and Creates Only ONE Instance of Each DAO

This is what you **should do**. These students did it:

- Chayayot
- Krasin
- Panitan
- Peerasu
- Phawit (creates only 1 instance of each DAO, but Factory not Singleton)
- Pontakorn (creates only 1 instance of each DAO, but Factory not Singleton) 

In Python, you can define a *metaclass* to force classes to be Singletons,
as Chayayot and Krasin did:

```python
class Singleton(type):
    """Maintain a map of class names to instances so that only one instance is created."""
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MovieDatabase(metaclass=Singleton):

    def __init__(self, ...):
        self.__movie_dao = None
        self.__db_session = ...

    def get_movie_dao(self):
        if self.__movie_dao is None:
            self.__movie_dao = MovieDao(session=self.__db_session)
        return self.__movie_dao
```

He could have applied the Singleton to MovieDao as well, and then he would 
not need to keep track of the dao instance (MovieDao would automatically be a Singleton):

```
class MovieDao(metaclass=Singleton):
```


## Misleading Names for DAO accessor methods in Factory

Accessors should be named `get_customer_dao()`, `get_songs_dao()`, etc.

Looks like these people just **copied** bad code from each other.

Do these names tell you *anything* about what the method actually does?

| Student   | DAO Accessor Method Names        |
|-----------|----------------------------------|
| Bhoken    |  customer, `jasmine_cice_sale`   |
| Chanunya  |  artists, songs                  |
| Chatcharawin  |  gpu, warehouse              |
| Chonchanok  |  `market_list`, `item_list`    |
| Jakarin  |  customer, laptop                 |
| Krittamate  |  athlete, country              |
| Kul  |  buyer, moto                          |
| Nabhan  |  `get_users`, `get_bicycle`        |
| Pakapop  | `user`, `booking`                 |
| Panu  | `character`, `weapon`                |
| Pattanan  | `brand`, `ads`                   |
| Phakarat  | `episodes`, `rating`             |
| Poomtoom  | `staffs`, `shows`                |
| Raweerat  | `product`, `customer`            |
| Siratee  | `user`, `lotto`                   |
| Sirawich  | `citizen`, `state`               |
| Soravit  | `employee`, `salary`              |
| Tanin  | `get_car`, `get_customer`           |
| Tawan  | `pet`, `customer`                   |
| Thanathip  | `user`, `car`                   |


## Looks Like Same Bad Design & Poor Code Copied from Each Other

- Same package names ("model", "utils", "utils/dao") 
- Same poor naming of DAO accessor methods (see above). Names are so bad, I can't believe everyone would do this independently.
- many have "model" suffix appended to class names (not descriptive).  
  - In POS, do we have "SaleModel", "LineItemModel", ProductModel"?  Of course not.
- same nondescriptive naming of DAO factory class (see above)
- hardcoding of database URL in factory class. Assignment said to use Protected Variations.

Looks like copies of same poor design and poor code:
- Chanunya
- Chatcharawin
- Chonchanok
- Jakarin
- Krittamate
- Kul
- Pakapop
- Panu
- Pattanan
- Phakarat
- Raweerat
- Siratee
- Sirawich
- Soravit
- Tanin
- Tawan
- Thanathip

Example of Poor Code (this is the DAO factory, **not** a "DB"):
```python
class LaptopDB:           ## This is a Dao Factory, NOT a database ("DB")

    def __init__(self):
        engine = create_engine('sqlite:///laptop_store.db', echo=True)
        session = sessionmaker(bind=engine)
        self.__session = session()

    def customer(self):  ## Really poor name for DAO accessor 
        return CustomerDao(self.__session)
                         ## Naive code returns new DAO each time
```

Everyone listed above wrote nearly identically-naive code.

