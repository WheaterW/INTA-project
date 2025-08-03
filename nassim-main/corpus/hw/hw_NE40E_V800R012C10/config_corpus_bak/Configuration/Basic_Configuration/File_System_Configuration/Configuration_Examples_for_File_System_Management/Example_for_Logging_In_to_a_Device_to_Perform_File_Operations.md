Example for Logging In to a Device to Perform File Operations
=============================================================

This section provides an example for logging in to a device to perform file operations, such as viewing and copying files.

#### Networking Requirements

You can log in to a device through a console port or using Telnet or STelnet to manage files on the device.

You must enter a correct path for storing files. If you do not specify a target file name, the source file name is the target file name by default.


#### Precautions

* To log in to a device through a console port, you must prepare a terminal and an RS-232 cable.
* To log in to a device using Telnet or STelnet, you must have configured a Telnet or STelnet server and ensure that the server and terminal are routable.
  
  For detailed configurations, see [User Login Configuration](dc_vrp_basic_cfg_0024.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, login through a console port is used to manage files.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure login through a console port.
2. View files in a directory.
3. Copy a file to this directory.
4. Check that the file is copied to the specified directory.

#### Data Preparation

To complete the configuration, you need the following data:

* Source and target file names
* Source and target file paths

#### Procedure

1. Configure login through a console port.
   
   
   
   For detailed configurations, see [Example for Configuring Login Through a Console Port](dc_vrp_basic_cfg_0046.html).
2. View files in the current directory.
   
   
   ```
   <HUAWEI> dir
   ```
   ```
   Directory of cfcard:/
     Idx  Attr     Size(Byte)  Date        Time(LMT)  FileName
       0  -rw-          1,235  Dec 17 2009 17:10:53   vrpcfg.cfg
       1  -rw-        524,575  Jan 25 2010 10:03:33   private-data.txt
       2  drw-              -  Sep 09 2009 09:42:52   src
       3  drw-              -  Sep 09 2009 09:42:53   logfile
       4  -rw-            280  Sep 09 2009 09:42:53   $_patch_rollback_state
       5  -rw-         11,772  Nov 25 2009 16:56:55   $_patchstate_a
       6  -rw-              4  Jan 19 2010 03:09:32   snmpnotilog.txt
       7  drw-              -  Sep 09 2009 09:43:00   lam
       8  -rw-          2,584  Jan 21 2010 12:02:18   vrpcfg.cfg
       9  drw-              -  Jan 21 2010 11:09:21   logfilelogfile
   
   180,862 KB total (305,358 KB free)
   ```
3. Copy **slave#cfcard:/sample.txt** to **cfcard:/sample1.txt**.
   
   
   ```
   <HUAWEI> copy slave#cfcard:/sample.txt cfcard:/sample1.txt
   ```
   ```
   Copy slave#cfcard:/sample.txt to cfcard:/sample1.txt?[Y/N]: y
   ```
   ```
   .100%  complete
   ```
   ```
   Info:Copied file slave#cfcard:/sample.txt to cfcard:/sample1.txt...Done.
   ```
4. Check that the file is copied to the specified directory.
   
   
   ```
   <HUAWEI> dir
   ```
   ```
   Directory of cfcard:/
     Idx  Attr     Size(Byte)  Date        Time(LMT)  FileName
       0  -rw-          1,235  Dec 17 2009 17:10:53   vrpcfg.cfg
       1  -rw-        524,575  Jan 25 2010 10:03:33   private-data.txt
       2  drw-              -  Sep 09 2009 09:42:52   src
       3  drw-              -  Sep 09 2009 09:42:53   logfile
       4  -rw-            280  Sep 09 2009 09:42:53   $_patch_rollback_state
       5  -rw-         11,772  Nov 25 2009 16:56:55   $_patchstate_a
       6  -rw-              4  Jan 19 2010 03:09:32   snmpnotilog.txt
       7  drw-              -  Sep 09 2009 09:43:00   lam
       8  -rw-          2,584  Jan 21 2010 12:02:18   vrpcfg.cfg
       9  drw-              -  Jan 21 2010 11:09:21   logfilelogfile
      10  drw-          1,605  Jan 23 2010 14:30:32   sample1.txt
   
   180,864 KB total (305,356 KB free)
   ```