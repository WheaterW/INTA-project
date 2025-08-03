lsa-age refresh disable (OSPFv3 view)
=====================================

lsa-age refresh disable (OSPFv3 view)

Function
--------



The **lsa-age refresh disable** command disables OSPFv3 LSA aging management.

The **undo lsa-age refresh disable** command enables OSPFv3 LSA aging management.



By default, OSPFv3 LSA aging management is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**lsa-age refresh disable**

**undo lsa-age refresh disable**


Parameters
----------

None

Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If an exception occurs in the age field of LSAs, LSAs may be aged unexpectedly, causing LSA flapping or a route calculation error. For example, if the abnormal aging time is 2500s and the actual aging time is 500s, LSAs are aged prematurely. To address this problem, OSPFv3 LSA aging management is enabled by default. If the aging time in a received LSA is greater than 1800s, OSPFv3 considers the LSA abnormal and changes the aging time to 1700s until the aging time values of all LSAs in the area become the same. In this case, routes can be calculated correctly.


Example
-------

# Disable OSPFv3 LSA aging management.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] lsa-age refresh disable

```