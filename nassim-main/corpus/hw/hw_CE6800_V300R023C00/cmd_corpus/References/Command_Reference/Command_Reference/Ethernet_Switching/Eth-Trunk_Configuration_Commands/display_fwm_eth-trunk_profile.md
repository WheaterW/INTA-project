display fwm eth-trunk profile
=============================

display fwm eth-trunk profile

Function
--------



The **display fwm eth-trunk profile** command displays the data table of an Eth-Trunk load balancing profile.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display fwm eth-trunk profile** *trunk-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk interface. | The value is an integer that ranges from 0 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After an Eth-Trunk interface is successfully configured, you can run the command to view the configuration of the Eth-Trunk interface, you can run this command to check the data table of an Eth-Trunk load balancing profile.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the data table of an Eth-Trunk load balancing profile.
```
<HUAWEI> display fwm eth-trunk profile 1
TRUNK_PROFILE table information:                                                                                                    
-------------------------------------------------------                                                                             
Slot 1                                                                                                                              
VSID              : 0                                                                                                               
Profile ID        : 1                                                                                                               
Profile name      : default                                                                                                         
L2 hash field     : 0000001c                                                                                                        
Ipv4 hash field   : 00000c6c                                                                                                        
Ipv6 hash field   : 00000c6c                                                                                                        
Mpls hash field   : 00000006

```

**Table 1** Description of the **display fwm eth-trunk profile** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| VSID | VS ID. |
| Profile ID | Load-balance profile ID. |
| Profile name | Load-balance profile name. |
| L2 hash field | Load balancing mode of Layer 2 packets. |
| Ipv4 hash field | Load balancing mode of IPv4 packets. |
| Ipv6 hash field | Load balancing mode of IPv6 packets. |
| Mpls hash field | Load balancing mode of MPLS packets. |