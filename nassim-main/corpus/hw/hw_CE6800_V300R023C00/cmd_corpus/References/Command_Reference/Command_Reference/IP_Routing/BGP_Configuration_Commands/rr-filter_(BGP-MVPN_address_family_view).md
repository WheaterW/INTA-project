rr-filter (BGP-MVPN address family view)
========================================

rr-filter (BGP-MVPN address family view)

Function
--------



The **rr-filter** command configures a reflection policy for an RR.

The **undo rr-filter** command cancels the configuration.



By default, there is no reflection policy for an RR.


Format
------

**rr-filter** *extcomm-filter-name*

**undo rr-filter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *extcomm-filter-name* | * Specifies the name of an extended community filter that an RR group supports. Only one extended community filter can be specified each time. * Specifies the number of the extended community filter that an RR group supports. Only one extended community filter can be specified each time. | * Name of an extended community filter: The name is a string of 1 to 51 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks. * Number of an extended community filter: The value is an integer ranging from 1 to 399. |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Full-mesh connections need to be established between IBGP peers in an AS to ensure the connectivity between the IBGP peers. When there are many IBGP peers, it is costly to establish a fully-meshed network. An RR or a confederation can be used to solve the problem. Only the IBGP route of which route-target extended community attribute meets the matching rules can be reflected. This allows load balancing among RRs.


Example
-------

# Create an RR group on a BGP device and enable the BGP device to filter incoming MVPN routing updates automatically based on the configured route-target extended community.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-filter 10 deny rt 200:200
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] rr-filter 10

```