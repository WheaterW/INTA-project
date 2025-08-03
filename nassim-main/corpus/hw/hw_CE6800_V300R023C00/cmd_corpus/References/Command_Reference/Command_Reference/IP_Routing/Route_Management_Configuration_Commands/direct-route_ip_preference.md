direct-route ip preference
==========================

direct-route ip preference

Function
--------



The **direct-route ip preference** command configures a preference for routes to the directly connected network segment on an interface.

The **undo direct-route ip preference** command restores the default preference of routes to the directly connected network segment on an interface.



By default, the preference of routes to the directly connected network segment on an interface is 0.


Format
------

**direct-route ip preference** *preference-value*

**undo direct-route ip preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *preference-value* | Sets a priority for direct subnet routes on an interface. | The value is an integer ranging from 0 to 255. |



Views
-----

VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure a priority for direct subnet routes on an interface, run the **direct-route ip preference** command. After the command is run and the interface is Up, the priority of direct subnet routes on the interface is changed to the configured preferenceValue.

**Precautions**

After the command is run on an interface, the newly configured priority takes effect on all direct subnet routes on the interface, whereas the priority of direct host routes remains unchanged.


Example
-------

# Set the priority of the route to the directly connected network segment on VBDIF10 to 10.
```
<HUAWEI> system-view
[~HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] direct-route ip preference 10

```

# Set the priority of direct subnet routes on the VLANIF interface to 10.
```
<HUAWEI> system-view
[~HUAWEI] vlan 200
[*HUAWEI-vlan200] quit
[*HUAWEI] interface vlanif 200
[*HUAWEI-Vlanif200] direct-route ip preference 10

```