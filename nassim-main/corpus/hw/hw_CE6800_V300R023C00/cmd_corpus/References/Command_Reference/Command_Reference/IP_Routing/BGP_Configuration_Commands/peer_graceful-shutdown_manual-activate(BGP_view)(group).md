peer graceful-shutdown manual-activate(BGP view)(group)
=======================================================

peer graceful-shutdown manual-activate(BGP view)(group)

Function
--------



The **peer graceful-shutdown manual-activate** command activates the g-shut feature for a peer group.

The **undo peer graceful-shutdown manual-activate** command restores the default configuration.



By default, the g-shut feature of a peer group is not activated.


Format
------

**peer** *groupName* **graceful-shutdown** **manual-activate**

**undo peer** *groupName* **graceful-shutdown** **manual-activate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupName* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To activate the g-shut feature for a peer group, run this command.




Example
-------

# Activate the g-shut feature for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group aa
[*HUAWEI-bgp] peer aa graceful-shutdown manual-activate

```