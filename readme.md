# Music Encrypt
### A Music based Encryption Program
#### Author: Mrinal Pande
#### License: MIT
<br>

## About
    Music encrypt is a music based encryption program. It uses Substitution cipher based on a key to 
    encrypt text based files and converts them to musical notes. Theses musical notes are then taken 
    and converted to midi based music files, so they look like normal music files.

## Dependencies: 
    Pyknon: https://github.com/kroger/pyknon
    Mido: https://github.com/olemb/mido/tree/stable

## Theory

### Musical Notes and Duration
    A musical Note is a singular entity that represents the differnt pitch which when produced in 
    succession or coalition creates music.

    In traditional sheet music musical notes are identified by different shapes. These shapes 
    indicates the duration of a particular note i.e. for how long will the note be played. 

    Types of notes which are used are Whole-Note, Half note, Quarter-Note, Eight-Note and 
    Sixteeth note. Each note is played for 1/2 times less time than the other. 
    For exaple: If a whole note is played for 4 seconds, a half note will be played for only 
    2 seconds. So a whole note can consistes of 2 half notes.
                    whole note
                        |       |       |       |
                    half note       half note

### Octave
    A octave in music as the name suggested is represented by eight notes. These eight notes 
    are in a interval between a primary notes and the next encounter of that primary note with 
    half or double its frequency. For example:

        The most common C major Scale is:
            C   D   E   F   G   A   B   C'
        
    Here the root note is C and C' is the higher couter part of the same note with double the 
    frequency of root note.

### Rest
    Rest in simple terms is the duration for which we have to wait for the next note to be played.

<br>

## Working
    The Music Encrypt follows a scheme where root note as the key. The Encryptions occurs using 
    a scheme based on the key note.

    First Seven notes in a octave are used for encryption. The Root note is the 
    key using which the whole file is encrypted. This part is the column identification 
    which helps to identidfy the column. 

    The rows are identified by the different type of note duration. The 5 duration that are used 
    are Whole-Note, Half note, Quarter-Note, Eight-Note, and Sixteeth note. The first row which 
    consists of the notes that are played is represented by whole-notes, the second row by half 
    notes and so on.

### Column Identification

    A major Scale as an Example:
                     key
    substituted note: C   D   E    F   G   A    B
                      H   I   J    K   L   M    N
                      O   P   Q    R   S   T    U
                      V   W   X    Y   Z

    Ignoring the # sign as we can read the above scheme as a simple A-Z,0-9. For every letter in 
    the 26 alphabet and digit there is a substitute note represented in the top line.
        HELLO -> CEGGC

### Row Identification
    Taking the same A major scale example

    A major Scale as an Example:
                   key
    Whole note:     C   D   E    F   G   A    B
    Half note:      H   I   J    K   L   M    N
    Quater note:    O   P   Q    R   S   T    U
    Eighth note:    V   W   X    Y   Z

    So HELLO -> HN WN HN HN QN
    HN: Half Note
    WN: Whole Note
    QN: Quater Note

Combining the Column and Row we get the Encrypted Music File. Therefore the above example of HELLO encrypts into.

        -------------------------------
                    H   E   L   L   O
        Notes       C   E   G   G   C
        Duration   HN  WN  HN  HN  QN
        -------------------------------


## Usage
    Encryption:
    python main.py -f <filename> -e -k <key> -o <output filename>

    Decryption:
    python main.py -f<filename> -d