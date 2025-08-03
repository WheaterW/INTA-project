ssh server acl
==============

ssh server acl

Function
--------



The **ssh server acl** command configures the ACL to control the access of clients for STelnet, SFTP, SCP and SNETCONF.

The **undo ssh server acl** command cancels the ACL configuration.



By default, no ACL is configured.


Format
------

**ssh server acl** { *acl4name* | *acl4num* }

**ssh ipv6 server acl** { *acl6name* | *acl6num* }

**undo ssh server acl**

**undo ssh ipv6 server acl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl4name* | Specifies the ACL4 name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *acl4num* | Specifies the IPv4 ACL number. | ACL number is an integer data type. The basic acl number value ranges from 2000 to 2999, the advanced acl number value ranges from 3000 to 3999. |
| **ipv6** | IPv6 protocol. | - |
| *acl6name* | Specify the ACL6 name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *acl6num* | Specifies the ACL6 number. | ACL number is an integer data type. The basic acl number value ranges from 2000 to 2999, the advanced acl number value ranges from 3000 to 3999. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a device serves as

* STelnet client, you can configure the ACL on the device to control the login of the local device to the STelnet server through STelnet.
* SFTP client, you can configure the ACL on the device to control the login of the local device to the SFTP server through SFTP.
* SFTP client, you can configure the ACL on the device to control the login of the local device to the SCP server through SFTP.
* SNETCONF client, you can configure the ACL on the device to control the login of the local device to the SNETCONF server through SNETCONF.

**Prerequisites**

Run the **acl** command to create an ACL.


Example
-------

# Set ACL rule 2000 to ssh server.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] ssh server acl 2000

```

# Set the ACL6 name of the SSH server to test.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name test
[*HUAWEI-acl6-advance-test] quit
[*HUAWEI] ssh ipv6 server acl test

```