# Pagination Project

This project demonstrates various pagination techniques in Python using a dataset of popular baby names. The project is divided into four main tasks, each focusing on a specific aspect of pagination.

## Directory Layout

0x00-pagination/
├── 0-simple_helper_function.py
├── 1-simple_pagination.py
├── 2-hypermedia_pagination.py
├── 3-hypermedia_del_pagination.py
├── Popular_Baby_Names.csv
├── README.md
├── __init__.py
└── tests/
    ├── 0-main.py
    ├── 1-main.py
    ├── 2-main.py
    └── 3-main.py


## Tasks

### Task 0: Simple Helper Function

A helper function `index_range` that calculates the start and end index for pagination.

### Task 1: Simple Pagination

A `Server` class that reads the `Popular_Baby_Names.csv` file and implements a method `get_page` to fetch a specific page of data.

### Task 2: Hypermedia Pagination

Extends the `Server` class to include a method `get_hyper` that provides pagination metadata along with the data.

### Task 3: Deletion-Resilient Hypermedia Pagination

Extends the `Server` class to handle pagination in a deletion-resilient manner using an indexed dataset.

## Setup

Place the `Popular_Baby_Names.csv` file in the same directory as the script files.

## Author

- Esianyo Dzisenu
