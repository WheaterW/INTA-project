redirect remote
===============

redirect remote

Function
--------



The **redirect remote** command configures an action of redirecting packets to the remote next hop in a traffic behavior.

The **undo redirect remote** command cancels the redirection configuration.



By default, the action of redirecting packets to a remote next hop is not configured in a traffic behavior.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**undo redirect**

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**redirect remote ipv6** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* &<1-16> [ **exact** ]

**undo redirect remote ipv6** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* &<1-16> [ **exact** ]

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**redirect remote** [ **vpn-instance** *vpn-instance-name* ] { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **exact** ] [ **low-precedence** ]

**undo redirect remote** [ **vpn-instance** *vpn-instance-name* ] { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **exact** ] [ **low-precedence** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**redirect remote ipv6** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* &<1-16> [ **exact** ] [ **local** ]

**undo redirect remote ipv6** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* &<1-16> [ **exact** ] [ **local** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**redirect remote** [ **vpn-instance** *vpn-instance-name* ] { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **exact** ] [ **low-precedence** ] [ **local** ]

**undo redirect remote** [ **vpn-instance** *vpn-instance-name* ] { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **exact** ] [ **low-precedence** ] [ **local** ]

For CE6885-LL (low latency mode):

**redirect remote** [ **vpn-instance** *vpn-instance-name* ] { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **exact** ] [ **local** ]

**undo redirect remote** [ **vpn-instance** *vpn-instance-name* ] { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **exact** ] [ **local** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** | Specifies the remote IPv6 next hop.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks (""). |
| *ipv6-address* | Specifies the IPv6 address of the remote next hop.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **exact** | Redirects packets to the remote next hop accurately. | - |
| *ip-address* | Specifies the IP address of the remote next hop. | The value is in dotted decimal notation. |
| **track** | Specifies the object to be traced. | - |
| **nqa** | Specifies an NQA test instance to be traced. | - |
| *admin-name* | Specifies the administrator name of an NQA test instance. | The value is a string of 1 to 32 case-sensitive characters including digits (0 to 9) and letters (a to z). It cannot contain spaces. |
| *test-name* | Specifies the administrator name and the name of an NQA test instance. | The value is a string of 1 to 32 case-sensitive characters including digits (0 to 9) and letters (a to z). It cannot contain spaces. |
| **reaction** | Cancels redirection. | - |
| **probe-failtimes** *fail-times* | Specifies the maximum number of link detection failures in an NQA test instance. | The value is an integer in the range from 1 to 15. |
| **low-precedence** | Specifies the low priority of the PBR.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **local** | Indicates local preferential forwarding.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To redirect packets to the IP address of the indirectly-connected next hop, run the **redirect remote** command. After redirection to an indirect next hop address is configured, the device searches the IP routing table. If the IP routing table contains a route to the IP address, the device forwards the packet based on the route.

* When ip-address or ipv6-address matches multiple entries in the IP routing table, the device selects the route according to the longest match rule.
* If an NQA test instance is configured following ip-address and the number of NQA probe failures is greater than or equal to the specified value, the current next hop is automatically canceled.
* When exact is specified, the IP routing table on the device must contain 32-bit host routes that match ip-address or ipv6-address; otherwise, the device cannot redirect packets. For example, when redirect remote 10.1.1.1 exact is configured, the IP routing table of the device must contain a route to 10.1.1.1/32; otherwise, the device cannot redirect packets.
* When multiple remote next hops are configured, the device redirects packets in active/standby mode. The IP address of the next hop configured first has a higher priority. Therefore, the first configured next-hop IP address is used as the active link, and other links are used as standby links. If the primary link goes Down, the switch automatically selects the path to the next-hop address with a higher priority as the primary link. When the high-priority link recovers, traffic is switched back to the high-priority link. When all links to which packets are redirected are unavailable, packets are forwarded through the interface found based on the destination address.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing redirection to a next-hop IP address.

**Precautions**



IPv6 PBR does not support redirection based on routes created using OSPFv3.




Example
-------

# Configure an action of redirecting packets to the remote next hop 10.0.0.1 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] redirect remote 10.0.0.1

```