downlink recover interval
=========================

downlink recover interval

Function
--------



The **downlink recover interval** command sets the delay after which downlink interfaces in a Monitor Link group go Up one by one.

The **undo downlink recover interval** command restores the default delay after which downlink interfaces in a Monitor Link group go Up.



By default, the delay after which downlink interfaces in a Monitor Link group go Up is 0s. That is, all downlink interfaces in a Monitor Link group are enabled.


Format
------

**downlink recover interval** *interval-value*

**undo downlink recover interval** [ *interval-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-value* | Specifies the delay after which a downlink interface goes Up. | The value is an integer ranging from 0 to 180, in seconds. |



Views
-----

Monitor link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A Monitor Link group consists of uplink interfaces and downlink interfaces. When all uplink interfaces fail, the Monitor Link group automatically shuts down all downlink interfaces. After the uplink interfaces of the Monitor Link group recover, all downlink interfaces are enabled. In an M-LAG scenario, ARP and ND entries pointing to the peer-link need to be updated to these downlink interfaces one by one. If a large number of downstream interfaces are enabled at the same time, a large number of ARP and ND entries need to be updated in a short period of time, which may degrade the switchback performance. In this case, you can configure a delay for downlink interfaces to go Up. After the uplink interfaces recover, the downlink interfaces are enabled one by one.



**Prerequisites**



A Monitor Link has been created using the **monitor-link group** command.



**Precautions**



If interval-value is set to 0, all downlink interfaces are enabled.




Example
-------

# Set the delay after which downlink interfaces in Monitor Link group 1 goes Up to 6 seconds.
```
<HUAWEI> system-view
[~HUAWEI] monitor-link group 1
[*HUAWEI-mtlk-group1] downlink recover interval 6

```