qos-local-id (BGP view)
=======================

qos-local-id (BGP view)

Function
--------



The **qos-local-id** command sets a value for the QoS local ID.

The **undo qos-local-id** command deletes the value set for the QoS local ID.



By default, no value is set for the QoS local ID.


Format
------

**qos-local-id** { *qos-local-id* | **route-policy** *route-policy-name* }

**undo qos-local-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *qos-local-id* | Specifies a value for the QoS local ID. | The value is an integer in the range from 1 to 1024. |
| **route-policy** *route-policy-name* | Specifies the name of the route-policy. | The value is a string of 1 to 200 case-sensitive characters, spaces not supported. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set a value for the QoS local ID, run the **qos-local-id** command. The set QoS local ID is delivered to the FIB. During forwarding, the system implements QoS policies based on the QoS local IDs in the FIB. Alternatively, you can use a route-policy to set a value for the QoS local ID.

**Precautions**

Using the **qos-local-id** command, you can set the QoS local ID locally. You can also run the **apply qos-local-id** command in the route-policy to set the QoS local ID when BGP imports routes. If the two configuration modes coexist and the QoS local IDs are different, the QoS local ID set through the route-policy takes effect preferentially.


Example
-------

# Set the QoS local ID to 10.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] qos-local-id 10

```