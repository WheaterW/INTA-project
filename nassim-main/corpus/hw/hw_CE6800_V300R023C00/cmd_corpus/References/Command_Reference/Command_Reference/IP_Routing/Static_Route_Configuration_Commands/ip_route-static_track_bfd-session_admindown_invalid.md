ip route-static track bfd-session admindown invalid
===================================================

ip route-static track bfd-session admindown invalid

Function
--------



The **ip route-static track bfd-session admindown invalid** command prevents a static route from being selected if the BFD session associated with it is in the AdminDown state.

The **undo ip route-static track bfd-session admindown invalid** command restores the default configuration.



By default, a static route can still be selected by the Router even though the BFD session associated with it is in the AdminDown state.


Format
------

**ip route-static track bfd-session session-name** *bfd-name* **admindown** **invalid**

**undo ip route-static track bfd-session** [ **session-name** *bfd-name* ] **admindown** **invalid**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **session-name** *bfd-name* | Specifies a BFD session associated with a static route. | The value is a string of 1 to 64 case-insensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, a static route can still be selected by Huawei devices even though the BFD session associated with it is in the AdminDown state, but not by non-Huawei devices. As a result, Huawei devices cannot interwork with non-Huawei devices.To address this problem, run the **ip route-static track bfd-session admindown invalid** command to configure the Router not to select the static route if the BFD session associated with it is in the AdminDown state.

**Prerequisites**

The BFD session has been created.

**Precautions**

The **undo ip route-static track bfd-session admindown invalid** command deletes the association between all static routes and BFD sessions in the AdminDown state.After the **undo bfd** command is run, the BFD parameters bound to the static route are deleted. As a result, the static route status may change and services may be interrupted.


Example
-------

# Prevent the static route from being selected if the BFD session associated with it is in the AdminDown state.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd bfda bind peer-ip 1.1.1.1
[*HUAWEI-bfd-session-bfda] discriminator local 20
[*HUAWEI-bfd-session-bfda] discriminator remote 10
[*HUAWEI-bfd-session-bfda] quit
[*HUAWEI] ip route-static track bfd-session session-name bfda admindown invalid

```