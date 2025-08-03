graceful-restart
================

graceful-restart

Function
--------



The **graceful-restart** command enables GR globally on a BGP speaker.

The **undo graceful-restart** command disables GR globally.



By default, GR is disabled globally.


Format
------

**graceful-restart**

**undo graceful-restart**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After you run the **graceful-restart** command to enable GR on a device, the device helps other GR-capable devices to perform GR during a BGP restart, preventing traffic interruption.Both static peers and network segment peers support the GR helper capability.

**Configuration Impact**



Enabling or disabling GR deletes and reestablishes all sessions and instances.



**Follow-up Procedure**



Run the **graceful-restart timer wait-for-rib** command to set the time for waiting for the End-Of-RIB flag.




Example
-------

# Enable GR globally for the speaker in BGP process 100.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] graceful-restart

```