isis ipv6 enable
================

isis ipv6 enable

Function
--------



The **isis ipv6 enable** command enables IS-IS IPv6 on an interface and specifies the IS-IS process ID to be associated with the interface.

The **undo isis ipv6 enable** command disables IS-IS IPv6 from an interface and dissociates the IS-IS process from the interface.



By default, IS-IS IPv6 is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 enable**

**isis ipv6 enable** *process-id*

**undo isis ipv6 enable**

**undo isis ipv6 enable** *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an IS-IS process is configured in the system view, enable IS-IS IPv6 on the IS-IS interface and associate the interface with the IS-IS process using the **isis ipv6 enable** command.

**Prerequisites**

The following steps have been performed:

* Run the **isis** command to enable an IS-IS process and run the **network-entity** command to configure a network entity title (NET) for the IS-IS device.
* Run the ipv6 enable (IS-IS) command in the IS-IS view to enable IPv6 for the IS-IS process.
* Run the **ipv6 enable** command on each interface that needs to run the IS-IS process to enable IPv6 and configure an IPv6 address.To perform IPv6-related configurations, enable IPv6 first.

Example
-------

# Create IS-IS routing process 1, enable IPv6, and enable IPv6 for the process on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] network-entity 10.0001.1010.1020.1030.00
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8:1::1/64
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis ipv6 enable 1

```