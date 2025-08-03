ip source check user-bind alarm threshold
=========================================

ip source check user-bind alarm threshold

Function
--------



The **ip source check user-bind alarm threshold** command sets the alarm threshold for IP packet check.

The **undo ip source check user-bind alarm threshold** command restores the default alarm threshold for IP packet check.



By default, the alarm threshold is 100.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip source check user-bind alarm threshold** *threshold*

**undo ip source check user-bind alarm threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold* | Specifies the alarm threshold for checking the received IP packets. | The value is an integer ranging from 1 to 1000. The default value is 100. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,VLAN view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the alarm function for IP packet check is enabled, you can run this command to set the alarm threshold for IP packet check.

**Prerequisites**

The alarm function of IP packet check has been enabled using the **ip source check user-bind alarm enable** command.


Example
-------

# Set the alarm threshold for checking the received IP packets to 200 pps on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ipv4 source check user-bind enable
[*HUAWEI-100GE1/0/1] ip source check user-bind alarm enable
[*HUAWEI-100GE1/0/1] ip source check user-bind alarm threshold 200

```