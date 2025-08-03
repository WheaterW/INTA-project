lsa-age refresh disable
=======================

lsa-age refresh disable

Function
--------



The **lsa-age refresh disable** command disables OSPF LSA aging management.

The **undo lsa-age refresh disable** command enables OSPF LSA aging management.



By default, OSPF LSA aging management is enabled.


Format
------

**lsa-age refresh disable**

**undo lsa-age refresh disable**


Parameters
----------

None

Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The lsa-age field is abnormal due to certain reasons. As a result, LSAs with abnormal aging time are generated on the device, which may cause LSA flapping or route calculation errors. For example, when an LSA with the age of 2500 seconds is received, the LSA has been generated for only 500 seconds. As a result, the LSA ages too early. To solve this problem, OSPF LSA aging management is enabled by default. If the aging time of a received LSA is greater than 1800s (the device considers the LSA abnormal), OSPF changes the aging time of the LSA to 1700s until the aging time of all LSAs in the area is the same. This ensures correct route calculation.


Example
-------

# Disable OSPF LSA aging management.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] lsa-age refresh disable

```