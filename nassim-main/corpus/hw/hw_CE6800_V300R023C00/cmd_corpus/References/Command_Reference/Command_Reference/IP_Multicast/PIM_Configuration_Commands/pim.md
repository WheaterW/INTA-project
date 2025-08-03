pim
===

pim

Function
--------



The **pim** command enables PIM and displays the PIM view of the public network instance.

The **undo pim** command clears all configurations in the PIM view, releases resources occupied by PIM, and restores the initial state.



By default, PIM is not enabled.


Format
------

**pim**

**undo pim**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

PIM parameters can be configured only after PIM is enabled, and global PIM parameters can be configured only in the PIM view of the public network instance.

**Precautions**

After the **configuration re-authentication enable** command is run, you need to enter the password and pass the authentication to validate the configuration when running the undo pim command.


Example
-------

# Enable PIM and enter the PIM view of the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim]

```