peer graceful-restart timer restart (BGP-VPN instance view) (group)
===================================================================

peer graceful-restart timer restart (BGP-VPN instance view) (group)

Function
--------



The **peer graceful-restart timer restart** command sets the maximum duration on a device for each peer in a specified group to wait for its BGP peer relationship to be reestablished with the device. After the command is run, the device will advertise the maximum duration to all the peers in the specified group.

The **undo peer graceful-restart timer restart** command deletes the configured duration.



By default, each peer in a specified group on a device waits for its BGP peer relationship to be reestablished for a maximum of 150 seconds.


Format
------

**peer** *group-name* **graceful-restart** **timer** **restart** *time-value*

**undo peer** *group-name* **graceful-restart** **timer** **restart**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *time-value* | Specifies the maximum duration on a device for each peer in a specified group to wait for its BGP peer relationship to be reestablished with the device. | The value is an integer ranging from 3 to 3600, in seconds. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If both the local end and a specified peer group support GR, you can run this command to set the maximum waiting time for the specified peer group to wait for the re-establishment of the local BGP peer relationship. After this command is run, when the specified peer group finds that the local end is Down, the BGP session enters the GR process, and the specified peer group must establish a connection with the local end within the period set by this command. Otherwise, the GR process exits and the optimal route is selected from the existing routes.

**Configuration Impact**

If this command is run, the BGP peer relationship is disconnected and re-established. Therefore, exercise caution when running this command.


Example
-------

# Set the maximum duration to 100s on a device for each peer in a specified group to wait for its BGP peer relationship to be reestablished with the device.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group a
[*HUAWEI-bgp-instance-vpn1] peer a graceful-restart timer restart 100

```