import pandas as pd


def generate_chunks(path, has_header=None, chunk_size=200000, **kwargs):
    csv_reader = pd.read_csv(path, iterator=True, chunksize=1, header=None)  # Don't change iterator=True, header=None
    # If you want to add other options to the csv_reader, do it here.
    if has_header:
        csv_reader.get_chunk()  # Gets rid of header

    # This assumes that the ID is in the first row. If the ID is elsewhere, change the iloc calls appropriately
    def iter_chunk_by_id(csv_reader):
        csv_reader.chunksize = chunk_size
        first_chunk = csv_reader.get_chunk()
        id = first_chunk.iloc[-1, 0]
        chunk = pd.DataFrame(first_chunk)
        csv_reader.chunksize = 1

        for l in csv_reader:
            csv_reader.chunksize = 1
            if id == l.iloc[0, 0]:
                id = l.iloc[-1, 0]
                chunk = pd.concat([chunk, l])
                continue
            id = l.iloc[0, 0]
            csv_reader.chunksize = chunk_size
            yield chunk
            chunk = pd.DataFrame(l)
        yield chunk

    return iter_chunk_by_id(csv_reader)
