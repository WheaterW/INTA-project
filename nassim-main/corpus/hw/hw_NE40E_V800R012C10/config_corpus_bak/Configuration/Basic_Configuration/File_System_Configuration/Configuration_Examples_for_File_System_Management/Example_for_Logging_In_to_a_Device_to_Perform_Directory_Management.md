Example for Logging In to a Device to Perform Directory Management
==================================================================

This section provides an example for logging in to a device to perform directory management, such as viewing and copying directories.

#### Networking Requirements

You can log in to a device through a console port or using Telnet or STelnet to manage directories on the device.


#### Precautions

* To log in to a device through a console port, you must prepare a terminal and an RS-232 cable.
* To log in to a device using Telnet or STelnet, you must have configured a Telnet or STelnet server and ensure that the server and terminal are routable.
  
  For detailed configurations, see [User Login Configuration](dc_vrp_basic_cfg_0024.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, login through a console port is used to manage directories.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure login through a console port.
2. View the current directory.
3. Create a directory.
4. Check that the new directory is created.

#### Data Preparation

To complete the configuration, you need the following data:

* Name of the directory to be created

#### Procedure

1. Configure login through a console port.
   
   
   
   For detailed configurations, see [Example for Configuring Login Through a Console Port](dc_vrp_basic_cfg_0046.html).
2. View the current directory.
   
   
   ```
   <HUAWEI> dir
   ```
   ```
   Directory of cfcard:/
   ```
   ```
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
3. Create a directory in the root directory.
   
   
   ```
   <HUAWEI> mkdir abc
   ```
   ```
   Info:Create directory cfcard:/abc/......Done.
   ```
4. View the current directory. The command output shows that the new directory has been created.
   
   
   ```
   <HUAWEI> dir
   ```
   ```
   Directory of cfcard:/
   ```
   ```
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
       10  drw-             -  Jan 23 2010 11:10:42   abc
   180,862 KB total (305,358 KB free)
   ```