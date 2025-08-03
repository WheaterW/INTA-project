display eth-trunk membership
============================

display eth-trunk membership

Function
--------



The **display eth-trunk membership** command displays information about member interfaces of an Eth-Trunk interface.




Format
------

**display eth-trunk membership** *trunk-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk interface. | The value is an integer ranging from 0 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



After an Eth-Trunk interface is successfully configured, you can run the command to view the configuration of the Eth-Trunk interface and its member interfaces.



**Precautions**



Before running the display trunkmembership eth-trunk command to view the configuration of Eth-Trunk interface in static LACP mode, ensure that the **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about Eth-Trunk 1 in manual load balancing mode and its member interfaces.
```
<HUAWEI> display eth-trunk membership 1
Trunk ID: 1
Used Status: Valid
Type: Ethernet
Working Mode: Normal
Number Of Ports in Trunk: 1
Number Of Up Ports in Trunk: 0
Operating Status: down

Interface 100GE1/0/1, valid, operate down, weight=1
Interface 100GE1/0/2, valid, operate down, weight=1

```

**Table 1** Description of the **display eth-trunk membership** command output
| Item | Description |
| --- | --- |
| Trunk ID | ID of the Eth-Trunk interface. |
| Used Status | Whether the Eth-Trunk interface is available:   * Valid: The Eth-Trunk interface is available. * inValid: The Eth-Trunk interface is unavailable. |
| Working Mode | Working mode of the Eth-Trunk interface:   * Normal: manual load balancing mode. * Static: static LACP mode. |
| Number Of Ports in Trunk | Number of interfaces that are added to the Eth-Trunk interface. |
| Number Of Up Ports in Trunk | Number of Up interfaces that are added to the Eth-Trunk interface. |
| Operating Status | Status of the Eth-Trunk interface:   * up. * down. |
| Type | Type of the trunk interface. |