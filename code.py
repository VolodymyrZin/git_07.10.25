from datetime import datetime
import logging


def analyze_heartbeat_log(input_file: str, output_file: str):
    logging.basicConfig(filename=output_file, level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    with open(input_file) as f:
        filtered_log = []
        for line in f:
            if "Key TSTFEED0300|7E3E|0400" in line:
                filtered_log.append(line)

    timestamps = []
    for log_line in filtered_log:
        if 'Timestamp ' in log_line:
            pos = log_line.find("Timestamp ")
            timestamp_str = log_line[pos + 10:pos + 18]
            dt_obj = datetime.strptime(timestamp_str, "%H:%M:%S")
            timestamps.append(dt_obj)

    for i in range(1, len(timestamps)):
        diff = abs((timestamps[i] - timestamps[i - 1]).total_seconds())

        if 31 < diff < 33:
            logging.warning(f"Heartbeat WARNING at {timestamps[i].time()}: {diff} sec")
        elif diff >= 33:
            logging.error(f"Heartbeat ERROR at {timestamps[i].time()}: {diff} sec")


analyze_heartbeat_log("hblog.txt", "hb_test.log")
