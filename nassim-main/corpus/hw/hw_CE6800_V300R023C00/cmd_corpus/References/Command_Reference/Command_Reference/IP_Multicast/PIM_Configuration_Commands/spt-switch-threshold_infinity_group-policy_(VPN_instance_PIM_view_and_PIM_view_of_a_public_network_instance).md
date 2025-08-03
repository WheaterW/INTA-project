spt-switch-threshold infinity group-policy (VPN instance PIM view/PIM view of a public network instance)
========================================================================================================

spt-switch-threshold infinity group-policy (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **spt-switch-threshold infinity group-policy** command configures the range of multicast groups for which the DR at the group member side never triggers the SPT switchover.

The **undo spt-switch-threshold infinity group-policy** command restores the default value.



By default, a receiver's DR performs a switchover from the RPT to the SPT immediately after receiving the first multicast data packet.


Format
------

**spt-switch-threshold infinity group-policy** { *basic-acl-number* | **acl-name** *acl-name* } [ **order** *order-value* ]

**undo spt-switch-threshold infinity group-policy** { *basic-acl-number* | **acl-name** *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl-number* | Indicates that a basic ACL is applied. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **order** *order-value* | Adjusts the order of the ACLs in the group-policy list. If a multicast group matches more than one ACL, the system determines the threshold to be used based on order-value of the ACLs. order-value specifies the updated number. | The value is any integer other than original one in the current group-policy list. If the parameter is not set, the order does not change. |
| **group-policy** | Limits the range of multicast groups for which a multicast data forwarding rate threshold is effective. | - |



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

# In the public network instance, add a group policy with the ACL name of myacl and configure the device never to trigger an SPT switchover.
```
<HUAWEI> system-view
[~HUAWEI] acl name myacl basic
[*HUAWEI-acl4-basic-myacl] rule permit source 10.1.1.1 0.0.0.0
[*HUAWEI-acl4-basic-myacl] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] spt-switch-threshold infinity group-policy acl-name myacl

```