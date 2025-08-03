register-source
===============

register-source

Function
--------



The **register-source** command specifies an interface using which the source's designated router (DR) sends Register messages.

The **undo register-source** command restores the default setting.



By default, no interface is specified for the source's DR to send Register messages.


Format
------

**register-source** { *interface-type* *interface-number* | *interface-name* }

**undo register-source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface using which the source's DR sends Register messages. | - |
| *interface-number* | Specifies the number of an interface using which the source's DR sends Register messages. | - |
| *interface-name* | Specifies the name of an interface. | - |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the source's DR uses more than one or a filtered out interface to send Register messages to the rendezvous point (RP), errors occur in the registration process and extra traffic occupies bandwidth on the network. To address this issue, run the **register-source** command to specify an interface (a loopback interface is recommended) using which the source's DR sends Register messages.

**Prerequisites**

PIM-SM has been enabled on the interface to be specified by the port-type port-number parameter.

**Configuration Impact**

If the **register-source** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The command configuration is effective only when the specified interface is in the Up state.


Example
-------

# In the public network instance view, specify loopback interface 0 as the interface using which the source's DR sends Register messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] quit
[*HUAWEI] pim
[*HUAWEI-pim] register-source loopback 0

```