traffic behavior
================

traffic behavior

Function
--------



The **traffic behavior** command creates a traffic behavior and displays the traffic behavior view, or directly displays the view of an existing traffic behavior.

The **undo traffic behavior** command deletes a traffic behavior.



By default, no traffic behavior is created in the system.


Format
------

**traffic behavior** *behavior-name*

**undo traffic behavior** *behavior-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *behavior-name* | Specifies the name of a traffic behavior. | The value is a string of 1 to 31 case-sensitive characters without spaces and question marks, and must start with letters or digits. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A traffic classifier is used to differentiate services and must be associated with a flow control or resource allocation action such as packet filtering and traffic statistics. The actions constitute a traffic behavior. The **traffic behavior** command creates a traffic behavior.

**Follow-up Procedure**

Configure an action in the traffic behavior view. For example, run the **statistics enable** command to configure the traffic statistics action.

**Precautions**

* To delete a traffic behavior, unbind the traffic policy containing the traffic behavior from the system, an interface, or a VLAN where the traffic policy is applied and unbind the traffic behavior from the traffic classifier. To modify only actions in a traffic behavior, you do not need to unbind the traffic policy containing the traffic behavior from the system, an interface, or a VLAN.
* On the device, a maximum of 2048 traffic behaviors can be created and multiple traffic actions can be configured in a traffic behavior.


Example
-------

# Define a traffic behavior named behavior1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior behavior1
[*HUAWEI-behavior-behavior1]

```