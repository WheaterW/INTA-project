peer ip-prefix import (BGP view) (group)
========================================

peer ip-prefix import (BGP view) (group)

Function
--------



The **peer ip-prefix import** command configures a policy based on an IP prefix list for filtering BGP routes received from a specified peer group.

The **undo peer ip-prefix import** command cancels this configuration.



By default, no route filtering policy based on an IP address prefix list is configured for a peer group.


Format
------

**peer** *group-name* **ip-prefix** *ip-prefix-name* **import**

**undo peer** *group-name* **ip-prefix** [ *ip-prefix-name* ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
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

The **peer ip-prefix import** command can be used to configure a route filtering policy that is based on an IP prefix list for filtering BGP routes to be received from a specified peer group, implementing route control.

**Prerequisites**

If the **peer ip-prefix** command specifies an IP prefix list that does not exist for a peer, use the **ip ip-prefix** command to create an IP prefix list.

**Configuration Impact**

If an IP prefix list is specified for a peer group, all peers in the peer group inherit the configuration.After an IP prefix list is specified for a peer group, the device filters the routes received from the peers in the peer group based on the IP prefix list and accepts only the routes that match the IP prefix list.

**Precautions**

If you run both this command and the **peer route-filter import** command, the latest configuration overrides the previous one.If the length of the filter name is less than or equal to six characters and the name matches the first six characters of import, when running the **undo peer ip-prefix import** command, you only need to enter the keyword import instead of the filter name.


Example
-------

# Configure a route filtering policy named prefix1 based on an IP prefix list.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix1 permit 10.1.1.1 8 greater-equal 17 less-equal 18
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test ip-prefix prefix1 import

```