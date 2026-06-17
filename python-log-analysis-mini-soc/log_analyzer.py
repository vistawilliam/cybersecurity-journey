from collections import Counter

LOG_FILE = "sample_logs.txt"


def extract_ip(line):
    parts = line.split()
    for part in parts:
        if part.startswith("ip="):
            return part.replace("ip=", "")
    return None


def analyze_logs(filename):
    failed_logins = []
    successful_logins = []

    with open(filename, "r") as file:
        for line in file:
            if "LOGIN_FAILED" in line:
                failed_logins.append(line.strip())
            elif "LOGIN_SUCCESS" in line:
                successful_logins.append(line.strip())

    failed_ips = []

    for entry in failed_logins:
        ip = extract_ip(entry)
        if ip:
            failed_ips.append(ip)

    ip_counter = Counter(failed_ips)

    print("=== Mini SOC Log Analysis Report ===")
    print()
    print(f"Total successful logins: {len(successful_logins)}")
    print(f"Total failed logins: {len(failed_logins)}")
    print()

    print("Failed login attempts by IP:")
    for ip, count in ip_counter.items():
        print(f"- {ip}: {count} failed attempts")

    print()
    print("Suspicious IPs:")

    suspicious_found = False

    for ip, count in ip_counter.items():
        if count >= 3:
            print(f"- {ip} triggered alert with {count} failed login attempts")
            suspicious_found = True

    if not suspicious_found:
        print("- No suspicious IPs detected")


if __name__ == "__main__":
    analyze_logs(LOG_FILE)
