snmp-agent acl
==============

snmp-agent acl

Function
--------



The **snmp-agent acl** command configures an ACL at SNMP protocol level.

The **undo snmp-agent acl** command deletes the ACL configuration at SNMP protocol level.



By default, no ACL is configured at SNMP protocol level.


Format
------

**snmp-agent acl** { *acl-number* | *aclName* }

**undo snmp-agent acl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of an ACL. | It is an integer ranging from 2000 to 3999. |
| *aclName* | Specifies an ACL name.  If no matching rule is configured for the referenced ACL, the matching rule is permit by default. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve security, run this command to allow only SNMP users included in ACL to access a specific device.If you need to specify an ACL when configuring an SNMP community name, SNMP group, or SNMP user, run this command first.

**Configuration Impact**



If the ACL configured using the **snmp-agent acl** command has the same name on IPv4 and IPv6 networks, the ACL takes effect on both IPv4 and IPv6 networks.




Example
-------

# Configure ACL 2000 for SNMP (including IPv4 and IPv6).
Note:
If only acl 2000 is specified, only IPv4 ACL 2000 takes effect after snmp-agent acl 2000 is configured.
If only acl ipv6 2000 is specified, only IPv6 ACL 2000 takes effect after snmp-agent acl 2000 is configured.
If both acl 2000 and acl ipv6 2000 are specified, ACL 2000 takes effect for both IPv4 and IPv6 after snmp-agent acl 2000 is configured.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] snmp-agent acl 2000

```