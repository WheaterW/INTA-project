ospf bfd
========

ospf bfd

Function
--------



The **ospf bfd** command enables bidirectional forwarding detection (BFD) on an OSPF interface, or sets parameter values for a BFD session.

The **undo ospf bfd** command disables BFD from an interface, or restores the default parameter values of a BFD session.



By default, BFD is not enabled in the OSPF interface view.


Format
------

**ospf bfd** { **min-tx-interval** *transmit-interval* | **min-rx-interval** *receive-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*

**undo ospf bfd** { **min-tx-interval** [ *transmit-interval* ] | **min-rx-interval** [ *receive-interval* ] | **detect-multiplier** [ *multiplier-value* ] | **frr-binding** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *transmit-interval* | Specifies the minimum interval at which BFD packets are sent to the remote device. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **min-rx-interval** *receive-interval* | Specifies the minimum interval for receiving BFD messages from the peer. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **detect-multiplier** *multiplier-value* | Specifies the local detect multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |
| **frr-binding** | Binds the BFD session status to OSPF IP FRR. When BFD detects a link fault on an interface, the BFD session goes Down and triggers FRR to switch traffic from the faulty link to the backup link. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A link fault or topology change on a network causes route recalculation in an area. Shortening the convergence time of routing protocols is important to improve network performance.Link faults cannot be completely avoided. Therefore, it is feasible to speed up fault detection and notify routing protocols of the faults. BFD is associated with routing protocols. Once a link fails, BFD can speed up the convergence of routing protocols.When configuring OSPF IP FRR, you can configure the frr-binding parameter so that the lower layer can rapidly respond to link changes and switch traffic to the backup link.



**Prerequisites**



BFD has been enabled on the interface.



**Implementation Procedure**



The receive-interval is negotiated by the local and peer ends by comparing the values of the local min-rx-interval and the peer min-tx-interval. If the local end fails to receive a BFD packet from the peer end within an interval of receive-interval \* multiplier-value, the local end considers the peer end Down.



**Configuration Impact**



If global BFD is not enabled, you can enable BFD on an interface, but BFD sessions cannot be set up in this case. Similarly, if only parameters of a BFD session are set but the **ospf bfd enable** command is not used, the BFD session cannot be set up.BFD configured on an interface takes precedence over BFD configured for a process. If BFD is enabled on an interface, the BFD parameters on the interface are used to establish BFD sessions.



**Precautions**

* After BFD is enabled, BFD sessions can be created only between the two ends that have set up an OSPF neighbor relationship and the relationship is in the Full state.
* The **ospf bfd enable** command and ospf bfd block command are mutually exclusive in function, and the later configuration overwrites the previous one.
* After BFD is disabled from an interface using the undo **ospf bfd enable** command, the parameters for setting up BFD sessions remain.


Example
-------

# Enable BFD on the interface and specify the minimum interval at which BFD packets are received to 40 ms and the local detection multiplier to 4.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf bfd enable
[*HUAWEI-100GE1/0/1] ospf bfd min-rx-interval 40 detect-multiplier 4

```