if-match ip route-source ip-prefix
==================================

if-match ip route-source ip-prefix

Function
--------



The **if-match ip route-source ip-prefix** command configures a filtering rule that is based on IP addresses of the source devices from which routes are received.

The **undo if-match ip route-source ip-prefix** command cancels the configuration.



By default, no filtering rule based on IP addresses of the source devices from which routes are received is configured.


Format
------

**if-match ip route-source ip-prefix** *ip-prefix-name*

**undo if-match ip route-source** [ **ip-prefix** *ip-prefix-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-prefix** *ip-prefix-name* | Specifies the name of the IP prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **if-match ip** command must be used together with an IP prefix list or ACL. Otherwise, the matching condition does not take effect. For example:

* If if-match ip next-hop ip-prefix aa is configured but ip-prefix aa is not configured, all routes are permitted. This rule also applies to ACLs.
* If if-match ip next-hop ip-prefix aa and ip ip-prefix aa permit 1.1.1.1 32 are both configured, the routes with the next hop address 1.1.1.1 are permitted. This rule also applies to ACLs.

The IP address of the source device from which a route is received is the peer address.

**Prerequisites**



A route-policy has been configured using the route-policy command.An IP prefix has been configured using the **ip ip-prefix** command.



**Configuration Impact**



When you filter routes based on the source addresses, the routes that match the filtering rule are permitted and the route that do not match the filtering rule are denied.



**Precautions**



If the next hop address or source address of a route to be filtered is 0.0.0.0, by default, the system considers the mask length as 0 and matches the route.If the next hop address or source address of a route to be filtered is not 0.0.0.0, by default, the system considers the mask length as 32 and matches the route.




Example
-------

# Define a rule to match the routes with the source address matching the prefix list named p1.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p1 permit 10.0.192.0 8 greater-equal 17 less-equal 18
[*HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match ip route-source ip-prefix p1

```