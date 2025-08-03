Configuring Software Rollback Prevention
========================================

Configuring Software Rollback Prevention

#### Context

Earlier software versions generally have more vulnerabilities. Attackers can exploit the vulnerabilities to penetrate the software system. To significantly reduce this risk, you can use the function that prevents system software from being rolled back to an earlier version without authentication or authorization.

Currently, there are two modes of this function:

* Secure version mode
  
  After startup, the device checks whether the secure software version in each slot is earlier than the specified secure version in the CPU. If so, the slot reports an alarm to prompt the user to upgrade the secure version. Once the software is upgraded to the target secure version, it cannot be rolled back to the previous version.
  
  This mode applies only to basic software packages.
* Version revoke list (VRL) file mode:
  
  The VRL file specifies the system software of an earlier version that has vulnerabilities. After the VRL file is loaded to the device, the system software cannot be rolled back to a version in the VRL file.
  
  This mode applies to all software packages, including basic software packages, feature software packages, patch files, and module files.

These two modes can be used together.


#### Procedure

* Upgrading the secure version
  
  
  1. (Optional) Check the secure version of the device.
     ```
     [display startup secure-version](cmdqueryname=display+startup+secure-version)
     ```
     
     If the value of the **Status** field is **Need refresh** in the command output, the secure version needs to be upgraded. If the value of the **Status** field is **Unsupport**, the device does not support the secure version mode. In this case, the device supports only the VRL file mode.
  2. Upgrade the secure version of the device.
     ```
     [refresh startup secure-version](cmdqueryname=refresh+startup+secure-version) { slot slot-name | all }
     ```
* Loading a VRL file
  
  
  1. Load a VRL file to the system.
     ```
     [software vrl load](cmdqueryname=software+vrl+load) vrlName
     ```

#### Verifying the Configuration

Run the [**display startup secure-version**](cmdqueryname=display+startup+secure-version) command to check the information about the secure version of the device.

Run the [**display software vrl**](cmdqueryname=display+software+vrl) command to check information about the loaded VRL file.