distribute-weight
=================

distribute-weight

Function
--------

The **distribute-weight** command configures the weight of load balancing for a member interface.

The **undo distribute-weight** command deletes the configured weight of load balancing of a member interface.

By default, the weight of load balancing on a member interface is 1.



Format
------

**distribute-weight** *weight-value*

**undo distribute-weight**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *weight-value* | Specifies the weight of an Eth-Trunk member interface. | The value is a decimal integer ranging from 1 to 256. |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk member interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

On an Eth-Trunk interface, you can load-balance traffic among member interfaces according to the weights configured for the member interfaces.

The higher the weight of a member interface, the heavier the load over the member link. Therefore, you can run this command to configure a higher weight for a member interface so that the member link can carry a heavier load.It is recommended that this function be used when each Eth-Trunk member interface has a different bandwidth. Configure a large weight for higher-bandwidth interfaces to carry larger amounts of load.To restore the weight of a member interface to the default value, you can run either of the following commands in the Ethernet interface view:

* undo distribute-weight, which restores the weight of a member interface to the default value
* distribute-weight 1, which forcibly sets the weight of a member interface to the default value 1.

**Prerequisites**

An Eth-Trunk interface has been correctly configured, and interfaces have been added to the Eth-Trunk interface.

**Configuration Impact**

The higher the weight of a member interface, the heavier the load over the member link.

**Precautions**

* If this command is run more than once to configure member interface weights, the latest configured weight overrides the previous one.
* The total weight of all member interfaces of an Eth-Trunk interface cannot exceed the maximum number of member interfaces supported by the Eth-Trunk interface. For example, if three member interfaces with weights 3, 3, and 2 are added to an Eth-Trunk interface that supports a maximum of eight member interfaces, the total weight of the three member interfaces is 8. In this case, the configuration is valid. If the total weight exceeds 8 after a new member interface is added, the configuration is invalid.



Example
-------

# Set the load balancing weight of the Eth-Trunk member interface
100GE
1/0/1 to 3.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk1
[*HUAWEI-Eth-Trunk1] trunkport 100GE 1/0/1
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] distribute-weight 3

```