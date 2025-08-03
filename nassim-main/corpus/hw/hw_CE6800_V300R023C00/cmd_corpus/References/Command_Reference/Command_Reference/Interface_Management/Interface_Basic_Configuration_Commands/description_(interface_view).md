description (interface view)
============================

description (interface view)

Function
--------



The **description** command configures the description of an interface.

The **undo description** command deletes the description of an interface.



By default, the description of an interface is empty.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies the description of an interface. | The value is a string of 1 to 242 case-sensitive characters, with spaces supported. |



Views
-----

200GE interface view,all-interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To help simplify interface management, run the **description** command on an interface to identify the interface and describe the function of the interface.



**Implementation Procedure**



Run the **description** command to configure the description of an interface. Note that the description is displayed from the first non-space character, and a maximum of 242 characters can be displayed.



**Configuration Impact**



After the **description** command is run in the port group view, the command takes effect on its member interfaces. In the port group view, the configuration of this command does not exist in the configuration file.



**Follow-up Procedure**



After running the **description** command to configure the description of an interface, run the display interface **description** command to view the description.



**Precautions**



It is recommended that the descriptions of all activated interfaces be standardized based on customers.




Example
-------

# Set the description of a specified interface to "Connect to DeviceA 100GE 1/0/1 interface."
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] description Connect to DeviceA 100GE 1/0/1 interface

```