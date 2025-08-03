timer wtr
=========

timer wtr

Function
--------



The **timer wtr** command sets a switchback delay for a Smart Link group.

The **undo timer wtr** command restores the default switchback delay.



The default switchback delay is 60s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**timer wtr** *wtr-time*

**undo timer wtr**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *wtr-time* | Specifies a switchback delay for a Smart Link group. | The value is an integer ranging from 0 to 1200, in seconds. |



Views
-----

Smart Link group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the primary link in a Smart Link group fails, traffic automatically switches to the secondary link. The primary link remains blocked after it recovers to ensure uninterrupted traffic forwarding. To switch traffic back to the primary link after a specified time, run the timer wtr command to configure a switchback delay. Traffic automatically switches back to the primary link after the switchback delay expires.

**Prerequisites**

The switchback function has been enabled using the **restore enable** command.

**Precautions**

If the network is unstable or does not require a short switchback delay, you can set a longer switchback delay to avoid frequent link switchovers.


Example
-------

# Set the switchback delay for Smart Link group 1 to 120s.
```
<HUAWEI> system-view
[~HUAWEI] smart-link group 1
[*HUAWEI-smlk-group1] timer wtr 120

```