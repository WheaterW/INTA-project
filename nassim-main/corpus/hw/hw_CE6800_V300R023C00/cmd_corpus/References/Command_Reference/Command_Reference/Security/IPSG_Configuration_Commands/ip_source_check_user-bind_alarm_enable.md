ip source check user-bind alarm enable
======================================

ip source check user-bind alarm enable

Function
--------



The **ip source check user-bind alarm enable** command enables the alarm function for checking the received IP packets.

The **undo ip source check user-bind alarm enable** command disables the alarm function for checking the received IP packets.



By default, the alarm function of IP packet check is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip source check user-bind alarm enable**

**undo ip source check user-bind alarm enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,VLAN view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After this command is run, the device records logs when discarding IP packets. If the number of discarded packets exceeds the alarm threshold, the device sends an alarm to the NMS.

**Prerequisites**

IP packet check has been enabled using the **ipv4 source check user-bind enable** command in the interface view or VLAN view.

**Follow-up Procedure**

After the alarm function is enabled using this command, run the **ip source check user-bind alarm threshold** command to configure the alarm threshold.

**Precautions**

If the alarm function of IP packet check is enabled in both the VLAN view and the view of the interface added to the VLAN, the function takes effect in the view where the function is enabled first. To change the sequence in which the function takes effect, you need to disable the function in the view where the function takes effect and then enable the function in the view where the function needs to be enabled.


Example
-------

# Enable the IP packet check alarm function on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ipv4 source check user-bind enable
[*HUAWEI-100GE1/0/1] ip source check user-bind alarm enable

```