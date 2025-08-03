vrrp recover-delay (Interface view)
===================================

vrrp recover-delay (Interface view)

Function
--------



The **vrrp recover-delay** command sets a status recovery delay for all VRRP groups configured on a specified interface.

The **undo vrrp recover-delay** command restores the default setting.



By default, the status recovery delay is 0 seconds, indicating that VRRP group flapping is not suppressed.


Format
------

**vrrp recover-delay** *delay-value*

**undo vrrp recover-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-value* | Specifies a status recovery delay for all VRRP groups. | The value is an integer ranging from 0 to 3600, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Frequent changes to the status of the interface on which a VRRP group resides result in the VRRP status frequently flapping. To prevent VRRP status flapping, run the **vrrp recover-delay** command to set a status recovery delay to suppress VRRP status flapping.When a device or board is restarted and a large number of services are configured, the backup device may not immediately receive protocol packets from the master device after the restart. As a result, the backup device becomes the master device because it does not receive protocol packets within a specified period, causing VRRP status flapping or the configured preemption delay to fail to take effect. To prevent this problem, run the **vrrp recover-delay** command to set a status recovery delay for the VRRP group.

**Configuration Impact**

After a status recovery delay is set for a VRRP group, the VRRP group responds to a received interface Up event only after the configured status recovery delay elapses, which prevents interface flapping from causing VRRP group flapping.

**Precautions**

If the **vrrp recover-delay** command is run in the interface view on a device, the same status recovery delay is set for all VRRP groups on the interface. The **vrrp recover-delay** command configured in the interface view takes precedence over that configured in the system view.


Example
-------

# Set the status recovery delay for a VRRP group to 5 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[~HUAWEI-100GE1/0/1] vrrp vrid 10 virtual-ip 10.10.10.10
[*HUAWEI-100GE1/0/1] vrrp recover-delay 5

```