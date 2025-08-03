display dfs-group heartbeat
===========================

display dfs-group heartbeat

Function
--------



The **display dfs-group heartbeat** command displays HB DFS information negotiated by M-LAG devices through the heartbeat link.




Format
------

**display dfs-group** *dfs-group-id* **heartbeat**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dfs-group** *dfs-group-id* | DFS group ID. | The value is 1. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display dfs-group heartbeat** command to view node information synchronized between the two M-LAG devices through the heartbeat link, including necessary information for DFS group master/backup negotiation (such as the DFS group priority and system MAC address).The **display dfs-group heartbeat** command displays heartbeat information of the two M-LAG devices only after the peer device's IP address (source ip peer) is specified in the DFS group view. Otherwise, only heartbeat information of the local device is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about DFS group 1.
```
<HUAWEI> display dfs-group 1 heartbeat
--------------------------------------------------------------------------------
Heart beat status     : Lost
Local:
  Dfs-Group ID        : 1
  Priority            : 100
  Udp port            : 1025
  Dual-active Address : --
  VPN-Instance        : public net
  System ID           : 00e0-fc12-3456
  Heart beat state    : --
Peer:
  Dfs-Group ID        : --
  Priority            : --
  Udp port            : --
  Dual-active Address : --
  VPN-Instance        : public net
  System ID           : --
  Heart beat state    : --
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display dfs-group heartbeat** command output
| Item | Description |
| --- | --- |
| Heart beat status | Heartbeat status:  OK: The heartbeat status is online.  Lost: The heartbeat status is offline. |
| Heart beat state | HB DFS master/backup status of the device:  Master: The device is in active state.  Backup: The device is in backup state. |
| Dfs-Group ID | ID of the DFS group. |
| Priority | Priority of the DFS group. |
| Udp port | UDP port number. |
| Dual-active Address | IP address bound to the DFS group. |
| VPN-Instance | VPN Instance. |
| System ID | System MAC address. |
| Local | Local device. |
| Peer | Peer device. |