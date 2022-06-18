from requests import get
import argparse
from api import Api

def check():
    try:
        get("https://www.google.com/")
    except:
        exit()

parser = argparse.ArgumentParser()
parser.add_argument('--num', type=str, default=0, help="Target Number.")
parser.add_argument('--mes', type=int, default=0, help="Number of Messages.")

args = parser.parse_args()
target = str(args.num)
msgs = args.mes

check()
Api.infinite(target, msgs)
print("Done!")
exit()

