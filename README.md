# chunker
This is a simple performance adaptation of https://stackoverflow.com/questions/42228770/load-pandas-dataframe-with-chunksize-determined-by-column-variable/42229904#42229904

I use this often when dealing with large files that don't fit in memory. Usage is just like the pandas read_csv function.

```python
# normal
df = pd.read_csv("train_data.csv", chunksize=200000, header=1)

for chunk in df:
  do_something()

# using chunker:
df = generate_chunks(path="train_data.csv", header=1, chunk_size=200000)

for chunk in df:
  do_something()
  
```

This will chunk based on the ID values of the first column. For more options in read_csv, please change the internal call for now, but keep header=None and iterator=True. 
