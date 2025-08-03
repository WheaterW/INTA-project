dn-bit-set disable
==================

dn-bit-set disable

Function
--------



The **dn-bit-set disable** command disables the device from setting the DN bit in LSAs.

The **undo dn-bit-set disable** command configures the device to set the DN bit in LSAs.



By default, the DN bit in LSAs is set.


Format
------

**dn-bit-set disable** { **summary** | **ase** | **nssa** }

**undo dn-bit-set disable** { **summary** | **ase** | **nssa** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **summary** | Sets the DN bit in Type 3 LSAs. | - |
| **ase** | Sets the DN bit in AS-external-LSAs. | - |
| **nssa** | Sets the DN bit in NSSA LSAs. | - |



Views
-----

OSPFv3 view,OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent routing loops, an OSPF multi-instance process uses a bit as a flag bit, which is called the DN bit.The **dn-bit-set disable** command is recommended only in the following scenarios:

* In a VPN Option A scenario, the local PE imports BGP routes to generate LSAs and advertises the LSAs to the peer PE. According to the standard protocol, the peer PE cannot calculate the route because the DN bit is suppressed. In this case, you can run the **dn-bit-set disable** command to configure the local PE not to set the DN bit.

**Prerequisites**

* Run the **ip vpn-instance vpn-instance-name** command to create a VPN instance and enter the VPN instance view.
* The IPv4 address family has been enabled for the VPN instance using the **ipv4-family vpn-instance-name** command in the VPN instance view.
* Run the ospf [ process-id ] [ vpn-instance vpn-instance-name ] command to enable OSPF multi-instance and enter the OSPF multi-instance view.

**Configuration Impact**

After the **dn-bit-set disable ase** command is run, the DN bit is not set in Type 5 LSAs translated from Type 7 LSAs even if the DN bit is set in the Type 7 LSAs.

**Precautions**

* The **dn-bit-set disable** command can be run only in OSPF or OSPFv3 VPN processes and takes effect only on PEs.
* You can run the **dn-bit-check disable** command to disable OSPF/OSPFv3 from checking the DN bit during route calculation.
* If you run the **dn-bit-set disable** command to disable the device from setting the DN bit in LSAs, routing loops may occur. If ase or nssa is specified, you can run the **route-tag** command to set the same tag value for AS-external-LSAs or NSSA LSAs to prevent routing loops. Therefore, you are advised to run the **dn-bit-set disable** command only in the scenarios described in Usage Scenarios.


Example
-------

# Disable OSPF from setting the DN bit in ASE LSAs.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv4-family
[*HUAWEI-vpn-instance-huawei-af-ipv4] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ospf 100 vpn-instance huawei
[*HUAWEI-ospf-100] dn-bit-set disable ase

```

# Disable OSPFv3 from setting the DN bit in AS-external-LSAs.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv6-family
[*HUAWEI-vpn-instance-huawei-af-ipv6] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ospfv3 100 vpn-instance huawei
[*HUAWEI-ospfv3-100] dn-bit-set disable ase

```