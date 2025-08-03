Backing Up DHCP Snooping Binding Entries
========================================

Backing Up DHCP Snooping Binding Entries

#### Context

DHCP snooping binding entries that are not backed up will be lost after the device restarts. In this case, DHCP users must go online again so that the device generates DHCP snooping binding entries for them. If DHCP snooping binding entries are backed up, they can be restored after the device restarts, ensuring that the preceding problem does not occur. Such entries can be automatically backed up to a local device or a remote SFTP server. To back up the entries to a remote SFTP server, you need to compile a script based on the OPS API. For details, see "Example for Configuring the Function of Automatically Backing Up DHCP Snooping Binding Entries to a Remote Server (Based on a Script Assistant)" in Configuration Guide > System Management Configuration > OPS Configuration.


#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Enable local automatic backup for DHCP snooping binding entries.
   
   
   ```
   [dhcp snooping user-bind autosave](cmdqueryname=dhcp+snooping+user-bind+autosave) file-name [ write-delay delay-time ]
   ```
   
   By default, local automatic backup is disabled for DHCP snooping binding entries.