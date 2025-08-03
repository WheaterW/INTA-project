c-rp policy
===========

c-rp policy

Function
--------



The **c-rp policy** command limits the range of valid candidate-rendezvous point (C-RP) addresses and the range of multicast addresses served by a C-RP. The bootstrap router (BSR) drops C-RP messages that carry addresses not in the range of valid C-RP addresses.

The **undo c-rp policy** command restores the default configuration.



By default, the range of valid C-RP addresses and the range of multicast groups served by a C-RP are not limited. That is, the BSR considers all received C-RP messages valid.


Format
------

**c-rp policy** { *policyNum* | **acl-name** *acl-name* }

**undo c-rp policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policyNum* | Specifies the number of an advanced ACL that defines the filtering policy for the range of C-RP addresses and the range of group addresses served by a C-RP. | The value is an integer ranging from 3000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a PIM SM network that uses the BSR mechanism, any router can be configured as a C-RP, and serves the multicast groups in a specified address range. Each C-RP sends its information to the BSR in unicast mode. The BSR summarizes all received C-RP information as an RP-set, and floods it through BSR messages on the entire network. The local router then works out the RP to which a specific multicast group address range corresponds based on the RP-set.To protect valid C-RPs from being spoofed, run the **c-rp policy** command to limit the range of valid C-RP addresses and the range of multicast group addresses served by a C-RP. You must configure the same filtering rule on each C-BSR because any C-BSR may become the BSR.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.ACL rules have been configured.

**Configuration Impact**

If the **c-rp policy** command is run more than once, the latest configuration overrides the previous one.If an ACL rule is specified but no C-RP address range is set, all C-RP messages are denied.


Example
-------

# Configure a C-RP policy in the public network instance, configure the router with the address 1.1.1.1/32 to function as the C-RP, and configure the router to serve only the multicast groups with addresses on the network segment 225.1.0.0/16.
```
<HUAWEI> system-view
[~HUAWEI] acl number 3100
[*HUAWEI-acl4-advance-3100] rule permit ip source 1.1.1.1 0 destination 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-advance-3100] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] c-rp policy 3100

```