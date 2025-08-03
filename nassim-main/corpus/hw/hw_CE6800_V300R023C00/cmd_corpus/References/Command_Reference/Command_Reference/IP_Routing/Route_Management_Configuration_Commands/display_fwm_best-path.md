display fwm best-path
=====================

display fwm best-path

Function
--------



The **display fwm best-path** command displays the currently effective optimal forwarding paths.

The **display fwm best-path switch** command displays the records of optimal forwarding path switching.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display fwm best-path slot** *slot-id* **cpu** *cpu-id* **chip** *chip-id* [ **vpn-instance** *vpnname* ] **dip** *dest-ip*

**display fwm best-path switch slot** *slot-id* **cpu** *cpu-id* **chip** *chip-id* [ **vpn-instance** *vpnname* ] **dip** *dest-ip* **history**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cpu** *cpu-id* | Specifies the CPU ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **chip** *chip-id* | Specifies a chip ID. | The value is an integer ranging from 0 to 7. |
| **vpn-instance** *vpnname* | Specifies a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **dip** *dest-ip* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| **switch** | Indicates the path switchover. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **history** | Indicates the path switchover history. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

In the load balancing scenario, after the adaptive routing function is enabled, you can run this command to query the effective optimal forwarding paths and the switching records of the optimal forwarding paths by specifying a route prefix.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the optimal path that takes effect on the current chip.
```
<HUAWEI> display fwm best-path slot 1 cpu 0 chip 0 vpn-instance mix_vrf dip 192.168.1.1
---------------------------------------------------------------------------------------------                                       
DestIp          EcmpIndex  DlbId   NhpBase  NhpBitMap  Interface            Role                                                    
---------------------------------------------------------------------------------------------                                       
192.168.1.1     4          2       414      2          100GE1/0/1           local-non-min                                           
---------------------------------------------------------------------------------------------

```

# Display the historical optimal paths.
```
<HUAWEI> display fwm best-path switch slot 1 cpu 0 chip 0 vpn-instance mix_vrf dip 192.168.1.1 history
Index: 0                                                                                                                            
------------------------------------------------------------------------------------------------------------------                  
DestIp          EcmpIndex  DlbId   NhpBase  NhpBitMap  Interface            Role            Switch-Time                             
------------------------------------------------------------------------------------------------------------------                  
192.168.1.1     4          2       414      2          100GE1/0/1           local-min       04-25 15:29:55.897                      
------------------------------------------------------------------------------------------------------------------                  
Index: 1                                                                                                                            
------------------------------------------------------------------------------------------------------------------                  
DestIp          EcmpIndex  DlbId   NhpBase  NhpBitMap  Interface            Role            Switch-Time                             
------------------------------------------------------------------------------------------------------------------                  
192.168.1.1     4          2       414      1          100GE1/0/2           local-non-min   04-25 15:28:44.637                      
------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display fwm best-path** command output
| Item | Description |
| --- | --- |
| DestIp | Destination port. |
| EcmpIndex | Load balancing index. |
| DlbId | Dynamic load balancing ID. |
| NhpBase | Index of the next-hop base address. |
| NhpBitMap | Next-hop bitmap. |
| Interface | Outbound interface. |
| Role | Role:   * global-min: indicates the shortest inter-group path. * global-non-min: indicates the inter-group non-shortest path. * local-min: indicates the shortest path in a group. * local-non-min: indicates the non-shortest path in the group. |
| Switch-Time | Switching time. |
| Index | Index. |