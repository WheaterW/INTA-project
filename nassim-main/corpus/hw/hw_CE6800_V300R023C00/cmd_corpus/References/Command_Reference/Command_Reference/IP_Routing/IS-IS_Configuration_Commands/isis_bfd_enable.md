isis bfd enable
===============

isis bfd enable

Function
--------



The **isis bfd** command configures BFD session parameters.

The **isis bfd enable** command enables BFD on an IS-IS interface to establish BFD sessions using default parameters.

The **undo isis bfd enable** command disables BFD from the IS-IS interface.



By default, the minimum interval at which BFD packets are received and the minimum interval at which BFD packets are sent are 1000 ms, and the local detection multiple is 3.

By default, BFD is not enabled.




Format
------

**isis bfd** { **min-tx-interval** *transmit-interval* | **min-rx-interval** *receive-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*

**isis bfd enable**

**undo isis bfd enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *transmit-interval* | Specifies the minimum interval at which BFD packets are sent to the peer end. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000 milliseconds. |
| **min-rx-interval** *receive-interval* | Specifies the minimum interval at which BFD packets are received from the peer end. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000 milliseconds. |
| **detect-multiplier** *multiplier-value* | Specifies a local detection multiplier. | The value is an integer that ranges from 3 to 50. |
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

BFD can provide millisecond-level fault detection. It can work with IS-IS to fast detect faults on neighboring devices and instruct IS-IS to recalculate routes for correct packet forwarding. The **isis bfd** command can be used to set BFD session parameters on a specified interface. The **isis bfd enable** command can be used to enable BFD on a specified interface and establish a BFD session with default parameter values.

**Prerequisites**



Before running the **isis bfd** command, you need to enable BFD globally and run the **isis bfd enable** command on the interface.Before running the **isis bfd enable** command, you need to enable BFD globally and enable the IS-IS process on a specified interface.



**Precautions**



The BFD priority of the interface is higher than the BFD priority of the process. If BFD of the interface is enabled, the BFD session is set up based on the BFD parameters on the interface.The set BFD session parameters take effect only when BFD is enabled on the interface.If global BFD is not enabled, you can configure BFD parameters on an interface but cannot establish a BFD session.If the **isis bfd block**, **isis bfd enable**, **isis bfd static**, and **isis bfd track session-name** commands are configured at the same time, only the last configured command takes effect.




Example
-------

# Enable BFD on 100GE1/0/1 and set the minimum interval at which BFD packets are received to 400 milliseconds and local detection multiplier to 4.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis bfd enable
[*HUAWEI-100GE1/0/1] isis bfd min-rx-interval 400 detect-multiplier 4

```

# Enable IS-IS BFD on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis bfd enable

```