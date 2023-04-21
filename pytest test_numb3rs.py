Def validate(ip):
    # Split the input string by period delimiter
    Octets = ip.split(“.”)

    # Check if the input string contains exactly 4 octets
    If len(octets) != 4:
        Return False

    # Check if each octet is a valid integer in the range [0, 255]
    For octet in octets:
        If not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            Return False

    Return True


From numb3rs import validate

Def test_valid_ipv4_address():
    Assert validate(“192.168.0.1”) == True
    Assert validate(“10.0.0.0”) == True
    Assert validate(“172.16.0.255”) == True

Def test_invalid_ipv4_address():
    Assert validate(“256.168.0.1”) == False
    Assert validate(“172.16.0.256”) == False
    Assert validate(“1.2.3”) == False
    Assert validate(“1.2.3.4.5”) == False


