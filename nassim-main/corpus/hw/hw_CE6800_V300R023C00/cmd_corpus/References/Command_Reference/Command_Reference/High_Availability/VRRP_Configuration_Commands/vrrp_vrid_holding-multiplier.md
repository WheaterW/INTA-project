vrrp vrid holding-multiplier
============================

vrrp vrid holding-multiplier

Function
--------



The **vrrp vrid holding-multiplier** command sets a multiplier of the interval at which VRRP Advertisement packets are sent for the timeout period of a backup device in a VRRP backup group.

The **undo vrrp vrid holding-multiplier** command restores the default multiplier of the interval at which VRRP Advertisement packets are sent for the timeout period of a backup device in a VRRP backup group.



By default, the timeout period of a backup device in a VRRP backup group is three times the interval at which VRRP Advertisement packets are sent.


Format
------

**vrrp vrid** *virtual-router-id* **holding-multiplier** *holding-multiplier-value*

**undo vrrp vrid** *virtual-router-id* **holding-multiplier** [ *holding-multiplier-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **holding-multiplier** *holding-multiplier-value* | Specifies a multiplier of the interval at which VRRP Advertisement packets are sent for the timeout period of a backup device in a VRRP backup group. | The value is an integer ranging from 3 to 10. |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set a multiplier of the interval at which VRRP Advertisement packets are sent for the timeout period of a backup device in a VRRP backup group, run the vrrp vrid holding-multiplier command.

**Prerequisites**

A VRRP backup group has been configured using the **vrrp vrid** command.

**Configuration Impact**

If a VRRP backup group is not configured to monitor a service, a larger multiplier results in a longer timeout period for a backup device when the interval at which VRRP Advertisement packets are sent is the same.

**Precautions**

If a VRRP backup group is configured to monitor a service (for example, VRRP association with BFD or NQA), the vrrp vrid holding-multiplier command does not affect the timeout period of a backup device.If a VRRP backup group is not configured to monitor a service (for example, VRRP association with link/peer BFD), a larger multiplier results in a longer timeout period for a backup device when the interval at which VRRP Advertisement packets are sent is the same.


Example
-------

# Set a multiplier of the interval at which VRRP Advertisement packets are sent for the timeout period of a backup device in VRRP backup group 1 to 4.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.10.10.10
[*HUAWEI-100GE1/0/1] vrrp vrid 1 holding-multiplier 4

```