#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import hashlib

desc = """ch3cksum helps you to hash file in order to compare them with a provided checksum.
    SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 as well as MD5 algorithm. Based on hashlib."""
mode_choices = ['hash', 'compare']
hash_choices = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

def hash_file(file, type):
    try:
        with open(file, "rb") as file_open:
            hash_type_func_dic = {
                'md5': hashlib.md5,
                'sha1': hashlib.sha1,
                'sha224': hashlib.sha224,
                'sha256': hashlib.sha256,
                'sha384': hashlib.sha384,
                'sha512': hashlib.sha512
            }

            hash = hash_type_func_dic[type]()

            while chunk := file_open.read(1024):
                hash.update(chunk)
            hex_hash = hash.hexdigest()

            return hex_hash
    except IOError:
        print_error('File ' + file + ' not found')
        return None

def compare(file, type, checksum):
    hash_found = hash_file(file, type)
    if(hash_found != None):
        return verify_checksum(checksum, hash_found)

    return False

def verify_checksum(checksum, hash):
    return checksum == hash

def print_hash(hash):
    len_hash = len(hash)
    print('+-------' + str(''.join(['-' for e in range(len_hash)])) + '-------+')
    print('|       ' + str(''.join(' ' for e in range(len_hash))) + '       |')
    print('|\t' + hash + '       |')
    print('|       ' + str(''.join(' ' for e in range(len_hash))) + '       |')
    print('+-------' + str(''.join(['-' for e in range(len_hash)])) + '-------+')

def print_compare(result):
    if result:
        print('Success')
    else:
        print('Different')

def print_error(error):
    print('*** error: ' + error + ' ***')

def get_parser():
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "mode",
        help="the choosen mode",
        choices=mode_choices,
    )
    parser.add_argument(
        "type",
        help="hash type",
        choices=hash_choices
    )
    parser.add_argument("file")
    parser.add_argument(
        "-c",
        "--checksum",
        dest="checksum",
        help="any checksum to compare"
    )

    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.mode == 'hash':
        hash = hash_file(args.file, args.type)
        if hash != None:
            print_hash(hash)
    elif args.mode == 'compare':
        if args.checksum:
            result = compare(args.file, args.type, args.checksum)
            print_compare(result)
        else:
            print_error('Checksum not specified with compare mode')

if __name__ == "__main__":
    main()

