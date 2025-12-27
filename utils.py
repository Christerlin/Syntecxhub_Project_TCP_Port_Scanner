# Validate that the port range is within valid TCP/UDP port bounds (1-65535)
def validate_ports(start, end):
    # Raise an error if ports are outside the valid range
    if start < 1 or end > 65535:
        raise ValueError("Port range must be between 1 and 65535")
