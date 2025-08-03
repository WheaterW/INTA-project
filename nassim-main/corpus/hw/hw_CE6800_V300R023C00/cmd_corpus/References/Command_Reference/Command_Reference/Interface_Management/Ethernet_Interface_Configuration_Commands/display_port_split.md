display port split
==================

display port split

Function
--------



The **display port split** command displays the current status of a split or merged interface.




Format
------

**display port split** [ **all** | { **slot** *slot-id* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays the current status of all the split or merged interfaces. | - |
| **slot** *slot-id* | Specifies the ID of a slot to be queried. | The value depends on the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



Interface split allows a high-bandwidth physical interface on a device to be split into multiple independent low-bandwidth interfaces. You can choose to use the original high-bandwidth interface or split the interface into multiple low-bandwidth interfaces based on the interface type provided by the peer device. The interface split function improves networking flexibility and reduces device purchase costs.After an interface is split, you can run this command to check the current status of the split interface. In a port switching scenario, for example, a 100GE port is switched to a 200GE port, split information about the source port is retained.



**Precautions**



The CE6820H, CE6820S, CE6863H and CE6881H do not support this command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the current status of a split or merged interface.
```
<HUAWEI> display port split
----------------------------------------------------------------------------------
Port                   Status       Split-port
----------------------------------------------------------------------------------
100GE1/0/1              Enable      100GE1/0/1:1          100GE1/0/1:2
                                    100GE1/0/1:3          100GE1/0/1:4
100GE1/0/2              Disable
100GE1/0/3              Disable
100GE1/0/4              Disable
----------------------------------------------------------------------------------

```

**Table 1** Description of the **display port split** command output
| Item | Description |
| --- | --- |
| Port | Port that can be split or merged. |
| Status | Current status of a split or merged interface:   * Enable: Interface split is enabled. * Disable: Interface split is disabled. |
| Split-port | Interfaces that have been split. |