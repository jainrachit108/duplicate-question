import gzip

compressed_file = 'model.pkl.gz'
output_file = 'model.pkl'

with gzip.open(compressed_file, 'rb') as f_in:
    with open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)
        
print(f'Extracted file created: {output_file}')
