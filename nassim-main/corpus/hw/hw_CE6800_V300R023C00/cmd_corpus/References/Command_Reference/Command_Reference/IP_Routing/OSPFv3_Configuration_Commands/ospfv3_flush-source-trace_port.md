ospfv3 flush-source-trace port
==============================

ospfv3 flush-source-trace port

Function
--------



The **ospfv3 flush-source-trace port** command configures a UDP port number for OSPFv3 flush LSA source tracing packets.

The **undo ospfv3 flush-source-trace port** command restores the default UDP port number for OSPFv3 flush LSA source tracing packets.



By default, the UDP port number of global OSPFv3 flush LSA source tracing packets is 50122.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 flush-source-trace port** *port-number*

**undo ospfv3 flush-source-trace port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies a UDP port number. | The value is an integer ranging from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The OSPFv3 flush LSA source tracing port receives and sends OSPFv3 flush LSA source tracing packets, and the port is identified by a UDP port number. If the UDP port number conflicts with that of an application, you can change the UDP port number of OSPFv3 flush LSA source tracing packets using the **ospfv3 flush-source-trace port** command.


Example
-------

# Set the UDP port number of OSPFv3 flush LSA source tracing packets to 1512.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 flush-source-trace port 1512

```