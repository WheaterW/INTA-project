lacp alarm-control link-failure
===============================

lacp alarm-control link-failure

Function
--------



The **lacp alarm-control link-failure** command enables LACP alarm control.

The **undo lacp alarm-control link-failure** command disables LACP alarm control.



By default, LACP alarm control is disabled.


Format
------

**lacp alarm-control link-failure**

**undo lacp alarm-control link-failure**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A device reports an LACP alarm if its Eth-Trunk service in LACP mode fails. To prevent the device from frequently reporting such alarms, run the **lacp alarm-control link-failure** command to enable LACP alarm control. After this function is enabled, the device reports hwLacpNegotiateFailed, hwLacpPartialLinkLoss, hwLacpTotalLinkLoss, hwLacpStateDown, or Eth-Trunk linkdown alarms only when LACP negotiation fails due to the following reasons:

* The device's physical link goes Down.
* LACP negotiation times out.
* LACP determines that packets are looped back.
* LACP determines that the system ID and port key in the LACPDU from the peer end on the local port are inconsistent with those from the peer end on the reference port.A reference port is preferentially selected from the Up member ports after LACP calculation.

**Configuration Impact**



After the command is run, users do not expect to report LACP-related alarms.



**Precautions**



A device that has reported an hwLacpNegotiateFailed, hwLacpPartialLinkLoss, hwLacpTotalLinkLoss, hwLacpStateDown, or Eth-Trunk linkdown alarm will report a clear alarm if the following conditions are met:The **lacp alarm-control link-failure** command is run.The trigger conditions for the reported alarm are beyond the four reasons for LACP negotiation Down.Although a clear alarm is reported, the problem triggering the alarm persists.After the **lacp alarm-control link-failure** command is run, the hwLacpNegotiateFailed, hwLacpPartialLinkLoss, hwLacpTotalLinkLoss, hwLacpStateDown, and Eth-Trunk linkdown alarms are not reported except for the preceding four reasons. Therefore, exercise caution when running this command.




Example
-------

# Enable LACP alarm control.
```
<HUAWEI> system-view
[~HUAWEI] lacp alarm-control link-failure

```