ftp ipv6 server acl
===================

ftp ipv6 server acl

Function
--------



The **ftp ipv6 server acl** command configures the ACL to control the access of clients to the FTP server.

The **undo ftp ipv6 server acl** command cancels the configuration of the ACL.



By default, no ACL is configured for FTP server.


Format
------

**ftp ipv6 server acl** { *acl-number* | *name* }

**undo ftp ipv6 server acl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the basic or advanced ACL number. | ACL number is an integer data type. The basic acl number value ranges from 2000 to 2999, the advanced acl number value ranges from 3000 to 3999. |
| *name* | Specifies the ACL name. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces and starts with a letter (a to z or A to Z). |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a device serves as FTP server, you can configure the ACL on the device to control the login of the clients to the device.FTPS only supports ACL matching based on the following parameters: source IP address, destination IP address, source port number, destination port number, and VPN.

**Precautions**

If no rule is configured, the incoming and outgoing calls are not restricted after the command ftp server acl is run.


Example
-------

# Allow the client whose ACL name is acl1 to log in to the FTP server.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name acl1
[*HUAWEI-acl6-advance-acl1] quit
[*HUAWEI] ftp ipv6 server acl acl1

```

# Set the ACL number as 2000 to access the FTP server.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] ftp ipv6 server acl 2000

```