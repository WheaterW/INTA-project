maxage-lsa route-calculate-delay
================================

maxage-lsa route-calculate-delay

Function
--------



The **maxage-lsa route-calculate-delay** command enables delayed route calculation during OSPF router LSA aging or update.

The **undo maxage-lsa route-calculate-delay** command disables delayed route calculation during OSPF router LSA aging or update.



By default, the delayed route calculation function is enabled when OSPF router LSAs are aged or updated.


Format
------

**maxage-lsa route-calculate-delay** *delay-interval*

**undo maxage-lsa route-calculate-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-interval* | Specifies a route calculation delay. | The value is an integer ranging from 0 to 65535, in seconds. The default value is 20 seconds. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Continuous aging or update of OSPF router LSAs on the peer device causes route flapping on the local device, affecting normal service traffic. In this case, you can run the **maxage-lsa route-calculate-delay** command on the local device to delay route calculation, which suppresses route flapping on the local device.


Example
-------

# Set the route calculation delay to suppress frequent OSPF LSA flapping to 200s.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] maxage-lsa route-calculate-delay 200

```