nacm enable
===========

nacm enable

Function
--------



The **nacm enable** command enables the NACM function.

The **undo nacm enable** command disables the NACM function.



By default, the NACM function is disabled.


Format
------

**nacm enable**

**undo nacm enable**


Parameters
----------

None

Views
-----

NACM view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To enable the NACM function, run the nacm enable command.

**Configuration Impact**

After the **undo nacm enable** command is run, the default authentication mode HUAWEI-NACM takes effect.

**Follow-up Procedure**

Configure NACM rules.


Example
-------

# Enable the NACM function.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm
[~HUAWEI-netconf-nacm] nacm enable

```