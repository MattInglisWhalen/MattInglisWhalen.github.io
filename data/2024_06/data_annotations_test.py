from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

def read_url_contents(url):
    """
    Takes a url, e.g. https://www.google.com, and reads html content into a list of
    tuples of the form (int, char, int).

    If the url does not exist, or the contents of the html do not match the expected
    for, then an error is thrown
    """
    x_char_ys = []

    try:
        with urlopen(url) as fp:
            data_bytes = fp.read()
            data_str = data_bytes.decode("utf8")
    except URLError as e:
        print(f"Could not find data at {url}")
        raise

    soup = BeautifulSoup(data_str, features='html.parser')

    data_tags = soup.body.find_all('td', attrs={'colspan': '1', 'rowspan': '1'})
    if len(data_tags) < 1 or len(data_tags) % 3 != 0:
        print(f"Content of {url} does not match expected row pattern with {data_tags=}")
        print(soup)
        raise ValueError

    for idatum in range(len(data_tags) // 3):

        if idatum == 0 :
            # first row is just column headers
            continue

        x_char_ys.append((
            int(data_tags[idatum * 3 + 0].get_text()),
            data_tags[idatum * 3 + 1].get_text(),
            int(data_tags[idatum * 3 + 2].get_text())
        ))

    return x_char_ys

def decode_x_char_ys(x_char_ys):
    """
    The x-character-y tuples hold a code to be placed on a grid with grid locations
    given by the x- and y-coordinates. This function returns the filled-in grid.
    """
    max_x = max((row[0] for row in x_char_ys))
    max_y = max((row[2] for row in x_char_ys))

    grid = [[' ' for _ in range(max_x+1)] for _ in range(max_y+1)]

    for x, char, y in x_char_ys:
        grid[max_y-y][x] = char

    return grid


def print_decoded_data(dec_data):
    """
    Sends the provided (decoded) data row-by-row to the console
    """
    for row in dec_data:
        print(''.join(row))

def print_url_contents(url):
    """
    Reads the html at url and assuming the url contains data in the expected form,
    will decode this data to be printed for human readability
    """
    x_char_y_rows = read_url_contents(url)
    decoded_data = decode_x_char_ys(x_char_y_rows)
    print_decoded_data(decoded_data)


if __name__ == "__main__":
    # print_url_contents(
    #     "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxm"
    #     "v-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    # )
    print_url_contents(
        "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYr"
        "EdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
    )
