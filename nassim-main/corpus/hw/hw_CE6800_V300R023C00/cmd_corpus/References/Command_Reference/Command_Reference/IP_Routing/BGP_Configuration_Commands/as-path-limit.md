as-path-limit
=============

as-path-limit

Function
--------



The **as-path-limit** command sets the maximum number of AS numbers in the AS\_Path attribute.

The **undo as-path-limit** command restores the default setting.



By default, the maximum number of AS numbers in the AS\_Path attribute is 2000, and the maximum number of AS numbers carried in the AS\_Path attribute is also limited by the BGP message length.


Format
------

**as-path-limit** *limit*

**as-path-limit**

**undo as-path-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit* | Specifies the maximum number of AS numbers in the AS\_Path attribute. | The value is an integer ranging from 1 to 2000. The default value is 255.  The maximum value of limit for the 2-byte and 4-byte AS number is the same.  If limit is not specified, the maximum number of AS numbers in the AS\_Path attribute is 255. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command is used to limit the maximum number of AS numbers in the AS\_Path attribute only when the AS\_Path attribute is reconstructed, routes are summarized to generate new routes, routes are newly learned from peers, or routes are advertised to peers.

**Configuration Impact**

After the **as-path-limit** command is configured, the device checks whether the number of AS numbers in the AS\_Path attribute of the routes to be received or sent exceeds the upper limit. The learned routes are not checked. If the number of AS numbers exceeds the upper limit, the device discards the route. Therefore, if the maximum number of AS numbers in the AS\_Path attribute is set too small, routes will be lost.


Example
-------

# Set the maximum number of AS numbers in the AS\_Path attribute to 200.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] as-path-limit 200

```