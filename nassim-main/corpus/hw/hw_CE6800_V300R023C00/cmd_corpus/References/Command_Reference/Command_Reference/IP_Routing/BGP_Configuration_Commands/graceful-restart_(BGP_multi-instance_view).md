graceful-restart (BGP multi-instance view)
==========================================

graceful-restart (BGP multi-instance view)

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

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A BGP restart causes traffic interruption. To prevent traffic interruption, run the **graceful-restart** command on a BGP speaker to enable GR globally. This enables all the peers specified on the BGP speaker to perform GR during a BGP restart.



**Configuration Impact**



Enabling or disabling GR deletes and reestablishes all sessions and instances.



**Follow-up Procedure**



Run the **graceful-restart timer wait-for-rib** command to set the time for waiting for the End-Of-RIB flag.




Example
-------

# Enable GR globally for the speaker in BGP process 100.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] graceful-restart

```