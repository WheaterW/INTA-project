display interface status
========================

display interface status

Function
--------



The **display interface status** command displays the status of all MEth management interfaces on a device.




Format
------

**display interface** *meth* **status**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *meth* | Specifies an interface type. | MEth interface |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the status of the MEth management interface or determine which MEth management interface is working when the device has multiple MEth management interfaces, run this command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of MEth management interfaces on a device.
```
<HUAWEI> display interface meth status
---------------------------------------                                                                                             
Interface        Port status   Active                                                                                               
---------------------------------------                                                                                             
MEth5/0/0        Up            Y                                                                                                    
---------------------------------------

```

**Table 1** Description of the **display interface status** command output
| Item | Description |
| --- | --- |
| Interface | Number of a physical management interface. |
| Port status | Up/Down status of an interface. |
| Active | Activation status.   * Y: The interface is activated. * N: The interface is not activated. |