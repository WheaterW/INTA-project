spt-switch-threshold infinity group-policy
==========================================

spt-switch-threshold infinity group-policy

Function
--------



The **spt-switch-threshold infinity group-policy** command configures the range of multicast groups so that a DR on the group member side never triggers an SPT switchover.

The **undo spt-switch-threshold infinity group-policy** command restores the default configuration.



By default, a receiver's DR performs a switchover from the RPT to the SPT immediately after receiving the first multicast data packet.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**spt-switch-threshold infinity group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* } [ **order** *order-value* ]

**undo spt-switch-threshold infinity group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Indicates that a basic ACL is applied. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |
| **order** *order-value* | Specifies the order of an IPv6 ACL in the group policy.  If a multicast group matches more than one IPv6 ACL, the system determines the threshold to be used based on order-value of the IPv6 ACLs. | The value is an integer and is any value other than original one in the current group-policy list. If this parameter is not specified, the original IPv6 ACL order is used. |
| **group-policy** | Limits the range of multicast groups for which a multicast data forwarding rate threshold is effective. | - |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In PIM-SM, a source's DR encapsulates multicast data packets in a Register message and sends the Register message to the rendezvous point (RP). The RP then transmits the multicast data packets along the RPT. The RP and the receiver's DR are responsible for checking the rate of multicast data packets.If a rate threshold is configured on the receiver's DR, the receiver's DR sends a Join message to the source only it finds that the rate of multicast data packets exceeds the threshold and then triggers the switchover from the RPT to the SPT. To set such a rate threshold, run the spt-switch-threshold command.This command takes effect on the Router that functions as the receiver's DR, but does not take effect on the RP.


Example
-------

# In the public network instance, add a group policy with the ACL number of 2010 and configure the device never to trigger an SPT switchover.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2010
[*HUAWEI-acl6-basic-2010] rule permit source ff02:: 96
[*HUAWEI-acl6-basic-2010] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] spt-switch-threshold infinity group-policy 2010

```