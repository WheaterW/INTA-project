group-member
============

group-member

Function
--------



The **group-member** command adds one or more interfaces to a permanent interface group.

The **undo group-member** command deletes one or more interfaces from a permanent interface group.



By default, a permanent interface group does not contain any interfaces.


Format
------

**group-member** { { *interface-name-start* | *interface-type-start* *interface-number-start* } [ **to** { *interface-name-end* | *interface-type-end* *interface-number-end* } ] } &<1-10>

**undo group-member** { { *interface-name-start* | *interface-type-start* *interface-number-start* } [ **to** { *interface-name-end* | *interface-type-end* *interface-number-end* } ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name-start* | Specifies a start interface name. | - |
| *interface-type-start* | Specifies the type of the first interface to be added to a permanent port group.   * The interface types of interface-type-start interface-number-start and interface-type-end interface-number-end must be the same. The value of interface-number-end must be greater than or equal to the value of interface-number-start. interface-number-end and interface-number-start specify a range of interfaces. * The interfaces before and after the keyword to must have the same attribute. * If to interface-type-end interface-number-end is not specified, only the interface specified by interface-type-start interface-number-start is added.   A maximum of 10 interface number ranges can be specified using to in a group-member command. | - |
| *interface-number-start* | Specifies the number of the first interface to be added to a permanent port group.   * The interface types of interface-type-start interface-number-start and interface-type-end interface-number-end must be the same. The value of interface-number-end must be greater than or equal to the value of interface-number-start. interface-number-end and interface-number-start specify a range of interfaces. * The interfaces before and after the keyword to must have the same attribute. * If to interface-type-end interface-number-end is not specified, only the interface specified by interface-type-start interface-number-start is added.   A maximum of 10 interface number ranges can be specified using to in a group-member command. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-name-end* | Specifies an end interface name. | - |
| *interface-type-end* | Specifies the last interface type to be added to a permanent port group.   * The interface types of interface-type-start interface-number-start and interface-type-end interface-number-end must be the same. The value of interface-number-end must be greater than or equal to the value of interface-number-start. interface-number-end and interface-number-start specify a range of interfaces. * The interfaces before and after the keyword to must have the same attribute. * If to interface-type-end interface-number-end is not specified, only the interface specified by interface-type-start interface-number-start is added.   A maximum of 10 interface number ranges can be specified using to in a group-member command. | - |
| *interface-number-end* | Specifies the number of the last interface to be added to a permanent port group.   * The interface types of interface-type-start interface-number-start and interface-type-end interface-number-end must be the same. The value of interface-number-end must be greater than or equal to the value of interface-number-start. interface-number-end and interface-number-start specify a range of interfaces. * The interfaces before and after the keyword to must have the same attribute. * If to interface-type-end interface-number-end is not specified, only the interface specified by interface-type-start interface-number-start is added.   A maximum of 10 interface number ranges can be specified using to in a group-member command. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After a permanent interface group is created using the **port-group** command, the permanent interface group does not contain any interfaces. To add one or more interfaces to the permanent interface group, run the **group-member** command. When you run a command in the interface group view, the system automatically applies the command to all the interfaces in the permanent interface group. Then interfaces in a permanent interface group are configured in a batch.



**Prerequisites**



A permanent interface group has been created using the **port-group** command in the system view.



**Precautions**



A permanent interface group supports the maximum of 512 member interfaces.

Similar to the **group-member** command, the **port-group group-member** command adds one or more interfaces to a temporary interface group, implementing batch interface configurations. The differences between permanent and temporary interface groups are described as follows:After a user leaves a temporary port group, member interfaces in the temporary port group are automatically deleted. To delete member interfaces from a permanent port group, run the **undo group-member** command.

Information about a permanent interface group can be viewed using the **display port-group** command, whereas information about a temporary interface group cannot.

After a permanent port group is configured, a configuration file is generated. However, no configuration file is generated after a temporary port group is configured.




Example
-------

# Create a permanent interface group named portgroup1, add interfaces 100GE 1/0/1 to 100GE 1/0/3 to the permanent interface group, and run the port link-type trunk command in the interface group view.
```
<HUAWEI> system-view
[~HUAWEI] port-group portgroup1
[*HUAWEI-port-group-portgroup1] group-member 100GE 1/0/1 to 100GE 1/0/3
[*HUAWEI-port-group-portgroup1] port link-type trunk

```