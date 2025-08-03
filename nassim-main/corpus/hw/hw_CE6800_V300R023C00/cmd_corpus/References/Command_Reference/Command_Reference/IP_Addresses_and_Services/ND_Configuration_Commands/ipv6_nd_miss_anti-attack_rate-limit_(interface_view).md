ipv6 nd miss anti-attack rate-limit (interface view)
====================================================

ipv6 nd miss anti-attack rate-limit (interface view)

Function
--------



The **ipv6 nd miss anti-attack rate-limit** command sets the rate limit value for ND Miss messages.

The **undo ipv6 nd miss anti-attack rate-limit** command deletes the rate limit value for ND Miss messages.



By default, the rate limit for ND Miss messages anti-attack function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd miss anti-attack rate-limit** *limit*

**undo ipv6 nd miss anti-attack rate-limit** *limit*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rate-limit** *limit* | Specify the speed limit value for ND Miss messages. | The value is an integer ranging from 0 to 5000, in pps. |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device sends an IPv6 packet, if the MAC address corresponding to the destination IPv6 address of the IPv6 packet does not exist, an ND Miss message is generated. This consumes device resources and affects the processing of other services. To resolve this problem, run the ipv6 nd miss anti-attack rate-limit command to configure the rate at which ND Miss messages are sent. With this configuration, the device processes only the allowed number of ND Miss messages within a specified period to ensure normal service running.

**Configuration Impact**

After the rate at which ND Miss messages are sent is limited, a device collects statistics about the number of received ND Miss messages. If the number of ND Miss messages received within a specified period exceeds the upper limit, the device discards the excess ND Miss messages.

**Precautions**

If the rate of sending ND Miss messages is set to a small value, STelnet login fails. In this case, you can log in to the device through the console port and set the rate to a proper value.


Example
-------

# Set the rate limit for ND Miss messages to 550.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd miss anti-attack rate-limit 550

```