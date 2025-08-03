Configuring DHCPv6 Server File Integrity Check
==============================================

Configuring DHCPv6 Server File Integrity Check

#### Security Policies

To prevent data loss caused by device faults, you can enable DHCPv6 address pool data saving and restoration. After the function is enabled, the system generates and saves the **lease.txt** and **conflict.txt** files in the **dhcpv6** folder on a CF card. The **lease.txt** and **conflict.txt** files store address lease and conflict information, respectively. An encrypted file integrity check code is added to the **lease.txt** and **conflict.txt** files to prevent tampering. After the device restarts, the system decrypts this code and uses it to verify the file integrity before restoring the address lease and conflict information from the **lease.txt** and **conflict.txt** files. If the verification is successful, the data is restored; otherwise, it is discarded and a log is recorded.


#### Attack Methods

An attacker tampers with the **lease.txt** and **conflict.txt** files. After the device restarts, the address lease and conflict information in the address pool are incorrect. As a result, the server may fail to assign addresses.


#### Configuration and Maintenance Methods

Set the file integrity authentication mode to force-check in the system view.

```
<HUAWEI> system-view
[~HUAWEI] dhcpv6 server database authentication-mode force-check
[*HUAWEI] commit
```

#### Configuration and Maintenance Suggestions

If you use a backup file generated on another device to restore data, run the **dhcpv6 server database authentication-mode no-check** command to set the file integrity authentication mode to no-check before the restart.

For compatibility with earlier versions, data can be restored based on an earlier version of a file that does not carry the file integrity check code after a restart. To forcibly check whether data is tampered with based on an earlier version of a file, run the **dhcpv6 server database authentication-mode force-check** command to set the file integrity authentication mode to force-check before a restart.


#### Verifying the Security Hardening Result

Run the **display dhcpv6 server database** command to check the DHCPv6 server file integrity authentication mode.