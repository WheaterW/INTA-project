port-group group-member
=======================

port-group group-member

Function
--------



The **port-group group-member** command creates a temporary interface group and adds one or more interfaces to the temporary interface group. When you run a command in the interface group view, the system automatically applies the command to all the interfaces in the temporary interface group.



By default, no temporary interface group is configured.


Format
------

**port-group group-member** { { *startIfName* | *interface-type-start* *interface-number-start* } [ **to** { *interface-number-end* | *interface-type-end* *endIfNum* } ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *startIfName* | Specifies a start interface name. | - |
| *interface-type-start* *interface-number-start* **to** *interface-type-end* *endIfNum* | Specifies one or more interfaces to be added to a permanent interface group.   * interface-type-start interface-number-start indicates the first interface to be added to a permanent interface group. interface-type-end interface-number-end indicates the last interface to be added to a permanent interface group. * The interface type specified using interface-type-start interface-number-start must be the same as that specified using interface-type-end interface-number-end. The interface-number-end value must be greater than to the interface-type-start value. The interface-type-start and interface-number-end values together determine an interface number range. * The interfaces specified before and after the keyword to must have the same attribute. For example, they are both interfaces or sub-interfaces. If they are both sub-interfaces, they must belong to the same interface. * If to interface-type-end interface-number-end is not specified, only the interface specified using interface-type-start interface-number-start is added.   A maximum of 10 interface number ranges can be specified using to in a group-member command. | - |
| *interface-number-end* | Specifies an end interface name. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A switching device provides multiple interfaces, many of which have the same configuration. To simplify the configuration of interfaces, run the **port-group** command to create a permanent interface group and add interfaces to the permanent interface group. When you run a command in the interface group view, the system automatically applies the command to all the interfaces in the permanent interface group. In this manner, interfaces in a permanent interface group are configured in a batch.If some interfaces need to be temporarily configured in a batch, run the **port-group group-member** command to create a temporary interface group. After you complete the batch configuration and exit the view of the temporary interface group, the temporary interface group is automatically deleted.



**Configuration Impact**



If the **port-group group-member** command is run more than once, all configurations take effect.



**Precautions**

Each temporary interface group supports a maximum of 512 interfaces.Similar to the **group-member** command, the **port-group group-member** command adds one or more interfaces to a permanent interface group, implementing batch interface configurations. The differences between permanent and temporary interface groups are described as follows:

* After a user exits the view of a temporary interface group, the system automatically deletes the temporary interface group. A permanent interface group, however, can be deleted only using the **undo port-group** command.
* Information about a permanent interface group can be viewed using the **display port-group** command, whereas information about a temporary interface group cannot.
* After a permanent interface group is configured, a configuration file is generated. However, no configuration file is generated after a temporary interface group is configured.


Example
-------

# Add interfaces 100GE 1/0/2 and 100GE 1/0/3 to a temporary interface group and run the undo shutdown command in the view of the temporary interface group.
```
<HUAWEI> system-view
[~HUAWEI] port-group group-member 100GE 1/0/2 to 100GE 1/0/3
[*HUAWEI-port-group] undo shutdown

```