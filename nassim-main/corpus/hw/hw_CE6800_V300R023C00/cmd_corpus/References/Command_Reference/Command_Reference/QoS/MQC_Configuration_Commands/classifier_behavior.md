classifier behavior
===================

classifier behavior

Function
--------



The **classifier behavior** command binds a traffic behavior to a traffic classifier in a traffic policy.

The **undo classifier behavior** command unbinds a traffic behavior from a traffic classifier in a traffic policy.



By default, no traffic classifier or traffic behavior is bound to a traffic policy.


Format
------

**classifier** *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ]

**undo classifier** *classifier-name* [ **behavior** *behavior-name* [ **precedence** *precedence-value* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *classifier-name* | Specifies the name of a traffic classifier. | The value is a string of 1 to 31 case-sensitive characters, starting with a letter or digit. It cannot contain spaces or question marks (?). |
| *behavior-name* | Specifies the name of a traffic behavior. | The value is a string of 1 to 31 case-sensitive characters, starting with a letter or digit. It cannot contain spaces or question marks (?). |
| **precedence** *precedence-value* | Specifies the priority of a traffic classifier. | The value is an integer ranging from 0 to 65535. |



Views
-----

Traffic policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To take an action for packets of a certain type, use a traffic classifier to group the packets into one class and use a traffic behavior to define an action. Then associate the traffic classifier with the traffic behavior and bind them to a traffic policy.

**Prerequisites**

* A traffic classifier has been created using the **traffic classifier** command.
* A traffic behavior has been created using the **traffic behavior** command.
* A traffic policy has been created using the **traffic policy** command.

**Precautions**

* After a traffic policy in which a traffic classifier and a traffic behavior are bound is applied, you can change the binding relationship between the traffic classifier and the traffic behavior in the traffic policy view.
* Different traffic policies can use the same traffic behavior.
* In a traffic policy, a traffic classifier can be bound to only one traffic behavior.
* The binding between traffic classifiers and traffic behaviors with the same priority cannot be delivered.


Example
-------

# In the traffic policy p1, bind traffic classifier c1 to traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] quit
[*HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] quit
[*HUAWEI] traffic policy p1
[*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1

```