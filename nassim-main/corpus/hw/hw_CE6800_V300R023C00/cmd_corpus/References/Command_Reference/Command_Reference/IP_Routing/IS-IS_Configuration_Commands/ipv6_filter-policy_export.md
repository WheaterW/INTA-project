ipv6 filter-policy export
=========================

ipv6 filter-policy export

Function
--------



The **ipv6 filter-policy export** command configures IS-IS to filter imported IPv6 routes before route advertisement.

The **undo ipv6 filter-policy export** command disables such filtering.



By default, IS-IS does not filter imported IPv6 routes before route advertisement.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 filter-policy** { *acl6-number* | **acl6-name** *acl6-name-string* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* } { **export** [ **direct** | **static** | **ripng** *process-id* | **bgp** | **ospfv3** *process-id* | **isis** *process-id* ] }

**undo ipv6 filter-policy** [ *acl6-number* | **acl6-name** *acl6-name-string* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* ] { **export** [ **direct** | **static** | **ripng** *process-id* | **bgp** | **ospfv3** *process-id* | **isis** *process-id* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies a basic ACL6 number. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name-string* | Specifies the name of a named basic ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 address prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy to filter routes based on tags and other protocol parameters. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **direct** | Specifies to filter the imported direct routes before route advertisement. | - |
| **static** | Specifies to filter the imported static routes before route advertisement. | - |
| **ripng** *process-id* | Specifies the ID of an RIPng process. | The value is an integer ranging from 1 to 4294967295. |
| **bgp** | Specifies to filter the imported BGP routes before route advertisement. | - |
| **ospfv3** *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| **isis** *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **ipv6 filter-policy export** command is usually used with the ipv6 import-route command. The **ipv6 filter-policy export** command is used to filter imported routes so that only given routes are advertised to other devices. If protocol is not specified, the routes imported from all protocols are filtered; if protocol is specified, the routes imported from the specified protocol are filtered.Enable the IPv6 capability for the IS-IS process first before you run this command. For details, refer to isis ipv6 enable.


Example
-------

# Configure IS-IS to filter imported routes based on ACL6 2002 when advertising the routes to other devices.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2002
[*HUAWEI-acl6-basic-2002] quit
[*HUAWEI] isis
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 filter-policy 2002 export

```