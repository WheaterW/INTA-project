peer local-graceful-restart timer restart (BGP multi-instance view) (group)
===========================================================================

peer local-graceful-restart timer restart (BGP multi-instance view) (group)

Function
--------



The **peer local-graceful-restart timer restart** command sets the maximum duration for a device to wait for the BGP peer relationship with each peer in a specified group to be reestablished. After this command is run, the device will not advertise the maximum duration to any peer in the specified group.

The **undo peer local-graceful-restart timer restart** command deletes the configured duration.



By default, a device waits for the BGP peer relationship with each peer in a specified group to be reestablished for a maximum of 150s.


Format
------

**peer** *group-name* **local-graceful-restart** **timer** **restart** *restart-time*

**undo peer** *group-name* **local-graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *restart-time* | Specifies the maximum duration for a device to wait for the GR recovery of each peer in a specified group. | The value is an integer ranging from 3 to 3600, in seconds. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the local device supports GR but the specified peer does not support GR, you can run this command to set the maximum waiting time for the local device to wait for the re-establishment of the BGP peer relationship.After the **peer local-graceful-restart timer restart** command is run, if the local end finds that the peer group is Down, the BGP session enters the GR process. The local end must establish a connection with the peer group within the configured maximum waiting time. Otherwise, the local end selects the optimal route from the existing routes.




Example
-------

# Set the maximum duration to 250s for a device to wait for the peer relationship with each peer in a specified group to be reestablished.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance vpn1
[*HUAWEI-bgp-instance-vpn1] group aa
[*HUAWEI-bgp-instance-vpn1] peer aa local-graceful-restart timer restart 250

```