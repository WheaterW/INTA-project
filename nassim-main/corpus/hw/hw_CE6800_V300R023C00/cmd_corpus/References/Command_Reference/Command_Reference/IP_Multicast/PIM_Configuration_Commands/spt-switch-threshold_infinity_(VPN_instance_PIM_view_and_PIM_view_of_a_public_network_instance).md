spt-switch-threshold infinity (VPN instance PIM view/PIM view of a public network instance)
===========================================================================================

spt-switch-threshold infinity (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **spt-switch-threshold infinity** command configures the DR to never trigger an SPT switchover.

The **undo spt-switch-threshold infinity** command restores the default value.



By default, a receiver's DR performs a switchover from the RPT to the SPT immediately after receiving the first multicast data packet.


Format
------

**spt-switch-threshold infinity**

**undo spt-switch-threshold infinity**


Parameters
----------

None

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

# In the public network instance, configure the device never to trigger an SPT switchover.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] spt-switch-threshold infinity

```