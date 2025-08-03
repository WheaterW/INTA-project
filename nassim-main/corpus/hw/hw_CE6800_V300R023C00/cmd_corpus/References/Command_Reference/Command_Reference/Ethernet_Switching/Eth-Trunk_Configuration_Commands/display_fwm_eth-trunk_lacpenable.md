display fwm eth-trunk lacpenable
================================

display fwm eth-trunk lacpenable

Function
--------



The **display fwm eth-trunk lacpenable** command displays the LACP enablement data table.




Format
------

**display fwm eth-trunk lacpenable** *trunk-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk interface. | The value is an integer in the range from 0 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After an Eth-Trunk interface is successfully configured, you can run the command to view the configuration of the Eth-Trunk interface, you can run this command to check the LACP enablement data table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the LACP enablement data table.
```
<HUAWEI> display fwm eth-trunk lacpenable 3
Slot              : 1
Port number       : 0
---------------------------------------
    TB              TP
---------------------------------------
    4               10              
    4               11           
    4               12           
    4               13          
    4               14        
    4               15

```

**Table 1** Description of the **display fwm eth-trunk lacpenable** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Port number | Number of interfaces on which LACP is enabled. |
| TB | Index of a target board. |
| TP | Index of a target port. |