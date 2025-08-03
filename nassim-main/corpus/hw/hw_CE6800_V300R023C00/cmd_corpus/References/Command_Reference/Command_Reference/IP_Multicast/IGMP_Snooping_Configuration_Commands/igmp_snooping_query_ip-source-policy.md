igmp snooping query ip-source-policy
====================================

igmp snooping query ip-source-policy

Function
--------



The **igmp snooping query ip-source-policy** command configures a policy to filter IGMP Query messages based on source IP addresses in a VLAN.

The **undo igmp snooping query ip-source-policy** deletes the IGMP Query message filtering policy from a VLAN.



By default, no IGMP Query message filtering policy is configured in a VLAN.


Format
------

**igmp snooping query ip-source-policy** { *acl-number* | **acl-name** *acl-name* }

**undo igmp snooping query ip-source-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL or an advanced ACL. | The value is an integer that ranges from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a basic ACL or an advanced ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an attacker forges itself as an IGMP querier and sends a Query message with a smaller IP address than the IP address of the current IGMP querier, the IGMP snooping-enabled device forwards the IGMP Membership Report message to the attacker's network interface. As a result, multicast traffic cannot be forwarded normally. To improve Layer 2 multicast network security, you can configure a source address-based IGMP Query message filtering policy to allow only IGMP Query messages with specified source IP addresses to pass through and deny other IGMP Query messages.

**Prerequisites**

IGMP snooping has been enabled globally.

**Configuration Impact**

After an IGMP Query message filtering policy is configured, the system uses the ACL specified in the command to filter IGMP Query messages. IGMP Query messages are accepted only when their source IP addresses are permitted by the referenced ACL (within the address range following permit in the ACL rule).

**Precautions**

The configuration takes effect only after you run the **igmp snooping enable** command to enable IGMP snooping in the VLAN.


Example
-------

# Configure an IGMP Query message filtering policy in VLAN 3 to permit IGMP Query messages with source IP address 10.0.0.1 and drop other IGMP Query messages.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] rule permit source 10.0.0.1 0
[*HUAWEI-acl4-basic-2000] rule deny source any
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] igmp snooping enable
[*HUAWEI] vlan 3
[*HUAWEI-vlan3] igmp snooping enable
[*HUAWEI-vlan3] igmp snooping query ip-source-policy 2000

```