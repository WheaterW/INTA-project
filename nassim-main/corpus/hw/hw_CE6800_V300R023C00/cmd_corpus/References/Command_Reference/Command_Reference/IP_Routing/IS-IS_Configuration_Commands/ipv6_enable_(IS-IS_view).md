ipv6 enable (IS-IS view)
========================

ipv6 enable (IS-IS view)

Function
--------



The **ipv6 enable** command enables the IPv6 capability for an IS-IS process.

The **undo ipv6 enable** command disables the IPv6 capability.



By default, the IPv6 capability is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 enable** [ **topology** { **compatible** [ **enable-mt-spf** ] | **ipv6** | **standard** } ]

**undo ipv6 enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **topology** | Indicates a topology of the network. | - |
| **compatible** | Sets the compatible mode for the topology. If the compatible mode is specified, after an IPv6 IS-IS neighbor relationship is established, IS-IS advertises the neighbor information in both standard and IPv6 topologies but uses the standard topology to calculate IPv4 and IPv6 routes. | - |
| **enable-mt-spf** | Configures the device to use the IPv6 topology to calculate IPv6 routes when the topology mode is compatible. | - |
| **ipv6** | Sets the IPv6 mode for the topology. If the IPv6 mode is specified, after an IPv6 IS-IS neighbor relationship is established, IS-IS advertises the neighbor information only in the IPv6 topology and uses the IPv6 topology to calculate IPv6 routes. | - |
| **standard** | Sets the standard mode for the topology. If the standard mode is specified, after an IPv6 IS-IS neighbor relationship is established, IS-IS advertises the neighbor information only in the standard topology and uses the standard topology to calculate IPv4 and IPv6 routes. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In IS-IS, if the topology mode is set to standard or compatible, the device advertises neighbor information about an interface in the standard topology when the interface establishes either IPv4 or IPv6 neighbor relationships with other devices. In this case, other devices cannot determine whether the interface is configured with both IPv4 and IPv6 addresses, and both the local device and other devices use the interface to calculate IPv4 and IPv6 routes in the standard topology. As a result, traffic of the interface on which the IPv4 or IPv6 address family is not configured may be interrupted. To prevent this problem, you are advised to set the topology mode to IPv6 to isolate IPv6 services from IPv4 services. If the current topology mode is standard, you are advised to change it to IPv6. Before you change the mode, ensure that both IPv4 and IPv6 addresses are configured for IS-IS interfaces on the entire network. The configuration procedure is as follows:

1. Run the **ipv6 enable topology compatible** command on all devices on the network to set the topology mode to compatible.
2. Run the **ipv6 enable topology compatible enable-mt-spf** command on all devices on the network to set the topology mode to compatible with the enable-mt-spf parameter specified.
3. Run the **ipv6 enable topology ipv6** command on all devices on the network to set the topology mode to IPv6.

**Prerequisites**

Before running the **ipv6 enable** command, perform the following operations:

* Run the **isis** command to create an IS-IS process and enter the IS-IS process view.
* Run the **network-entity** command to set a NET for the device.

**Precautions**

If the **ipv6 enable** command is run more than once, the latest configuration overrides the previous one.When IPv6 is enabled for an IS-IS process, the topology type is IPv6 by default.In standard mode, IPv4 and IPv6 must be enabled on all IS-IS interfaces on the network. Otherwise, services are interrupted. Therefore, you are advised to configure the IPv6 mode to isolate IPv6 services from IPv4 services.Changing the IPv6 topology mode, for example, from IPv6 to standard, may interrupt services.Changing the parameters of the **ipv6 enable** command causes path recalculation and IPv6 route update.


Example
-------

# Enable the IPv6 capability for IS-IS process 1 in the ipv6 topology.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] network-entity 10.0001.1010.1020.1030.00
[*HUAWEI-isis-1] ipv6 enable topology ipv6

```