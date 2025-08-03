snmp-agent trap enable feature-name
===================================

snmp-agent trap enable feature-name

Function
--------



The **snmp-agent trap enable feature-name** command enables the device to send a specified trap about a specified feature to the NMS.

The **undo snmp-agent trap enable feature-name** command restores the default trap function.

The **clear configuration snmp-agent trap enable feature-name** command deletes all the trap function configurations of a feature in a one-click manner.



To view the default trap configuration, run the display snmp-agent trap all command.


Format
------

**snmp-agent trap enable feature-name** *feature-name* [ **trap-name** *trap-name* ]

**clear configuration snmp-agent trap enable feature-name** *feature-name*

**undo snmp-agent trap enable feature-name** *feature-name* [ **trap-name** *trap-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **feature-name** *feature-name* | Specifies the name of a feature that generates traps. | The value is a string of 1 to 255 characters, which are case-insensitive and cannot be blank spaces. |
| **trap-name** *trap-name* | Specifies the name of a trap. | The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If trap-name trap-name is not specified in the **snmp-agent trap enable feature-name** command, the device sends all traps about a specified feature to the NMS.The NMS can receive alarms only after you run the snmp-agent target-host inform or **snmp-agent target-host** command to configure a target host to receive SNMP trap messages.To delete the trap function configurations of a feature when enabling or disabling the trap function using the **snmp-agent trap enable feature-name** command, run the **clear configuration snmp-agent trap enable feature-name** command.

**Configuration Impact**

* When enabling or disabling the global trap function, running the **clear configuration snmp-agent trap enable feature-name feature-name** command deletes the trap function configurations of a feature specified by feature-name and restores the trap function state to be the same as that of the global trap function.
* If the global trap function is in the default state, running the **clear configuration snmp-agent trap enable feature-name feature-name** command deletes the trap function configurations of the feature specified by feature-name and restores the trap function state to the default.


Example
-------

# Enable the device to send the coldstart trap about SNMP to the NMS.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap enable feature-name snmp trap-name coldstart

```

# Delete all the trap function configurations of the FM feature in a one-click manner.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent
[*HUAWEI] clear configuration snmp-agent trap enable feature-name fm

```