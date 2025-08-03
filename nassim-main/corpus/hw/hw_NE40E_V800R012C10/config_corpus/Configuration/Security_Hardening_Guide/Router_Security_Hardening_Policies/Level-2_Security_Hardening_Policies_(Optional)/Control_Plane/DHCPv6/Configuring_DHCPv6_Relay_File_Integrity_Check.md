Configuring DHCPv6 Relay File Integrity Check
=============================================

Configuring DHCPv6 Relay File Integrity Check

#### Security Policies

To prevent data loss caused by device faults, you can enable automatic backup of prefix route information. After the function is enabled, the system generates a backup file. An encrypted file integrity check code is added to the backup file to prevent tampering. After the device restarts, the system decrypts this code and uses it to verify the file integrity before restoring prefix route information from the backup file. If the verification is successful, the data is restored; otherwise, it is discarded and a log is recorded.


#### Attack Methods

An attacker tampers with the backup file. After the device restarts, prefix route information is lost. As a result, downstream traffic of clients fails to be forwarded.


#### Configuration and Maintenance Methods

Set the file integrity authentication mode to force-check in the system view.

```
<HUAWEI> system-view
[~HUAWEI] dhcpv6 relay database authentication-mode force-check
[*HUAWEI] commit
```

#### Configuration and Maintenance Suggestions

If you use a backup file generated on another device to restore data, run the **dhcpv6 relay database authentication-mode no-check** command to set the file integrity authentication mode to no-check before the restart.

For compatibility with earlier versions, data can be restored based on an earlier version of a file that does not carry the file integrity check code after a restart. To forcibly check whether data is tampered with based on an earlier version of a file, run the **dhcpv6 relay database authentication-mode force-check** command to set the file integrity authentication mode to force-check before a restart.


#### Verifying the Security Hardening Result

Run the **display dhcpv6 relay configuration** command to check the DHCPv6 relay file integrity authentication mode.