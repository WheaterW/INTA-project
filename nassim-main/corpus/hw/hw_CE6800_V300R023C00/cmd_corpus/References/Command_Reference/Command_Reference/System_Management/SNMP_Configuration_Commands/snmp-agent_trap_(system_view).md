snmp-agent trap (system view)
=============================

snmp-agent trap (system view)

Function
--------



The **snmp-agent trap disable** command disables all traps in the system.

The **undo snmp-agent trap disable** command restores the default status of all traps.

The **snmp-agent trap enable** command enables all traps in the system.

The **undo snmp-agent trap enable** command restores the default status of all traps.



By default, the preceding command is not configured. Different trap functions of different modules have different default states. You can run the display snmp-agent trap all command to view the default states.


Format
------

**snmp-agent trap enable**

**snmp-agent trap disable**

**undo snmp-agent trap** { **enable** | **disable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | disable. | - |
| **enable** | enable. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The **snmp-agent trap enable** command must be used together with the **snmp-agent target-host inform** command or snmp-agent target-host command.To enable a device to send trap messages, run at least the **snmp-agent target-host inform** command or snmp-agent target-host command on the device to specify the destination address of the trap messages.To enable the trap function for all features, run the **snmp-agent trap enable** command. To enable the trap function for a specified feature, run the snmp-agent trap enable feature-name command.

* To disable the trap functions of all modules, run the snmp-agent trap disable command.
* To restore the trap function for all features to the default status, run the undo snmp-agent trap disable or **undo snmp-agent trap enable** command.Note: To disable the trap function for a specified feature, run the **undo snmp-agent trap enable feature-name** command.

**Precautions**

The **snmp-agent trap enable** command and the related commands are used in the following scenarios:

* To enable trap functions of all modules at a time, run the **snmp-agent trap enable** command.
* To enable trap functions of a specified module, run the snmp-agent trap enable feature-name command.
* If you want to disable the trap function of a specified module, run the **undo snmp-agent trap enable feature-name** command.
* To enable specified trap functions of a specified module, run the **snmp-agent trap enable feature-name trap-name** command.
* To disable the trap function of a specified module, run the **undo snmp-agent trap enable feature-name trap-name** command.
* To restore all default trap functions at a time, run the **undo snmp-agent trap enable** command.

Example
-------

# Disable the trap function for all features.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap disable

```

# Enable the trap function for all features.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap enable

```