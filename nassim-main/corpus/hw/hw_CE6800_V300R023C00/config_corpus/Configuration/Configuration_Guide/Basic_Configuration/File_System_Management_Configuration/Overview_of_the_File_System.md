Overview of the File System
===========================

Overview of the File System

#### File System

The file system manages files and directories in storage media. It allows users to create, delete, and modify files and directories, as well as view the contents of files.


#### Storage Medium

The device supports the flash memory and USB flash drive. The device also supports the read-only backup partition to prevent the device from failing to read the files from the primary partition when the primary partition is faulty.

![](public_sys-resources/note_3.0-en-us.png) 

Ensure that the format of the USB flash drive is set to FAT32.



#### File Naming Rules

A file name must be a string of 1 to 255 case-sensitive characters without spaces. The file name formats are as follows:

* File name
  
  The file name format is *filename*. If a file name is in this format, the file is in the current working directory.
* Path + File name
  
  The file name format is *drive*/*path*/*filename*, which uniquely identifies a file in a specified path.
  
  **drive** indicates the storage medium in the device. For example, if the flash memory is specified for storage, replace **drive** with **flash:**.
  
  Besides, **path** indicates the path where a file is stored. The path name is case-sensitive and cannot contain spaces or the following special characters: ~ \* / \ : ' "
  
  The path can be an absolute path or a relative path: A path that contains the root directory (specified by *drive*) is an absolute path. A relative path can be designated relative to either the root directory or the current working directory. A relative path beginning with a slash (/) is a path relative to the root directory.
  + The path **flash:/****my/test/** is an absolute path.
  + The path **/selftest/** is a path relative to the root directory and indicates the **selftest** directory in the root directory.
  + The path **selftest/** is a path relative to the current working directory and indicates the **selftest** directory in the current working directory.
  
  For example, in the [**dir**](cmdqueryname=dir) **flash:/my/test/mytest.txt** command, the path **flash:/my/test/** is an absolute path.
  
  If a path relative to the root directory is used, the command becomes [**dir**](cmdqueryname=dir) **/my/test/mytest.txt**.
  
  If a path relative to the current working directory such as **flash:/my/** is used, the command becomes [**dir**](cmdqueryname=dir) **test/mytest.txt**.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  + In file operation commands, a file name is specified by **filename**.
  + In file operation commands, a directory is specified by **directory** in the format of *drive/path*.

#### File List Information

You can run the [**dir**](cmdqueryname=dir) command to view the file list of the system.

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
    6  -rw-         14,940  Nov 11 2019 17:56:29   SPH001.PAT    
    7  -rw-    572,847,476  Oct 21 2019 15:21:23   software.cc  
    8  -rw-         34,505  Nov 11 2019 20:01:07   device.sys 
    9  drwx              -  Nov 11 2019 21:01:39   logfile

2,994,228 KB total (801,664 KB free)
```
[Table 1](#EN-US_CONCEPT_0000001564110693__tab_01) describes the file list information displayed using the [**dir**](cmdqueryname=dir) command.

**Table 1** Description of file list information
| Item | Description |
| --- | --- |
| $\_checkpoint | Directory where configuration rollback point information is saved |
| $\_install\_mod | Directory where dynamic module packages are saved |
| $\_license | Directory where activated license files are backed up |
| $\_security\_info | Directory where historical information about AAA users is saved. |
| $\_startup | Directory where the startup configuration file is saved |
| $\_system | Linux system-predefined directory where system scripts are saved |
| \*.pat/\*.PAT | Patch file |
| \*\*.cc | Software version file |
| device.sys | System hardware configuration file |
| logfile | Log file |