mac-address static (System view)
================================

mac-address static (System view)

Function
--------



The **mac-address static vni** command configures a static MAC address entry for a VXLAN tunnel.

The **undo mac-address static vni** command deletes a static MAC address entry of a VXLAN tunnel.



By default, no static MAC address entry is configured for any VXLAN tunnel.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-address static** *mac-address* **bridge-domain** *bd-id* **source** *source-ip-address* **peer** *peer-ip* **vni** *vni-id*

**mac-address static** *mac-address* **bridge-domain** *bd-id* **source-ipv6** *source-ipv6* **peer-ipv6** *peer-ipv6* **vni** *vni-id*

**undo mac-address static** *mac-address* **bridge-domain** *bd-id* [ [ **source** *source-ip-address* ] [ **peer** *peer-ip* ] [ **vni** *vni-id* ] ]

**undo mac-address static** *mac-address* **bridge-domain** *bd-id* [ [ **source-ipv6** *source-ipv6* ] [ **peer-ipv6** *peer-ipv6* ] [ **vni** *vni-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a destination MAC address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF or a multicast address starting with 01. |
| **bridge-domain** *bd-id* | Specifies the ID of a BD to which a VNI is to be mapped.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |
| **source** *source-ip-address* | Specifies the IP address of a local VTEP.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in dotted decimal notation. |
| **peer** *peer-ip* | Specifies an IP address for a remote VTEP.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in dotted decimal notation. |
| **vni** *vni-id* | Specifies a VNI ID.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The default type is UINT32, and the maximum value range is 1-4294967295. The system automatically obtains the value range according to the actual situation. |
| **source-ipv6** *source-ipv6* | Specifies an IPv6 address for a local VTEP.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **peer-ipv6** *peer-ipv6* | Specifies an IPv6 address for a remote VTEP.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After the source NVE on a VXLAN tunnel receives broadcast, unknown unicast, and multicast (BUM) packets, the local VTEP sends a copy of the BUM packets to every VTEP in the ingress replication list with the same VNI. To reduce the volume of broadcast traffic, run the **mac-address static vni** command to configure a static MAC entry for forwarding traffic. This configuration also prevents unauthorized data access, enhancing network security.




Example
-------

# Configure a static MAC address entry with the destination MAC address of e0-fc-12 for a VXLAN tunnel.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] vxlan vni 5000
[*HUAWEI-bd10] quit
[*HUAWEI] interface nve 1
[*HUAWEI-Nve1] source 1.1.1.1
[*HUAWEI-Nve1] vni 5000 head-end peer-list 2.2.2.2
[*HUAWEI-Nve1] quit
[*HUAWEI] mac-address static e0-fc-12 bridge-domain 10 source 1.1.1.1 peer 2.2.2.2 vni 5000

```

# Configure a static MAC address entry with the destination MAC address of e0-fc-12 for an IPv6 VXLAN tunnel.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] vxlan vni 5000
[*HUAWEI-bd10] quit
[*HUAWEI] interface nve 1
[*HUAWEI-Nve1] source 2001:db8:1::1
[*HUAWEI-Nve1] vni 5000 head-end peer-list 2001:db8:1::2
[*HUAWEI-Nve1] quit
[*HUAWEI] mac-address static e0-fc-12 bridge-domain 10 source-ipv6 2001:db8:1::1 peer-ipv6 2001:db8:1::2 vni 5000

```