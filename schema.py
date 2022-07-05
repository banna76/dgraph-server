from array import array
import typing
import strawberry

@strawberry.type
class Book:
    title: str
    description: str
    price: float
    thumbnail: str
    currency: str
    author: 'Author'
    
@strawberry.type
class Author:
  firstName: str
  lastName: str
  thumbnail: str

@strawberry.type
class OrderBook:
  title: str
  price: float

@strawberry.input
class AuthorInput:
  firstName: str
  lastName: str

@strawberry.input
class OrderBookInput:
  title: str
  price: float

@strawberry.input
class AddBookInput:
    title: str
    description: str
    price: float
    thumbnail: str
    currency: str
    author: AuthorInput

orders: list[OrderBook] = []
books: list[Book] = []
authors: list[Author] = []

async def get_books(self) -> list[Book]:
    return [
        Book(
        title = 'Remarkably Bright Creatures: A Novel',
        description = 'Remarkably Bright Creatures is a beautiful examination of how loneliness can be transformed, cracked open, with the slightest touch from another living thing.',
        price = 17.76,
        thumbnail ='assets/img/remarkably.jpg',
        currency =  '€',
            author = Author (
                firstName ="Shelby Van",
                lastName = "Pelt",
                thumbnail = 'assets/img/shelby_van_pelt.jpg',
            )
        ),
        Book(
            title = 'What My Bones Know: A Memoir of Healing from Complex Trauma',
            description= 'A searing memoir of reckoning and healing by acclaimed journalist Stephanie Foo, investigating the little-understood science behind complex PTSD and how it has shaped her life.',
            price= 18.76,
            thumbnail='assets/img/whatMyBonesKnow.jpg',
            currency=  '€',
            author= Author (
                firstName="Stephanie",
                lastName="Foo",
                thumbnail='assets/img/stephanie_foo.jpg',
            )
        ),
        Book(
            title = 'All My Rage: A Novel',
            description= 'An INSTANT NEW YORK TIMES BESTSELLER!An INSTANT INDIE BESTSELLER!"All My Rage is a love story, a tragedy and an infectious teenage fever dream about what home means when you feel you don’t fit in." — New York Times Book Review',
            price= 12.93,
            thumbnail='assets/img/AllMyRage.jpg',
            currency=  '€',
            author= Author (
                firstName="Sabaa",
                lastName="Tahir",
                thumbnail='assets/img/sabaa_tahir.jpg',
            )
        ),
        Book(
            title = 'River of the Gods: Genius, Courage, and Betrayal in the Search for the Source of the Nile',
            description= 'NEW YORK TIMES BESTSELLER • The harrowing story of one of the great feats of exploration of all time and its complicated legacy—from the New York Times bestselling author of The River of Doubt and Destiny of the Republic.',
            price= 19.50,
            thumbnail='assets/img/RiverOfTheGods.jpg',
            currency=  '€',
            author= Author (
                firstName="Candice",
                lastName="Millard",
                thumbnail='assets/img/candice_millard.jpg',
            )
        ),
        Book(
            title = 'The Maid: A Novel ',
            description= '#1 NEW YORK TIMES BESTSELLER • GOOD MORNING AMERICA BOOK CLUB PICK • “A heartwarming mystery with a lovable oddball at its center” (Real Simple), this cozy whodunit introduces a one-of-a-kind heroine who will steal your heart.',
            price= 16.04,
            thumbnail='assets/img/TheMaidANovel.jpg',
            currency=  '€',
            author= Author (
                firstName="Nita",
                lastName="Prose",
                thumbnail='assets/img/nita_prose.jpg',
            )  
        )
    ]

async def get_authors(self):
    return [
        Author (
            firstName ="Shelby Van",
            lastName = "Pelt",
            thumbnail = 'assets/img/shelby_van_pelt.jpg',
        ),
        Author(
                firstName="Stephanie",
                lastName="Foo",
                thumbnail='assets/img/stephanie_foo.jpg',
        ),
        Author(
            firstName="Sabaa",
            lastName="Tahir",
            thumbnail='assets/img/sabaa_tahir.jpg',
        ),
        Author(
            firstName="Candice",
            lastName="Millard",
            thumbnail='assets/img/candice_millard.jpg',
        ),
        Author(
            firstName="Nita",
            lastName="Prose",
            thumbnail='assets/img/nita_prose.jpg',
        )]

async def get_orders(self) -> list[OrderBook]:
    return orders

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    authors: typing.List[Author] = strawberry.field(resolver=get_authors)
    orders: typing.List[OrderBook] = strawberry.field(resolver=get_orders)

@strawberry.type
class Mutation:
  
  @strawberry.mutation
  async def order_book(self, orderbook: OrderBookInput) -> OrderBook:
    orders.append(orderbook)
    return orderbook

  @strawberry.mutation
  async def add_book(self, book: AddBookInput) -> Book:
    books.append(book)
    return book

  @strawberry.mutation
  async def add_author(self, author: AuthorInput) -> Author:
    authors.append(author)
    return author

schema = strawberry.Schema(query=Query,mutation=Mutation)