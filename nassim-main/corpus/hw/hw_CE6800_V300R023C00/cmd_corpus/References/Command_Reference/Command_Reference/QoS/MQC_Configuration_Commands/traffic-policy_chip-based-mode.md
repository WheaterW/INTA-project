traffic-policy chip-based-mode
==============================

traffic-policy chip-based-mode

Function
--------



The **traffic-policy chip-based-mode** command enables the device to accurately deliver the traffic policy that is applied to a VLAN, a VLANIF interface, or an Eth-Trunk.

The **undo traffic-policy chip-based-mode** command cancels the configuration.



By default, the device is not enabled to accurately deliver the traffic policy that is applied to a VLAN, a VLANIF interface, or an Eth-Trunk.


Format
------

**traffic-policy chip-based-mode**

**undo traffic-policy chip-based-mode**


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

When a traffic policy is applied to a VLAN, VLANIF interface, or Eth-Trunk interface, the traffic policy is delivered to all chips of the device. You can run the **traffic-policy chip-based-mode** command to enable accurate delivery of a traffic policy applied to a VLAN, VLANIF interface, or Eth-Trunk interface. If some chips do not have the corresponding VLAN, VLANIF interface, or member interface of the Eth-Trunk interface, the traffic policy is not delivered to the chips.

**Precautions**

This command is valid for only the new traffic policy. To make this command take effect for existing traffic policies, delete the traffic policies and reconfigure them.


Example
-------

# Enable the device to accurately deliver the traffic policy that is applied to a VLAN, a VLANIF interface, or an Eth-Trunk.
```
<HUAWEI> system-view
[~HUAWEI] traffic-policy chip-based-mode

```