configuration file auto-save backup-to-server
=============================================

configuration file auto-save backup-to-server

Function
--------



The **configuration file auto-save backup-to-server server** command configures the system to periodically save the configuration file to an IPv4 server.

The **undo configuration file auto-save backup-to-server server** command disables the system from periodically saving the configuration file to an IPv4 server.

The **configuration file auto-save backup-to-server server ipv6** command configures the system to periodically save the configuration file to an IPv6 server.

The **undo configuration file auto-save backup-to-server server ipv6** command disables the system from periodically saving the configuration file to an IPv6 server.



By default, the system does not periodically save configurations to a server.


Format
------

**configuration file auto-save backup-to-server server** *server-ip* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **tftp** | { **ftp** | **sftp** } [ **port** *port-value* ] **user** *user-name* **password** *password* } [ **path** *folder* ]

**configuration file auto-save backup-to-server server** *server-ip* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **sftp** [ **port** *port-value* ] **user** *user-name* **password** }

**configuration file auto-save backup-to-server server** *server-ip* [ **vpn-instance** *vpn-instance-name* ] **path** *folder*

**configuration file auto-save backup-to-server server ipv6** *server-ip* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **tftp** | { **ftp** | **sftp** } [ **port** *port-value* ] **user** *user-name* **password** *password* } [ **path** *folder* ]

**configuration file auto-save backup-to-server server ipv6** *server-ip* [ **vpn-instance** *vpn-instance-name* ] **path** *folder*

**configuration file auto-save backup-to-server server ipv6** *server-ip* [ **vpn-instance** *vpn-instance-name* ] **transport-type** { **sftp** [ **port** *port-value* ] **user** *user-name* **password** }

**undo configuration file auto-save backup-to-server server** [ *server-ip* | *server-ip* **vpn-instance** *vpn-instance-name* | *server-ip* **vpn-instance** *vpn-instance-name* **port** *port-value* ]

**undo configuration file auto-save backup-to-server server ipv6** [ *server-ip* | *server-ip* **vpn-instance** *vpn-instance-name* | *server-ip* **vpn-instance** *vpn-instance-name* **port** *port-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **transport-type** | Indicates the transmission mode. | The value can be ftp, tftp, or sftp. |
| **tftp** | Specifies the transmission mode is TFTP. | - |
| **ftp** | Specifies the transmission mode is FTP. | - |
| **sftp** | Specifies the transmission mode is SFTP. | - |
| **port** *port-value* | Specifies the port number used to send a configuration file to a server. | The value is an integer ranging from 1 to 65535. |
| **user** *user-name* | Specifies the name of the user that accesses the server using FTP or SFTP. | The value is a string of 1 to 64 characters without spaces.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| **password** *password* | Specifies the password of the user that accesses the server using FTP or SFTP. | In the case of a password in plaintext, the value is a string of 1 to 255 case-sensitive characters without spaces. In the case of a ciphertext password, the value is a string of 20 to 432 case-sensitive characters without spaces. A 24-character ciphertext password configured in an earlier version is also supported in this version.  Except the question mark (?) and space. However, when quotation marks (") are used around the password, spaces are allowed in the password. |
| **path** *folder* | Specifies the path of the configuration file on the server. If this parameter is not configured, the root path of FTP, SFTP, or TFTP services is used by default. | The value is a string of 1 to 64 case-sensitive characters. |
| **server** *server-ip* | Specifies the IP address of the server to which the system periodically saves the configuration file. | The IP address is in dotted decimal notation. |
| **ipv6** *server-ip* | Specifies the IPv6 address of the server to which the system periodically saves the configuration file. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To back up the configuration file, you can run this command to specify a server. The configuration file is automatically saved to the specified server, improving database security.
* The format of the configuration file backed up to the server is the same as that of the configuration file for next startup. If the configuration file for next startup is in .dat format, the generated configuration file is in .dat format. If the configuration file for next startup is in .cfg or .zip format, the generated configuration file is in .zip format. The configuration file backed up to the server is named in the format of date, time, and system name. The names of the configuration files backed up at different time are different and do not overwrite the previous backup files.
* You can run this command multiple times to configure multiple file servers.

**Prerequisites**

Before running this command, run the **configuration file auto-save** command to enable the automatic saving function and enable the FTP, SFTP, or TFTP service on the server.The interval for periodically saving configurations depends on the interval configured using the **configuration file auto-save** command.Alternatively, run the **configuration current backup-to-server monthly** command to enable monthly configuration backup to the server. (Note that this function does not save the configuration file for the next startup and only uploads the current running configuration to the server.)

**Precautions**

* The system supports a maximum of five file servers. The servers are independent of each other. If the file fails to be uploaded to a server path, the system reports an alarm to the NMS and records a log on the device.
* During the configuration file upload, if the automatic saving time arrives, the device does not save the configuration file until all configuration files are uploaded.
* The time of the configuration file generated by running this command is the UTC time.
* After the bound VPN is deleted, the configuration is not cleared, and the VPN ID is set to the default value. If a VPN with the same name is reconfigured, the corresponding VPN ID is updated.
* If the same IP address but different VPN instances are configured using the **configuration file auto-save backup-to-server** command, only the latest configuration takes effect.
* When you run this command to save the configuration file to the server, the system supports only the binary transfer mode. The server must support the binary transfer mode.
* The configuration file auto-save backup-to-server server [ ipv6 ] server-ip [ vpn-instance vpn-instance-name ] transport-type { sftp [ port port-value ] user user-name password } command is supported only in FIPS mode.
* The configuration file auto-save backup-to-server server [ ipv6 ] server-ip [ vpn-instance vpn-instance-name ] path folder command is supported only in FIPS mode.
* The specified path parameter folder can be a relative path or an absolute path. If the value is a relative path, the root path of the relative path is the root path of the FTP, SFTP, or TFTP server.
* The value of port-value must be the same as the port number of the FTP, SFTP, or TFTP server.


Example
-------

# Configure the system to periodically save configuration files to a server using the transmission mode TFTP.
```
<HUAWEI> system-view
[~HUAWEI] configuration file auto-save backup-to-server server 10.1.1.1 transport-type tftp

```

# Configure the system to periodically save configuration files to a server by FTP with the port number of 88.
```
<HUAWEI> system-view
[~HUAWEI] configuration file auto-save backup-to-server server 10.1.1.1 transport-type ftp port 88 user huawei password YsHsjx_202206

```

# Configure the system to periodically save the configuration file to the server. Set the transfer mode to FTP, port number to 88, and path to D:/FTP/TEST.
```
<HUAWEI> system-view
[~HUAWEI] configuration file auto-save backup-to-server server 10.1.1.1 transport-type ftp port 88 user huawei password YsHsjx_202206 path D:/FTP/TEST

```