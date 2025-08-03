vrrp recover-delay
==================

vrrp recover-delay

Function
--------



The **vrrp recover-delay** command sets a status recovery delay for all VRRP groups.

The **undo vrrp recover-delay** command restores the default value.



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

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the status of the interface on which the VRRP group is configured frequently changes, the VRRP status frequently flaps. To prevent this problem, run the **vrrp recover-delay** command to set a status recovery delay to suppress VRRP group flapping.When a device or board is restarted and a large number of services are configured, the backup device may not immediately receive protocol packets from the master device after the restart. As a result, the backup device becomes the master device because it does not receive protocol packets within a specified period, causing VRRP status flapping or the configured preemption delay to fail to take effect. To prevent this problem, run the **vrrp recover-delay** command to set a status recovery delay for the VRRP group.

**Prerequisites**

After a status recovery delay is set for a VRRP group, the VRRP group responds to a received interface Up event only after the configured status recovery delay elapses, which prevents interface flapping from causing VRRP group flapping.

**Precautions**

If the **vrrp recover-delay** command is run in the system view on a device, the same status recovery delay is set for all VRRP groups on the device.


Example
-------

# Set the status recovery delay for a VRRP group to 5 seconds.
```
<HUAWEI> system-view
[~HUAWEI] vrrp recover-delay 5

```