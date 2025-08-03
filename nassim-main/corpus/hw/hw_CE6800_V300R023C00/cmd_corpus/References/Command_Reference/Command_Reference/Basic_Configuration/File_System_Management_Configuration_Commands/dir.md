dir
===

dir

Function
--------



The **dir** command displays information about a specified file or a directory of a storage device on the device.



By default, information about files in the current directory is displayed.


Format
------

**dir**

**dir /all**

**dir** *filename*

**dir /all** *filename*

**dir /all-filesystems**

**dir /all /all-filesystems**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **/all** | Displays all files, including the dumped files in the recycle bin. | - |
| **/all** *filename* | Displays all files (including files that have been deleted to the recycle bin). | The value is a character string in the format of [ <drive> ][ <path> ][ <file-name> ]. An absolute <path> name is a string of 1 to 255 characters. A relative <path> name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute <path> is in the format of <drive> [ <path> ][ <file-name> ], and a relative <path> is in the format of [ <path> ][ <file-name> ]. That is, a relative <path> is the root <path> of the current working <path> . |
| *filename* | Displays all files (excluding files that have been deleted to the recycle bin). | The value is a character string in the format of [ <drive> ][ <path> ][ <file-name> ]. An absolute <path> name is a string of 1 to 255 characters. A relative <path> name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute <path> is in the format of <drive> [ <path> ][ <file-name> ], and a relative <path> is in the format of [ <path> ][ <file-name> ]. That is, a relative <path> is the root <path> of the current working <path> . |
| **/all-filesystems** | Displays information about all files in the root directory of storage medium. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the dir /all command to view information about all files, including the dumped files in the recycle bin. The name of a deleted file is enclosed in square brackets ([]), for example, [text].The wildcard \* can be used for matching.Table 1 lists the file information displayed in the **dir** command output.The displayed files are related to the system software version and service configuration. Only common files are listed here.Hidden files occupy disk space.\*\* Table 1 \*\* File information description table

| File Name | File Description |
| --- | --- |
| $\_checkpoint | File in which configuration rollback point information is saved. |
| $\_install\_mod | Directory for storing the MOD (dynamic module package). |
| $\_license | Directory where activated licenses are backed up. |
| $\_security\_info | Directory for storing the history data of AAA users. |
| $\_startup | Directory for storing the configuration file for the next startup. |
| $\_system | Linux directory for storing scripts used by the system. |
| \*.cc | Software version file. |
| NextFwdTemplet.txt | Forwarding profile. This file exists in the system after the forwarding mode is set. |
| device.sys | System hardware configuration file. |
| logfile | Log information file. |
| \*.log / \*.xml | Log information file. log.log: a common log file that is smaller than a specified size. diag.log: a diagnostic log file that is smaller than a specified size. log.xml: a common log file that is smaller than a specified size. oper.xml: an operation log file that is smaller than a specified size. security.xml: a security log file that reaches a specified size. alarm\_number.xml: an alarm log file that reaches a specified size. LocFail\_\*.log: a diagnostic log file containing logs generated each time a board exception occurs. logbuf\_slotxx.log: a log file containing logs about information recorded before the device resets. You can run the **display logbuffer** command to view the event logs and other logs. |
| lost+found | File management module's file that is damaged and then restored during a device restart. |
| \*.zip / \*.cfg / \*.dat | System configuration file. For details, see save.    After being compressed, log files are suffixed with .zip. log\_slot ID\_time.log.zip: a common log file that reaches a specified size. diaglog\_slot ID\_time.log.zip: a diagnostic log file that reaches a specified size. log\_time.xml.zip: a common log file that reaches a specified size. OpLog\_time.xml.zip: an operation log file that reaches a specified size. SecLog\_time.xml.zip: a security log file that reaches a specified size. alarm\_number.xml.zip: an alarm log file that reaches a specified size.    You can run the **info-center logfile size** command to set the size of a log file. |
| \*.pat / \*.PAT | Patch file. |
| selftest | Hardware self-check information file during system startup. |




Example
-------

# Display file information in flash:/.
```
<HUAWEI> dir
Directory of flash:/

  Idx  Attr     Size(Byte)  Date        Time       FileName                     
    0  dr-x              -  Nov 11 2019 20:16:35   $_checkpoint                 
    1  dr-x              -  Nov 06 2019 15:51:57   $_install_mod                
    2  dr-x              -  Oct 12 2019 18:12:15   $_license                    
    3  dr-x              -  Oct 12 2019 18:12:26   $_security_info              
    4  dr-x              -  Nov 11 2019 20:16:31   $_startup                    
    5  dr-x              -  Nov 11 2019 20:15:06   $_system                                                
    6  -rw-         14,940  Nov 11 2019 17:56:29   111.cc            
    7  -rw-    572,847,476  Oct 21 2019 15:21:23   123.cc                       
    8  -rw-         34,505  Nov 11 2019 20:01:07   device.sys                                                    
    9  drwx              -  Nov 11 2019 21:01:39   logfile                      
                
2,994,228 KB total (801,664 KB free)

```

**Table 1** Description of the **dir** command output
| Item | Description |
| --- | --- |
| Directory of flash | Directory on the flash card. |
| Idx | File index. |
| Attr | File attribute. |
| Size(Byte) | File size, in bytes. |
| Date | Date when a file was created. |
| Time | Time when a file was created. |
| FileName | Name of a module file. |