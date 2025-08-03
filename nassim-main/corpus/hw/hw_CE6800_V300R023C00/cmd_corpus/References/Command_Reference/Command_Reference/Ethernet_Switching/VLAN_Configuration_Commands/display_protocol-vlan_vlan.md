display protocol-vlan vlan
==========================

display protocol-vlan vlan

Function
--------



The **display protocol-vlan vlan** command displays the protocol and index of the protocol template configured for VLANs.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display protocol-vlan vlan** { *vlan-id1* [ **to** *vlan-id2* ] | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Indicates the start VLAN ID. | The value is an integer ranging from 1 to 4094. |
| *vlan-id2* | Indicates the end VLAN. | The value is an integer ranging from 1 to 4094. The value of <vlan-id2> must be greater than or equal to the value of <vlan-id1>. |
| **all** | Displays information about all VLANs classified based on protocols. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the classification of VLANs based on protocols is configured, you can run the **display protocol-vlan vlan** command to view entries in the Protocol-VLAN table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the protocols and protocol indexes of all VLANs.
```
<HUAWEI> display protocol-vlan vlan all
----------------------------------------------------------------
 VLAN           Protocol Index    Protocol Type
----------------------------------------------------------------
 2              2                 ipv4

```

**Table 1** Description of the **display protocol-vlan vlan** command output
| Item | Description |
| --- | --- |
| VLAN | ID of the VLAN classified based on protocols. |
| Protocol Index | Index of the protocol template. |
| Protocol Type | Protocol type specified in the protocol template:   * at. * ipv4. * ipv6. * ipx. * user-defined protocol type. |