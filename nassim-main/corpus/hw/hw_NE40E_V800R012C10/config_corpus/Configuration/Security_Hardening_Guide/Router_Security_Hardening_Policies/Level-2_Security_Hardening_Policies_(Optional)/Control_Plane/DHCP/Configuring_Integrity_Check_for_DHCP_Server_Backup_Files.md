Configuring Integrity Check for DHCP Server Backup Files
========================================================

Configuring Integrity Check for DHCP Server Backup Files

#### Security Policy

To prevent data loss caused by device faults, you can run the **[**dhcp server database**](cmdqueryname=dhcp+server+database)** command to enable the DHCP data saving function. After the function is enabled, the system generates and saves the **lease.txt** and **conflict.txt** files in the **DHCP** folder on a CF card. The **lease.txt** and **conflict.txt** files store address lease and conflict information, respectively. After one-to-many mapping between one MAC address and many sessions is enabled on a device, the device generates an option82\_index.data file to save Option 82 information.

To configure an integrity authentication mode for the **lease.txt** and **conflict.txt** files, run the [**dhcp server database authentication-mode**](cmdqueryname=dhcp+server+database+authentication-mode) command. This prevents the files from being tampered with. After this command is run, an encrypted file integrity authentication code is added to the files. After the device restarts, the system decrypts this code and uses it to verify the file integrity before restoring the address lease and conflict information from the **lease.txt** and **conflict.txt** files. If the verification is successful, the data is restored; otherwise, it is discarded and a **DHCP\_FILE\_RECOVER\_FAIL** log is recorded.


#### Attack Methods

An attacker tampers with the **lease.txt** and **conflict.txt** files. After the device restarts, the address lease and conflict information in the address pool are incorrect. As a result, the server may fail to assign addresses.


#### Configuration and Maintenance Methods

Set the file integrity authentication mode to force-check in the system view.

```
<HUAWEI> system-view
[~HUAWEI] dhcp server database authentication-mode force-check
[*HUAWEI] commit
```

#### Configuration and Maintenance Suggestions

If you use a backup file generated on another device to restore data, set the file integrity authentication mode to no-check before a restart.

For compatibility with earlier versions, data can be restored based on an earlier version of a file that does not carry the file integrity check code after a restart. To forcibly check whether data is tampered with based on an earlier version of a file, set the file integrity authentication mode to force-check before a restart.


#### Verifying the Security Hardening Result

Run the **display dhcp server database** command to check the DHCPv4 server file integrity authentication mode.