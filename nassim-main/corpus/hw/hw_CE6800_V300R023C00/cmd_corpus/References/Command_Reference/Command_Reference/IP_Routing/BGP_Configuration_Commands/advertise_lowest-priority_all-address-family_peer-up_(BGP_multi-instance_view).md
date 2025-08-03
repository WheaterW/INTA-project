advertise lowest-priority all-address-family peer-up (BGP multi-instance view)
==============================================================================

advertise lowest-priority all-address-family peer-up (BGP multi-instance view)

Function
--------



The **advertise lowest-priority all-address-family peer-up** command configures BGP to minimize the priorities of the routes to be advertised to BGP peers when the peers go Up from Down.

The **undo advertise lowest-priority all-address-family peer-up** command restores the default configuration.



By default, the priorities of the BGP routes to be advertised remain unchanged.


Format
------

**advertise lowest-priority all-address-family peer-up** [ **delay** *delay* ]

**undo advertise lowest-priority all-address-family peer-up** [ **delay** *delay* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **delay** *delay* | Specifies a delay. | The value is an integer ranging from 1 to 864000, in seconds. The default value is 0. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the **advertise lowest-priority all-address-family peer-up** command is not run, BGP routes with unchanged priorities are advertised to peers when the peers go Up from Down. After the peers receive the routes, traffic may be switched back to the original paths. Consequently, lengthy packet loss may occur. To address this problem, run the **advertise lowest-priority all-address-family peer-up** command. After the command is run, routes advertised to the peers carry the lowest priorities (largest MED value and smallest Local\_Pref value) until delay expires.



**Precautions**



If you run the **advertise lowest-priority all-address-family peer-up delay** command and then the **advertise lowest-priority all-address-family peer-up** command in sequence, the latest configuration overrides the previous one. That is, the delay time is cleared.The advertise lowest-priority all-address-family peer-up and **advertise lowest-priority on-startup** commands are mutually exclusive.




Example
-------

# Configure BGP to minimize the priorities of the routes to be advertised to BGP peers when the peers go Up from Down.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] advertise lowest-priority all-address-family peer-up

```