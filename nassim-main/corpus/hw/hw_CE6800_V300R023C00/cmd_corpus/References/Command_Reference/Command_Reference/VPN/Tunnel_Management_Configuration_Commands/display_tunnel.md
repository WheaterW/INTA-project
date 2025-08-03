display tunnel
==============

display tunnel

Function
--------



The **display tunnel** command displays information about tunnels.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display tunnel all**

**display tunnel** *tunnel-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tunnel-id* | Displays information about a tunnel with the specified ID. | The value is a string of 1 to 20 characters.  The value consists of three parts: 4-byte VPN index, 1-byte tunnel type, and 4-byte tunnel ID, for example, 0x000000000300000001.  If the specified tunnel ID does not exist, no information is displayed. |
| **all** | Displays information about all tunnels. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about the tunnels that are already set up, including the tunnel IDs, tunnel types, and destination IP addresses, run the **display tunnel all** command.To view detailed information about a specific tunnel, run the display tunnel tunnel-id command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all tunnels.
```
<HUAWEI> display tunnel all
Tunnel ID            Type                Destination                             Status
----------------------------------------------------------------------------------------
0x00000000050000004e gre                 2.2.2.2                                 DOWN

```

# Display information about a tunnel.
```
<HUAWEI> display tunnel 00000000050000004e
Tunnel ID:       0x00000000050000004e            
Type:            gre                 
Name:            Tunnel1                         
Destination:     2.2.2.2                                 
Instance ID:     0               
Cost:            0               
Status:          DOWN            
Out Interface:   Tunnel1                                                                 
  NextHop:       0.0.0.0

```

**Table 1** Description of the **display tunnel** command output
| Item | Description |
| --- | --- |
| Tunnel ID | Tunnel ID. Tunnel IDs identify tunnels with the same instance ID and same tunnel type. |
| Instance ID | ID of the VPN instance (0 indicates that the tunnel is a public network tunnel). |
| Type | Tunnel type. The options are as follows:   * gre. * ds-lite.   The command output varies according to the tunnel type.  The supported tunnel types depend on the actual situation. |
| Destination | Destination IP address of the tunnel. |
| Status | Tunnel status. |
| Out Interface | Outbound interface. |
| Name | Tunnel name. |
| Cost | Tunnel cost. |
| NextHop | Next hop address. |