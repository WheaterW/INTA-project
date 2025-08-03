dn-bit-check disable
====================

dn-bit-check disable

Function
--------



The **dn-bit-check disable** command disables a device from checking the DN bit in LSAs.

The **undo dn-bit-check disable** command enables a device to check the DN bit in LSAs.



By default, the DN bit in LSAs is checked.


Format
------

**dn-bit-check disable** { **ase** | **nssa** }

**dn-bit-check disable summary** [ **router-id** *router-id* ]

**undo dn-bit-check disable** { **ase** | **nssa** }

**undo dn-bit-check disable summary** [ **router-id** *router-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ase** | Indicates that the DN bit in ASE LSAs is not checked. | - |
| **nssa** | Indicates that the DN bit in NSSA LSAs is not checked. | - |
| **summary** | Indicates that the DN bit in summary LSAs is not checked. | - |
| **router-id** *router-id* | Specifies the router ID of a device on which the DN bit in summary LSAs is checked. | The value is in dotted decimal notation. |



Views
-----

OSPFv3 view,OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To prevent routing loops, the OSPF/OSPFv3 multi-instance process uses a bit as the flag bit, which is called the DN bit.In a VPN Option A scenario, the local PE imports BGP routes to generate LSAs and advertises the LSAs to the remote PE. According to the standard protocol, the peer PE cannot calculate the route because the DN bit is suppressed. In this case, you can run the **dn-bit-check disable** command to disable the peer PE from checking the DN bit during route calculation.



**Prerequisites**

* Run the **ip vpn-instance vpn-instance-name** command to create a VPN instance and enter the VPN instance view.
* The IPv4 address family has been enabled for the VPN instance using the **ipv4-family vpn-instance-name** command in the VPN instance view.
* Run the ospf [ process-id ] [ vpn-instance vpn-instance-name ] command to enable OSPF multi-instance and enter the OSPF multi-instance view.

**Configuration Impact**



The **dn-bit-check disable** command disables a device from checking the DN bit in LSAs, which may cause routing loops. If ase or nssa is specified, you can run the **route-tag** command to set the same tag value for AS-external-LSAs or NSSA LSAs to prevent routing loops. Therefore, you are advised to run the **dn-bit-check disable** command only in the scenarios described in Usage Scenarios.



**Precautions**

When a PE is connected to an MCE and the vpn-instance-capability simple command is not run on the MCE, the MCE checks the DN bit by default. To disable the MCE from checking the DN bit, run the **dn-bit-check disable** command.Using the **dn-bit-set disable** command, you can set or cancel the DN bit on the local PE.


Example
-------

# Disable OSPF from checking the DN bit in summary LSAs.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv4-family
[*HUAWEI-vpn-instance-huawei-af-ipv4] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ospf 100 vpn-instance huawei
[*HUAWEI-ospf-100] dn-bit-check disable summary router-id 1.1.1.1

```

# Disable OSPFv3 from checking the DN bit in Type 3 LSAs.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv6-family
[*HUAWEI-vpn-instance-huawei-af-ipv6] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ospfv3 100 vpn-instance huawei
[*HUAWEI-ospfv3-100] dn-bit-check disable summary router-id 1.1.1.1

```