pim hello-option dr-priority
============================

pim hello-option dr-priority

Function
--------



The **pim hello-option dr-priority** command configures a designated router (DR) election priority for a PIM interface.

The **undo pim hello-option dr-priority** command restores the default priority.



By default, the DR election priority of a PIM interface is 1.


Format
------

**pim hello-option dr-priority** *priority*

**undo pim hello-option dr-priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies a DR election priority. A larger value indicates a higher priority. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a PIM-SM shared network segment, a DR is dynamically elected among candidate Router interfaces. DR election is based on priorities and IP addresses of interfaces on Routers. In a DR election process, Routers exchange Hello messages carrying DR election priorities.

* If all Routers support Hello messages that carry DR election priorities, the interface with the highest DR election priority wins. If all interfaces have the same DR election priority, the interface with the largest IP address wins.
* If one or more Routers do not support Hello messages that carry DR priorities, the interface with the largest IP address wins.To change the DR election priority of an interface, run the pim hello-option dr-priority command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the pim hello-option dr-priority command is run more than once, the latest configuration overrides the previous one.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the DR election priority of PIM interface vlanif1 to 3.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim hello-option dr-priority 3

```