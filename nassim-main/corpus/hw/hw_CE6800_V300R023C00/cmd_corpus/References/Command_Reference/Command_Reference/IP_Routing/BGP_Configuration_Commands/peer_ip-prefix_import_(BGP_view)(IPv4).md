peer ip-prefix import (BGP view)(IPv4)
======================================

peer ip-prefix import (BGP view)(IPv4)

Function
--------



The **peer ip-prefix import** command configures a policy based on an IP prefix list for filtering BGP routes received from a specified peer.

The **undo peer ip-prefix import** command cancels this configuration.



By default, no route filtering policy based on an IP address prefix list is configured for a peer.


Format
------

**peer** *ipv4-address* **ip-prefix** *ip-prefix-name* **import**

**undo peer** *ipv4-address* **ip-prefix** [ *ip-prefix-name* ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP address prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **import** | Applies a filtering policy to the routes received from a peer group. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer ip-prefix import** command can be used to configure a route filtering policy that is based on an IP prefix list for filtering BGP routes to be received from a specified peer, implementing route control.

**Prerequisites**

If the **peer ip-prefix** command specifies an IP prefix list that does not exist for a peer, use the **ip ip-prefix** command to create an IP prefix list.

**Configuration Impact**

After an IP prefix list is specified for a peer, the device filters routes based on the IP prefix list when receiving routes from the peer. Only the routes that match the IP prefix list can be accepted.

**Precautions**

If you run both this command and the **peer route-filter import** command, the latest configuration overrides the previous one.If the length of the filter name is less than or equal to six characters and the name matches the first six characters of import, when running the **undo peer ip-prefix import** command, you only need to enter the keyword import instead of the filter name.


Example
-------

# Configure a route filtering policy named prefix1 based on an IP prefix list.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix1 permit 10.1.1.1 8 greater-equal 17 less-equal 18
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] peer 10.1.1.1 ip-prefix prefix1 import

```