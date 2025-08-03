arp anti-attack check user-bind alarm threshold
===============================================

arp anti-attack check user-bind alarm threshold

Function
--------



The **arp anti-attack check user-bind alarm threshold** command sets the alarm threshold for the number of ARP packets discarded by DAI.

The **undo arp anti-attack check user-bind alarm threshold** command restores the default alarm threshold for the number of ARP packets discarded by DAI.



By default, the alarm threshold for ARP packets discarded by DAI is 100.


Format
------

**arp anti-attack check user-bind alarm threshold** *threshold*

**undo arp anti-attack check user-bind alarm threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold* | Specifies the alarm threshold for the ARP packets discarded by DAI. | The value is an integer that ranges from 1 to 1000. The default value is 100 in the system view.  If this parameter is not configured in other views, the configuration in the system view takes effect. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,VLAN view,Bridge domain view,Interface group view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to set the alarm threshold for the number of ARP packets discarded by DAI. When the number of ARP packets discarded by DAI exceeds the alarm threshold, the device sends an alarm to the network administrator.

**Prerequisites**

You need to run the **arp anti-attack check user-bind enable** command in the corresponding view to enable DAI and run the **arp anti-attack check user-bind alarm enable** command to enable the alarm function for ARP packets discarded by DAI.

**Precautions**



The arp anti-attack check user-bind alarm threshold command takes effect in the system view only when DAI and the alarm function for discarded ARP packets are enabled in the interface, BD, or VLAN view. The global configuration takes effect on all interfaces, BDs, or VLANs where DAI and the alarm function for discarded ARP packets are enabled.The alarm threshold configured in the interface view, BD view, or VLAN view takes precedence over the alarm threshold configured in the system view. If the alarm threshold is not configured in the interface view, BD view, or VLAN view, the alarm threshold configured in the interface view, BD view, or VLAN view is the same as that configured in the system view.



The arp anti-attack check user-bind alarm threshold command takes effect in the system view only when DAI and the alarm function for discarded ARP packets are enabled in the interface or VLAN view. The global configuration takes effect on all interfaces or VLANs where DAI and the alarm function for discarded ARP packets are enabled.The alarm threshold configured in the interface view or VLAN view takes precedence over the alarm threshold configured in the system view. If the alarm threshold is not configured in the interface view or VLAN view, the alarm threshold configured in the interface view or VLAN view is the same as that configured in the system view.




Example
-------

# Set the alarm threshold for the number of packets discarded by DAI on 100GE1/0/1 to 200.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] arp anti-attack check user-bind enable
[*HUAWEI-100GE1/0/1] arp anti-attack check user-bind alarm enable
[*HUAWEI-100GE1/0/1] arp anti-attack check user-bind alarm threshold 200

```