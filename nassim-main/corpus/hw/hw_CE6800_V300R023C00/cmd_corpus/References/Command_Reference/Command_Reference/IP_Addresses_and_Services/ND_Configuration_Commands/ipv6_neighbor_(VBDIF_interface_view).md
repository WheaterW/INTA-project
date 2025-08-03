ipv6 neighbor (VBDIF interface view)
====================================

ipv6 neighbor (VBDIF interface view)

Function
--------



The **ipv6 neighbor** command configures a static entry in the IPv6 neighbor discovery cache.

The **undo ipv6 neighbor** command deletes a static entry from the IPv6 neighbor discovery cache.



By default, no static entry is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 neighbor** *ipv6-address* *mac-address* **vni** *vni-id* **source-ip** *source-ip* **peer-ip** *peer-ip-address*

**ipv6 neighbor** *ipv6-address* *mac-address* **vni** *vni-id* **source-ipv6** *source-ipv6* **peer-ipv6** *peer-ipv6-address*

**ipv6 neighbor** *ipv6-address* *mac-address* **vlan** *vlan-id* { *interface-type* *interface-number* | *interface-name* }

**ipv6 neighbor** *ipv6-address* *mac-address* **vlan** *vlan-id* **cevlan** *ce-vid* { *interface-type* *interface-number* | *interface-name* }

**ipv6 neighbor** *ipv6-address* *mac-address* { *interface-type* *interface-number* | *interface-name* }

**undo ipv6 neighbor** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a static entry.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *mac-address* | Specifies the data link layer address of the static entry.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be a multicast MAC address or an all-F broadcast MAC address. |
| **vni** *vni-id* | Specifies the VNI ID of a VXLAN tunnel.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The bd-id value is an integer ranging from 1 to 16777215. |
| **source-ip** *source-ip* | Specifies the source VTEP's IPv4 address of a VXLAN tunnel.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in dotted decimal notation. |
| **peer-ip** *peer-ip-address* | Specifies the remote VTEP's IPv4 address of a VXLAN tunnel.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in dotted decimal notation. |
| **source-ipv6** *source-ipv6* | Specifies the source VTEP's IPv6 address of a VXLAN tunnel.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **peer-ipv6** *peer-ipv6-address* | Specifies the remote VTEP's IPv6 address of a VXLAN tunnel.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vlan** *vlan-id* | Specifies the outer VLAN ID of PE.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4094. |
| *interface-type* *interface-number* | Specifies the type and number of a physical interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *interface-name* | Specifies the name of a physical interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **cevlan** *ce-vid* | Specifies the inner VLAN ID of CE.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4094. |



Views
-----

VBDIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To filter the illegal packets, you can create static ND entries, binding the destination IPv6 addresses of these packets to nonexistent MAC addresses.



**Prerequisites**



The IPv6 function has been enabled on an interface using the **ipv6 enable** command.



**Configuration Impact**



An ND entry enters the REACHABLE state after being created, indicating that the interface connected to this neighbor is Up. If the interface connected to this neighbor turns Down, the ND entry needs to be deleted.The static ND entries overwrite the ND entries dynamically learnt by routers. That is, static ND entries are of higher priorities than dynamically learnt ND entries.



**Precautions**



Only static VXLAN tunnels can be specified for ND entries. Dynamic tunnels cannot be specified.




Example
-------

# Configure static neighbor entries on VBDIF 1.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 1
[*HUAWEI-bd10] quit
[*HUAWEI] interface Vbdif 1
[*HUAWEI-Vbdif1] ipv6 enable
[*HUAWEI-Vbdif1] ipv6 neighbor 2001:db8:1::1 00-e0-fc-12-34-56 Ethernet1/0/8.1

```