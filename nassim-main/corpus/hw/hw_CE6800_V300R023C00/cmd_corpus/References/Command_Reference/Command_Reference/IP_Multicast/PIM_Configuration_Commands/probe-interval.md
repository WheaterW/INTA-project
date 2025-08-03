probe-interval
==============

probe-interval

Function
--------



The **probe-interval** command sets an interval at which Probe messages (null Register message) are sent to the rendezvous point (RP).

The **undo probe-interval** command restores the default interval.



By default, Probe messages are sent to the RP at an interval of 5 seconds.


Format
------

**probe-interval** *interval*

**undo probe-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which Probe messages are sent to the RP. | The value is an integer ranging from 1 to 1799, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving a Register-Stop message, the source's designated router (DR) stops sending Register messages and enters the register suppression state. During register suppression, the source's DR sends Probe messages to notify the RP that the multicast source is still in the Active state. After register suppression times out, the source's DR starts to send Register messages. To set the interval at which Probe messages are sent to the RP, run the probe-interval command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the probe-interval command is run several times, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 6 seconds as the interval at which Probe messages are sent to the RP.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] probe-interval 6

```