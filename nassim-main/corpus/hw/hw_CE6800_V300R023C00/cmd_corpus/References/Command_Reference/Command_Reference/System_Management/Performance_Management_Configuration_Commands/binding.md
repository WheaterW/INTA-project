binding
=======

binding

Function
--------



The **binding** command binds an instance to a performance statistics task.

The **undo binding** command unbinds an instance from a performance statistics task.



By default, no instance is bound to a performance statistics task.


Format
------

**binding instance-type** *instance-type* { *all* | *instance* { *vpn-instance-name* } &<1-8> }

**undo binding instance-type** *instance-type* { *all* | *instance* { *vpn-instance-name* } &<1-8> }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance-type** *instance-type* | Specifies the type of an instance bound to a performance statistics task. The instance type is predefined in each feature. Each instance type is defined in a feature. | You can use the instance-type parameter to view the instance types supported by the device. |
| *all* | Specifies all instances of a specific type. | This parameter is not supported by all instance types. For details, see the help information of the instance type. |
| *instance* | Specifies single instances of a specific type. | This parameter is not supported by all instance types. For details, see the help information of the instance type. |
| *vpn-instance-name* | Specifies the name of an instance bound to a performance statistics task. | The value is a string of 1 to 255 case-insensitive characters, spaces not supported. |



Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To bind an instance to a performance statistics task, run the binding command to allow the system to collect performance statistics about the instance.

**Prerequisites**

* The performance statistics function has been enabled using the **statistics enable** command.
* A performance statistics task has been configured.
* An instance that is to be bound to the performance statistics task has existed.

**Precautions**

If the bound instance is a physical interface or Eth-Trunk interface, note the following aspects:Traffic statistics on the interface are collected at the default interval (300s), meaning that the forwarding rate and bandwidth usage of the interface will not change within 300s. If the value of cycle specified in the **statistics-cycle** command is less than 300s (5 minutes), the performance statistics (the forwarding rate and bandwidth usage) about the interface remain unchanged, which cannot reflect the actual traffic on the interface.To resolve this issue, use either of the following methods:

* Run the **set flow-stat interval** command to set the interval at which traffic statistics on the interface are collected to a smaller value, ranging from 10 to 600, in seconds.
* Run the **statistics-cycle** command to increase the interval at which performance statistics about an interface are collected.


Example
-------

# Bind an interface instance with 100GE 1/0/1 statistics objects to the performance statistics task named huawei.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task huawei
[*HUAWEI-pm-statistics-huawei] binding instance-type interface instance 100GE1/0/1

```