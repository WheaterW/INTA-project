spt-switch-threshold (VPN instance PIM view/PIM view of a public network instance)
==================================================================================

spt-switch-threshold (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **spt-switch-threshold** command sets a multicast data forwarding rate threshold at which a receiver's designated router (DR) performs a switchover from the rendezvous point tree (RPT) to the shortest path tree (SPT).

The **undo spt-switch-threshold** command restores the default value.



By default, a receiver's DR performs a switchover from the RPT to the SPT immediately after receiving the first multicast data packet.


Format
------

**spt-switch-threshold** *traffic-rate*

**undo spt-switch-threshold** [ *traffic-rate* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *traffic-rate* | Specifies a multicast data forwarding rate threshold at which a receiver's DR performs a switchover between the RPT and the SPT.  Multicast data forwarding rate = Number of multicast data bytes received in a period/Duration of the period (the duration can be specified using the timer spt-switch command).  When the multicast data forwarding rate exceeds traffic-rate, the system performs a switchover from the RPT to the SPT. After the switchover is complete, the system does not switch traffic back to the RPT any more. | The value is an integer ranging from 1 to 4194304, in kbit/s. |



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

# In the public network instance, set the multicast data forwarding rate threshold to 4 kbit/s. If the rate of multicast data packets transmitted from the source to the multicast exceeds the threshold, the Router triggers the switchover from the RPT to the SPT.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] spt-switch-threshold 4

```