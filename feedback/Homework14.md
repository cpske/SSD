Why Do You Write Such Poor Code?

## Hardcode URL of database in Factory

*Almost everyone!*

## Misleading Name for DAO Factory

Typical name would be `DaoFactory` or similar.

- Bhoken `JasmineRiceSaleDb` - it is **not** a database
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

## Naive DAO Accessor Methods create a new DAO instance each time called

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


## DaoFactory is Singleton and Creates Only ONE Instance of Each DAO

This is what you should do.

- Chayayot
- Krasin
- Panitan
- Peerasu


## Misleading Names for DAO-accessor methods in Factory

Accessors should be named `get_customer_dao()`, `get_songs_dao()`, etc.

Looks like these people just **copied** bad code from each other.

- Bhoken: Customer, JasmineRiceSale
- Chanunya: artists, songs
- Chatcharawin: gpu, warehouse
- Chonchanok: `market_list`, `item_list`
- Jakarin: customer, laptop
- Krittamate: athlete, country
- Kul: buyer, moto
- Nabhan: `get_users`, `get_bicycle`
- Pakapop `user`, `booking`
- Panu `character`, `weapon`
- Pattanan `brand`, `ads`
- Phakarat `episodes`, `rating`



## Looks Like Bad Design & Poor Code Copied from Each Other

- Same package names ("model", "util") 
- Same stupid naming of DAO accessors (see above)
- same "model" suffix appended to class names (not descriptive)
- same stupid naming of DAO factory
- same hardcoding of database URL in factory class

- Chanunya, Chatcharawin, Chonchanok, Jakarin, Krittamate, Kul, Pakapop, Panu, Pattanan, Phakarat



Example of Bad Code (this is the DAO factory, **not** a "DB"):
```python
class LaptopDB:           ## This is a Dao Factory, NOT a database ("DB")

    def __init__(self):
        engine = create_engine('sqlite:///laptop_store.db', echo=True)
        session = sessionmaker(bind=engine)
        self.__session = session()

    def customer(self):  ## Really poor name for DAO accessor 
        return CustomerDao(self.__session)
                         ## Stupid code returns new DAO each time
```

Everyone listed above wrote nearly identically-naive code.




