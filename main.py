import argparse

print('main module')

parser = argparse.ArgumentParser(
    "obfuscated",
    description="This is the obfuscated description",
    epilog='Yeah this is our epilog',
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument("--version", action='version', version=f"obfuscation v3.2.81")

# files
parser.add_argument(
    "simpleinputfile",
    type=argparse.FileType("r"),
    help="Input file (read mode) (simpleinputfile)"
)

parser.add_argument(
    "--simpleoptionalinputfile",
    type=argparse.FileType("r"),
    nargs="?",
    # default=sys.stdin,
    help="Optional input file or stdin (simpleoptionalinputfile)"
)

parser.add_argument(
    "--required-inputfile",
    type=argparse.FileType("r"),
    required=True,
    help="Required input file (required-inputfile)"
)

# TODO: we save this for later if one might need it
# parser.add_argument( # this would require the user to enter an output filename. In an approahc as below this
#     "--output",
#     type=argparse.FileType("w"),
#     help="Output file (write mode)"
# )

# parser.add_argument(
#     "--output-path",
#     type=str,
#     metavar="OUTFILE",
#     help="Output file path, opened manually"
# )
# ^^^^^^^^^^^^^^


# textual and numeric arguments
parser.add_argument(
    "--str-optional-name",
    type=str,
    help="Optional string: user name"
)

parser.add_argument(
    "--str-required-username",
    type=str,
    required=True,
    help="Required string: user login name"
)


# metavar is just display name. so we should display that if it is present
# parser.add_argument(
#     "--input-path",
#     type=str,
#     metavar="FILENAME",
#     help="File path, validated or opened manually later"
# )

# boolean flags #TODO

# choices  #TODO
# parser.add_argument(
#     "--choice-file",
#     type=str,
#     choices=["file1.txt", "file2.txt"],
#     help="File must be one of the allowed choices"
# )

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

# subparsers #TODO
