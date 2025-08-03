isis purge-source-trace port
============================

isis purge-source-trace port

Function
--------



The **isis purge-source-trace port** command configures a UDP port number for IS-IS purge LSP source tracing packets.

The **undo isis purge-source-trace port** command restores the default port number.



By default, the UDP port number carried in IS-IS purge LSP source tracing packets is 50121.


Format
------

**isis purge-source-trace port** *port-number*

**undo isis purge-source-trace port** [ *port-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies a UDP port number for IS-IS purge LSP source tracing packets. | The value is an integer ranging from 1025 to 65535. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The IS-IS purge LSP source tracing port receives and sends IS-IS purge LSP source tracing packets, and the port is identified by a UDP port ID.




Example
-------

# Set the UDP port number to 1512 for IS-IS purge LSP source tracing packets.
```
<HUAWEI> system-view
[~HUAWEI] isis purge-source-trace port 1512

```