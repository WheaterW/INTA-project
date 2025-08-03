pads
====

pads

Function
--------



The **pads disable** command disables the protocol auxiliary diagnosis system (PADS).

The **undo pads disable** command enables the PADS.

The **pads switch** command enables or disables a specific function in the protocol-aided diagnosis system.

The **undo pads switch** command enables or disables a specific function in the protocol-aided diagnosis system.



By default, the protocol-assisted diagnosis system is enabled. The status of the protocol-assisted diagnosis system depends on the settings of the pads disable command.


Format
------

**pads disable**

**pads switch** *appName* **enable**

**pads switch** *appName* **disable**

**undo pads disable**

**undo pads switch** *appName* **enable**

**undo pads switch** *appName* **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *appName* | Specifies a module name. | The value is an enumerated type. You can enter a question mark (?) and select a value from the displayed value range. |
| **enable** | Enable protocol aided diagnosis system. | - |
| **disable** | Disable protocol aided diagnosis system. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The PADS helps diagnose protocol problems such as IP address conflict. To enable a function in the PADS, run the **pads switch** command. To disable the PADS, run the **pads disable** command.If the **pads switch** command is not run, the status of functions in the PADS depends on whether the PADS is enabled. If the **pads switch** command is run, the status of functions in the PADS is determined by this command, no matter whether the PADS is enabled.


Example
-------

# Disable the PADS.
```
<HUAWEI> system-view
[~HUAWEI] pads disable

```

# Enable the ARP diagnosis in the protocol-aided diagnosis system.
```
<HUAWEI> system-view
[~HUAWEI] pads switch arp-learning enable

```

# Enable the EUM diagnosis in the protocol-aided diagnosis system.
```
<HUAWEI> system-view
[~HUAWEI] pads switch eum-health enable

```