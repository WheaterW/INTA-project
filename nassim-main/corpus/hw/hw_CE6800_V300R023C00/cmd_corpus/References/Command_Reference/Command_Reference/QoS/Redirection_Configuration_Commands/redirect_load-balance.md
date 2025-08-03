redirect load-balance
=====================

redirect load-balance

Function
--------



The **redirect load-balance** command configures an action of redirecting packets to multiple next-hop IP addresses in a traffic behavior.

The **undo redirect** command deletes the redirection configuration.



By default, the action of redirecting packets to multiple next-hop IP addresses is not configured in a traffic behavior.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**redirect ipv6 load-balance** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ipv6-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ]

**undo redirect ipv6 load-balance** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ipv6-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ:

**undo redirect**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**redirect load-balance** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ] [ **low-precedence** ]

**undo redirect load-balance** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ] [ **low-precedence** ]

For CE6885-LL (low latency mode):

**redirect load-balance** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ]

**undo redirect load-balance** [ **vpn-instance** *vpn-instance-name* ] **nexthop** { *ip-address* [ **track** **nqa** *admin-name* *test-name* [ **reaction** **probe-failtimes** *fail-times* ] ] } &<1-16> [ **fail-action** **discard** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot be \_public\_. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **nexthop** | Redirects packets to the next hop. | - |
| *ipv6-address* | Specifies the next-hop IPv6 address. The address cannot be of the link-local type.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **track** **nqa** | Indicates an NQA test instance. | - |
| *admin-name* | Specifies the administrator name of an NQA test instance. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *test-name* | Specifies the name of an NQA test instance. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **reaction** | Cancels redirection. | - |
| **probe-failtimes** *fail-times* | Specifies the maximum number of link detection failures in an NQA test instance. | The value is an integer in the range from 1 to 15. |
| **fail-action** **discard** | Indicates that packets are forcibly discarded if all next hops are unreachable. | - |
| **undo** | Cancels the current configuration. | - |
| **ipv6** | Specifies the IPv6 addresses of multiple next hops to which a packet is redirected.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *ip-address* | Specifies the IP address of the next hop. | It is in dotted decimal notation. |
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

The **redirect load-balance** command allows you to specify a maximum of 16 next-hop IP addresses (using the ip-address parameter for multiple times). If multiple next-hop IP addresses are specified, the device redirects packets in ECMP load balancing mode.

If the outbound interface corresponding to a next-hop IP address becomes Down or a route changes, the device switches traffic to the outbound interface corresponding to an available next hop. If the specified next hops are unavailable, the device forwards the packets to the original destination.

If an NQA test instance is configured to detect the link for the redirection next-hop IP address and the number of NQA link detection failures is greater than or equal to the configured maximum value, the current next hop will be canceled. If multiple next hops work in load balancing mode, this next hop will not participate in load balancing, and traffic is load balanced between the remaining reachable next hops.

PBR is implemented based on the redirection action configured in a traffic behavior and takes effect only on incoming packets of interfaces. By default, a device forwards packets to the next hop found in its routing table. If PBR is configured, the device forwards packets to the next hop specified by PBR. After you specify the low-precedence parameter, the device forwards packets matching PBR to the next hop/outbound interface of the specific route in its routing table. When the specific route becomes invalid, the device forwards packets to the next hop/outbound interface specified by PBR. When both the next hop of the specific route and next hop specified by PBR become invalid, and the routing table has default routes, the device continues forwarding packets according to the matching default route.

**Precautions**

* The **redirect load-balance** command allows a maximum of 16 next-hop IP addresses. If the device has no ARP entry matching the specified next-hop IP address, the **redirect load-balance** command can be used but redirection does not take effect. The device still forwards packets to the original destination until the device has the corresponding ARP entry.
* The redirected IP address cannot be the IP address of the device.
* IPv6 PBR does not support redirection based on routes created using OSPFv3.

Example
-------

# Configure three next-hop IP addresses in the traffic behavior b1: 10.1.1.1, 10.2.1.1, and 192.168.1.1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] redirect load-balance nexthop 10.1.1.1 10.2.1.1 192.168.1.1

```