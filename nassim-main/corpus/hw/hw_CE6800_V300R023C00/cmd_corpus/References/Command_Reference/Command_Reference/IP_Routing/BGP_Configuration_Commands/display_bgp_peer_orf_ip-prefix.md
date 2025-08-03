display bgp peer orf ip-prefix
==============================

display bgp peer orf ip-prefix

Function
--------



The **display bgp peer orf ip-prefix** command displays the prefix-based Outbound Route Filtering (ORF) learned from a specified peer.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp peer** *ipv4-address* **orf** **ip-prefix**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp peer** *ipv6-address* **orf** **ip-prefix**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in the dotted decimal format. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After a device successfully negotiates the ORF capability with its peer, you can run the display bgp peer orf ip-prefix command to view information about the prefix-based ORF learned from the peer.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the prefix-based ORF learned from a peer at 10.1.1.2.
```
<HUAWEI> display bgp peer 10.1.1.2 orf ip-prefix
Total number of ip-prefix received: 1
 Index  Action  Prefix           MaskLen  MinLen  MaxLen
 10     Permit  4.4.4.0          24       32      32

```

**Table 1** Description of the **display bgp peer orf ip-prefix** command output
| Item | Description |
| --- | --- |
| Total number of ip-prefix received | Number of received prefix-based ORF messages. |
| Index | Index of an IP prefix list. |
| Action | Action associated with an IP prefix list:   * deny. * permit. |
| Prefix | Prefix length. |
| MaskLen | Mask length of an IP prefix. |
| MinLen | Minimum mask length of an IP prefix. |
| MaxLen | Maximum mask length of an IP prefix. |