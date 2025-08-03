ospf flush-source-trace disable
===============================

ospf flush-source-trace disable

Function
--------



The **ospf flush-source-trace disable** command disables OSPF flush LSA source tracing globally.

The **undo ospf flush-source-trace disable** command enables OSPF flush LSA source tracing globally.



By default, OSPF flush LSA source tracing is enabled globally.


Format
------

**ospf flush-source-trace** [ **vlink** ] **disable**

**undo ospf flush-source-trace** [ **vlink** ] **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlink** | Specifies an OSPF virtual link. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If network-wide OSPF LSAs are flushed, network stability will be adversely affected. In this case, source tracing must be implemented to locate the root cause of the fault immediately to minimize the impact. However, OSPF itself does not support source tracing. A conventional solution is isolation node by node until the faulty node is located. The solution is complex and time-consuming. OSPF flush LSA source tracing can address this problem. In the preceding scenario, OSPF flush LSA source tracing packets are flooded on the network, and the node that flushed the LSAs can be queried on any device on the network, which speeds up fault locating and faulty node isolation.To disable OSPF flush LSA source tracing globally, run the **ospf flush-source-trace disable** command. To disable Vlink OSPF flush LSA source tracing, run the **ospf flush-source-trace vlink disable** command.




Example
-------

# Disable OSPF flush LSA source tracing globally.
```
<HUAWEI> system-view
[~HUAWEI] ospf flush-source-trace disable

```