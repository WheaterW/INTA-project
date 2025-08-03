acl (VTY-type user interface view)
==================================

acl (VTY-type user interface view)

Function
--------



The **acl** command restricts the incoming and outgoing calls on the user interface.

The **undo acl** command can cancels the current settings.



By default, there is no restriction on incoming and outgoing calls.


Format
------

**acl** { *acl4name* | *acl4num* } { **inbound** | **outbound** }

**acl ipv6** { *acl6name* | *acl6num* } { **inbound** | **outbound** }

**undo acl inbound**

**undo acl outbound**

**undo acl ipv6 inbound**

**undo acl ipv6 outbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl4name* | Specifies the name of ACL rule. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *acl4num* | Specifies the ID of an ACL. | For basic ACL, the value is an integer ranging from 2000 to 2999.  For advanced ACL, the value is an integer ranging from 3000 to 3999. |
| **inbound** | Restricts the incoming calls on the user interface. | - |
| **outbound** | Restricts the outgoing calls on the user interface. | - |
| **ipv6** | Specifies the IPv6 protocol. | - |
| *acl6name* | Specifies the name of ipv6 ACL rule. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *acl6num* | Specifies the ID of an ipv6 ACL. | For basic ACL, the value is an integer ranging from 2000 to 2999.  For advanced ACL, the value is an integer ranging from 3000 to 3999. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* Before running this command, you need to run the **acl** command and the rule command to configure the ACL.
* Only the ACL of the same type can be configured without conflict on a user interface, namely, IPv4 inbound, IPv4 outbound, IPv6 inbound, and IPv6 outbound. Only one ACL can be configured for each type.
* After the configurations of this ACL take effect, all users in the user interface are under the restriction of this ACL.

**Precautions**

If no ACL rule is configured, running the **acl** command does not restrict the outgoing calls of user interfaces.


Example
-------

# Restrict outgoing calls on the user interface VTY 0.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] user-interface vty 0
[*HUAWEI-ui-vty0] acl 2000 outbound

```