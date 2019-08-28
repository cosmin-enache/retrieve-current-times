from urllib.request import urlopen
import os


# uses ANSI escape/colour codes to color text in shell
def greenify(string_to_print):
    return "\u001b[32m" + string_to_print + "\u001b[0m"


print("Retrieving data...")

# requests document from url and decodes it from utf-8, then prints out desired details
with urlopen("https://tycho.usno.navy.mil/cgi-bin/timer.pl") as doc:
    str_to_escape = "<BR>"
    os.system("clear")
    os.system("echo Times Retrieved:")
    print()
    for line in doc:
        line = line.decode('utf-8')
        if str_to_escape in line:
            desired_output = line[len(str_to_escape):len(line)]
            print(greenify(desired_output))
