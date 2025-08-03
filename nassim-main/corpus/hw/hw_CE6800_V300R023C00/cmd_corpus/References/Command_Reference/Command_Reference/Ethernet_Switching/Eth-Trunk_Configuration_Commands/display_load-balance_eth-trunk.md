display load-balance eth-trunk
==============================

display load-balance eth-trunk

Function
--------



The **display load-balance eth-trunk** command displays detailed information about a specified load balancing mode in effect of an Eth-Trunk interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display load-balance eth-trunk** *trunk-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk. | The value is an integer that ranges from 0 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays detailed information about a specified load balancing, including the load balancing mode of IP , Layer 2, and MPLS packets.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information of Eth-Trunk1 about a specified load balancing mode in effect.
```
<HUAWEI> display load-balance eth-trunk 1
Load-balance info: Eth-Trunk1
Packet HashField
---------------------------------------------------                                                                                 
IP             session-id      dst-qp
               src-ip          dst-ip
               l4-src-port     l4-dst-port
L2             src-mac         dst-mac
               vlan
MPLS           top-label       2nd-label
Eth-Trunk      hash-mode(1)    seed(1)
---------------------------------------------------

```

**Table 1** Description of the **display load-balance eth-trunk** command output
| Item | Description |
| --- | --- |
| Load-balance info | Load balancing information. |
| Packet | Packet type. |
| HashField | Load balancing mode. |