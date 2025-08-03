igmp snooping ip-source-policy (Bridge domain view)
===================================================

igmp snooping ip-source-policy (Bridge domain view)

Function
--------



The **igmp snooping ip-source-policy** command configures a policy for filtering Report messages by source IP address.

The **undo igmp snooping ip-source-policy** command restores the default setting.



By default, no policy is configured. This means that any user can enjoy multicast services.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping ip-source-policy** { *acl-number* | **acl-name** *acl-name* }

**undo igmp snooping ip-source-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of an ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve multicast service deployment security, configure a policy to filter out IGMP Report or Leave messages sent by specific hosts.If a basic ACL is specified in the igmp snooping ip-source-policy command, IGMP Report or Leave messages with specified source IP addresses are accepted or rejected. If an advanced ACL is specified in this command, IGMP Report or Leave messages with specified source IP addresses are accepted or rejected.

**Prerequisites**

IGMP snooping has been enabled globally.


Example
-------

# Disable a user host with the IP address of 10.0.0.1 in BD 10 from joining multicast group 225.0.0.1.
```
<HUAWEI> system-view
[~HUAWEI] acl 3000
[*HUAWEI-acl-adv-3000] rule deny ip destination 225.0.0.1 0 source 10.0.0.1 0
[*HUAWEI-acl-adv-3000] rule permit ip
[*HUAWEI-acl-adv-3000] quit
[*HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping ip-source-policy 3000

```