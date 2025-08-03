vrrp6 vrid holding-multiplier
=============================

vrrp6 vrid holding-multiplier

Function
--------



The **vrrp6 vrid holding-multiplier** command sets a multiplier of the interval at which VRRP6 Advertisement packets are sent for the timeout period of a backup device in a VRRP6 backup group.

The **undo vrrp6 vrid holding-multiplier** command restores the default multiplier of the interval at which VRRP6 Advertisement packets are sent for the timeout period of a backup device in a VRRP6 backup group.



By default, the timeout period of a backup device in a VRRP6 backup group is three times the interval at which VRRP6 Advertisement packets are sent.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 vrid** *virtual-router-id* **holding-multiplier** *holding-multiplier-value*

**undo vrrp6 vrid** *virtual-router-id* **holding-multiplier** [ *holding-multiplier-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP6 group. | The value is an integer ranging from 1 to 255. |
| *holding-multiplier-value* | Specifies a multiplier of the interval at which VRRP6 Advertisement packets are sent for the timeout period of a backup device in a VRRP6 backup group. | The value is an integer ranging from 3 to 10. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set a multiplier of the interval at which VRRP6 Advertisement packets are sent for the timeout period of a backup device in a VRRP6 backup group, run the vrrp6 vrid holding-multiplier command.

**Prerequisites**

A VRRP6 backup group has been configured using the **vrrp6 vrid** command.

**Configuration Impact**

If a VRRP6 backup group is not configured to monitor a service, a larger multiplier results in a longer timeout period for a backup device when the interval at which VRRP6 Advertisement packets are sent is the same.

**Precautions**

If a VRRP6 backup group is configured to monitor a service, the vrrp6 vrid holding-multiplier command hardly affects the timeout period of a backup device.


Example
-------

# Set the timeout period of a backup device in VRRP6 group 1 to four times the interval at which VRRP6 Advertisement packets are sent.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::7 link-local
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 holding-multiplier 4

```