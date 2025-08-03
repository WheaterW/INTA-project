display nqa support-server-type
===============================

display nqa support-server-type

Function
--------



The **display nqa support-server-type** command displays server types supported by NQA.




Format
------

**display nqa support-server-type**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Both the server and the client have been configured before a TCP, UDP, UDP jitter, and ICMP jitter test instance is started. Otherwise, a test instance cannot be started.The **display nqa support-server-type** command displays server types supported by NQA. Currently, the following server types are supported:

* TCP server, supporting TCP test instances
* UDP server, supporting UDP and UDP jitter test instances
* ICMP server, supporting ICMP jitter test instances that enable the interface board to send packets

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display server types supported by NQA.
```
<HUAWEI> display nqa support-server-type
NQA support server type information:
----------------------------------------------------
  Type            Description
  tcp server      NQA TCP server
  udp server      NQA UDP server
----------------------------------------------------

```

**Table 1** Description of the **display nqa support-server-type** command output
| Item | Description |
| --- | --- |
| NQA support server type information | Information of server types that NQA supports. |
| Type | Type of an NQA server. |
| Description | Description of an NQA server. |