igmp on-demand
==============

igmp on-demand

Function
--------



The **igmp on-demand** command configures entries of dynamically joined IGMP groups not to age on a specified interface.

The **undo igmp on-demand** command restores the default configuration.



By default, entries of dynamically joined IGMP groups age periodically on a specified interface


Format
------

**igmp on-demand**

**undo igmp on-demand**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

igmp on-demand enables a host to become a static data receiver of a multicast group on a multicast device's interface connected to an access device, thus reducing packet exchanges and workloads of the multicast and access devices. To enable this function, run the **igmp on-demand** command, so that entries of dynamically joined IGMP groups will not age on a specified interface.This command applies only to IGMPv2 and IGMPv3 interfaces connected to access devices, not to user hosts.

**Configuration Impact**

The **igmp on-demand** command configuration does not take effect for existing entries of dynamically joined IGMP groups.

**Precautions**

After the **igmp on-demand** command is run on a multicast device connected to an IGMP proxy-enabled access device:

* The interface sends only one IGMP General Query message to the network.
* If an interface receives an IGMP Leave message, the interface immediately deletes the record of the corresponding IGMP group.After the **igmp on-demand** command is run in IGMPv3, the device does not process IGMPv2 non-SSM Join requests.

Example
-------

# Configure entries of dynamically joined IGMP groups not to age on Vlanif1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp on-demand

```