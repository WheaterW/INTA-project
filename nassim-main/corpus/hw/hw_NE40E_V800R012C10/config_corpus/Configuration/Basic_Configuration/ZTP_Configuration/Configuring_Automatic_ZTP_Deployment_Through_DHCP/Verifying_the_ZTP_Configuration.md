Verifying the ZTP Configuration
===============================

Verifying the ZTP Configuration

#### Procedure

1. After the ZTP process is complete, log in to the device and run the [**display startup**](cmdqueryname=display+startup) command to check whether the device startup file is as required.
2. Run the [**display ztp status**](cmdqueryname=display+ztp+status) command to check whether automatic deployment is complete through ZTP.
3. If automatic deployment fails, analyze ZTP logs on the device to determine the failure causes.
   
   
   
   ZTP logs are saved to the file named **ztp\_***YYYYMMDDHHMMSS***.log** in the directory **cfcard:/ztp**.