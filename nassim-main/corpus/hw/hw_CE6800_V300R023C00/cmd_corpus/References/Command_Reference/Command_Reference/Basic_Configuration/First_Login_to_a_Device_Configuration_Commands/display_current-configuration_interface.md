display current-configuration interface
=======================================

display current-configuration interface

Function
--------



The **display current-configuration interface** command displays the set parameters that take effect on the device.




Format
------

**display current-configuration interface** [ *interface-type* [ *interface-number* ] | *interface-name* ] [ **include-default** ]

**display current-configuration controller** [ *interface-type* [ *interface-number* ] | *interface-name* ] [ **include-default** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **include-default** | Displays both the configurations that users have performed and default configurations. | - |
| **interface** [ *interface-type* [ *interface-number* ] | *interface-name* ] | Displays the specified interface type, number, and name. | - |
| **controller** | Displays the configuration information about a controller interface. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* After a set of configurations are complete, you can run the **display current-configuration** command to check the parameters that take effect. The parameters that do not take effect are not displayed.
* If include-default is not specified, the **display current-configuration** command displays only configurations that users have performed.
* If include-default is specified, the **display current-configuration** command displays both default configurations and configurations that users have performed.A tilde symbol (~) is added before the default device command in the displayed information to help you distinguish between user configurations and default device configurations.

**Precautions**

The following configurations are not displayed in the command output.

* Configurations that are the same as default ones
* Configurations that have not been committed


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration parameters that take effect on a specified interface.
```
<HUAWEI> display current-configuration interface Eth-Trunk 0
#
interface Eth-Trunk0
 shutdown
#
return

```