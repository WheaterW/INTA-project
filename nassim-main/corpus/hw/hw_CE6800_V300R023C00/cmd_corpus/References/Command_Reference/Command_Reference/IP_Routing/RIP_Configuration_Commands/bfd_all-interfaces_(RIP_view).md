bfd all-interfaces (RIP view)
=============================

bfd all-interfaces (RIP view)

Function
--------



The **bfd all-interfaces** command sets the parameter values of a BFD session.

The **undo bfd all-interfaces** command restores the default parameter values of a BFD session.



By default, BFD sessions use default parameter values.


Format
------

**bfd all-interfaces** { **min-tx-interval** *min-transmit-value* | **min-rx-interval** *min-receive-value* | **detect-multiplier** *detect-multiplier-value* } \*

**undo bfd all-interfaces** { **min-tx-interval** [ *min-transmit-value* ] | **min-rx-interval** [ *min-receive-value* ] | **detect-multiplier** [ *detect-multiplier-value* ] } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *min-transmit-value* | Specifies the minimum interval at which BFD packets are sent to the remote device. | The value is an integer ranging from 3 to 1000. The default value is 10. |
| **min-rx-interval** *min-receive-value* | Specifies the minimum interval for receiving BFD messages from the peer. | The value is an integer ranging from 3 to 1000. The default value is 10. |
| **detect-multiplier** *detect-multiplier-value* | Specifies the local detect multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After BFD for RIP is enabled, the default BFD parameters take effect. The minimum interval at which BFD packets are received and sent are 100 ms, and the detection multiplier is 3.If the default parameters cannot meet network requirements, run the**bfd all-interfaces** command to modify the parameters to change the route convergence speed. If the local end does not receive any BFD packet from its neighbor within the detection period, the local end considers this neighbor Down. The relationships between the parameters and actual intervals or the detection period are as follows:

* Actual interval at which BFD packets are sent on the local end = Max { local min-tx-interval, remote min-rx-interval}
* Actual interval at which BFD packets are received on the local end = Max { remote min-tx-interval, local min-rx-interval}
* Actual detection period = Actual interval at which BFD packets are received on the local end x Remote

**Prerequisites**

Before running this command, ensure the following operations have been performed:

* Global BFD has been enabled using the **bfd** command.
* A RIP process has been created and the RIP view has been displayed using the **rip** command.
* BFD has been enabled on interfaces using the **bfd all-interfaces enable** command.

**Precautions**

Parameters set using the **rip bfd** command in the interface view takes precedence over those set using the **bfd all-interfaces** command.


Example
-------

# Configure BFD for a RIP process and specify the minimum interval at which BFD packets are sent to 100 ms.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] rip
[*HUAWEI-rip-1] bfd all-interfaces enable
[*HUAWEI-rip-1] bfd all-interfaces min-tx-interval 100

```