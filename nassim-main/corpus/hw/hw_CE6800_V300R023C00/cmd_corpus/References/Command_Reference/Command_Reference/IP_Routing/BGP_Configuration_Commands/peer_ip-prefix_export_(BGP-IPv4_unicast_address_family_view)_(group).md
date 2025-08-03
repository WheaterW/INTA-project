peer ip-prefix export (BGP-IPv4 unicast address family view) (group)
====================================================================

peer ip-prefix export (BGP-IPv4 unicast address family view) (group)

Function
--------



The **peer ip-prefix export** command configures a policy based on an IP prefix list for filtering BGP routes to be advertised to a specified peer group.

The **undo peer ip-prefix export** command cancels this configuration.



By default, no route filtering policy based on an IP address prefix list is configured for a peer group.


Format
------

**peer** *group-name* **ip-prefix** *ip-prefix-name* **export**

**undo peer** *group-name* **ip-prefix** [ *ip-prefix-name* ] **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP address prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **export** | Applies a route-filter to the routes to be advertised to a specified peer group. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer ip-prefix export** command can be used to configure a route filtering policy that is based on an IP prefix list for filtering BGP routes to be advertised to a specified peer group, implementing route control.

**Prerequisites**

If the **peer ip-prefix** command specifies an IP prefix list that does not exist for a peer, use the **ip ip-prefix** command to create an IP prefix list.

**Configuration Impact**

If an IP prefix list is specified for a peer group, all the members of the peer group inherit the configuration.After an IP prefix list is specified for a peer group, the peers in the peer group filter routes based on the IP prefix list when advertising routes to peers. Only the routes that pass the filtering of the IP prefix list can be advertised.

**Precautions**

If you run both this command and the **peer route-filter export** command, the latest configuration overrides the previous one.If the length of the filter name is less than or equal to six characters and the name matches the first six characters of export, when running the **undo peer ip-prefix export** command, you only need to enter the keyword export instead of the filter name.


Example
-------

# Configure a route filtering policy named prefix1 based on an IP prefix list.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix1 permit 10.1.1.1 8 greater-equal 17 less-equal 18
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer test ip-prefix prefix1 export

```