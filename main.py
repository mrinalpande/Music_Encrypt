### Author: Mrinal Pande
### Date:   Aug,15 2017
import sys

def main():
    print("---------------------------------------------------")
    print("Music Encrypt - Music Based Encryption")
    print("Author: Mrinal Pande")
    print("License: MIT")
    print("---------------------------------------------------")

    if  len(sys.argv) != 2:
        print("For Help:",sys.argv[0],"-h")
    elif sys.argv[1] == "-h":
        print("Help For Music Encrypt")
        print("---------------------------------------------------")
        print("Options                         Description")
        print("-f                              file to encrypt/Decrypt")
        print("-e                              Encrypt the file")
        print("-d                              Decrypt the file")
        print("-k                              Key to Encrypt")
        print("-o                              Do nothing to the file")
    else:
        print("Nothing to do here")
main()