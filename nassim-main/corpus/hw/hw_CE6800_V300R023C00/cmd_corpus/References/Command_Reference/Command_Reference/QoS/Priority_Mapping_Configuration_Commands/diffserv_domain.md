diffserv domain
===============

diffserv domain

Function
--------



The **diffserv domain** command creates a DiffServ domain and displays the DiffServ domain view, or displays an existing DiffServ domain view.

The **undo diffserv domain** command deletes a specified DiffServ domain.



By default, the system defines a DiffServ mode named default.


Format
------

**diffserv domain** *ds-domain-name*

**undo diffserv domain** *ds-domain-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ds-domain-name* | Specifies the name of a DiffServ domain. | The value is a string of 1 to 31 case-sensitive characters without spaces or question marks (?). It cannot be n, no, non, none, b, br, bri, brie, or brief. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A DiffServ domain defines the mapping between the packet priority and PHB/colors packets for managing and avoiding congestion. You can run the **display diffserv domain** command to view the mappings and packet colors defined in the DiffServ domain.A DiffServ domain defines the mapping between the PHBs/colors and packet priorities (802.1p and DSCP). When binding a DiffServ domain to an interface, you can run the **trust** command to configure 802.1p or DSCP priority mapping on the interface.



**Precautions**

The DiffServ domain default exists on a device by default. In addition to the DiffServ domain default, a maximum of seven DiffServ domains can be created on a device. You can only change the mapping in the DiffServ domain default, but cannot delete the domain.


Example
-------

# Create DiffServ domain d1 and display the corresponding DiffServ domain view.
```
<HUAWEI> system-view
[~HUAWEI] diffserv domain d1
[*HUAWEI-dsdomain-d1]

```