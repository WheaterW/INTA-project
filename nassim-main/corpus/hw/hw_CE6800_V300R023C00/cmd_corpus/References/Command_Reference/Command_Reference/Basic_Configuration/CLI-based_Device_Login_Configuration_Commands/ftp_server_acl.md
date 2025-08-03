ftp server acl
==============

ftp server acl

Function
--------



The **ftp server acl** command configures the ACL to control the access of clients to the FTP server.

The **undo ftp server acl** command cancels the configuration of the ACL.



By default, no ACL is configured for FTP server.


Format
------

**ftp server acl** { *acl-number* | *name* }

**undo ftp server acl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the basic or advanced ACL number. | ACL number is an integer data type. The basic acl number value ranges from 2000 to 2999, the advanced acl number value ranges from 3000 to 3999. |
| *name* | Specifies the ACL name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The value must start with a letter (a to z or A to Z) and cannot contain only digits. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a device functions as an FTP server, you can configure an ACL on the device to control the clients that can log in to the device through FTP.The FTP server supports ACL filtering only based on the source IP address, destination IP address, source port number, destination port number, and VPN parameters.For details about ACL configuration commands, see ACL4 Configuration Commands in the Command Reference - IP Addresses and Services.

**Precautions**

* If no ACL rule is configured, the incoming and outgoing calls are not restricted after the command is executed.
* The **ftp acl** command takes effect only on IPv4 clients.
* The FTP protocol has security risks. You are advised to use the SFTP protocol.

Example
-------

# Allow the client whose ACL name is acl1 to log in to the FTP server.
```
<HUAWEI> system-view
[~HUAWEI] acl name acl1
[*HUAWEI-acl4-advance-acl1] quit
[*HUAWEI] ftp server acl acl1

```