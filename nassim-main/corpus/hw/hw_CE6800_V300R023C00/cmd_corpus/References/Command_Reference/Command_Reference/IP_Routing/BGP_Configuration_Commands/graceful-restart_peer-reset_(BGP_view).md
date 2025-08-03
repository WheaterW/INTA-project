graceful-restart peer-reset (BGP view)
======================================

graceful-restart peer-reset (BGP view)

Function
--------



The **graceful-restart peer-reset** command enables the device to reset a BGP connection in GR mode.

The **undo graceful-restart peer-reset** command restores the default configuration.



By default, the device is not enabled to reset a BGP connection in GR mode.


Format
------

**graceful-restart peer-reset**

**undo graceful-restart peer-reset**


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

Currently, BGP does not support dynamic capability negotiation. Therefore, BGP capability changes cause peer relationships to be re-established and routing entries to be deleted, interrupting services. To solve this problem, run the **graceful-restart peer-reset** command to enable the device to reset BGP connections in GR mode after GR is enabled globally.After the function of resetting a BGP connection in GR mode is configured, if a BGP peer relationship in another address family is established based on the BGP IPv4 unicast peer session, BGP enters GR and renegotiates capabilities. During this process, the BGP IPv4 unicast peer session is re-established. The original routing entries, however, are not deleted, and the forwarding module can still guide packet forwarding according to the routing information. This ensures that IPv4 services are not interrupted.It is recommended that you enable this function when establishing BGP peers.

**Prerequisites**

GR has been enabled using the **graceful-restart** command in the BGP view. Running the **graceful-restart** command for the first time deletes and re-establishes all sessions and instances, causing service interruptions.

**Precautions**

If the **graceful-restart** command is run but the **graceful-restart peer-reset** command is not run, the peer relationship reestablishment triggered by the reset bgp command or dynamic capability negotiation will not reset the BGP connection in GR mode. The peer relationship reestablishment triggered by the reset bgp command or dynamic capability negotiation resets the BGP connection in GR mode only after both the graceful-restart and **graceful-restart peer-reset** commands are run.


Example
-------

# Enable the device to reset a BGP connection in GR mode.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] graceful-restart
[*HUAWEI-bgp] graceful-restart peer-reset

```