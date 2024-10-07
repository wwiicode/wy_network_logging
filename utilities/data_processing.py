import logging


logging.basicConfig(filename='error_log.log', 
                    filemode='w',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def process_flow_logs(flow_log_file, lookup_table):
    tag_counts = {}
    port_protocol_counts = {}
    
    with open(flow_log_file, 'r') as file:
        for line in file:
            try:
                parts = line.strip().split()           
                if parts[0] != '2':
                    logging.error(f"Currently only version 2 is accepted")
                    continue        

                dstport = int(parts[5]) 
                protocol = parts[7]
                
                if protocol == '6':
                    protocol_str = 'tcp'
                elif protocol == '17':
                    protocol_str = 'udp'
                elif protocol == '1':
                    protocol_str = 'icmp'
                else:
                    protocol_str = None

                if protocol_str is None:
                    logging.error(f"Unknown protocol: {protocol}")
                    continue

                tag = lookup_table.get((dstport, protocol_str), 'Untagged')
                
                if tag not in tag_counts:
                    tag_counts[tag] = 0
                tag_counts[tag] += 1
                
                if (dstport, protocol_str) not in port_protocol_counts:
                    port_protocol_counts[(dstport, protocol_str)] = 0
                port_protocol_counts[(dstport, protocol_str)] += 1

            except IndexError:
                logging.error(f"Malformed line with too few entry): {line.strip()}")
                continue  
            except ValueError as e:
                logging.error(f"ValueError: {e}, Line: {line.strip()}")
                continue 
    
    return tag_counts, port_protocol_counts

