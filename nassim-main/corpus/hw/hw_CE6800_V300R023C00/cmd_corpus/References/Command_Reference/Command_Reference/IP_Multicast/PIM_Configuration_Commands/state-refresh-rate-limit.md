state-refresh-rate-limit
========================

state-refresh-rate-limit

Function
--------



The **state-refresh-rate-limit** command configures the time that a Router has to wait before receiving the next State-Refresh message.

The **undo state-refresh-rate-limit** restores the default setting.



By default, a Router has to wait 30s before receiving the next State-Refresh message.


Format
------

**state-refresh-rate-limit** *interval*

**undo state-refresh-rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the time that a router has to wait before receiving the next State-Refresh message. | The value is an integer ranging from 1 to 65535, in seconds. The default value is recommended. |



Views
-----

PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a PIM-DM Network, it is possible for a Router to receive State-Refresh messages from more than one Router. Some of these messages are duplicate. Upon the receipt of the first State-Refresh message, a Router with the state-refresh-rate-limit command configured immediately resets the Prune timer and starts the State-Refresh timer. The lifetime of the State-Refresh timer is equal to the time that the Router has to wait before receiving the next State-Refresh message.

* Before the State-Refresh timer expires, the Router discards the State-Refresh messages it receives.
* After the State-Refresh timer expires, the Router is allowed to receive the next State-Refresh message.

Example
-------

# In the public network instance, set the time that a Router has to wait before receiving the next State-Refresh message to 45s.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] state-refresh-rate-limit 45

```