ipv6 nd neighbor-limit
======================

ipv6 nd neighbor-limit

Function
--------



The **ipv6 nd neighbor-limit** command configures the maximum number of dynamic neighbor entries allowed by an interface.

The **undo ipv6 nd neighbor-limit** command cancels the configuration.



By default, the maximum number of dynamic neighbor entries allowed by an interface is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd neighbor-limit** *max-number*

**undo ipv6 nd neighbor-limit**

**undo ipv6 nd neighbor-limit** *max-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-number* | Specifies the maximum number of dynamic neighbor entries allowed by an interface. | The value is an integer ranging from 0 to 16384. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Upon receipt of a large number of RA messages from an attacker, a device learns dynamic neighbor entries, which consumes high CPU and memory resources. To defend against RA flooding attacks, run the ipv6 nd neighbor-limit command to configure the maximum number of dynamic neighbor entries allowed by an interface.When the number of dynamic neighbor entries exceeds the upper limit and a large amount of redundant information is generated, the device stops recording the information. In this case, you can run the **reset ipv6 neighbors** command to clear specified dynamic neighbor entries. However, this operation affects IPv6 packet forwarding. Exercise caution when performing this operation.Setting max-number to 0 is equivalent to running the undo ipv6 nd neighbor-limit [ max-number ] command.

**Prerequisites**

Before running this command, run the **ipv6 enable** command in the interface view to enable the IPv6 function.


Example
-------

# Configure the maximum number of dynamic neighbor entries allowed by an interface as 16000.
```
<HUAWEI> system-view
[~HUAWEI] interface vlanif 10
[~HUAWEI-Vlanif10] ipv6 enable
[*HUAWEI-Vlanif10] ipv6 nd neighbor-limit 16000

```