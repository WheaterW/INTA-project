rip bfd
=======

rip bfd

Function
--------



The **rip bfd** command sets BFD session parameters on the specified interface.

The **undo rip bfd** command restores default BFD session parameters.

The **rip bfd enable** command enables BFD on the specified interface to establish a BFD session with default parameters.

The **undo rip bfd enable** command disables BFD on the specified interface.



By default, BFD session parameters use the default values.

By default, BFD is disabled on a RIP interface.




Format
------

**rip bfd enable**

**rip bfd** { **min-tx-interval** *min-transmit-value* | **min-rx-interval** *min-receive-value* | **detect-multiplier** *detect-multiplier-value* } \*

**undo rip bfd enable**

**undo rip bfd** { **min-tx-interval** [ *min-transmit-value* ] | **min-rx-interval** [ *min-receive-value* ] | **detect-multiplier** [ *detect-multiplier-value* ] } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *min-transmit-value* | Specifies the minimum interval at which BFD packets are sent to the remote device. | The value is an integer ranging from 3 to 1000. The default value is 10. |
| **min-rx-interval** *min-receive-value* | Specifies the minimum interval for receiving BFD messages from the peer. | The value is an integer ranging from 3 to 1000. The default value is 10. |
| **detect-multiplier** *detect-multiplier-value* | Specifies the local detect multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure BFD for RIP, enable BFD globally first and then on RIP-capable interfaces. You can perform either of the following operations to enable BFD on interfaces:

* Run the **bfd all-interfaces enable** command to enable BFD on all RIP-capable interfaces in a process.
* Run the **rip bfd enable** command to enable BFD on specified RIP-capable interfaces.After BFD for RIP is enabled, the default BFD parameters take effect. The minimum interval at which BFD packets are received and sent are 100 ms, and the detection multiplier is 3.If the default parameters cannot meet network requirements, run the **rip bfd** command to modify the parameters to change the route convergence speed. If the local end does not receive any BFD packet from its neighbor within the detection period, the local end considers this neighbor Down. The relationships between the parameters and actual intervals or the detection period are as follows:
* Actual interval at which BFD packets are sent on the local end = Max { local Txvalue, remote Rxvalue}
* Actual interval at which BFD packets are received on the local end = Max { remote Txvalue, local Rxvalue}
* Actual detection period = Actual interval at which BFD packets are received on the local end x Remote mul-value

**Prerequisites**

Before running this command, ensure the following operations have been performed:

* Global BFD has been enabled using the **bfd** command.
* BFD has been enabled using the rip bfd enable or **bfd all-interfaces enable** command.

**Precautions**

The BFD session parameters configured using the **rip bfd** command in the interface view take precedence over those configured using the **bfd all-interfaces** command. If both commands are run, the BFD session parameters configured using the **rip bfd** command are used to establish a BFD session.If the rip bfd block, rip bfd enable, rip bfd static, and rip bfd static binding commands are run more than once, the latest configuration overrides the previous one.


Example
-------

# Enable BFD on 100GE 1/0/1 and set the minimum interval at which BFD packets are sent to 600 ms and local detection multiplier to 4.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip bfd enable
[*HUAWEI-100GE1/0/1] rip bfd min-tx-interval 600 detect-multiplier 4

```

# Enable BFD on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip bfd enable

```