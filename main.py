### Author: Mrinal Pande
### Date:   Aug,15 2017
import sys
import os.path
import encrypt

def main():
    print("---------------------------------------------------")
    print("Music Encrypt - Music Based Encryption")
    print("Author: Mrinal Pande")
    print("---------------------------------------------------")
    if  len(sys.argv) < 2:
        print("For Help:",sys.argv[0],"-h")
    elif sys.argv[1] == "-h":
        print("Help For Music Encrypt")
        print("---------------------------------------------------")
        print("Options      Description")
        print("-f           File to encrypt/Decrypt")
        print("-e           Encrypt the file")
        print("-d           Decrypt the file")
        print("-k           Key to Encrypt")
        print("-o           name of output file")
        print("\nFor encrypting a file:")
        print("python main.py -f <filename> -e -k <key> -o <output file name>")
        print("\nFor decrypting a file:")
        print("python main.py -f <filename> -d")
        print("---------------------------------------------------")
    elif sys.argv[3] == "-e" and len(sys.argv) == 8:
        fpath = sys.argv[2]
        key = sys.argv[5]
        outfile = sys.argv[7]
        print("Starting Encryption...")
        if os.path.isfile(fpath):
            encrypt.encrypt(fpath,key,outfile)
        else:
            print("File not found \n")
            print("For Help:",sys.argv[0],"-h")
    elif sys.argv[3] == "-d" and len(sys.argv) == 4:
        print("Decryption")
        fpath = sys.argv[2]
        if os.path.isfile(fpath):
            print("file found")
        else:
            print("File not found \n")
            print("For Help:",sys.argv[0],"-h")
    else:
        print("For Help:",sys.argv[0],"-h")
main()