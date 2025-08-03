display bgp routing-table statistics
====================================

display bgp routing-table statistics

Function
--------



The **display bgp routing-table statistics** command displays related information about BGP route statistics.




Format
------

**display bgp routing-table statistics active**

**display bgp routing-table statistics cidr**

**display bgp routing-table statistics different-origin-as**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **statistics** | Displays statistics about BGP routes. | - |
| **cidr** | Displays classless inter-domain routing (CIDR) information. | - |
| **different-origin-as** | Displays routes that have the same destination address but different source AS numbers. | - |
| **active** | Displays statistics about active routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

When you need to view the statistics of BGP routes, run this command and specify the required parameters.

**Precautions**

During route flapping, the route statistics may differ from the actual number of routes on the network because some routes are on the way and have not arrived.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display active route statistics.
```
<HUAWEI> display bgp routing-table statistics active

 Total Number of Prefix Advertised to RM : 2
 Total Number of Active Route : 2

```

**Table 1** Description of the **display bgp routing-table statistics** command output
| Item | Description |
| --- | --- |
| Total Number of Prefix Advertised to RM | Number of routes delivered to the RM module. |
| Total Number of Active Route | Number of active routes. |