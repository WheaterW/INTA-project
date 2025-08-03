flow-control
============

flow-control

Function
--------



The **flow-control** command configures a flow control mode.

The **undo flow-control** command restores the default flow control mode.



By default, the flow control mode is set to none, indicating that traffic is not controlled.


Format
------

**flow-control** *flowtype*

**undo flow-control**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *flowtype* | Specifies the flow control mode. | The value is an enumerated type, which can be:   * none: Implements no flow control. * hardware: Implements hardware-based flow control. * software: Implements software-based flow control. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Flow control prevents packet loss caused by network congestion. You can run this command to control the packet rate on a console interface.

**Precautions**

* The configuration is effective only in the console interface view.
* When the configuration is delivered in the VTY user interface view, an error message is displayed, and the configuration does not take effect.


Example
-------

# In the console user interface view, configure software-based flow control.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] flow-control software

```