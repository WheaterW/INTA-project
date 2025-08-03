tftp server acl
===============

tftp server acl

Function
--------



The **tftp server acl** command configures the ACL to control the access of clients to the FTP server.

The **undo tftp server acl** command cancels the configuration of the ACL.



By default, no ACL is configured for the TFTP client.


Format
------

**tftp server acl** { *acl-number* | *acl4-name* }

**undo tftp server acl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the IPv4 ACL number. | The number of a basic ACL is an integer that ranges from 2000 to 2999. |
| *acl4-name* | Specifies the ACL4 name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The value must start with a letter (a to z or A to Z) and cannot contain only digits. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a device functions as a TFTP client, you can configure an ACL on the device to control the TFTP servers that the device can log in to through TFTP.

* A basic ACL can be used to restrict source addresses, and an advanced ACL can be used to restrict both source and destination addresses.
* The TFTP server supports ACL filtering only based on the source address, destination address, source port number, destination port number, and VPN parameters.

**Precautions**

If no rule is configured, the incoming and outgoing calls are not restricted after the command tftp server acl is run.The command tftp server acl takes effect for ipv4 function.


Example
-------

# Set ACL rule 2000 to TFTP server.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] tftp server acl 2000

```