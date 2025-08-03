Example for Managing Files Locally
==================================

Example for Managing Files Locally

#### Networking Requirements

A user logs in to a device using the console port, Telnet, or STelnet, and needs to perform the following operations on the files on the device:

* View files and subdirectories in the current directory.
* Create a directory named **test**. Copy the **vrpcfg.zip** file to the directory **test** and rename the file **backup.zip**.
* View files in the **test** directory.

#### Procedure

1. View files and subdirectories in the current directory.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device
   [*HUAWEI] commit
   [~Device] quit
   <Device> dir
   Directory of flash:/
   
     Idx  Attr     Size(Byte)  Date        Time       FileName
       0  -rw-            889  Mar 01 2019 14:41:56   private-data.txt
       1  -rw-          6,311  Feb 17 2019 14:05:04   backup.cfg
       2  -rw-          2,393  Mar 06 2019 17:20:10   vrpcfg.zip
       3  -rw-            812  Nov 12 2019 15:43:10   hostkey
       4  drw-              -  Mar 01 2019 14:41:46   compatible
       5  -rw-            540  Nov 12 2019 15:43:12   serverkey
   ...
   670,092 KB total (569,904 KB free)
   ```
2. Create a directory named **test**. Copy the **vrpcfg.zip** file to the directory **test** and rename the file **backup.zip**.
   
   
   
   # Create the **test** directory.
   
   ```
   <Device> mkdir test
   Info: Create directory flash:/test/......Done.
   ```
   
   # Copy the **vrpcfg.zip** file to the **test** directory and rename the file **backup.zip**.
   
   ```
   <Device> copy vrpcfg.zip flash:/test/backup.zip 
   Info: Are you sure to copy flash:/vrpcfg.zip to flash:/test/backup.zip?[Y/N]:y
   100%  complete
   Info: Copied file flash:/vrpcfg.zip to flash:/test/backup.zip...Done.
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the destination file name is not specified, the source file name is used as the destination file name by default. That is, the destination file has the same name as the source file.

#### Verifying the Configuration

# Access the **test** directory.

```
<Device> cd test
```

# View the current directory.

```
<Device> pwd
flash:/test/

```

# View files in the **test** directory.

```
<Device> dir
Directory of flash:/test/

  Idx  Attr     Size(Byte)  Date        Time       FileName
    0  -rw-          2,399  Mar 12 2012 11:16:44   backup.zip

670,092 KB total (569,900 KB free)
```

#### Configuration Scripts

```
#
sysname Device
#
return
```