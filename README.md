# Library Management Software

A command-line library system written in Python, with separate menus for students, faculty and
the librarian. Book records, logins and book requests are kept in plain CSV and text files.

## Features

**Students and faculty**
- View the book list
- Borrow and return books
- Request a book the library does not have (students)

**Librarian**
- View the full catalogue, including who has borrowed each book

## Data files

| File | Contents |
|---|---|
| `books.csv` | Catalogue: serial number, title, due date, cost and borrower ID |
| `logins.csv` | Login IDs and passwords |
| `requests.txt` | The latest book request |

## Running

Requires Python 3 on Windows (the menus use `msvcrt` and `cls`).

```bash
git clone https://github.com/aditya-lawankar/Library-Management-Software.git
cd Library-Management-Software
python library.py
```

Sample login IDs and passwords are in `logins.csv`.

## License

MIT
