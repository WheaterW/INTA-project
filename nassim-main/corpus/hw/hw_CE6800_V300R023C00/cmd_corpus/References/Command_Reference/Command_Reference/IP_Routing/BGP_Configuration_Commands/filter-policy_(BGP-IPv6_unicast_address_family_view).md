filter-policy (BGP-IPv6 unicast address family view)
====================================================

filter-policy (BGP-IPv6 unicast address family view)

Function
--------



The **filter-policy import** command configures a device to filter received routes.

The **undo filter-policy import** command restores the default configuration.

The **filter-policy export** command configures a device to use an export policy to filter the routes to be advertised so that only the routes that match the export policy are advertised.

The **undo filter-policy export** command restores the default configuration.



By default, the received or advertised routes are not filtered.

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
| **static** | Configures a device to filter the static routes to be advertised. | - |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **filter-policy export** command affects the routes advertised by BGP. After the **filter-policy export** command is run, BGP filters the routes imported using the **import-route** command before importing them. Only the routes that pass the filtering can be added to the local BGP routing table and advertised by BGP.The **filter-policy import** command can be used to filter the routes received by a BGP device globally and determine whether to add the routes to the BGP routing table.If a protocol is specified, only the routes imported from the specified protocol are filtered. The routes imported from other protocols are not affected. If protocol is not specified, the routes imported from all protocols will be filtered.When configured filtering conditions are used for a named ACL, only the configurations specified by source and time-range take effect.

**Configuration Impact**

If the **filter-policy export** command with the same protocol specified is run more than once, the latest configuration overrides the previous one.If the **filter-policy import** command runs more than once, the latest configuration overrides the previous one.


Example
-------

# Use ACL 2000 to filter all the routes to be advertised by BGP.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] filter-policy 2000 import

```