import argparse


parser = argparse.ArgumentParser(description='Compute sum of two number.')
parser.add_argument('first_number', type=int, metavar='x')
parser.add_argument('second_number', type=int)
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()

s = args.first_number + args.second_number

if args.verbose:
    print(f'The sum is: {s}.\nThank you for using our script!')
else:
    print(s)
