Uploading a Patch File
======================

This part describes how to upload a patch file to the storage medium of a device.

#### Procedure

1. Upload a patch file to the storage medium of the AMB.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The device can use FTP and TFTP to transfer files. For details, see [Using FTP to Access Other Devices](dc_vrp_basic_cfg_0094.html) and [Using TFTP to Access Other Devices](dc_vrp_basic_cfg_0088.html). Choose FTP or TFTP as needed to upload files to the device.
2. (Optional) In the user view, run [**copy**](cmdqueryname=copy) *source-filename destination-filename*
   
   
   
   A patch file is copied to the storage medium of the SMB.

#### Follow-up Procedure

Run the [**check patch**](cmdqueryname=check+patch) { *file-name* | **startup** } command to check the integrity of the patch file before it is installed in the system.