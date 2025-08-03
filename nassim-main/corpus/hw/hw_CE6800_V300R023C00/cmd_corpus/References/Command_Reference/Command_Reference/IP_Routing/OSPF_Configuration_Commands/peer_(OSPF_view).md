peer (OSPF view)
================

peer (OSPF view)

Function
--------



The **peer** command sets an IP address and a DR priority for an adjacent device on an NBMA network.

The **undo peer** command cancels the configured IP address and DR priority.



By default, IP address and a DR priority for an adjacent device on an NBMA network is not set.


Format
------

**peer** *ip-address* [ **dr-priority** *priority* ]

**undo peer** *ip-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address for an adjacent router. | Dotted decimal notation. |
| **dr-priority** *priority* | Sets a priority for an adjacent router for DR election. | The value is an integer ranging from 0 to 255. The default value is 1. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On an NBMA network (such as an X.25 network), the entire network can be fully meshed if adjacent router mapping is configured. With the mapping, there is a virtual link between any two routers. In this case, the OSPF network can be considered as a broadcast network where a DR or BDR can be selected. However, adjacent routers cannot be detected dynamically by broadcasting Hello packets. To address this problem, run the **peer** command to specify an IP address and a DR priority for each adjacent router.


Example
-------

# Set the IP address of the adjacent router to 1.1.1.1 on an NBMA network.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] peer 1.1.1.1

```