Backing Up the Configuration File to the Storage Medium
=======================================================

Backing Up the Configuration File to the Storage Medium

#### Context

You can back up the configuration file to the storage medium. The backup configuration file can be used if the configuration file restoration fails due to unexpected device damage.


#### Procedure

1. (Optional) Save the configuration file.
   
   
   ```
   [save](cmdqueryname=save) configuration-file
   ```
2. Copy the configuration file to the storage medium.
   
   
   ```
   [copy](cmdqueryname=copy) source-filename destination-filename
   ```