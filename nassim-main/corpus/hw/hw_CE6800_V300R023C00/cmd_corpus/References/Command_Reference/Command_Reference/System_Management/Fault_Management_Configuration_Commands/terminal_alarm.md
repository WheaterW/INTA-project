terminal alarm
==============

terminal alarm

Function
--------



The **terminal alarm** command enables the device to send alarms to a terminal.

The **undo terminal alarm** command disables the device from sending alarms to a terminal.



By default, the Router is enabled to send alarms to a terminal.


Format
------

**terminal alarm**

**undo terminal alarm**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The terminal alarm command is used to control whether to send alarms to a terminal.By default, the Router is enabled to send alarms to the terminal. To prevent alarms in device maintenance, run the **undo terminal alarm** command to disable the Router from sending alarms to a terminal.

**Configuration Impact**

After the **undo terminal alarm** command is run, the Router does not send alarms to a terminal.


Example
-------

# Disable the Router from sending alarms to a terminal.
```
<HUAWEI> undo terminal alarm

```

# Enable the Router to send alarms to a terminal.
```
<HUAWEI> terminal alarm

```