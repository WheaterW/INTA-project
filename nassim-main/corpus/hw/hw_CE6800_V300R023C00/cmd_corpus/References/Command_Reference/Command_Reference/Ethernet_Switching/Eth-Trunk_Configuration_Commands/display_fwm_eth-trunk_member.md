display fwm eth-trunk member
============================

display fwm eth-trunk member

Function
--------



The **display fwm eth-trunk member** command displays information about member interfaces of an Eth-Trunk interface.




Format
------

**display fwm eth-trunk member** *trunk-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the number of the interface. | The value is an integer in the range from 0 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After an Eth-Trunk interface is successfully configured, you can run the command to view the configuration of the Eth-Trunk interface, you can run this command to check information about member interfaces of an Eth-Trunk interface, including the TB, TP, weight, and forwarding status.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about member interfaces of an Eth-Trunk interface.
```
<HUAWEI> display fwm eth-trunk member 127
TRUNK_MEMBER table information:                                                                                                     
-------------------------------------------------------                                                                             
Slot 1                                                                                                                              
Trunk Member Number : 2                                                                                                             
Member List :                                                                                                                       
Tb          Tp          Weight          Forward state                                                                               
0           11          1               0                                                                                           
0           12          1               0

```

**Table 1** Description of the **display fwm eth-trunk member** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Trunk Member Number | Number of member interfaces. |
| Member List | List of member interfaces. |
| Tb | Destination board ID. |
| Tp | Destination port number. |
| Weight | Weight. |
| Forward state | Forward state. |