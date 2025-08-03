display fwm eth-trunk status
============================

display fwm eth-trunk status

Function
--------



The **display fwm eth-trunk status** command displays the status of an Eth-Trunk interface.




Format
------

**display fwm eth-trunk status** *trunk-id*


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

After an Eth-Trunk interface is successfully configured, you can run the command to view the configuration of the Eth-Trunk interface, you can run this command to check the status of an Eth-Trunk interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of an Eth-Trunk interface.
```
<HUAWEI> display fwm eth-trunk status 3
TRUNK_STATUS table information:                                                                                                     
---------------------------------------                                                                                             
Slot 1                                                                                                                            
Hash type            : 0                                                                                                            
IfIndex              : 69                                                                                                           
Trunk state          : 0                                                                                                            
Eth-Trunk valid flag : 1

```

**Table 1** Description of the **display fwm eth-trunk status** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Hash type | Hash type. |
| IfIndex | Interface index. |
| Trunk state | Trunk state. |
| Eth-Trunk valid flag | Eth-Trunk valid flag. |