statistics enable (Layer 3 sub-interface view)
==============================================

statistics enable (Layer 3 sub-interface view)

Function
--------

The **statistics enable** command enables traffic statistics collection on a Layer 3 sub-interface.

The **undo statistics enable** command disables traffic statistics collection on a Layer 3 sub-interface.

By default, traffic statistics collection is disabled on a Layer 3 sub-interface.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**statistics** { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ]

**undo statistics** { **ipv4** | **ipv6** } **enable** [ **inbound** | **outbound** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Enables traffic statistics collection of IPv4 packets. | - |
| **ipv6** | Enables traffic statistics collection of IPv6 packets. | - |
| **inbound** | Enables traffic statistics collection in the inbound direction of an interface. | - |
| **outbound** | Enables traffic statistics collection in the outbound direction of an interface. | - |




Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

To check the network status or locate network faults, you can enable traffic statistics collection on Layer 3 sub-interfaces and collect traffic statistics on the Layer 3 sub-interfaces.

You can run the
**display interface** command to check traffic statistics on the interfaces.

**Precautions**

* If the inbound and outbound parameters are not specified, traffic statistics collection is enabled in both the inbound and outbound directions of a Layer 3 sub-interface.
* If you run the **reset interface counters** command to clear traffic statistics on a physical interface, traffic statistics on the corresponding Layer 3 sub-interfaces will not be cleared.
* After you run the **undo statistics enable** command on a Layer 3 sub-interface, the device stops collecting traffic statistics on the Layer 3 sub-interface, and collected traffic statistics will be cleared.
* For Layer 3 Eth-Trunk sub-interfaces, if member interfaces of the Eth-Trunk reside on multiple cards and a card is removed and reinstalled or is faulty, traffic statistics collection on Layer 3 sub-interfaces of the other cards is not affected.
* Configuring traffic statistics collection in the inbound and outbound directions or only in the outbound direction of Layer 3 sub-interfaces on cards may affect the forwarding performance. For example, some packets may be discarded when all interfaces work at the line rate. Therefore, configure traffic statistics collection on Layer 3 sub-interfaces if necessary.
* When collecting traffic statistics in the outbound direction of Layer 3 sub-interfaces, the device does not count Layer 3 packets that match ACL rules and are sent to the CPU, as well as packets (such as ping packets) sent from the device.
* On Layer 3 sub-interfaces, error packet statistics collection is not supported, unicast and broadcast packet statistics cannot be collected separately, and multicast packet statistics collection is not supported.



Example
-------

# Enable IPv4 and IPv6 traffic statistics collection on a Layer 3 sub-interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] interface 100GE 1/0/1.1
[*HUAWEI-100GE1/0/1.1] statistics ipv4 enable
[*HUAWEI-100GE1/0/1.1] statistics ipv6 enable

```