flood proxy
===========

flood proxy

Function
--------



The **flood proxy** command configures a flood proxy IP address.

The **undo flood proxy** command deletes the configured flood proxy IP address.



By default, no flood proxy IP address is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**flood proxy** *ip-address*

**undo flood proxy** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a flood proxy IP address. | The value is in dotted decimal notation. |



Views
-----

NVE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On the VXLAN network, the source VTEP has multiple remote VTEPs. The **vni head-end peer-list** command is configured to specify the remote VTEPs. When source VTEP sends BUM packets in ingress replication mode, it needs to send one copy of the packets to each remote VTEP, causing the packet to be flooded and increasing the network load. To solve this problem, a flood gateway can be configured. You can run the **flood proxy** command on the gateway to configure it as the flood gateway, which is also called a centralized replicator. When source VTEP receives BUM packets, it only needs to send one copy of the packets to the centralized replicator. The centralized replicator then sends the packets to each remote VTEP, which reduces flooded traffic on the network.The source IP address encapsulated in the packets sent by the centralized replicator to other VTEPs is the IP address of source VTEP. Therefore, MAC address learning among the VTEPs is not affected.


Example
-------

# Set the flood proxy IP address to 2.2.2.2.
```
<HUAWEI> system-view
[~HUAWEI] interface nve 1
[*HUAWEI-Nve1] source 1.1.1.1
[*HUAWEI-Nve1] flood proxy 2.2.2.2

```