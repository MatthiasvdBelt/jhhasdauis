import argparse

print('main module')

parser = argparse.ArgumentParser(
    "obfuscated",
    description="This is the obfuscated description",
    epilog='Yeah this is our epilog',
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument("--version", action='version', version=f"obfuscation v3.2.81")

# common things
parser.add_argument(
    "single-metavar",
    metavar="jippie",
    help="Single metavar test"
)

parser.add_argument(
    "--multiple-metavar",
    nargs=3,
    metavar=("START", "MIDDLE", "END"),
    help="Start and end values"
)

parser.add_argument(
    "--dest-simple",
    type=int,
    dest="server_port",
    metavar="PORT",
    help="Custom destination and metavar: server port number"
)

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

parser.add_argument(
    "--str-optional-default",
    type=str,
    default="KOPPAL",
    help="Optional string with default string"
)

parser.add_argument(
    "str-positional-query",
    type=str,
    help="Positional string: search query (required)"
)

parser.add_argument(
    "str-positional-note_optional",
    nargs="?",
    type=str,
    help="Optional positional string: note or comment"
)

# Exactly three strings
parser.add_argument(
    "--string-specific-number",
    type=str,
    nargs=3,
    # metavar=("START", "END"),
    help="Exactly 3 strings."
)

parser.add_argument(
    "--str-single-narg",
    type=str,
    nargs=1,
    help="String wrapped in list via nargs=1"
)


# TODO
# parser.add_argument(
#     "tags",
#     nargs="*",
#     type=str,
#     help="Tags (zero or more values)"
# )
#
# parser.add_argument(
#     "keywords",
#     nargs="+",
#     type=str,
#     help="Keywords (one or more values required)"
# )

parser.add_argument(
    "--int-default-retries",
    type=int,
    default=3,
    help="Optional int with default: retry count (default: 3)"
)

parser.add_argument(
    "--int-required-timeout",
    type=int,
    required=True,
    help="Required integer: timeout in seconds"
)

# Multiple integers (1 or more)
parser.add_argument(
    # this is a duplicate one on accident
    "--int-nargs-plus",
    type=int,
    nargs="+",
    help="List of nargs plus integers"
)

# Zero or more integers
parser.add_argument(
    "--int-zero-or-more",
    type=int,
    nargs="*",
    help="Optional list of integers: score values (0 or more)"
)

# Exactly two integers
parser.add_argument(
    "--integers-specific-number",
    type=int,
    nargs=2,
    metavar=("START", "END"),
    help="Exactly 2 integers: start and end of range"
)

# Optional float
parser.add_argument(
    "--float-optional",
    type=float,
    help="Optional float: learning rate"
)

# Float with default
parser.add_argument(
    "--float-optional-with-default",
    type=float,
    default=0.9,
    help="Optional float with default: momentum (default: 0.9)"
)

parser.add_argument(
    "--float-required-with-default",
    type=float,
    default=4.8,
    help="aaa",
    required=True
)

parser.add_argument(
    "float-positional",
    type=float,
    default=1.2,
    help="Optional float with default: momentum (default: 0.9)",
)

# boolean flags
# Sets to True if present (default is False)
parser.add_argument(
    "--bool-test-true",
    action="store_true",
    help="Enable verbose output"
)

# Sets to False if present (default is True)
parser.add_argument(
    "--bool-test-store-false",
    action="store_false",
    help="Disable logging"
)

# mutually exclusive groups
# boolean
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "--bool-mode-light",
    action="store_true",
    dest="light_mode",
    help="Use light mode"
)
group.add_argument(
    "--bool-mode-dark",
    action="store_true",
    dest="light_mode",
    help="Use dark mode"
)

# more mutually exclusive groups?
# TODO: we will do that later when we encounter one.

# choices
parser.add_argument(
    "--simple-choice",
    choices=["red", "green", "blue"],
    help="Choose a color"
)

parser.add_argument(
    "--simple-choice-required",
    choices=["dev", "test", "prod"],
    required=True,
    help="Required: environment mode"
)

parser.add_argument(
    "--choice-with-default",
    choices=["low", "medium", "high", "ultra"],
    default="medium",
    help="Priority level (default: medium)"
)

parser.add_argument(
    "--choice-int-code",
    type=int,
    choices=[100, 200, 404],
    help="Integer status code"
)

parser.add_argument(
    # also tests what happens if someone uses underscores instead of dashes
    "--choice_int_code_with_default",
    type=int,
    choices=[101, 201, 408],
    default=201,
    help="Integer status code (default: 201)"
)

parser.add_argument(
    "--choice-float-code",
    type=float,
    choices=[100.01, 200.01, 404.01],
    help="Integer status code"
)

parser.add_argument(
    # also tests what happens if someone uses underscores instead of dashes
    "--choice_float_code_with_default",
    type=float,
    choices=[101.01, 201.01, 408.01],
    default=201.01,
    help="Integer status code (default: 201)"
)

# choices with nargs
# Multiple string choices (at least one)
parser.add_argument(
    "--choice-one-or-more",
    choices=["size", "speed", "color"],
    nargs="+",
    help="Enable one or more features"
)

parser.add_argument(
    "--choice-zero-or-more",
    choices=["x", "y", "z"],
    nargs="*",
    help="Zero or more options"
)

# choices positionals

parser.add_argument(
    "choice-positional",
    choices=["admin", "user", "guest"],
    help="Role (required positional)"
)

parser.add_argument(
    # also tests if _ work instead of -
    "choice_positional_0_or_more_with_default",
    nargs="?",
    choices=["json", "csv", "xml"],
    default="json",
    help="Optional output format (default: json)"
)

# subparsers
subparsers = parser.add_subparsers(dest='subparsers', required=True, help="Available subcommands")


init_parser = subparsers.add_parser("init", help="Initialize a project")
init_parser.add_argument(
    "init_project_name",
    type=str,
    help="Positional: project name"
)

init_parser.add_argument(
    "--init-template",
    type=str,
    default="default",
    help="Optional template name (default: 'default')"
)

build_parser = subparsers.add_parser("build", help="Build the project")
build_parser.add_argument(
    "--build-level",
    type=int,
    default=1,
    help="Integer build level (default: 1)"
)
build_parser.add_argument(
    "--build-verbose",
    action="store_true",
    help="Enable verbose build output"
)

deploy_parser = subparsers.add_parser("deploy", help="Deploy the project")
deploy_parser.add_argument(
    "--deploy-target",
    choices=["staging", "production"],
    required=True,
    help="Required: target environment"
)
deploy_parser.add_argument(
    "--deploy-force",
    action="store_true",
    help="Force deployment"
)

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
