domain-id
=========

domain-id

Function
--------



The **domain-id** command sets the ID for an OSPF domain.

The **undo domain-id** command restores the default setting.



By default, the domain ID is null.


Format
------

**domain-id** { **null** | { *domain-idvalue* | *domain-idvalue\_ipv4* } [ [ **type** { **0005** | **0105** | **0205** | **8005** } **value** *domainTypeValue* ] | **secondary** ] \* }

**undo domain-id** [ { *domain-idvalue* | *domain-idvalue\_ipv4* } [ **type** { **0005** | **0105** | **0205** | **8005** } **value** *domainTypeValue* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **null** | Indicates that the OSPF domain ID is null. | - |
| *domain-idvalue* | Specifies the ID of an OSPF domain as an integer. | It is an integer, the value ranges from 0 to 4294967295. The value is converted to dotted decimal notation (with 256 as a carry) when the ID is displayed. |
| *domain-idvalue\_ipv4* | Specifies the ID of an OSPF domain as an IP address. | It is in dotted decimal notation, it is displayed as entered. |
| **type** | Specifies the domain ID type. | - |
| **0005** | Specifies the type 0x0005. | - |
| **0105** | Specifies the type 0x0105. | - |
| **0205** | Specifies the type 0x0205. | - |
| **8005** | Specifies the type 0x8005. | - |
| **value** *domainTypeValue* | Specifies the value of the OSPF domain ID. | The value is a hexadecimal number ranging from 0 to FFFF, and the default value is 0. |
| **secondary** | Indicates the ID of a secondary domain. | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Domain IDs are used to identify domains.If the local OSPF area and an OSPF area of a remote VPN attempt to exchange Type 3 LSAs, the two areas must be in the same OSPF domain. You can run the **domain-id** command to configure the same domain ID for the two OSPF areas.The routes that are imported from a PE Router are advertised using External-LSAs. The routes destined for different nodes in the same OSPF domain are advertised based on Type-3 LSAs. This requires that the nodes in the same OSPF domain be configured with the same domain ID.OSPF direct routes to a PE do not carry the domain ID, whereas BGP direct routes to a PE do.If the **undo domain-id** command with no parameter specified is executed, the primary domain ID will be deleted.

**Configuration Impact**

Before sending routes to a remote CE Router, a PE Router sends Type-3 LSAs or Type-5 LSAs to the CE based on domain ID. If local domain IDs are the same as or compatible with remote domain IDs in BGP routes, the PE advertises Type 3 routes. If local domain IDs are different from or incompatible with remote domain IDs in BGP routes, the PE advertises Type 5 routes.

**Precautions**

* Each OSPF domain has one or multiple domain IDs. One of them is a primary ID, and the others are secondary IDs.
* If an OSPF instance does not have a specific domain ID, its ID is considered as null.
* If the value of the domain ID is 0, secondary cannot be configured.
* The maximum number of domain-id secondary items configured in an OSPF process is 1000.
* The **domain-id** command cannot be run on a public network.

Example
-------

# Set the VPN domain ID in OSPF VPN extension.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ospf 1 vpn-instance vpn1
[*HUAWEI-ospf-1] domain-id 234

```