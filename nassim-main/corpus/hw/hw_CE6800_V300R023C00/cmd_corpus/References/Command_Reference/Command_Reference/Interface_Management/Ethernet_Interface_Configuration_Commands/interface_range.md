interface range
===============

interface range

Function
--------



The **interface range** command creates a temporary interface group and adds specified interfaces to this temporary interface group. Commands configured for a temporary interface group then automatically run on all member interfaces.



By default, no temporary interface group is created.


Format
------

**interface range** { { *interface-name-start* | *interface-type-start* *interface-number-start* } [ **to** { *interface-name-end* | *interface-type-end* *interface-number-end* } ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type-start* | Specifies the type of a start interface. | - |
| *interface-number-start* | Specifies the number of a start interface. | - |
| **to** *interface-name-start* | Specifies a start interface name. | - |
| *interface-name-end* | Specifies an end interface name. | - |
| *interface-type-end* | Specifies the type of an end interface. | - |
| *interface-number-end* | Specifies the number of an end interface. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Typically, the device has a large number of ports and has the same configuration under many ports. At this point, configuring these interfaces on a case-by-case basis can be cumbersome and prone to input errors. Therefore, the interface that will need to execute the same configuration command, defined as a port group, will automatically execute these command lines under all member interfaces bound by the port group when the port group is configured.



**Configuration Impact**



If all member interfaces leave a temporary interface group, the system automatically deletes the temporary interface group.If the **interface range** command is run more than once, all configurations take effect.



**Precautions**

* Each temporary interface group supports a maximum of 48 member interfaces.
* This command has the same function as the **group-member** command run in the interface group view. You can also run the **group-member** command to add interfaces to a permanent interface group to implement batch interface configuration.
* When you input the keyword to in the port-group **group-member** command, note that:
* The interfaces specified by interface-type1 interface-number1 and interface-type2 interface-number2 must reside on the same interface board. To add several interfaces on another interface board to the same interface group, run this command several times or input to several times.
* The interfaces specified by interface-type1 interface-number1 and interface-type2 interface-number2 must be of the same type.
* The interfaces specified by interface-type1 interface-number1 and interface-type2 interface-number2 must be the same type of interface. For example, both are main interfaces or sub-interfaces. If sub-interfaces are specified, the sub-interfaces must be on the same main interface.If to is not input, the preceding limitations do not exist.
* The interface range and port-group **group-member** commands have the same functions. Therefore, use either of the commands.


Example
-------

# Add 100GE 1/0/1 and 100GE 1/0/2 to a temporary interface group and run the undo shutdown command in the interface group view.
```
<HUAWEI> system-view
[~HUAWEI] interface range 100GE 1/0/1 to 100GE 1/0/2
[*HUAWEI-port-group] undo shutdown

```