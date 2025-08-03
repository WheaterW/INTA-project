display this
============

display this

Function
--------

The **display this** command displays the configurations of the system in the current view.



Format
------

**display this** [ **include-default** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **include-default** | Displays both the configurations that users have performed and default configurations. | - |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

* After a set of configurations are complete in a certain view, you can run the **display this** command to check whether the configurations are correct.
* Effective parameters set to their defaults are not displayed.
* When you run the **display this** command:
  + If include-default is not specified, only the configured information is displayed.
  + If include-default is specified, both user configurations and default device configurations are displayed.
* Offline configurations are marked with asterisks (\*).

**Precautions**

* In the view of a specific interface, the **display this** command displays the configurations of the interface.
* In the view of a specific protocol, this command displays the configurations associated with the protocol.
* In the sub-view of a protocol, no configuration is displayed after this command is run.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the effective parameters in the current view on the device.
```
<HUAWEI> system-view
[~HUAWEI] display this
#
sysname HUAWEI
#
return

```