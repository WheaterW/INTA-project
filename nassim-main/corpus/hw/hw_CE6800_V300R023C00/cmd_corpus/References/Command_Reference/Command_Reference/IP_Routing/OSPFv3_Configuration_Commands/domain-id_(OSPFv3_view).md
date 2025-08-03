domain-id (OSPFv3 view)
=======================

domain-id (OSPFv3 view)

Function
--------



The **domain-id** command sets an OSPFv3 domain ID.

The **undo domain-id** command restores the default setting.



By default, the domain ID is null.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**domain-id** { **null** | { *domain-idvalue* | *domain-idvalue\_ipv4* } [ [ **type** { **0005** | **0105** | **0205** | **8005** } **value** *domainTypeValue* ] | **secondary** ] \* }

**undo domain-id** { *domain-idvalue* | *domain-idvalue\_ipv4* } [ [ **type** { **0005** | **0105** | **0205** | **8005** } **value** *domainTypeValue* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **null** | Sets the OSPFv3 domain ID to null. | - |
| *domain-idvalue* | Specifies the ID of an OSPF domain as an integer. | It is an integer, the value ranges from 0 to 4294967295. The value is converted to dotted decimal notation (with 256 as a carry) when the ID is displayed. |
| *domain-idvalue\_ipv4* | Specifies the ID of an OSPF domain as an IP address. | It is in dotted decimal notation, it is displayed as entered. |
| **type** | Specifies the domain ID type. | - |
| **0005** | Specifies the type 0x0005. | - |
| **0105** | Specifies the type 0x0105. | - |
| **0205** | Specifies the type 0x0205. | - |
| **8005** | Specifies the type 0x8005. | - |
| **value** *domainTypeValue* | Specifies the value of the OSPFv3 domain ID type. | The value is a hexadecimal number ranging from 0 to FFFF, and the default value is 0. |
| **secondary** | Indicates the ID of a secondary domain. | - |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Generally, the routes that are imported from a PE are advertised as External-LSAs. The routes that belong to different nodes of the same OSPFv3 domain are advertised as Type-3 LSAs (intra-domain routes). This requires that different nodes in the same OSPFv3 domain have the same domain ID.Two values, 0 and null, of the domain ID indicate different meanings.The maximum number of secondary domain IDs on each OSPFv3 process is 10, and the maximum number may vary with products.The parameter secondary can be configured only when the primary domain ID is configured. When the **undo domain-id** command is run, if no parameter is specified, the primary domain ID is deleted.


Example
-------

# Set the VPN domain ID in OSPFv3 VPN extension.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ospfv3 1 vpn-instance vpn1
[*HUAWEI-ospfv3-1] domain-id 234

```