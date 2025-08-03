Configuring DHCP Snooping File Integrity Check
==============================================

Configuring DHCP Snooping File Integrity Check

#### Security Policy

To prevent data loss caused by device faults, you can enable automatic backup of the DHCP snooping binding table. After the function is enabled, the system generates a backup file. An encrypted file integrity check code is added to the backup file to prevent tampering. After the device restarts, the system decrypts this code and uses it to verify the file integrity before restoring the binding table from the backup file. If the verification is successful, the data is restored; otherwise, it is discarded and a **DHCP\_FILE\_RECOVER\_FAIL** log is recorded.


#### Attack Methods

An attacker tampers with the binding table backup file. After the device restarts, an incorrect binding table is generated. As a result, invalid packets can be forwarded.


#### Configuration and Maintenance Methods

Set the file integrity authentication mode to force-check in the system view.

```
<HUAWEI> system-view
[~HUAWEI] dhcp snooping database authentication-mode force-check
[*HUAWEI] commit
```

#### Configuration and Maintenance Suggestions

If you use a backup file generated on another device to restore data, run the **dhcp snooping database authentication-mode no-check** command to set the file integrity authentication mode to no-check before the restart.

To forcibly check whether data is tampered with based on an earlier version of a file, run the **dhcp snooping database authentication-mode force-check** command to set the file integrity authentication mode to force-check before a restart.


#### Verifying the Security Hardening Result

Run the **display dhcp snooping global** command to check the DHCPv4 snooping file integrity authentication mode.