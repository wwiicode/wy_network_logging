from utilities import data_processing, write_output, load_lookup_table


def main():
    lookup_file = 'lookup_table.csv'
    # flow_log_file = 'flow_logs.txt'
    flow_log_file = 'flow_logs_with_errors.txt'  ## used this for testing, flawed log records will not block streaming

    output_file = 'output.txt'

    lookup_table = load_lookup_table.get_lookup_table(lookup_file)

    tag_counts, port_protocol_counts = data_processing.process_flow_logs(flow_log_file, lookup_table)

    write_output.get_output(tag_counts, port_protocol_counts, output_file)

if __name__ == "__main__":
    main()

