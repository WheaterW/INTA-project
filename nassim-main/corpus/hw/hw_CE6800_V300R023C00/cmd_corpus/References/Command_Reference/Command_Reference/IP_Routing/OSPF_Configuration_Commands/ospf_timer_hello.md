ospf timer hello
================

ospf timer hello

Function
--------



The **ospf timer hello** command sets the interval at which Hello packets are sent on an interface.

The **undo ospf timer hello** command restores the default value.



By default, for P2P and broadcast interfaces, the interval is 10 seconds, for P2MP and NBMA interfaces, the interval is 30 seconds.


Format
------

**ospf timer hello** *interval* [ **conservative** ]

**undo ospf timer hello**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which Hello packets are sent on an interface. | The value is an integer ranging from 1 to 65535, in seconds.  Setting hello interval to be longer than 2s is recommended. |
| **conservative** | Indicates the conservative mode of the dead timer. If the conservative mode is configured, the value configured for the dead timer using the ospf timer dead command takes effect even when the value is less than 10s. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Hello packets are periodically exchanged by OSPF interfaces to establish and maintain neighbor relationships. A Hello packet contains information about timers, DRs, BDRs, and known neighbors.The smaller the interval value, the faster a network topology change can be detected, and the larger the route cost. Ensure that the parameters of this interface and the adjacent routers are consistent.To speed up OSPF convergence in the case of a link failure, configuring BFD For OSPF is recommended. If the remote end does not support BFD for OSPF or you do not want to configure BFD for OSPF, specify conservative when you run the ospf timer hello command. If the conservative mode is configured, the value configured for the dead timer using the **ospf timer dead** command takes effect even when the value is less than 10s; if the value configured for the dead timer is greater than 10s, services may be affected.

**Precautions**



If OSPF packets are encapsulated with GRE packets, you are advised to set the interval for sending Hello packets to a large value. As OSPF Hello packets are encapsulated into GRE data packets, which have a low priority and may be easily discarded during network congestion, OSPF may fail to receive Hello packets within the dead time, interrupting the neighbor relationship.




Example
-------

# Set the interval at which Hello packets are sent on the interface to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf timer hello 20

```