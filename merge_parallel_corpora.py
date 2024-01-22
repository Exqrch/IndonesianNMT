import csv

def merge_parallel_corpora(src_files, tgt_files, src_label, tgt_label, out_file):
    # Check if the number of files in both lists is the same
    if len(src_files) != len(tgt_files):
        raise ValueError("The number of source and target files must be the same.")

    # Initialize lists to store lines from source and target files
    src_lines = []
    tgt_lines = []

    src_count = 0
    # Read lines from source files
    for src_file in src_files:
        with open(src_file, 'r', encoding='utf-8') as src_f:
            for line in src_f.readlines():
                src_lines.append(line)
                src_count += 1

    tgt_count = 0
    # Read lines from target files
    for tgt_file in tgt_files:
        with open(tgt_file, 'r', encoding='utf-8') as tgt_f:
            for line in tgt_f.readlines():
                tgt_lines.append(line)
                tgt_count += 1

    if len(src_lines) != len(tgt_lines):
        raise ValueError(f"The number of source and target lines must be the same.\nSRC={src_count}, TGT={tgt_count}") 

    # Combine source and target lines into a list of tuples
    combined_lines = [(src_lines[i].strip(), tgt_lines[i].strip()) for i in range(len(src_lines))]

    # Write the combined lines to a TSV file
    with open(out_file, 'w', encoding='utf-8', newline='') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t')
        # Write header
        tsv_writer.writerow([src_label, tgt_label])
        # Write data
        tsv_writer.writerows([(line[0], line[1]) for line in combined_lines])

# Example usage:
# id-jv
src_files_list = ['10shot-id-jv.id', 'davinci-id-jv.id', 'id-jv.id']
tgt_files_list = ['10shot-id-jv.jv', 'davinci-id-jv.jv', 'id-jv.jv']
src_label = "Indonesian" 
tgt_label = "Javanese" 
output_csv_file = 'id-jv.tsv'
merge_parallel_corpora(src_files_list, tgt_files_list, src_label, tgt_label, output_csv_file)

# id-ban
src_files_list = ['id-ban.id']
tgt_files_list = ['id-ban.ban']
src_label = "Indonesian" 
tgt_label = "Balinese" 
output_csv_file = 'id-ban.tsv'
merge_parallel_corpora(src_files_list, tgt_files_list, src_label, tgt_label, output_csv_file)

# id-min
src_files_list = ['id-min.id']
tgt_files_list = ['id-min.min']
src_label = "Indonesian" 
tgt_label = "Minangkabau" 
output_csv_file = 'id-min.tsv'
merge_parallel_corpora(src_files_list, tgt_files_list, src_label, tgt_label, output_csv_file)

# id-su
src_files_list = ['id-su.id']
tgt_files_list = ['id-su.su']
src_label = "Indonesian" 
tgt_label = "Sundanese" 
output_csv_file = 'id-su.tsv'
merge_parallel_corpora(src_files_list, tgt_files_list, src_label, tgt_label, output_csv_file)