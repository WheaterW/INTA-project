isis ipv6 tag-value
===================

isis ipv6 tag-value

Function
--------



The **isis ipv6 tag-value** command configures an IPv6 administrative tag for an interface.

The **undo ipv6 isis tag-value** command deletes the IPv6 administrative tag.



By default, no IPv6 administrative tag is configured for an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 tag-value** *tag* [ **level-1** | **level-2** ]

**undo isis ipv6 tag-value** [ *tag* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tag* | Specifies an administrative tag. | The value is an integer ranging from 1 to 4294967295. |
| **level-1** | Configures an administrative tag for a Level-1 interface. | - |
| **level-2** | Configures an administrative tag for a Level-2 interface. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An administrative tag carries administrative information about IPv6 address prefixes. Administrative tags can advertise IPv6 address prefixes in the IS-IS area to control routes, simplifying management.The **isis ipv6 tag-value** command is used to configure the administrative tag value for an interface, and the tag can be used to filter out unwanted routes.

**Prerequisites**

IPv6 has been enabled for the IS-IS interface using the **isis ipv6 enable** command.

**Precautions**

If the IS-IS cost type is wide, wide-compatible, or compatible, the administrative tag of an interface is advertised through an LSP. The cost type can be configured using the **cost-style** command.


Example
-------

# Set the IPv6 administrative tag for 100GE1/0/1 to 77.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] isis ipv6 enable 1
[*HUAWEI-100GE1/0/1] isis ipv6 tag-value 77

```