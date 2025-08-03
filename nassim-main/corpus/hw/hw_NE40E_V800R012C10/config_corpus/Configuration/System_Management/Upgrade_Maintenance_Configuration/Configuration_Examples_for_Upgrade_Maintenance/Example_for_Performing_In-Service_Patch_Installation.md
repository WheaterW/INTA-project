Example for Performing In-Service Patch Installation
====================================================

This section provides an example for installing patches without interrupting services.

#### Networking Requirements

In-service patch installation can be performed on a device if the device performance needs to be optimized without affecting the use of the current system software and the device must work uninterruptedly for a long time.

As shown in [Figure 1](#EN-US_TASK_0172361364__fig2172913514), the performance of DeviceA needs to be optimized. Huawei has provided a patch file for the customer to install.

**Figure 1** Networking diagram for performing in-service patch installation  
![](figure/en-us_image_0000001493555118.png)

#### Precautions

* The patch file versions on the active and standby main control boards must be the same.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Upload a patch file to the storage medium of the main control board.
2. Load and run the patch.
3. Verify the configuration.

#### Data Preparation

To complete the configuration, you need the following data:

* Username and password used by the SFTP client for login, which in this example are **user1** and **YsHsjx\_202206**, respectively.
* IP address of the SFTP server, which is **10.1.1.1** in this example.

* Name of the patch, which is **V\*\*\*R\*\*\*SPH001.pat** in this example
* Patch file storage path on the main control board, which is **cfcard:/** in this example

#### Procedure

1. Configure a device as an SFTP server.
   
   
   
   For configuration details, see [Example for Using SFTP to Operate Files](dc_vrp_vfm_cfg_0026.html).
2. Upload the new patch file to the SFTP server.
   
   
   
   # Run the [**sftp**](cmdqueryname=sftp) *10.1.1.1* command on the CLI of the PC to set up an SFTP connection with DeviceA. Then run the [**put**](cmdqueryname=put) command to upload the new patch file V\*\*\*R\*\*\*SPH001.pat to DeviceA.
   
   After the patch file is uploaded successfully, run the **[**dir**](cmdqueryname=dir)** command on DeviceA to view the uploaded patch file.
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
       1  -rw-     85,925,409  Apr 16 2012 13:18:02   NE40EV800R023C00SPC500B063.cc
       2  -rw-              4  Oct 27 2011 17:25:22   snmpnotilog.txt
       3  -rw-          6,033  Jul 16 2012 16:40:02   private-data.txt
       4  -rw-          3,275  Jul 14 2012 14:18:08   vrpcfg.zip
       5  drw-              -  Nov 14 2011 19:14:26   sysdrv 
       6  drw-     88,239,759  Jul 16 2012 19:14:26   V***R***SPH001.pat
   
   670,092 KB total (569,904 KB free)
   ```
3. If the device has a standby main control board, copy the patch file to the storage medium of the standby main control board.
   
   
   ```
   <DeviceA> copy cfcard:/V***R***SPH001.pat slave#cfcard:/
   ```
   ```
   Copy cfcard:/V***R***SPH001.pat to slave#cfcard:/?[Y/N]:Y
   Info:Copied file cfcard:/V***R***SPH001.pat to slave#cfcard:/...Done
   ```
4. Load and run the patch.
   
   
   ```
   <DeviceA> patch load V***R***SPH001.pat all run
   ```
   ```
   Info: Operating, please wait for a moment......done.
   Info: Succeeded in running the patch.
   ```
5. Verify the configuration.
   
   
   
   After the preceding configurations, run the [**display patch-information**](cmdqueryname=display+patch-information) command, and you can view patches in the running state on DeviceA.
   
   ```
   <DeviceA> display patch-information
   ```
   ```
   Patch Package Name    :cfcard:/V***R***SPH001.PAT
   Patch Package Version :V***R***SPH001
   Patch Package State   :Running   
   Patch Package Run Time:2011-11-07 11:55:01
   ```

#### Configuration Files

None