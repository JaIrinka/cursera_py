import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.key and args.val:
    with open(storage_path, 'a') as f:
        new_string = {args.key: args.val}
        f.write(json.dumps(new_string) + '\n')
elif args.key and os.path.isfile(storage_path):
    result = []
    with open(storage_path, 'r') as f:
        for line in f:
            json_line = json.loads(line.strip())
            if args.key in json_line:
                result.append(json_line[args.key])
    print(', '.join(result))
