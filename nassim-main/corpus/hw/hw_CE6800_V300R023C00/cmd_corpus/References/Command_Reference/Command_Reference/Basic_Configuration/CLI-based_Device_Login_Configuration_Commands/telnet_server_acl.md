telnet server acl
=================

telnet server acl

Function
--------



The **telnet server acl** command configures the ACL to control the access of clients to the Telnet server.

The **undo telnet server acl** command cancels the configuration of the ACL.



By default, no ACL is configured.


Format
------

**telnet server acl** { *acl4name* | *acl4num* }

**telnet ipv6 server acl** { *acl6name* | *acl6num* }

**undo telnet server acl**

**undo telnet ipv6 server acl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl4name* | Specifies the ACL4 name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The value must start with a letter (a to z or A to Z) and cannot contain only digits. |
| *acl4num* | Specifies the IPv4 ACL number. | ACL number is an integer data type. The basic acl number value ranges from 2000 to 2999, the advanced acl number value ranges from 3000 to 3999. |
| **ipv6** | Filter IPv6 addresses. | - |
| *acl6name* | Specifies the ACL6 name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The value must start with a letter (a to z or A to Z) and cannot contain only digits. |
| *acl6num* | Specifies the IPv6 ACL number. | ACL number is an integer data type. The basic acl number value ranges from 2000 to 2999, the advanced acl number value ranges from 3000 to 3999. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a device functions as a server, you can configure an ACL on the device to control the Telnet clients that log in to the device through Telnet.

* A basic ACL can be used to restrict source addresses, and an advanced ACL can be used to restrict both source and destination addresses.
* The Telnet server supports ACL filtering only based on the source address, destination address, source port number, destination port number, and VPN parameters.

**Precautions**

* The Telnet protocol has security risks. You are advised to use the SSHv2 protocol.
* If no ACL rule is configured, the incoming and outgoing calls are not restricted after the acl command is executed.
* The **telnet server acl** command takes effect only for IPv4.

Example
-------

# Set ACL rule 2000 to Telnet server.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] telnet server acl 2000

```

# Set the ACL6 name to test for the Telnet server.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name test
[*HUAWEI-acl6-advance-test] quit
[*HUAWEI] telnet ipv6 server acl test

```