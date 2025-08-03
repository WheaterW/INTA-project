if-match ip route-source acl
============================

if-match ip route-source acl

Function
--------



The **if-match ip route-source acl** command configures a filtering rule that is based on IP addresses of the source devices from which routes are received.

The **undo if-match ip route-source acl** command cancels the configuration.



By default, no filtering rule based on IP addresses of the source devices from which routes are received is configured.


Format
------

**if-match ip route-source acl** { *acl-number* | *acl-name* }

**undo if-match ip route-source acl** { *acl-number* | *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer that ranges from 2000 to 2999. |
| *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
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

When you run the **if-match ip route-source acl** command to match the address of the source from which routes are received, an ACL must also be configured for the matching rule to take effect. For example:

* If if-match ip route-source acl 2000 is configured but acl 2000 is not configured, all routes are permitted.
* If if-match ip route-source acl 2000 and acl 2000 are configured, and the ACL rule is rule 1 permit source 1.1.1.1 32, the routes with the next hop address 1.1.1.1 are permitted.

The IP address of the source device from which a route is received is the peer address.

**Prerequisites**



A route-policy has been configured using the route-policy command.An ACL has been configured using the **acl** command.



**Configuration Impact**



When you filter routes based on source addresses, the routes that match the filtering rule are permitted and the route that do not match the filtering rule are denied.



**Precautions**



If the next hop address or source address of a route to be filtered is 0.0.0.0, by default, the system considers the mask length as 0 and matches the route.If the next hop address or source address of a route to be filtered is not 0.0.0.0, by default, the system considers the mask length as 32 and matches the route.For a named ACL, when the **rule** command is used to configure a filtering rule, only the source address range specified in source and the time period specified in time-range take effect on the filtering rule.




Example
-------

# Define a rule to match the routes with the source address matching ACL 2000.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-ac14-basic-2000] quit
[*HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match ip route-source acl 2000

```