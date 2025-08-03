if-match ip next-hop acl
========================

if-match ip next-hop acl

Function
--------



The **if-match ip next-hop acl** command configures a filtering rule that is based on next-hop IP addresses.

The **undo if-match ip next-hop acl** command cancels the configuration.



By default, no filtering rule based on next-hop IP addresses is configured.


Format
------

**if-match ip next-hop acl** { *acl-number* | *acl-name* }

**undo if-match ip next-hop acl** { *acl-number* | *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **acl** | Specifies the ACL for route filtering. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you run the **if-match ip next-hop acl** command to match the next hops of IPv4 routes, an ACL must be used together with the **if-match ip next-hop acl** command. For example:

* If if-match ip next-hop acl 2000 is configured but ACL 2000 is not configured, all routes are permitted.
* If if-match ip next-hop acl 2000 is configured, ACL 2000 is configured, and the ACL rule is rule 1 permit source 1.1.1.1 32, the routes with the next hop being 1.1.1.1 are permitted.

**Prerequisites**



A route-policy has been configured using the route-policy command.An ACL has been configured using the **acl** command.



**Configuration Impact**



When you filter routes based on the next hop addresses, the routes that match the filtering rule are permitted and the route that do not match the filtering rule are denied.



**Precautions**



If the next hop address or source address of a route to be filtered is 0.0.0.0, by default, the system considers the mask length as 0 and matches the route.If the next hop address or source address of a route to be filtered is not 0.0.0.0, by default, the system considers the mask length as 32 and matches the route.For a named ACL, when the **rule** command is used to configure a filtering rule, only the source address range specified in source and the time period specified in time-range take effect on the filtering rule.




Example
-------

# Define a rule to match the routes with the next hop address in the ACL list.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-ac14-basic-2000] quit
[*HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match ip next-hop acl 2000

```