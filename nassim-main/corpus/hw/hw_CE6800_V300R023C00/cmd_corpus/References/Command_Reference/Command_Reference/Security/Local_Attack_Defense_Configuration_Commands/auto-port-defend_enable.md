auto-port-defend enable
=======================

auto-port-defend enable

Function
--------



The **auto-port-defend enable** command enables the port attack defense function.

The **undo auto-port-defend enable** command disables the port attack defense function.



By default, the port attack defense function is enabled.


Format
------

**auto-port-defend enable**

**undo auto-port-defend enable**


Parameters
----------

None

Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an attacker initiates a DoS attack on a port, the malicious attack packets sent from this port to the CPU occupy bandwidth. As a result, the CPU cannot process the protocol packets sent from other ports, and services are interrupted.The port attack defense function effectively limits the number of packets sent to the CPU, and prevents DoS attacks aiming at the CPU.This function is enabled by default. You can enable port-based automatic local attack defense to resolve the problem. When the number of protocol packets received by a port exceeds the threshold for port attack defense or the sum of the top two quantities of protocol packets received on two ports exceeds the threshold for port attack defense, the protocol packets received by the ports are sent to a queue with a smaller CAR value. This prevents impacts on the sending of protocol packets on other normal ports.

**Precautions**



After the port attack defense function is enabled in an attack defense policy, the attack defense policy must be applied in the system view.On each switch, port-based automatic local attack defense takes effect only on a maximum of two ports.




Example
-------

# Enable the port attack defense function in the attack defense policy test view.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-port-defend enable

```