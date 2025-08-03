filter-policy (BGP-VPN instance IPv4 address family view)
=========================================================

filter-policy (BGP-VPN instance IPv4 address family view)

Function
--------



The **filter-policy export** command configures a device to use an export policy to filter the routes to be advertised so that only the routes that match the export policy are advertised.

The **undo filter-policy export** command restores the default configuration.

The **filter-policy import** command configures a device to filter received routes.

The **undo filter-policy import** command restores the default configuration.



By default, received routes or the routes to be advertised are not filtered.


Format
------

**filter-policy** { *acl-number* | **ip-prefix** *ip-prefix-name* | **acl-name** *acl-name* } { **import** | **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] }

**undo filter-policy** [ *acl-number* | **ip-prefix** *ip-prefix-name* | **acl-name** *acl-name* ] { **import** | **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies a basic ACL number. | The value is an integer ranging from 2000 to 2999. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IPv4 prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **direct** | Configures a device to filter the direct routes to be advertised. | - |
| **isis** *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **ospf** *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| **rip** *process-id* | Specifies a RIPng process ID. | The value is an integer ranging from 1 to 4294967295. |
| **static** | Filters the static routes to be advertised. | - |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Using the **filter-policy export** command, you can filter the routes to be advertised by the BGP-VPN instance IPv4 address family. After the **filter-policy export** command is run, BGP filters the routes imported using the **import-route** command before importing them. Only the routes that pass the filtering can be added to the local BGP routing table and advertised by BGP.You can run the **filter-policy import** command to filter the routes received by the BGP-VPN instance IPv4 address family on a BGP device and determine whether to add the routes to the BGP routing table.If a protocol is specified, only the routes imported from the specified protocol are filtered. The routes imported from other protocols are not affected. If protocol is not specified, the routes imported from any protocol are filtered.For a named ACL, when the **rule** command is used to configure a filtering rule, the filtering rule is valid only when the source address range is specified by the source parameter and the time period is specified by the time-range parameter.


Example
-------

# Use ACL 2000 to filter all the routes to be advertised by BGP.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] filter-policy 2000 export

```