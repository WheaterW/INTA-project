shell
=====

shell

Function
--------



The **shell** command enables the terminal services on the user interface.

The **undo shell** command removes the current settings.



By default, the terminal services are enabled on all the user interfaces.


Format
------

**shell**

**undo shell**


Parameters
----------

None

Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can use the **shell** command on a user interface to enable terminal services. This command enables users to enter commands through this interface to query device information and configure the device.To configure or maintain the parameters of a user interface through a channel as a network administrator, the **undo shell** command can be used to disable terminal services on the user interface. Then, other users are not allowed to log in to the device through this channel. After configuring parameters for the user interface, run the **shell** command to enable terminal services for the user interface. Otherwise, authorized users cannot log in to the device through this channel. After the **undo shell** command is configured in the VTY view, the user interface does not provide access services such as STelnet.


Example
-------

# Disable terminal services on the VTY 0 to VTY 4.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[~HUAWEI-ui-vty0-4] undo shell
Warning: ui-vty0-4 will be disabled. Do you want to continue? [Y/N]:y

```

# Enable terminal services on the console 0.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] shell

```