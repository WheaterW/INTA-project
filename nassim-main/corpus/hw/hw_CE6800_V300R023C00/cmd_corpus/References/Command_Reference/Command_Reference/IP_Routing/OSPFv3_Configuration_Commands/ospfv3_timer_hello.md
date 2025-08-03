ospfv3 timer hello
==================

ospfv3 timer hello

Function
--------



The **ospfv3 timer hello** command sets the interval at which Hello packets are sent on an interface.

The **undo ospfv3 timer hello** command restores the default value.



By default, for P2P and broadcast interfaces, the interval is 10 seconds, for P2MP and NBMA interfaces, the interval is 30 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 timer hello** *interval* [ **conservative** ] [ **instance** *instance-id* ]

**undo ospfv3 timer hello** [ *interval* [ **conservative** ] ] [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which the multi-area adjacency interface sends Hello packets. | The value is an integer ranging from 1 to 65535. |
| **conservative** | Indicates the conservative mode of the dead timer. If the conservative mode is configured, the value configured for the dead timer using the ospfv3 timer dead command takes effect even when the value is less than 10s. | - |
| **instance** *instance-id* | Specifies the interface instance ID. | The value is an integer that ranges from 0 to 255. The default value is <b>0</b>. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Hello packets are periodically exchanged by OSPFv3 interfaces to establish and maintain neighbor relationships. A Hello packet contains information about timers, DRs, BDRs, and known neighbors.The smaller the interval value, the faster a network topology change can be detected, and the larger the route cost. Ensure that the parameters of this interface and the adjacent routers are consistent.To speed up OSPFv3 convergence in the case of a link failure, configuring BFD For OSPFv3 is recommended. If the remote end does not support BFD for OSPFv3 or you do not want to configure BFD for OSPFv3, specify conservative when you run the ospfv3 timer hello command. If the conservative mode is configured, the value configured for the dead timer using the **ospfv3 timer dead** command takes effect even when the value is less than 10s; if the value configured for the dead timer is greater than 10s, services may be affected.

**Precautions**



OSPFv3 does not support null interfaces.If the configured interval (X) at which Hello packets are sent is less than 10 seconds, the actual interval at which Hello packets are sent is calculated using the following formula: Actual interval at which Hello packets are sent = X/2 + X %2 (X %2 indicates the modulo operation between X and 2). This prevents neighbor flapping and improves network reliability.If hello interval is set but ospfv3 timer dead is not set, the dead interval of an OSPFv3 neighbor is four times the value of hello interval. If the dead interval of an OSPFv3 neighbor is less than 10s, the neighbor relationship may be interrupted. Therefore, if the value of hello interval is less than or equal to 2, the dead interval of an OSPFv3 neighbor is greater than or equal to 10s. If the conservative mode is enabled for the dead timer, the dead interval of an OSPFv3 neighbor is still four times the value of hello interval.




Example
-------

# Set the interval at which Hello packets are sent on the interface in instance 1 to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0 instance 1
[*HUAWEI-100GE1/0/1] ospfv3 timer hello 20 instance 1

```