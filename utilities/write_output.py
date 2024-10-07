def get_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, 'w') as file:
        file.write("Tag Counts:\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")

        file.write("\nPort/Protocol Combination Counts:\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

    print("Completed writing log entries to output.txt")