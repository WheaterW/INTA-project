peer description(BGP view)(group)
=================================

peer description(BGP view)(group)

Function
--------



The **peer description** command configures a description for a peer group.

The **undo peer description** command deletes the description of a peer group.



By default, no description is configured for a peer group.


Format
------

**peer** *group-name* **description** *description-text*

**undo peer** *group-name* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *description-text* | Specifies a description. | The value is a string of 1 to 255 characters. Letters, digits, and spaces are supported. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The peer description can be used to configure a description for a peer group, which facilitates management of peers or peer groups. The description records information about the peer group, such as the VPN instance to which the peer group belongs, and devices that establish peer relationships with the peer group.

**Implementation Procedure**

The description configured by using the **peer description** command for a peer is displayed from the first non-space character.

**Configuration Impact**

If the command is run multiple times to configure a description for a peer, the latest configuration overwrites the previous one.

**Follow-up Procedure**

Run the display bgp peer verbose command to view the description of a peer configured using the **peer description** command.


Example
-------

# Configure a description for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test description ISP1

```