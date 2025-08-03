(Optional) Configuring the Function to Save or Restore DHCPv6 Data
==================================================================

(Optional) Configuring the Function to Save or Restore DHCPv6 Data

#### Context

When the device functions as a DHCPv6 server, you can enable the device to save or restore DHCPv6 data. This avoids data loss caused by device faults. After the function to save DHCPv6 data is enabled, the device saves DHCPv6 data at a specified interval in the **lease.txt** and **conflict.txt** files under the **dhcpv6** folder in the CF card. The data includes the last data saving time, names of IPv6 address pools, client DUIDs, IAIDs, IPv6 addresses and prefixes bound to client DUIDs and IAIDs, conflicting addresses, and conflict detection time. You can restore DHCPv6 data from the [**lease.txt**](cmdqueryname=lease.txt) and [**conflict.txt**](cmdqueryname=conflict.txt) files after the system restarts from a failure.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 server database**](cmdqueryname=dhcpv6+server+database) { **enable** | **recover** | **write-delay** *interval* }
   
   
   
   The function to save or restore DHCPv6 data is enabled.
   
   
   
   You can specify **write-delay** to modify the interval at which DHCPv6 data is saved. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An encrypted file integrity check code is added to the **lease.txt** and **conflict.txt** files to prevent tampering. After the device restarts, the system decrypts this code and uses it to verify the file integrity before restoring the address lease and conflict information from the **lease.txt** and **conflict.txt** files. If the verification is successful, the data is restored; otherwise, it is discarded and a log is recorded.
   
   * If you manually modify the content of a file, run the [**dhcpv6 server database authentication-mode no-check**](cmdqueryname=dhcpv6+server+database+authentication-mode+no-check) command to set the file integrity authentication mode to no-check before the restart.
   * The root keys for decrypting and encrypting the file integrity check code must be the same. Otherwise, the decryption fails. The root key on each device is unique to that device. If you use a backup file generated on another device to restore data, run the [**dhcpv6 server database authentication-mode no-check**](cmdqueryname=dhcpv6+server+database+authentication-mode+no-check) command to set the file integrity authentication mode to no-check before the restart.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.