filter-policy (BGP-VPN instance IPv6 address family view)
=========================================================

filter-policy (BGP-VPN instance IPv6 address family view)

Function
--------



The **filter-policy export** command configures a device to use an export policy to filter the routes to be advertised so that only the routes that match the export policy are advertised.

The **undo filter-policy export** command restores the default configuration.

The **filter-policy import** command configures a device to filter received routes.

The **undo filter-policy import** command restores the default configuration.



By default, received routes or the routes to be advertised are not filtered.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**filter-policy** { *acl6-number* | **ipv6-prefix** *ipv6-prefix-name* | **acl6-name** *acl6-name* } { **import** | **export** [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** ] }

**undo filter-policy** [ *acl6-number* | **ipv6-prefix** *ipv6-prefix-name* | **acl6-name** *acl6-name* ] { **import** | **export** [ **direct** | **isis** *process-id* | **ospfv3** *process-id* | **ripng** *process-id* | **static** ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies the number of a basic ACL6. | The value is an integer ranging from 2000 to 2999. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 prefix list. | The value is a string of 1 to 169 case-sensitive characters. The character string can contain spaces if it is enclosed in double quotation marks (""). |
| **acl6-name** *acl6-name* | Specifies the name of a basic named ACL6. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter or digit, and cannot contain only digits. |
| **direct** | Filters the direct routes to be advertised. | - |
| **isis** *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **ospfv3** *process-id* | Specifies a process ID of OSPFv3. | The value is an integer ranging from 1 to 4294967295. |
| **ripng** *process-id* | Specifies the RIPng process ID. | The value is an integer ranging from 1 to 4294967295. |
| **static** | Filters the static routes to be advertised. | - |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **filter-policy export** command filters the routes to be advertised by the BGP-VPN instance IPv6 address family. After the **filter-policy export** command is run, BGP filters the routes imported using the **import-route** command before importing them. Only the routes that pass the filtering can be added to the local BGP routing table and advertised by BGP.You can run the **filter-policy import** command to filter the routes received by the BGP-VPN instance IPv6 address family on a BGP device and determine whether to add the routes to the BGP routing table.If a protocol is specified, only the routes imported from the specified protocol are filtered. The routes imported from other protocols are not affected. If a protocol is not specified, the routes imported from any protocol are filtered.For a named ACL, when the **rule** command is used to configure a filtering rule, the filtering rule is valid only when the source address range is specified by the source parameter and the time period is specified by the time-range parameter.


Example
-------

# Use ACL 2000 to filter all the routes to be advertised by BGP.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] filter-policy 2000 export

```