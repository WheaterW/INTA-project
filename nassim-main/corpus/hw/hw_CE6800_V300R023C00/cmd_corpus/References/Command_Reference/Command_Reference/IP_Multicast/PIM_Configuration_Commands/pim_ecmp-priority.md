pim ecmp-priority
=================

pim ecmp-priority

Function
--------



The **pim ecmp-priority** command sets the PIM ECMP priority of an interface.

The **undo pim ecmp-priority** command deletes the PIM ECMP priority of an interface.



By default, no PIM ECMP priority is configured on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ecmp-priority** *priorityValue*

**undo pim ecmp-priority** [ *priorityValue* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priorityValue* | Specifies an ECMP priority value. | The value is an integer ranging from 1 to 128. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* In a PIM FRR scenario where multicast PIM FRR is implemented using unicast route ECMP, the primary and backup inbound interfaces for PIM FRR are selected based on the next-hop IP addresses of unicast routes. The interface with the largest next-hop IP address is selected as the primary inbound interface, and the interface with the second largest next-hop IP address is selected as the backup inbound interface. In this scenario, the selection of the primary and backup inbound interfaces depends on the next-hop IP addresses, which is not flexible. In this case, you can configure the PIM ECMP priority function. After the PIM ECMP priority function is configured, the device selects the primary and backup inbound interfaces based on the PIM ECMP priority. The interface with the highest PIM ECMP priority is selected as the PIM FRR primary inbound interface, and the interface with the second highest PIM ECMP priority is selected as the backup inbound interface.
* In a common PIM multicast scenario, if PIM entries are generated using ECMP for unicast routes, the upstream interface of a PIM entry is selected based on the next-hop IP address of the unicast route. The interface with the largest next-hop IP address is selected as the upstream interface. In this scenario, the selection of the upstream inbound interface depends on the next-hop IP address, which is not flexible. In this case, you can configure the PIM ECMP priority function. After the PIM ECMP priority function is configured, the device selects the upstream inbound interface based on the PIM ECMP priority. The interface with the highest PIM ECMP priority is selected as the upstream inbound interface.

**Prerequisites**

The **multicast routing-enable** command is run in the public network instance view or the VPN instance view.

**Precautions**

1. The PIM ECMP priority function takes effect only after PIM-SM is enabled on an interface.
2. This configuration takes effect only when the unicast routes to the multicast source or RP on inbound interfaces are ECMP routes.
3. There is no default PIM ECMP priority. In common PIM multicast, the PIM ECMP priority takes effect only when it is configured on two or more ECMP route interfaces. In PIM FRR scenarios, the PIM ECMP priority takes effect only when it is configured on both the primary and backup inbound interfaces. If more than two ECMP inbound interfaces need to be planned, you need to configure PIM ECMP priorities for all these inbound interfaces so that inbound interfaces can be selected based on priorities when routes change.
4. Inbound interfaces configured with PIM ECMP priorities do not support multicast load splitting.
5. After the PIM ECMP priority is configured, PIM entries are reconverged. After the PIM ECMP priority is configured on the multicast source DR, the PIM entry on the multicast source DR contains the registration outbound interface for a short period of time.

Example
-------

# Set the PIM ECMP priority of 100GE1/0/1 to 10.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] pim sm
[*HUAWEI-100GE1/0/1] pim ecmp-priority 10

```