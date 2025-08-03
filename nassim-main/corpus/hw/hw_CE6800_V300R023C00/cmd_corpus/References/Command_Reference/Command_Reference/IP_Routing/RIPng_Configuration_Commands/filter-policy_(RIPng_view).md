filter-policy (RIPng view)
==========================

filter-policy (RIPng view)

Function
--------



The **filter-policy export** command specifies the filtering policy for the sent routes. Only the routes that match the filtering policy can be advertised through Update packets.

The **undo filter-policy export** command cancels the configuration.

The **filter-policy import** command specifies the filtering policy for the received route Update packets. Only the route Update packets that match the filtering policy can be received.

The **undo filter-policy import** command cancels the configuration.



By default, the filtering function is disabled.


Format
------

**filter-policy** { **ipv6-prefix** *ipv6-prefix-name* | *acl6-number* | **acl6-name** *acl6-name* | **route-policy** *route-policy-name* } **export** [ **direct** | **static** | **bgp** | { **ospfv3** | **isis** | **ripng** } [ *process-id* ] ]

**filter-policy** { **ipv6-prefix** *ipv6-prefix-name* | *acl6-number* | **acl6-name** *acl6-name* | **route-policy** *route-policy-name* } **import**

**undo filter-policy export** [ **direct** | **static** | **bgp** | { **ospfv3** | **isis** | **ripng** } [ *process-id* ] ]

**undo filter-policy** { **ipv6-prefix** *ipv6-prefix-name* | *acl6-number* | **acl6-name** *acl6-name* | **route-policy** *route-policy-name* } **export** [ **direct** | **static** | **bgp** | { **ospfv3** | **isis** | **ripng** } [ *process-id* ] ]

**undo filter-policy import**

**undo filter-policy** { **ipv6-prefix** *ipv6-prefix-name* | *acl6-number* | **acl6-name** *acl6-name* | **route-policy** *route-policy-name* } **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 address prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *acl6-number* | Specifies the number of a basic IPv6 ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **route-policy** *route-policy-name* | Specifies the name of the route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **direct** | Specifies the direct routes. | - |
| **static** | Specifies static routes. | - |
| **bgp** | Specifies BGP routes. | - |
| **ospfv3** | Specifies OSPFv3 routes. | - |
| **isis** | Specifies IS-IS routes. | - |
| **ripng** | Specifies RIPng routes. | - |
| *process-id* | Displays information about the ABR or ASBR of an OSPF route in a specified OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

RIPng view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

For a named IPv6 ACL, when the **rule** command is used to configure a filtering rule, the filtering rule is effective only with the source address range that is specified by the source parameter and with the time period that is specified by the time-range parameter.Only the routes that match the filtering policy can be added to the RIPng routing table.


Example
-------

# Filter the received RIPng Update packets based on the IPv6 prefix list named filter1.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix filter1 deny 2001:db8::1 64
[*HUAWEI] ripng 1
[*HUAWEI-ripng-1] filter-policy ipv6-prefix filter1 import

```

# Filter the advertised RIPng Update packets based on the IPv6 prefix list named filter2.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix filter2 deny 2001:db8::1 64
[*HUAWEI] ripng 100
[*HUAWEI-ripng-100] filter-policy ipv6-prefix filter2 export

```