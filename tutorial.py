import bonobo
import csv
import os


# if resulting file exists remove it!
if os.path.exists('result.csv'):
    os.remove('result.csv')

FILE_PATH = 'demo.csv'


def extract():
    """Placeholder, change, rename, remove... """
    with open(FILE_PATH) as file:
        reader = csv.reader(file)
        row_num = 0

        for row in reader:
            row_num += 1
            if row_num != 1:
                yield row


def transform(row):
    """Placeholder, change, rename, remove... """
    del row[2]  # deleting population
    yield row


def another_transform(row):
    """Convert to upper case city name"""
    row[1] = row[1].upper()  # making capital city uppercase
    return row


def load(row):
    """Placeholder, change, rename, remove... """
    with open('result.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)


def get_graph(**options):
    """
    This function builds the graph that needs to be executed.

    :return: bonobo.Graph

    """
    graph = bonobo.Graph()
    graph.add_chain(extract, transform, another_transform, load)

    return graph


def get_services(**options):
    """
    This function builds the services dictionary, which is a simple dict of names-to-implementation used by bonobo
    for runtime injection.

    It will be used on top of the defaults provided by bonobo (fs, http, ...). You can override those defaults, or just
    let the framework define them. You can also define your own services and naming is up to you.

    :return: dict
    """
    return {}


# The __main__ block actually execute the graph.
if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
