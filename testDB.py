import dataBaseStuff


# we'll save this one for the next tests
test_api_data_entry = [{"id": "tttestdata", "rank": "10002", "title": "Comp490 Project 1 Show",
                        "fullTitle": "Comp490 Project 1 Show (2022)", "year": "2022", "image": "",
                        "crew": "Prof. Santore and many hardworking students", "imDbRating": "9.2",
                        "imDbRatingCount": "41"}]


# test here actually showed me a hidden error in my database
def test_enter_data():
    # I should really do some of this in a fixture, but I wanted to do it with just what you already have
    # the database needs to be deleted everytime to make this test run, which is good for github actions
    test_data_entry = [("tttestdata", 10002, "Comp490 Project 1 Show", "Comp490 Project 1 Show (2022)", 2022,
                        "", "Prof. Santore and many hardworking students", 9.2, 41)]

    connection, db_cursor = dataBaseStuff.open_db("testDatabase.sqlite")
    dataBaseStuff.create_top250_table(db_cursor)
    dataBaseStuff.put_top_250_in_database(test_data_entry, db_cursor)
    connection.commit()
    # this test in the next four lines wasn't technically required, but I wanted to demo the count feature
    # and it is a good idea. I could test by checking the len of record_count_set also
    db_cursor.execute("SELECT COUNT() FROM top_show_data WHERE ttid = 'tttestdata'")
    record_count_set = db_cursor.fetchone()
    number_of_records = record_count_set[0]  # the count returns a tuple, the count is the first element
    assert number_of_records == 1
    db_cursor.execute("SELECT * FROM top_show_data WHERE ttid = 'tttestdata'")
    record_set = db_cursor.fetchall()
    assert record_set[0] == test_data_entry[0]