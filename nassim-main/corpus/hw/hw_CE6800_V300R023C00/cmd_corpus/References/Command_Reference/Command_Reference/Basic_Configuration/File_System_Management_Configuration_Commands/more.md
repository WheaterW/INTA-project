more
====

more

Function
--------



The **more** command displays the contents of a specified file.




Format
------

**more** *file-name* [ *offset* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the name of a file. | The value is a string of case-sensitive characters in the format of [ drive ] [ path ] [ file-name ]. An absolute path name is a string of 1 to 255 characters. A relative path name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute path is in the format of drive [ path ] [ file-name ], and a relative path is in the format of [ path ][ file-name ]. That is, a relative path is the root path of the current working path. |
| *offset* | Specifies the offset of the file to be displayed. | The value is an integer ranging from 0 to 2147483647 in bytes. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the more command to view the contents of a specified file. The system displays the contents of a file in text format.


Example
-------

# Display the contents of the file tmp.txt.
```
<HUAWEI> more tmp.txt
AppWizard has created this test application for you.
This file contains a summary of what you will find in each of the files that make up your test application.

```