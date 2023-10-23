# Specify input and output file names
input_file = "your_input.fasta"
output_file = "sorted_output.fasta"

# Define a custom sorting function to sort based on the numeric part of the header
def sort_key(header):
    parts = header.split()
    if len(parts) >= 2 and parts[0].startswith(">"):
        try:
            return int(parts[0][1:])
        except ValueError:
            pass
    return header

# Read the input FASTA file
with open(input_file, 'r') as f:
    fasta_data = f.read().split('>')

# Sort the FASTA data based on the sorting key
sorted_fasta_data = sorted(fasta_data[1:], key=sort_key)

# Write the sorted data to the output FASTA file
with open(output_file, 'w') as f:
    f.write('>' + '>'.join(sorted_fasta_data))
