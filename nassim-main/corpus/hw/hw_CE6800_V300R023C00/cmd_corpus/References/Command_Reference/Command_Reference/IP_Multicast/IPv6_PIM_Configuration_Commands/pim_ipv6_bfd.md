pim ipv6 bfd
============

pim ipv6 bfd

Function
--------



The **pim ipv6 bfd** command enables BFD on an interface and configures BFD parameters.

The **undo pim ipv6 bfd** command disables BFD on an interface.



By default, BFD for IPv6 PIM is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 bfd enable**

**pim ipv6 bfd** { **min-tx-interval** *tx-value* | **min-rx-interval** *rx-value* | **detect-multiplier** *multiplier-value* } \*

**undo pim ipv6 bfd enable**

**undo pim ipv6 bfd** { **min-tx-interval** *tx-value* | **min-rx-interval** *rx-value* | **detect-multiplier** *multiplier-value* } \*

**undo pim ipv6 bfd** { **min-tx-interval** | **min-rx-interval** | **detect-multiplier** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *tx-value* | Specifies the minimum interval for sending PIM IPv6 BFD packets. | The value is an integer ranging from 3 to 1000. |
| **min-rx-interval** *rx-value* | Specifies the minimum interval for receiving PIM IPv6 BFD packets. | The value is an integer ranging from 3 to 1000. |
| **detect-multiplier** *multiplier-value* | Specifies the local detection multiplier of PIM IPv6 BFD packets.   * For a stable link, you can set the detection multiplier to a large value to avoid frequent link detection. * For an unstable link, a small detection multiplier may cause BFD session flapping. Therefore, it is recommended that you set the detection multiplier to a large value. | The value is an integer in the range 3 to 50. The default value is 3. |
| **enable** | Specifies that enables BFD for IPv6 PIM on an interface. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To minimize the impact of a fault on services and improve network availability, a network device is required to fast detect a communication fault between adjacent devices so that the upper layer protocol can rectify the fault to ensure normal services.In multicast applications, if the current Designated router (DR) or Assert winner at the shared network segment is faulty, other PIM neighbors start a new DR election or Assert election after the neighbor relationship or the Assert timer times out. Consequently, multicast data transmission is discontinued. The discontinue period, usually in seconds, is longer than the timeout period of the neighbor relationship or the Assert timer.BFD can detect the status of the link at the shared network segment within milliseconds and fast respond to the fault on the PIM neighbor. If the interface configured with BFD for IPv6 PIM does not receive any BFD packets from the current DR or Assert winner within a detection period, it considers that a fault occurs on the current DR or Assert winner. BFD fast notifies the Routing Management (RM) of the session status and the RM then notifies PIM of the session status. PIM triggers a new DR election or Assert election immediately rather than waits until the neighbor relationship or the Assert timer times out. This reduces the discontinue period of multicast data transmission and thus improves the reliability of multicast data transmission.If you need to control detection parameters of PIM IPv6 BFD packets, run the **pim ipv6 bfd** command to configure the sending interval, receiving interval, and local detection multiplier for PIM IPv6 BFD packets.min-tx-interval, min-rx-interval, and detect-multiplier parameters can be configured separately on two ends, that is, the two link ends can send or receive BFD packets at different rates. If there is no special requirement for the detection period and the link is stable, you are recommended to configure the same parameter values for the routing devices of the same performance at the shared network segment.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.BFD for IPv6 PIM depends on the BFD protocol. Therefore, you need first to enable BFD globally to validate the BFD for IPv6 PIM function.Before configuring BFD for IPv6 PIM, enable IPv6 PIM-SM in the interface view. If the **undo pim ipv6 sm** command is run, IPv6 PIM-SM is disabled and the BFD for IPv6 PIM function is removed from the interface at the same time.The **pim ipv6 bfd** command and the **pim ipv6 bfd enable** command need to be used together. To validate PIM IPv6 BFD, ensure that a BFD session has been set up and the session is in the Up state.


Example
-------

# Enable BFD for IPv6 PIM on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 sm
[*HUAWEI-100GE1/0/1] pim ipv6 bfd enable

```

# Set the minimum interval at which BFD packets are sent to 200 ms, the minimum interval at which BFD packets are received to 200 ms, and the local detection multiplier to 5 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 bfd min-tx-interval 200 min-rx-interval 200 detect-multiplier 5

```