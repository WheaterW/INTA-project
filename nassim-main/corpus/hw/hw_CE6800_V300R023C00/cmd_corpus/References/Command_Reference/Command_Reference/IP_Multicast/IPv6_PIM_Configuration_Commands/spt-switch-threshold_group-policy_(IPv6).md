spt-switch-threshold group-policy (IPv6)
========================================

spt-switch-threshold group-policy (IPv6)

Function
--------



The **spt-switch-threshold group-policy** command sets a multicast data forwarding rate threshold at which a receiver's designated router (DR) performs a switchover from the rendezvous point tree (RPT) to the shortest path tree (SPT).

The **undo spt-switch-threshold group-policy** command restores the default value.



By default, a receiver's DR performs a switchover from the RPT to the SPT immediately after receiving the first multicast data packet.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**spt-switch-threshold** *traffic-rate* **group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* } [ **order** *order-value* ]

**undo spt-switch-threshold** [ *traffic-rate* ] **group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *traffic-rate* | Specifies a multicast data forwarding rate threshold at which a receiver's DR performs a switchover from the RPT to the SPT.  Multicast data forwarding rate = Number of multicast data bytes received in a period/Duration of the period (the duration can be specified using the timer spt-switch command).  When the multicast data forwarding rate exceeds traffic-rate, the system performs a switchover from the RPT to the SPT. After the switchover is complete, the system does not switch traffic back to the RPT any more. | The value is an integer ranging from 1 to 4194304, in kbit/s. |
| *basic-acl6-number* | Specify a basic ACL6. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **order** *order-value* | Specifies the order of an IPv6 ACL in the group policy.  If a multicast group matches more than one IPv6 ACL, the system determines the threshold to be used based on order-value of the IPv6 ACLs. | The value is an integer and is any value other than original one in the current group-policy list. If this parameter is not specified, the original IPv6 ACL order is used. |



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

# In the public network instance, configure a group policy: Set the ACL number to 2010 and rate threshold to 100 kbit/s. Insert the ACL at the first place.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2010
[*HUAWEI-acl6-basic-2010] rule permit source ff02:: 96
[*HUAWEI-acl6-basic-2010] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] spt-switch-threshold 100 group-policy 2010 order 1

```

# In the public network instance, configure a group policy: Set the ACL name to myacl6 and rate threshold to 100 kbit/s. Insert the ACL at the first place.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl6 basic
[*HUAWEI-acl6-basic-myacl6] rule permit source ff03::101 128
[*HUAWEI-acl6-basic-myacl6] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] spt-switch-threshold 100 group-policy acl6-name myacl6 order 1

```