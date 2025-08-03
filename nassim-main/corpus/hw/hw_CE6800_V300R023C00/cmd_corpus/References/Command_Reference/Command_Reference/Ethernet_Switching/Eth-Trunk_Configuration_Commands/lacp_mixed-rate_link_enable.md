lacp mixed-rate link enable
===========================

lacp mixed-rate link enable

Function
--------



The **lacp mixed-rate link enable** command enables interfaces working at different rates to forward packets after they are added to an Eth-Trunk interface in static or dynamic Link Aggregation Control Protocol (LACP) mode.

The **undo lacp mixed-rate link enable** command disables interfaces working at different rates from forwarding data packets after they are added to an Eth-Trunk interface in static or dynamic LACP mode.



By default, after interfaces working at different rates are added to an Eth-Trunk interface in static or dynamic LACP mode, traffic is forwarded through the member interface with a higher LACP priority on the Actor. If the member interfaces have the same LACP priority, traffic is forwarded through the member interface with a smaller interface ID.


Format
------

**lacp mixed-rate link enable**

**undo lacp mixed-rate link enable**


Parameters
----------

None

Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, after interfaces operating at different rates are added to an Eth-Trunk interface in static or dynamic LACP mode, traffic is forwarded at only one of the rates through the corresponding interfaces. This operation cannot implement load balancing on the Eth-Trunk interface.

To implement load balancing, run the **lacp mixed-rate link enable** command to enable the Eth-Trunk interface's member interfaces operating at different rates to share packets.



**Prerequisites**



The Eth-Trunk interface has been configured to work in static LACP mode using the **mode lacp-static** command in the Eth-Trunk interface view or in dynamic mode using the **mode lacp-dynamic** command in the Eth-Trunk interface view.NOTE:The rate of the interface added to the Eth-Trunk interface is not limited. For example, 10G and 100G interfaces can be added to the same Eth-Trunk interface. The maximum forwarding rate of an Eth-Trunk interface is the sum of rates of the Eth-Trunk interface's member interfaces.



**Follow-up Procedure**



You can run the distribute-weight weight-value command to set the distribute-weight of the member interface with different rates. By default, the weight of an Eth-Trunk member interface is 1.



**Precautions**



After the **lacp mixed-rate link enable** command is run, member interfaces are renegotiated, and the member interfaces may alternate between Up and Down.




Example
-------

# Enable interfaces operating at different rates to forward packets after the interfaces are added to an Eth-Trunk interface in static LACP mode.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp mixed-rate link enable

```