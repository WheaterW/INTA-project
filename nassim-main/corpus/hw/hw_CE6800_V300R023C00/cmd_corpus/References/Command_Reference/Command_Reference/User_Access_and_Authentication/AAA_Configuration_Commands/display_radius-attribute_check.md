display radius-attribute check
==============================

display radius-attribute check

Function
--------



The **display radius-attribute check** command displays the attributes to be checked in RADIUS Access-Accept packets.




Format
------

**display radius-attribute** [ **template** *template-name* ] **check**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **template** *template-name* | Displays the RADIUS attribute configuration of a specified RADIUS server template. | e RADIUS server template must already exist. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the **radius-attribute check** command is executed to configure the attributes to be checked in RADIUS Access-Accept packets, you can use the display **radius-attribute check** command to view these attributes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Check the attributes to be checked in RADIUS Access-Accept packets.
```
<HUAWEI> display radius-attribute check
Server-template-name: test1                                                     
--------------------------------------------------                              
check-attr                                                                      
--------------------------------------------------                              
Framed-Protocol                                                                 
--------------------------------------------------

```

**Table 1** Description of the **display radius-attribute check** command output
| Item | Description |
| --- | --- |
| check-attr | Attributes to be checked in RADIUS Access-Accept packets. |
| Framed-Protocol | Encapsulation protocol for services of the Frame type. |
| Server-template-name | Name of the RADIUS server template. |