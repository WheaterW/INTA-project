arp anti-attack check user-bind alarm enable
============================================

arp anti-attack check user-bind alarm enable

Function
--------



The **arp anti-attack check user-bind alarm enable** command enables the alarm function for ARP packets discarded by DAI.

The undo arp anti-attack check user-bind alarm enable command disables the alarm function for ARP packets discarded by DAI.



By default, the alarm function for ARP packets discarded by DAI is disabled.


Format
------

**arp anti-attack check user-bind alarm enable**

**undo arp anti-attack check user-bind alarm enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,VLAN view,Bridge domain view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After DAI is enabled, if you want the device to generate an alarm when a large number of ARP packets that do not match binding entries are discarded, run the arp anti-attack check user-bind alarm enable command. When the number of discarded ARP packets exceeds the alarm threshold, the device generates an alarm.

**Prerequisites**

DAI has been enabled using the **arp anti-attack check user-bind enable** command in the corresponding view.

**Follow-up Procedure**

You can run the **arp anti-attack check user-bind alarm threshold** command to configure the alarm threshold.

**Precautions**



If you run this command in multiple views, the command takes effect in the BD view, interface view, and VLAN view in sequence. Only the CE6863H, CE6863H-K, CE6881H and CE6881H-K support the BD view.




Example
-------

# Enable the alarm function for ARP packets discarded by DAI on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] arp anti-attack check user-bind enable
[*HUAWEI-100GE1/0/1] arp anti-attack check user-bind alarm enable

```