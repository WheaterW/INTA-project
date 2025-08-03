zip
===

zip

Function
--------



The **zip** command compresses files or directories.




Format
------

**zip** *source-filename* *destination-filename* [ **password** *password* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-filename* | Specifies the name of the source file. | The value is a string of case-sensitive characters in the format of [ <drive> ][ <path> ][ <file-name> ]. An absolute <path> name is a string of 1 to 255 characters. A relative <path> name is a string of 1 to 128  characters. Up to 8 levels of directories are supported.  An absolute <path> is in the format of <drive> [ <path> ][ <file-name> ], and a relative <path> is in the format of [ <path> ][ <file-name> ]. That is, a relative <path> is the root <path> of the current working <path>. |
| *destination-filename* | Specifies the name of the destination file. | The value is a string of case-sensitive characters in the format of [ <drive> ][ <path> ][ <file-name> ]. An absolute <path> name is a string of 1 to 255 characters. A relative <path> name is a string of 1 to 128  characters. Up to 8 levels of directories are supported.  An absolute <path> is in the format of <drive> [ <path> ][ <file-name> ], and a relative <path> is in the format of [ <path> ][ <file-name> ]. That is, a relative <path> is the root <path> of the current working <path>. |
| **password** *password* | Specifies the password. | The value is a string of 8 to 20 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* If the file is too large, you can run the **zip** command to compress the file to facilitate storage.
* To view detailed information about a compressed file, run the **unzip** command to decompress the file.
* The system supports compression/decompression on the local board and inter-board compression/decompression.
* If you want to compress multiple files, move or copy them to the same directory and run the **zip** command to compress the directory.
* The **unzip** command cannot decompress a package that contains multiple files.

**Precautions**

If only the path of the target file is specified but the target file name is not specified, the target file name is the same as the source file name. After compression, the source file still exists.If the target file has high security requirements, you are advised to encrypt the file.Compresses or decompresses a single file.A single directory can be compressed, but a compressed package of a single file cannot be decompressed.If the compressed directory contains files in the recycle bin, the generated package also contains these files.


Example
-------

# Compress the dir1 directory into the dir1.zip file in the device directory.
```
<HUAWEI> zip dir1 dir1.zip
Info: Compress flash:/dir1 to flash:/dir1.zip? [Y/N]:Y

```

# Compress file1.txt into file1.zip in the directory of the master main control board.
```
<HUAWEI> zip file1.txt file1.zip
Info: Compress flash:/file1.txt to flash:/file1.zip? [Y/N]:Y

```