undo isis bfd
=============

undo isis bfd

Function
--------



The **undo isis bfd** command restores the default parameter values of the BFD session.



By default, the minimum interval at which BFD packets are received and the minimum interval at which BFD packets are sent are 10 ms, and the local detection multiple is 3.


Format
------

**undo isis bfd** { **min-tx-interval** [ *transmit-interval* ] | **min-rx-interval** [ *receive-interval* ] | **detect-multiplier** [ *multiplier-value* ] | **frr-binding** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *transmit-interval* | Specifies the minimum interval at which BFD packets are sent to the peer end. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000 ms. |
| **min-rx-interval** *receive-interval* | Specifies the minimum interval at which BFD packets are received from the peer end. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **detect-multiplier** *multiplier-value* | Specifies a local detection multiplier. | The value ranges from 3 to 50. |
| **frr-binding** | Binds the status of the BFD session to IS-IS Auto FRR. When BFD detects a link fault on the interface, the BFD session goes Down, triggering FRR on the interface. Then, traffic is switched from the faulty link to the backup link. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD can provide millisecond-level fault detection. It can work with IS-IS to fast detect faults on neighboring devices and instruct IS-IS to recalculate routes for correct packet forwarding. After setting BFD parameters, you can run this command to restore the default values of the parameters.

**Prerequisites**

BFD has been enabled globally, and the **isis bfd enable** command has been run on the interface.

**Configuration Impact**

The minimum interval at which BFD packets are received is obtained after the receive-interval value and the remote transmit-interval value are compared. If the local end does not receive any BFD packet from its neighbor within the period (minimum interval at which BFD packets are received x multiplier-value), the local end declares the neighbor Down.

**Precautions**

The priority of BFD configured on an interface is higher than that of BFD configured in a process. If BFD is enabled on an interface, BFD sessions are established with the BFD parameters set on the interface.The set BFD session parameters take effect only when BFD is enabled on the interface.


Example
-------

# Restores the default values of BFD session parameters on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] undo isis bfd min-rx-interval 400 detect-multiplier 4

```