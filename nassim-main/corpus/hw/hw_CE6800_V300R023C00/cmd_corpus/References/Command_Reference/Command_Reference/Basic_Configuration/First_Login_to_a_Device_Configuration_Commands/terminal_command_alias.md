terminal command alias
======================

terminal command alias

Function
--------



The **terminal command alias** command enables the command alias function for the current terminal.

The **undo terminal command alias** disables the function.



By default, the function is enabled.


Format
------

**terminal command alias**

**undo terminal command alias**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The alias configured by the **alias** command can take effect only when the command alias function is enabled.If you run the **undo terminal command alias** command to disable the command alias function for the current terminal, the command alias function can still be configured, and the configuration information of command alias is not deleted, but the alias configured cannot take effect.

**Precautions**

The terminal command **alias** command takes effect only on the current terminal.The command alias function can only be used in human-to-machine mode.


Example
-------

# Enable the command alias function for the current terminal.
```
<HUAWEI> terminal command alias

```