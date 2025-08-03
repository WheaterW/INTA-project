arp static
==========

arp static

Function
--------



The **arp static** command configures a static ARP entry.

The **undo arp static** command deletes a static ARP entry.



By default, no static ARP entry is configured.


Format
------

**arp static** *ip-address* *mac-address*

**arp static** *ip-address* *mac-address* **vpn-instance** *vpn-instance-name*

**arp static** *ip-address* *mac-address* { **vlan** *vlan-id* [ **interface** { *interface-name* | *interface-type* *interface-number* } ] | **interface** { *interface-name* | *interface-type* *interface-number* } }

**arp static** *ip-address* *mac-address* **vlan** *vlan-id* **cevlan** *cevid* **interface** { *interface-name* | *interface-type* *interface-number* }

**undo arp static** *ip-address* [ *mac-address* ]

**undo arp static** *ip-address* [ *mac-address* ] **vpn-instance** *vpn-instance-name*

**undo arp static** *ip-address* [ *mac-address* ] { **vlan** *vlan-id* [ **interface** { *interface-name* | *interface-type* *interface-number* } ] | **interface** { *interface-name* | *interface-type* *interface-number* } }

**undo arp static vpn-instance** *vpn-instance-name*

**undo arp static all**

**undo arp static** *ip-address* [ *mac-address* ] **vlan** *vlan-id* **cevlan** *cevid* **interface** { *interface-name* | *interface-type* *interface-number* }

**arp static** *ip-address* *mac-address* **vni** *vni-id* **source-ip** *source-ip* **peer-ip** *peer-ip*

**arp static** *ip-address* *mac-address* **vni** *vni-id* **source-ip** *source-ipv6* **peer-ip** *peer-ipv6*

**undo arp static** *ip-address* *mac-address* **vni** *vni-id* **source-ip** *source-ip* **peer-ip** *peer-ip*

**undo arp static** *ip-address* *mac-address* **vni** *vni-id* **source-ip** *source-ipv6* **peer-ip** *peer-ipv6*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address in a static ARP entry. | The value is in dotted decimal notation. |
| *mac-address* | Specifies the MAC address in a static ARP entry. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name of a static ARP entry. | The value is a string of 1 to 31 characters. |
| **interface** *interface-name* | Specifies the name of the outbound interface of static ARP packets. | - |
| **interface** *interface-type* *interface-number* | Specifies the outbound interface of static ARP packets. | - |
| **vlan** *vlan-id* | Specifies the outer VLAN ID corresponding to a static ARP entry. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **cevlan** *cevid* | Specifies the inner VLAN ID corresponding to a static ARP entry. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **all** | Deletes all static ARP entries. | - |
| **vni** *vni-id* | Specifies the VNI ID.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is an integer ranging from 1 to 16000000. |
| **vni** *vni-id* | Specifies the VNI ID.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is an integer in the range from 1 to 16000000. |
| **source-ip** *source-ip* | Specifies the IP address of the source VTEP.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is in dotted decimal notation. |
| **source-ip** *source-ipv6* | Specifies the IPv6 address of the source VTEP.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| **peer-ip** *peer-ip* | Specifies the IP address of the remote VTEP.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is in dotted decimal notation. |
| **peer-ip** *peer-ipv6* | Specifies the IPv6 address of the remote VTEP.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure mapping between IP addresses and MAC addresses for security or management purposes, run the arp static command.The IP and MAC address mapping in a static ARP entry is fixed. Neither the host nor the device can adjust the mapping. Static ARP entries remain valid when the routing device works normally.

* To allow packets whose destination IP addresses are not on a network segment to be forwarded by a certain gateway on the network segment.
* To filter out packets with invalid destination IP addresses. These invalid IP addresses can be bound to a non-existent MAC address.

Note that ip-address must be on the same network segment as the IP address of the outbound interface specified by interface.

**Configuration Impact**

After a static ARP entry is configured, the ARP entry cannot be dynamically learned.

**Precautions**

When configuring static ARP on a QinQ VLAN tag termination sub-interface, dot1q VLAN tag termination sub-interface, or VBDIF interface, you must specify an outbound interface. Otherwise, traffic cannot be forwarded, and the interface does not learn the outbound interface based on packets.

* On a VXLAN network, if a Layer 2 sub-interface is used as a service access point, you can configure the mapping between IP and MAC addresses on the user access side by specifying \*\*interface \*\**interface-type interface-number*as a Layer 2 sub-interface.
* You can also specify the inner and outer VLAN IDs, but you need to distinguish the traffic encapsulation types of Layer 2 sub-interfaces.
* Dot1q traffic encapsulation type: **vlan** *vlan-id*can be specified. The value must be the same as that in the **encapsulation dot1q** [ **vid** *low-pe-vid*] command.
* QinQ traffic encapsulation type: **vlan** *pevlan-id***cevlan** *cevlan-id*can be specified. The values must be the same as those in the **encapsulation qinq** [ **vid** *pe-vid**ce-vid low-ce-vid*] command.


Example
-------

# Configure a static ARP entry with the IP address 1.1.1.1 mapped to the MAC address 00e0-fc12-3456, outer VLAN ID as 100, and inner VLAN ID as 200.
```
<HUAWEI> system-view
[~HUAWEI] arp static 1.1.1.1 00e0-fc12-3456 vlan 100 cevlan 200 interface 100GE 1/0/1.1

```

# Configure a static ARP entry with the IP address 10.0.0.1 mapped to the MAC address aa-fcc-12.
```
<HUAWEI> system-view
[~HUAWEI] arp static 10.0.0.1 00e0-fc12-3456

```