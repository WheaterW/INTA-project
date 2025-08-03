display backup-file
===================

display backup-file

Function
--------



The **display backup-file** command displays information about all files in the backup area.




Format
------

**display backup-file**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The **display backup-file** command displays information about all files in the backup area.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all files in the backup area.
```
<HUAWEI> display backup-file
Directory of backup:/

  Idx  Attr     Size(Byte)  Date        Time       FileName
    0  dr-x              -  Feb 18 2021 09:58:07   $_install_mod
    1  -r-x              -  Feb 18 2021 09:58:07   $_install_mod/mod1.mod    
    2  -rwx              0  Feb 18 2021 10:46:59   example1.ini                 

103,081,248 KB total (33,834,868 KB free)

```

**Table 1** Description of the **display backup-file** command output
| Item | Description |
| --- | --- |
| Directory of backup | Directory in the backup area. |
| Idx | File index. |
| Attr | File attribute. |
| Size(Byte) | File size, in bytes. |
| Date | Date when a file was created. |
| Time | Time when a file was created. |
| FileName | Name of a module file. |