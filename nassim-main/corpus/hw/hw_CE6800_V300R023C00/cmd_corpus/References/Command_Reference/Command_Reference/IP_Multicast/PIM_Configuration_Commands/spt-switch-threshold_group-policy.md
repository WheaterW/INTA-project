spt-switch-threshold group-policy
=================================

spt-switch-threshold group-policy

Function
--------



The **spt-switch-threshold group-policy** command sets a multicast data forwarding rate threshold at which a receiver's designated router (DR) performs a switchover from the rendezvous point tree (RPT) to the shortest path tree (SPT).

The **undo spt-switch-threshold group-policy** command restores the default value.



By default, a receiver's DR performs a switchover from the RPT to the SPT immediately after receiving the first multicast data packet.


Format
------

**spt-switch-threshold** *traffic-rate* **group-policy** { *basic-acl-number* | **acl-name** *acl-name* } [ **order** *order-value* ]

**undo spt-switch-threshold** [ *traffic-rate* ] **group-policy** { *basic-acl-number* | **acl-name** *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *traffic-rate* | Specifies a multicast data forwarding rate threshold at which a receiver's DR performs a switchover between the RPT and the SPT.  Multicast data forwarding rate = Number of multicast data bytes received in a period/Duration of the period (the duration can be specified using the timer spt-switch command).  When the multicast data forwarding rate exceeds traffic-rate, the system performs a switchover from the RPT to the SPT. After the switchover is complete, the system does not switch traffic back to the RPT any more. | The value is an integer ranging from 1 to 4194304, in kbit/s. |
| *basic-acl-number* | Indicates the number of a basic ACL, which defines a range of multicast groups. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **order** *order-value* | Specifies the order of an ACL in the group policy.  If a multicast group matches more than one ACL, the system determines the threshold to be used based on order-value of the ACLs. | The value is an integer and is any value other than original one in the current group-policy list. If this parameter is not specified, the original ACL order is used. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In PIM-SM, a source's DR encapsulates multicast data packets in a Register message and sends the Register message to the rendezvous point (RP). The RP then transmits the multicast data along the RPT to receivers. The RP and the receiver's DR are responsible for checking the forwarding rate of multicast data packets.If a rate threshold is configured on the receiver's DR, the receiver's DR sends a Join message to the source only it finds that the forwarding rate of multicast data packets exceeds the threshold and then triggers the switchover from the RPT to the SPT. To set such a rate threshold, run the spt-switch-threshold command.This command takes effect on the Router that functions as the receiver's DR, but does not take effect on the RP.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Precautions**

NOTE:If the spt-switch-threshold command is run more than once for one multicast group, the first command that the multicast group matches takes effect.


Example
-------

# In the public network instance, configure a group policy. Set the ACL name to myacl and rate threshold to100 kbit/s. Insert the ACL at the first place.
```
<HUAWEI> system-view
[~HUAWEI] acl name myacl basic
[*HUAWEI-acl4-basic-myacl] rule permit source 10.1.1.1 0.0.0.0
[*HUAWEI-acl4-basic-myacl] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] spt-switch-threshold 100 group-policy acl-name myacl order 1

```

# In the public network instance, configure a group policy. Set the ACL number to 2010 and rate threshold to 100 kbit/s. Insert the ACL at the first place.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2010
[*HUAWEI-acl4-basic-2010] rule permit source 10.1.1.1 0.0.0.0
[*HUAWEI-acl4-basic-2010] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] spt-switch-threshold 100 group-policy 2010 order 1

```