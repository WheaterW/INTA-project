Restoring DHCP Snooping Binding Entries
=======================================

Restoring DHCP Snooping Binding Entries

#### Context

After DHCP snooping binding entries are backed up, you can restore them when needed.


#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Restore DHCP snooping binding entries from a specified file.
   
   
   ```
   [dhcp snooping user-bind recover](cmdqueryname=dhcp+snooping+user-bind+recover) file-name
   ```