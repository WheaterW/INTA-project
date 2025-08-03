ospf flush-source-trace port
============================

ospf flush-source-trace port

Function
--------



The **ospf flush-source-trace port** command configures a UDP port number for OSPF flush LSA source tracing packets.

The **undo ospf flush-source-trace port** command restores the default UDP port number for OSPF flush LSA source tracing packets.



By default, the UDP port number of global OSPF flush LSA source tracing packets is 50122, and the UDP port number of Vlink OSPF flush LSA source tracing packets is 50123.


Format
------

**ospf flush-source-trace port** *port-number*

**ospf flush-source-trace vlink port** *port-number*

**undo ospf flush-source-trace port**

**undo ospf flush-source-trace vlink port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies a UDP port number. | The value is an integer ranging from 1025 to 65535. |
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



The OSPF flush LSA source tracing port receives and sends OSPF flush LSA source tracing packets, and the port is identified by a UDP port number.If the UDP port number conflicts with that of an application, you can change the UDP port number of OSPF flush LSA source tracing packets using the **ospf flush-source-trace port** command. To change the UDP port number of Vlink OSPF flush LSA source tracing packets, run the **ospf flush-source-trace vlink port** command.




Example
-------

# Set the UDP port number of OSPF flush LSA source tracing packets to 1512.
```
<HUAWEI> system-view
[~HUAWEI] ospf flush-source-trace port 1512

```