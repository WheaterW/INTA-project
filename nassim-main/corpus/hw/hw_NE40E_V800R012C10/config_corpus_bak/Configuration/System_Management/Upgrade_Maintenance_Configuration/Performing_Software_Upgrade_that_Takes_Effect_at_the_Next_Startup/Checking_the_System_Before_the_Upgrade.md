Checking the System Before the Upgrade
======================================

The system must be checked against the checklist to ensure a smooth upgrade.

#### Prerequisites

* Necessary hardware has been prepared.
* Software required for the upgrade has been obtained. The new system software (.cc file) and relevant documents for the upgrade must be obtained from Huawei.

#### Procedure

1. In the user view, run [**display version**](cmdqueryname=display+version)
   
   
   
   The version of the system software running on the device is checked.
2. Run the following commands to check the device status:
   
   
   * In the user view, run [**display health**](cmdqueryname=display+health)
     
     Memory usage of the main board on the device is displayed.
     
     If the value will lead upgrading the system software failed, reduce the value.
   * In the user view, run [**display alarm information**](cmdqueryname=display+alarm+information)
     
     Alarm information on the device is displayed.
     
     If alarm information is displayed in the command output, contact technical support personnel to check whether the device can be upgraded.
   * In the user view, run [**display device**](cmdqueryname=display+device)
     
     The operating status of main boards and interface boards is displayed.
     
     If the value of the Register field is Unregistered, the board in the specified slot cannot register. If the value of the Status field is Abnormal, the board in the specified slot functions improperly.
   * In the user view, run [**display logfile**](cmdqueryname=display+logfile) *path*
     
     The log file information is recorded.
     
     If a fault failed to be located during the upgrade, contact technical support personnel for troubleshooting.
3. Prepare the environment of upgrading the system software using FTP or TFTP. The current resource file can be backed up and the new resource file can be uploaded.
   
   
   
   When [upgrading the system software using FTP](dc_vrp_basic_cfg_0094.html), note the following points:
   
   * If the device to be upgraded functions as a client and the PC functions as a server, install FTP server software on the PC. The software needs to be purchased and installed separately.
   * If the device to be upgraded functions as a server and the PC functions as a client, you do not need to install FTP server software on the PC. The device to be upgraded can provide the FTP server function. By default, the FTP server function is disabled on the device to be upgraded. To enable it, run the [**ftp server enable**](cmdqueryname=ftp+server+enable) command in the system view.
   
   When [upgrading the system software using TFTP](dc_vrp_basic_cfg_0088.html), you must install TFTP server software on the PC. This is because the device to be upgraded can only function as a client and does not provide the TFTP server function.
4. In the user view, run [**copy**](cmdqueryname=copy) *source-filename destination-filename*
   
   
   
   Back up key data in the storage medium of the device to be upgraded.
5. In the user view, run [**dir**](cmdqueryname=dir) [ /[**all**](cmdqueryname=all) ] [ *filename* ]
   
   
   
   Check the remaining space of the storage medium to ensure that there is sufficient space for saving the target system software and related documents.