display protocol-vlan interface
===============================

display protocol-vlan interface

Function
--------



The **display protocol-vlan interface** command displays the configuration of interfaces that are associated with VLANs classified based on protocols.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display protocol-vlan interface** { { *interface-type* *interface-number* | *interface-name* } | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | Specifies the interface name. | - |
| **all** | Displays the configuration of all interfaces that are associated with VLANs classified based on protocols. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After interfaces are associated with VLANs classified based on protocols, you can run this command to view the configuration of the specified interface that is associated with VLANs classified based on protocols.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of 100GE 1/0/1 that is associated with VLANs classified based on protocols.
```
<HUAWEI> display protocol-vlan interface 100ge 1/0/1
-------------------------------------------------------------------------------
 Interface                VLAN    Index        Protocol Type           Priority
-------------------------------------------------------------------------------
 100GE1/0/1               2       2            ipv4                    4

```

**Table 1** Description of the **display protocol-vlan interface** command output
| Item | Description |
| --- | --- |
| Interface | Interface that is associated with VLANs classified based on protocols. |
| VLAN | ID of the VLAN classified based on protocols. |
| Index | Index of the protocol template. |
| Protocol | Protocol template. |
| Protocol Type | Protocol type specified in the protocol template:   * at. * ipv4. * ipv6. * ipx. * user-defined protocol type. |
| Priority | 802.1p priority of the VLAN to be associated with the protocol. |