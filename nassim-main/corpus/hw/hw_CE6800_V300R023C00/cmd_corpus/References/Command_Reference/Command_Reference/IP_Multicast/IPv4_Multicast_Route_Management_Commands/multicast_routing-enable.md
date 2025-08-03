multicast routing-enable
========================

multicast routing-enable

Function
--------



The **multicast routing-enable** command enables the multicast function.

The **undo multicast routing-enable** command restores the default configuration.



By default, the multicast function is disabled. When the multicast function is not enabled, the Router cannot forward multicast packets.


Format
------

**multicast routing-enable**

**undo multicast routing-enable**


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

The multicast function should be enabled in public network instance before you configure all the multicast commands.

**Precautions**

After the **undo multicast routing-enable** command is run, all multicast configurations in the public network instance are deleted and the multicast services running in the instance are interrupted. To restore the multicast services in the instance, you have to re-run the deleted multicast commands.After the **configuration re-authentication enable** command is run, the **undo multicast routing-enable** command takes effect only after the user enters the correct password and is authenticated.


Example
-------

# Enable the multicast function in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable

```