tftp server ipv6 acl
====================

tftp server ipv6 acl

Function
--------



The **tftp server ipv6 acl** command enables the IPv6-based ACL configuration.

The **undo tftp server ipv6 acl** command cancels the IPv6-based access control of the TFTP server that the local device can access.



By default, no ACL is configured for the TFTP client.


Format
------

**tftp server ipv6 acl** { *acl6-number* | *acl6-name* }

**undo tftp server ipv6 acl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies the IPv6 ACL number. | ACL number is an integer data type. The basic acl number value ranges from 2000 to 2999. |
| *acl6-name* | Specifies the ACL6 name. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a device serves as a TFTP client, you can configure the ACL on the device to control the login of the local device to the TFTP server through TFTP.

**Precautions**

If no rule is configured, the incoming and outgoing calls are not restricted after the command tftp server acl is run.


Example
-------

# Enable the ipv6 ACL configuration on a TFTP server.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name test
[*HUAWEI-acl6-advance-test] quit
[*HUAWEI] tftp server ipv6 acl test

```