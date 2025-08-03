ospfv3 flush-source-trace disable
=================================

ospfv3 flush-source-trace disable

Function
--------



The **ospfv3 flush-source-trace disable** command disables OSPFv3 flush LSA source tracing globally.

The **undo ospfv3 flush-source-trace disable** command enables OSPFv3 flush LSA source tracing globally.



By default, OSPFv3 flush LSA source tracing is enabled globally.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 flush-source-trace disable**

**undo ospfv3 flush-source-trace disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If network-wide OSPFv3 LSAs are flushed, network stability will be adversely affected. In this case, source tracing must be implemented to locate the root cause of the fault immediately to minimize the impact. However, OSPFv3 itself does not support source tracing. A conventional solution is isolation node by node until the faulty node is located. The solution is complex and time-consuming. OSPFv3 flush LSA source tracing can address this problem. In the preceding scenario, OSPFv3 flush LSA source tracing packets are flooded on the network, and the node that flushed the LSAs can be queried on any device on the network, which speeds up fault locating and faulty node isolation.


Example
-------

# Disable OSPFv3 flush LSA source tracing globally.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 flush-source-trace disable

```