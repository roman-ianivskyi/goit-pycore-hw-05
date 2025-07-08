import sys
import collections


def parse_log_line(line: str) -> dict:
    # 4 parts: 2024-01-22 | 09:00:45 | ERROR | Database connection failed.
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path) as f:
            for line in f:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error {e} while reading file {file_path}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    return collections.Counter(map(lambda log: log["level"], logs))


def display_log_counts(counts):  # print in a table format
    print("Log Level Statistics:\n")
    print(f"{'Level':<20}|{'Count':^10}")
    print("-" * 20 + "|" + "-" * 11)
    for level in counts.most_common():
        print(f"{level[0]:<20}| {level[1]:<10}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file> [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    specific_level = None

    if len(sys.argv) >= 3:
        specific_level = sys.argv[2].upper()

    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    print(counts)
    display_log_counts(counts)

    print()
    if specific_level:
        filtered_logs = filter_logs_by_level(logs, specific_level)
        if filtered_logs:
            print(f"Detailed information for level '{specific_level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
