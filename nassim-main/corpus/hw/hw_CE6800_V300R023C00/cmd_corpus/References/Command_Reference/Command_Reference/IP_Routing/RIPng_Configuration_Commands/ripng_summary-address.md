ripng summary-address
=====================

ripng summary-address

Function
--------



The **ripng summary-address** command enables RIPng route summarization and specifies the IPv6 prefix of the summary route to be advertised.

The **undo ripng summary-address** command disables RIPng route summarization.



By default, RIPng route summarization is disabled.


Format
------

**ripng summary-address** *ipv6-address* *prefix-length* [ **avoid-feedback** ]

**undo ripng summary-address** *ipv6-address* *prefix-length*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of the summary route. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the length of the IPv6 prefix of the summary route. | It is an integer ranging from 0 to 128. |
| **avoid-feedback** | Prevents the routes summarized on an interface from being learned by the interface. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a medium or large RIPng network, a device's RIPng routing table contains many routes. Storing, transmitting, and processing these routes consume a significant amount of memory and network resources. To solve this problem, RIPng provides the route summarization function, which can be configured using the **ripng summary-address** command.Route summarization allows multiple routes with the same IPv4 prefix to be summarized into one route. This effectively reduces the number of entries in the routing table and the consumption of system resources. If a link frequently alternates between Up and Down, the link status change is not advertised to devices outside the network segment of the summary route. This prevents route flapping and improves network stability.

**Prerequisites**

RIPng has been enabled on the interface using the **ripng enable** command.

**Configuration Impact**

The cost of the summary route is the smallest cost of the specific routes that participate in the summarization.


Example
-------

# Enable route summarization on 100GE 1/0/1 and set the destination address of the summariy IPv6 route to 2001:db8::/35.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng 100 enable
[*HUAWEI-100GE1/0/1] ripng summary-address 2001:db8:: 35

```