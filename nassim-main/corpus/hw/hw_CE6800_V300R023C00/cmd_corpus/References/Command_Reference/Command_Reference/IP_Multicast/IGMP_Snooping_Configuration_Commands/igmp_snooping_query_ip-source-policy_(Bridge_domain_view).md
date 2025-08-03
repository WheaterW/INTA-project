igmp snooping query ip-source-policy (Bridge domain view)
=========================================================

igmp snooping query ip-source-policy (Bridge domain view)

Function
--------



The **igmp snooping query ip-source-policy** command configures a policy to filter IGMP Query messages based on source IP addresses in a BD.

The **undo igmp snooping query ip-source-policy** deletes the IGMP Query message filtering policy from a BD.



By default, no IGMP Query message filtering policy is configured in a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an attacker sends Query messages with a smaller IP address than the real IGMP querier on the network, switches running IGMP snooping consider the attacker as a querier and forward IGMP Membership Report messages to the attacker. In this case, multicast traffic cannot be forwarded correctly. You can configure an IGMP Query message filtering policy to defend against such attacks. An IGMP Query message filtering policy permits only IGMP Query messages with specified source IP addresses and rejects other IGMP Query messages. This improves security of a Layer 2 multicast network.

**Prerequisites**

IGMP snooping has been enabled globally.

**Configuration Impact**

After an IGMP Query message filtering policy is configured, the system uses the ACL specified in the command to filter IGMP Query messages. IGMP Query messages are accepted only when their source IP addresses are permitted by the referenced ACL (within the address range following permit in the ACL rule).

**Precautions**

The configuration takes effect only after you run the **igmp snooping enable** command to enable IGMP snooping in the BD.


Example
-------

# Configure an IGMP Query message filtering policy in BD 10 to permit IGMP Query messages with source IP address 10.0.0.1 and drop other IGMP Query messages.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] rule permit source 10.0.0.1 0
[*HUAWEI-acl4-basic-2000] rule deny source any
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable
[*HUAWEI-bd10] igmp snooping query ip-source-policy 2000

```