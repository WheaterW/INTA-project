Configuring DHCPv6 Snooping File Integrity Check
================================================

Configuring DHCPv6 Snooping File Integrity Check

#### Security Policy

To prevent data loss caused by device faults, you can enable automatic backup of the DHCPv6 snooping binding table. After the function is enabled, the system generates a backup file. An encrypted file integrity check code is added to the backup file to prevent tampering. After the device restarts, the system decrypts this code and uses it to verify the file integrity before restoring the binding table from the backup file. If the verification is successful, the data is restored; otherwise, it is discarded and a log is recorded.


#### Attack Methods

An attacker tampers with the binding table backup file. After the device restarts, an incorrect binding table is generated. As a result, invalid packets can be forwarded.


#### Configuration and Maintenance Methods

Set the file integrity authentication mode to force-check in the system view.

```
<HUAWEI> system-view
[~HUAWEI] dhcpv6 snooping database authentication-mode force-check
[*HUAWEI] commit
```

#### Configuration and Maintenance Suggestions

If you use a backup file generated on another device to restore data, run the **dhcpv6 snooping database authentication-mode no-check** command to set the file integrity authentication mode to no-check before the restart.

To forcibly check whether data is tampered with based on an earlier version of a file, run the **dhcpv6 snooping database authentication-mode force-check** command to set the file integrity authentication mode to force-check before a restart.