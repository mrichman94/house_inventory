import requests
from xml.etree import ElementTree


def read_isbndb(isbn):
    # isbn = "9780321762184"
    isbn = str(isbn)
    url = "http://isbndb.com/api/books.xml?access_key=T4TGN01Y&index1=isbn&value1=" + isbn
    response = requests.get(url)
    try:
        tree = ElementTree.fromstring(response.content)
    except Exception:
        return [None, None, None, None]
    returndata = []

    try:
        return_isbn = tree[0][0].attrib['isbn13']
    except IndexError:
        return_isbn = None
    finally:
        returndata.append(return_isbn)

    try:
        return_title = tree[0][0][0].text
    except IndexError:
        return_title = None
    finally:
        returndata.append(return_title)

    try:
        return_authors = tree[0][0][2].text
    except IndexError:
        return_authors = None
    finally:
        returndata.append(return_authors)

    try:
        return_publishers = tree[0][0][3].text
    except IndexError:
        return_publishers = None
    finally:
        returndata.append(return_publishers)

    return returndata  # return_isbn, return_title, return_authors, return_publishers

# print(read_isbndb(9780752265629)[1])
