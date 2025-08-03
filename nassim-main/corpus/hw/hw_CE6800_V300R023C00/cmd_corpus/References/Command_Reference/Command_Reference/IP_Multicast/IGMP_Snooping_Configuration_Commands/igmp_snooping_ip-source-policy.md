igmp snooping ip-source-policy
==============================

igmp snooping ip-source-policy

Function
--------



The **igmp snooping ip-source-policy** command configures a policy to filter Report/Leave messages in a VLAN. This policy controls the users that can receive the multicast service.

The **undo igmp snooping ip-source-policy** command restores the default configuration in a VLAN.



By default, no policy is configured. This means that any user can enjoy multicast services.


Format
------

**igmp snooping ip-source-policy** { *acl-number* | **acl-name** *acl-name* }

**undo igmp snooping ip-source-policy**


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

To enhance security of the multicast service, use this command to filter out IGMP Report/Leave messages from specified hosts.

**Prerequisites**

IGMP snooping has been enabled globally.

**Precautions**

The configuration takes effect only after you run the **igmp snooping enable** command to enable IGMP snooping in the VLAN.When a basic ACL is specified in a filter policy, the policy filters IGMP Report/Leave messages based on source addresses. When an advanced ACL is specified in a filter policy, the policy filters IGMP Report/Leave messages based on source and destination IP addresses.


Example
-------

# Prohibit the user host with the source IP address 10.0.0.1 in VLAN 11 from receiving the multicast service.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] rule deny source 10.0.0.1 0
[*HUAWEI-acl4-basic-2000] rule permit source any
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] igmp snooping enable
[*HUAWEI] vlan 11
[*HUAWEI-vlan11] igmp snooping enable
[*HUAWEI-vlan11] igmp snooping ip-source-policy 2000

```