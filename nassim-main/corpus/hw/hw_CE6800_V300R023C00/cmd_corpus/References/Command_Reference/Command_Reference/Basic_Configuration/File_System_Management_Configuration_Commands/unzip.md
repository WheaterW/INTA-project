unzip
=====

unzip

Function
--------



The **unzip** command decompresses a file.




Format
------

**unzip** *source-filename* *destination-filename* [ **password** *password* ]


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

* To save a large file with fewer memory resources occupied, you can run the **zip** command to compress the file.
* To view the contents of a compressed file, you can run the **unzip** command to decompress the file.
* Files can be compressed or decompressed on the local board or on other boards.

**Precautions**

Only one file can be compressed or decompressed at a time.


Example
-------

# Decompress file1.zip into file1.txt in the directory of the device.
```
<HUAWEI> unzip flash:/file1.zip file1.txt
Info: Extract flash:/file1.zip to flash:/file1.txt? [Y/N]:y
100%  complete
Info: Decompressing file flash:/file1.zip to flash:/file1.txt...Done.

```