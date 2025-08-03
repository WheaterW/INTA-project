dldp delaydown-timer
====================

dldp delaydown-timer

Function
--------



The **dldp delaydown-timer** command sets the delay time for the DelayDown timer.

The **undo dldp delaydown-timer** command restores the default setting.



The default delay time for the DelayDown timer is 1 second.


Format
------

**dldp delaydown-timer** *time*

**undo dldp delaydown-timer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time* | Specifies the delay time for the DelayDown timer. | The value is an integer ranging from 1 to 5 seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

DLDP in Active, Advertisement, or Probe state may detect a port-Down event. If a TX end of the local port to which a fiber is inserted goes faulty, optical signals on the RX end of the peer port jitter. The peer port status alternates between Up and Down. If a delay time is set, DLDP does not immediately enter Inactive state and remove the peer entry. Instead, it goes to DelayDown state and starts the DelayDown timer. Ports in this state retain DLDP peer information and respond to port-Up events. Running the dldp delaydown-timer command sets the delay time for the DelayDown timer. The delay time determines port status:

* If the port in DelayDown state does not detect a port-Up event after the delay time expires, the port removes the DLDP peer entry and enters Inactive state.
* If the port detects a port-Up event before the delay time expires, it resumes its original DLDP state.

**Prerequisites**

DLDP has been enabled globally using the **dldp enable** command.

**Configuration Impact**

After the dldp delaydown-timer command is run, DLDP status is not affected if the port in DelayDown state alternates between Up and Down within the delay time of the DelayDown timer.


Example
-------

# Set the delay time for the DelayDown timer to 2 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dldp delaydown-timer 2

```