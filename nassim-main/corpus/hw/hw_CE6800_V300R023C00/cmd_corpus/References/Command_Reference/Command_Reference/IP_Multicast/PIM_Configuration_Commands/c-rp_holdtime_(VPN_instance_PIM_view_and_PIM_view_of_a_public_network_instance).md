c-rp holdtime (VPN instance PIM view/PIM view of a public network instance)
===========================================================================

c-rp holdtime (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **c-rp holdtime** command sets a timeout period during which the bootstrap router (BSR) waits to receive Advertisement messages from candidate-rendezvous points (C-RPs).

The **undo c-rp holdtime** command restores the default setting.



By default, a timeout period during which the BSR waits to receive Advertisement messages from C-RPs is 150 seconds.


Format
------

**c-rp holdtime** *interval*

**undo c-rp holdtime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a timeout period during which the BSR waits to receive Advertisement messages from C-RPs. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the c-rp holdtime command is run for a C-RP, the C-RP encapsulates interval in an Advertisement message and sends it to the BSR. The BSR obtains this interval from the message and starts the timer. If the BSR does not receive the Advertisement message from the C-RP after the timeout period expires, the BSR regards the C-RP invalid or unreachable.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the c-rp holdtime command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 100 seconds as the timeout period during which the BSR waits to receive Advertisement messages from C-RPs.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] c-rp holdtime 100

```