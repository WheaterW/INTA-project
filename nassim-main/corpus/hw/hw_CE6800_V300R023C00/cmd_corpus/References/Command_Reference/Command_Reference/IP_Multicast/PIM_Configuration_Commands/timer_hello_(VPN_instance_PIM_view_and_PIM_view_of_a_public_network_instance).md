timer hello (VPN instance PIM view/PIM view of a public network instance)
=========================================================================

timer hello (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **timer hello** command globally sets an interval at which PIM interfaces send Hello messages.

The **undo timer hello** command restores the default value of the interval.



By default, PIM interfaces send Hello messages at an interval of 30 seconds.


Format
------

**timer hello** *interval*

**undo timer hello**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which PIM interfaces send Hello messages. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A Router on a PIM-SM network needs to send Hello messages periodically to maintain PIM neighbor relationships. To set the interval at which PIM interfaces send Hello messages, run the **timer hello** command. To have a Router rapidly sense PIM neighbor changes, set a Hello packet sending interval smaller than the configured neighbor timeout period.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the **timer hello** command is run more than once, the latest configuration overrides the previous one.The **timer hello** command can be run in the PIM view of a VPN instance to change the interval for sending Hello messages on all interfaces of the VPN instance.


Example
-------

# In the public network instance, specify 40 seconds as the interval at which PIM interfaces send Hello messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] timer hello 40

```