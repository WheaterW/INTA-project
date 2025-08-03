Configuring Software Package Rollback
=====================================

Configuring Software Package Rollback

#### Context

Software package rollback applies to the following scenarios:

* A device is functioning properly, but the current software package must be rolled back to the source version to meet service requirements.
* After the system is upgraded, functions or services cannot be used properly, requiring the current software package to be rolled back to the source version.

You can roll back a software package in either of the following modes:

* Automatic mode: When a next-startup software package is specified or a software package is upgraded on an in-service device, the system automatically creates a rollback point. You can configure the rollback point for the next startup to roll back the software package.
* Manual mode: You can manually create a rollback point and configure the rollback point for the next startup to roll back a software package.

After a software package is successfully rolled back, the corresponding basic software package, feature software package, patch, and module file are all rolled back to the source version.


#### Procedure

1. Create a rollback point. Use either of the following methods to create a rollback point.
   
   
   * Configure the function of automatically creating a rollback point.
     1. Configure the function of automatically creating a rollback point.
        ```
        [undo startup checkpoint auto-save disable](cmdqueryname=undo+startup+checkpoint+auto-save+disable)
        ```
        
        After you run this command to enable the function of automatically creating a rollback point, the system automatically creates a rollback point when you run the [**startup system-software**](cmdqueryname=startup+system-software), [**startup feature-software**](cmdqueryname=startup+feature-software), or [**upgrade feature-software**](cmdqueryname=upgrade+feature-software) command.
        
        By default, the function of automatically creating a rollback point is enabled. To disable this function, run the [**startup checkpoint auto-save disable**](cmdqueryname=startup+checkpoint+auto-save+disable) command.
     2. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
   * Manually create a rollback point.
     ```
     [startup checkpoint](cmdqueryname=startup+checkpoint) checkpoint-name
     ```
     
     If a rollback point is not required, run the [**undo startup checkpoint**](cmdqueryname=undo+startup+checkpoint) *checkpoint-name* command to delete it.
2. Check the rollback point information and confirm the rollback point to which a software package needs to be rolled back.
   
   
   ```
   [display startup checkpoint](cmdqueryname=display+startup+checkpoint) [ checkpoint-name ] [verbose](cmdqueryname=verbose)
   ```
3. (Optional) Verify the rollback point.
   
   
   ```
   [check startup checkpoint](cmdqueryname=check+startup+checkpoint) checkpoint-name
   ```
   
   If the verification is successful, the rollback point can be used for rollback. Otherwise, the rollback point cannot be used for rollback.
4. Configure the rollback point for next startup.
   
   
   ```
   [restore startup checkpoint](cmdqueryname=restore+startup+checkpoint) checkpoint-name
   ```
5. Restart the device.
   
   
   ```
   [reboot](cmdqueryname=reboot)
   ```

#### Verifying the Configuration

Run the [**display startup**](cmdqueryname=display+startup) command to check whether the displayed information is the same as the file name of the software package to be rolled back.