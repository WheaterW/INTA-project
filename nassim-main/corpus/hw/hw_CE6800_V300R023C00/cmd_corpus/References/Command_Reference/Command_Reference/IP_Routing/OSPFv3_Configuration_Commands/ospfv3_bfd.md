ospfv3 bfd
==========

ospfv3 bfd

Function
--------



The **ospfv3 bfd** command enables BFD on an OSPFv3 interface and sets parameter values for a BFD session.

The **undo ospfv3 bfd** command disables BFD from an interface, or restores the default parameter values of a BFD session.



By default, BFD is not enabled on an OSPFv3 interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 bfd** { **min-transmit-interval** *min-transmit-value* | **min-receive-interval** *min-receive-value* | **detect-multiplier** *detect-multiplier-value* | **frr-binding** } \* [ **instance** *instance-id* ]

**undo ospfv3 bfd** { **min-transmit-interval** [ *min-transmit-value* ] | **min-receive-interval** [ *min-receive-value* ] | **detect-multiplier** [ *detect-multiplier-value* ] | **frr-binding** } \* [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-transmit-interval** *min-transmit-value* | Specifies the minimum interval at which BFD packets are sent to the remote device. | The value is an integer that ranges from 3 to 1000, in milliseconds. |
| **min-receive-interval** *min-receive-value* | Specifies the minimum interval for receiving BFD messages from the peer. | The value is an integer that ranges from 3 to 1000, in milliseconds. |
| **detect-multiplier** *detect-multiplier-value* | Specifies the local detect multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |
| **frr-binding** | Associates the BFD session status with the link status on an interface. | - |
| **instance** *instance-id* | Indicates the ID of the instance to which the interface belongs. | The value is an integer that ranges from 0 to 255. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Either a link fault or topology change on a network will cause routes to be re-calculated within an area. As such, speeding up the convergence of a routing protocol is critical to improving the network performance.As link faults are inevitable, rapidly detecting these faults and notifying routing protocols is an effective way to quickly mitigate them. This includes associating BFD with a routing protocol to speed up convergence of the routing protocol once a link fault occurs.During the configuration of OSPFv3 IP FRR, the lower layer can fast respond to the link change so that traffic can be rapidly switched to the backup link if the primary link fails. By setting frr-binding, you can associate the BFD session status with the link status of an interface (when the BFD session goes Down, the link status of the interface becomes Down) so that link faults can be rapidly detected.



**Prerequisites**



BFD has been enabled on the interface.



**Implementation Procedure**



The receive-interval is negotiated by the local and peer ends by comparing the values of the local min-rx-interval and the peer min-tx-interval. If the local end fails to receive a BFD packet from the neighbor within an interval of receive-interval \* multiplier-value, the local end considers the neighbor Down.



**Configuration Impact**



If global BFD is not enabled, BFD can be enabled on an interface. The BFD session, however, cannot be set up after BFD is enabled on the interface. If the parameters of a BFD session are set but the **ospfv3 bfd enable** command is not run, the BFD session cannot be set up.The BFD configuration on an interface takes precedence over that in a process. If BFD is enabled on an interface, a BFD session is established according to the BFD parameters set on the interface.




Example
-------

# Enable BFD on an interface and specify the minimum receiving interval to 40 ms and local detection multiple to 4.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 bfd enable
[*HUAWEI-100GE1/0/1] ospfv3 bfd min-receive-interval 40 detect-multiplier 4

```