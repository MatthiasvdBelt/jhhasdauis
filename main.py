import argparse

print('main module')

parser = argparse.ArgumentParser(
    "obfuscated",
    description="This is the obfuscated description",
    epilog='Yeah this is our epilog',
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument("--version", action='version', version=f"obfuscation v3.2.81")

mp = parser.add_argument_group("MousePad")
mp.add_argument("files", help="Upload your files here", nargs="*")

mp.add_argument(
    "-r",
    "--road",
    help="Roads should help us, but they cause traffic jams...",
    nargs="+",
)
mp.add_argument(
    "-do",
    "--do_it",
    help="This arg makes it help do it",
    action="store_true",
)

o = parser.add_argument_group("Others")
o.add_argument("-klam", "--kkaoqq", type=int, help="Help for KLAM")
o.add_argument("-doooooo", "--ddsacxx", help="Help for doooooooooooooooooooo")
o.add_argument("-aaaac", "--sadas", help="Help for the a's", default=2)
