redirect nexthop
================

redirect nexthop

Function
--------



The **redirect nexthop** command configures an action of redirecting packets to a next-hop IP address in a traffic behavior.

The **undo redirect** command deletes the redirection configuration.



By default, the action of redirecting packets to a remote next hop is not configured in a traffic behavior.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**redirect** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ] [ **low-precedence** ]

**undo redirect** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ] [ **low-precedence** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**redirect ipv6** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ipv6-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ]

**undo redirect ipv6** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ipv6-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ:

**undo redirect**

For CE6885-LL (low latency mode):

**redirect** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ]

**undo redirect** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *ip-address* | Specifies the next-hop IPv4 address. | The value is in dotted decimal notation. |
| **track** **nqa** | Indicates an NQA test instance. | - |
| *admin-name* | Specifies the administrator name of an NQA test instance. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *test-name* | Specifies the name of an NQA test instance. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **fail-action** | Specifies the action to be taken if the next hop is unreachable. | - |
| **discard** | Discards the packets. | - |
| **ipv6** | Specifies the next-hop IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *ipv6-address* | Specifies the next-hop IPv6 address. The address cannot be of the link-local type.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **reaction** | Cancels redirection. | - |
| **probe-failtimes** *fail-times* | Specifies the maximum number of link detection failures in an NQA test instance. | The value is an integer in the range from 1 to 15. |
| **low-precedence** | Specifies the low priority of policy-based routing.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **redirect nexthop** command allows you to specify a maximum of 16 next-hop IP addresses (using the ip-address parameter for multiple times). If multiple next-hop IP addresses are configured, the device redirects packets in active/standby mode. The device determines the primary link and backup links according to the sequence in which next-hop IP addresses were configured. The next-hop IP address that was configured first has the highest priority and this next hop is used as the primary path. Other next hops are used as backup paths. When the primary link becomes Down, a next hop with higher priority is used as the primary path.

If an NQA test instance is configured to detect the link for the redirection next-hop IP address and the number of NQA link detection failures is greater than or equal to the configured maximum value, the current next hop will be canceled. If multiple next hops work in active/standby mode, traffic will be automatically switched to a reachable next hop.PBR is implemented based on the redirection action configured in a traffic behavior and takes effect only on incoming packets of interfaces. By default, a device forwards packets to the next hop found in its routing table. If PBR is configured, the device forwards packets to the next hop specified by PBR. After you specify the low-precedence parameter, the device forwards packets matching PBR to the next hop/outbound interface of the specific route in its routing table. When the specific route becomes invalid, the device forwards packets to the next hop/outbound interface specified by PBR. When both the next hop of the specific route and next hop specified by PBR become invalid, and the routing table has default routes, the device continues forwarding packets according to the matching default route.



**Precautions**

* If no ARP entry matches the next-hop address on the device, the device triggers ARP learning. If the ARP entry cannot be learned, redirection does not take effect and packets are forwarded along the original forwarding path.
* The redirected IP address cannot be the IP address of the device.
* IPv6 PBR does not support redirection based on routes created using OSPFv3.



The NQA test instance associated with redirection must be of the ICMP type.




Example
-------

# Configure an action of redirecting packets to the next hop at 10.0.0.1 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] redirect nexthop 10.0.0.1

```