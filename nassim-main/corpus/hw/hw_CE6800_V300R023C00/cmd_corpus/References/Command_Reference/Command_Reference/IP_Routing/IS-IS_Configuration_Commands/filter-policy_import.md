filter-policy import
====================

filter-policy import

Function
--------



The **filter-policy import** command configures IS-IS to filter the received routes to be added to the IP routing table.

The **undo filter-policy import** command disables IS-IS from filtering received routes.



By default, IS-IS does not filter received routes.


Format
------

**filter-policy** { *acl-number* | **acl-name** *acl-name-string* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } **import**

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name-string* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies a basic ACL number. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name-string* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ip-prefix** *ip-prefix-name* | Indicates the name of the IP prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy to filter routes based on tags and other protocol parameters. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

IS-IS routing entries need to be added to an IP routing table for IP packet forwarding.If an IS-IS routing table has routes destined for a specific network segment, but you do not want to add these routes to an IP routing table, run the filter-policy import command with specified parameters to add only the needed IS-IS routes to the IP routing table.

**Prerequisites**

An IS-IS process has been created.

**Configuration Impact**

Running the filter-policy import command on a router does not affect LSP flooding and LSDB synchronization on the router, but affects the local IP routing table.


Example
-------

# Filter received routes based on route policy policy1.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix-a index 10 permit 172.17.1.0 24
[*HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] if-match ip-prefix prefix-a
[*HUAWEI-route-policy] quit
[*HUAWEI] isis
[*HUAWEI-isis-1] filter-policy route-policy policy1 import

```