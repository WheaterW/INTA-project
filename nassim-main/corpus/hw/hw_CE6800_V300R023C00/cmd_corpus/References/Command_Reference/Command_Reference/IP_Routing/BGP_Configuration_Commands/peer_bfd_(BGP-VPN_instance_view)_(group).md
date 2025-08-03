peer bfd (BGP-VPN instance view) (group)
========================================

peer bfd (BGP-VPN instance view) (group)

Function
--------



The **peer bfd** command sets BFD detection parameters for a peer group.

The **undo peer bfd** command restores default BFD detection parameter values.



By default, the interval at which BFD packets are sent is 1000 milliseconds, the interval at which BFD packets are received is 1000 milliseconds, the local detection time multiplier is 3.


Format
------

**peer** *group-name* **bfd** { **min-tx-interval** *min-tx-interval* | **min-rx-interval** *min-rx-interval* | **detect-multiplier** *multiplier* } \*

**undo peer** *group-name* **bfd** { **min-tx-interval** | **min-rx-interval** | **detect-multiplier** } \*

**undo peer** *group-name* **bfd** { **min-tx-interval** *min-tx-interval* | **min-rx-interval** *min-rx-interval* | **detect-multiplier** *multiplier* } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **min-tx-interval** *min-tx-interval* | Specifies the interval at which BFD packets are sent. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000 milliseconds. |
| **min-rx-interval** *min-rx-interval* | Specifies an interval at which BFD packets are received. | The value is an integer that ranges from 3 to 1000, in milliseconds. The default value is 1000 milliseconds. |
| **detect-multiplier** *multiplier* | Specifies the local detection time multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

BFD provides millisecond-level fault detection. It helps BGP to detect faults in neighboring devices or links more quickly, and instructs BGP to recalculate routes for correct packet forwarding. The peer bfd command can be used to set the values of BFD session parameters on a specified interface.The BFD configuration of a peer takes precedence over that of the peer group to which the peer belongs. If BFD is not configured on a peer and the peer group to which the peer belongs is enabled with BFD, the peer will inherit the BFD configurations of the peer group.


Example
-------

# Configure BFD and set detection parameters on its peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test external
[*HUAWEI-bgp-instance-vpn1] peer test bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 5

```