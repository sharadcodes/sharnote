# SharNote
A command line note taking utility developed in Python that saves notes in JSON format.

# Installation

```bash
pip3 install sharnote
```

# Usage

```bash
sharnote This is a dummy note
```

#  Flags:

### --help or --h
For showing help
##### Example 
```
sharnote --help    or    sharnote --h
```

### --notedir or --nd
For changing notes directory
##### Example 
```
sharnote --notesdir    or    sharnote --nd
```

### --search or --s
For searching in notes
##### Example 
```
sharnote --search "My search string"    or    sharnote --s "My search string"
```

### --today or --t
For showing today's notes
##### Example
```
sharnote --t    or    sharnote --t
```

### --date or --d
For showing notes of a particaular date
##### Example
```
sharnote --date 2019-09-27    or    sharnote --d 2019-09-27
```