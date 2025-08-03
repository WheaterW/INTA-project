Example for Performing Software Upgrade that Takes Effect at the Next Startup
=============================================================================

This section provides configuration procedures for performing software upgrade that takes effect at the next startup. This will help you complete the configuration task quickly and accurately.

#### Networking Requirements

Software upgrade that takes effect at the next startup can be performed on a device if the current system software cannot provide additional features or larger specifications required by customers, and the device must work uninterruptedly for a long time.

As shown in [Figure 1](#EN-US_TASK_0172361362__fig034402255020), the system software of DeviceA cannot meet customer's requirements and needs to be upgraded. Huawei has provided related upgrade software files.

**Figure 1** Networking diagram for performing software upgrade that takes effect at the next startup  
![](figure/en-us_image_0000001493554698.png)

#### Precautions

* The key data in the storage medium on the device must be backed up to the PC.
* The CPU usage and the remaining space in the storage medium must meet the upgrade requirement.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Upload the new system software.
2. Specify the system software to be used at the next startup.
3. Restart the device.
4. Verify the configuration.

#### Data Preparation

To complete the configuration, you need the following data:

* Username and password used by the SFTP client for login, which in this example are **user1** and **YsHsjx\_202206**, respectively.
* IP address of the SFTP server, which is **10.1.1.1** in this example.

* System software source version, which is NE40EV800R023C00SPC500B000 in this example
* System software version to be specified, which is NE40EV800R023C00SPC500B003 in this example
* Remaining space of the storage medium for saving the new system software (if the remaining space is insufficient, release some space as required)

#### Procedure

1. Configure the device as an SFTP server.
   
   
   
   For configuration details, see [Example for Using SFTP to Operate Files](dc_vrp_vfm_cfg_0026.html).
2. Upload the new system software file to the SFTP server.
   
   
   
   # Run the [**sftp**](cmdqueryname=sftp) *10.1.1.1* command on the CLI of the PC to set up an SFTP connection with DeviceA, and then run the [**put**](cmdqueryname=put) command to upload the new system software file NE40EV800R023C00SPC500B003 to DeviceA.
   
   After the system software file is uploaded successfully, run the **[**dir**](cmdqueryname=dir)** command on DeviceA to view the uploaded system software file.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] quit
   ```
   ```
   <DeviceA> dir
   ```
   ```
   Directory of  cfcard:/
   
     Idx  Attr     Size(Byte)  Date        Time       FileName
       0  drw-              -  Apr 16 2012 13:19:58   logfile
       1  -rw-     85,925,409  Apr 16 2012 13:18:02   NE40EV800R023C00SPC500B000.cc
       2  -rw-              4  Oct 27 2011 17:25:22   snmpnotilog.txt
       3  -rw-          6,033  Jul 16 2012 16:40:02   private-data.txt
       4  -rw-          3,275  Jul 14 2012 14:18:08   vrpcfg.zip
       5  drw-              -  Nov 14 2011 19:14:26   sysdrv 
       6  drw-     88,239,759  Jul 16 2012 19:14:26   NE40EV800R023C00SPC500B003.cc
   
   670,092 KB total (569,904 KB free)
   ```
   
   
   
   # If the device has a standby main control board, copy the new system software file from the active main control board to the standby main control board.
   
   ```
   <DeviceA> copy cfcard:/NE40EV800R023C00SPC500B003.cc slave#cfcard:/
   ```
3. Specify the system software to be loaded at the next startup.
   
   
   
   # Specify the system software to be loaded at the next startup.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When you specify the system software package for next startup, the device automatically specifies the configuration file for next startup. You can run the [**reset saved-configuration**](cmdqueryname=reset+saved-configuration) command to clear the configuration file.
   
   ```
   <DeviceA> startup system-software NE40EV800R023C00SPC500B003.cc
   ```
   ```
   Succeeded in setting the software for booting system.
   ```
   ```
   <DeviceA> startup system-software NE40EV800R023C00SPC500B003.cc slave-board
   ```
   ```
   Succeeded in setting the software for booting system.
   ```
   
   # Check the system software to be loaded at the next startup and make sure that it is the specified version.
   
   ```
   <DeviceA> display startup
   ```
   ```
   MainBoard                               :
     Configured startup system software    : NE40EV800R023C00SPC500B000.cc
     Startup system software               : NE40EV800R023C00SPC500B000.cc
     Next startup system software          : NE40EV800R023C00SPC500B003.cc
     Startup saved-configuration file      :
     Next startup saved-configuration file : cfcard:/vrpcfg.zip
   SlaveBoard                              :
     Configured startup system software    : NE40EV800R023C00SPC500B000.cc
     Startup system software               : NE40EV800R023C00SPC500B000.cc
     Next startup system software          : NE40EV800R023C00SPC500B003.cc
     Startup saved-configuration file      :
     Next startup saved-configuration file : cfcard:/vrpcfg.zip
   ```
4. Restart DeviceA.
   
   
   
   # Restart DeviceA.
   
   ```
   <DeviceA> reboot
   ```
5. Verify the configuration.
   
   
   
   After DeviceA is restarted, run the [**display version**](cmdqueryname=display+version) command. If the version of the current system software in the command output is a target one, it means that the upgrade succeeds.
   
   The target system software version is NE40EV800R023C00SPC500B003.cc.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] display version
   ```
   ```
   Huawei Versatile Routing Platform Software
   VRP (R) software, Version 8.230 (NE40EV800R023C00SPC500)
   Copyright (C) 2012-2021 Huawei Technologies Co., Ltd.
   HUAWEI NE40E uptime is 0 day, 3 hours, 37 minutes
   ```

#### Configuration Files

None