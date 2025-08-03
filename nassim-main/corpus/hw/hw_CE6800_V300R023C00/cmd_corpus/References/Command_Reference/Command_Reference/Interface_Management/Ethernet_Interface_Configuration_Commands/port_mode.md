port mode
=========

port mode

Function
--------



The **port mode** command configures an interface to work at another rate.

The **undo port mode** command restores the default rate of an interface.



By default:

* If a 40GE 1-to-4 medium is installed on a 25GE interface split from a 100GE interface, the 25GE interface automatically works at the rate of 10 Gbit/s. If a 100GE 1-to-4 medium with variable rate is installed on a 25GE interface split from a 100GE interface, the 25GE interface works at the rate of 25 Gbit/s.
* If a 10GE medium is installed on a native 25GE interface, the interface automatically works at the rate of 10 Gbit/s. If a 25GE medium with variable rate is installed on a native 25GE interface, the interface works at the rate of 25 Gbit/s. If a GE medium is installed on a native 25GE interface, the interface enters the Error-Down state.


Format
------

**port mode 10G**

**port mode GE**

**undo port mode** [ **10G** ]

**undo port mode** [ **GE** ]


Parameters
----------

None

Views
-----

25GE-L2 view,25GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A 100GE interface can be split into four 25GE interfaces. When a 40GE 1-to-4 medium (for example, a 1-to-4 high-speed cable) is installed on the interface, the interface automatically works at the rate of four 10 Gbit/s. If a 100G 1-to-4 medium with variable rate is installed on a converted interface, run the **port mode 10G** command in the view of the converted interface to configure the converted interface to work at the rate of 10 Gbit/s.A 25GE interface can work at the rate of 25 Gbit/s, 10 Gbit/s, or 1 Gbit/s.

* When a 25GE medium whose rate cannot be changed is installed, the rate is 25 Gbit/s.
* If a 25GE medium with variable rate is installed on an interface, you can run the **port mode 10G** command to configure the interface to work at the rate of 10 Gbit/s.
* After the **port mode GE** command is run, all interfaces in the same interface group are configured to work at the rate of 1 Gbit/s. In this case, you need to install a GE medium on the interfaces so that the interfaces can go Up. If a medium with a different rate is installed on the interfaces, the interfaces go Down.

**Prerequisites**

Before running the **port mode GE** command, ensure that all interfaces in the interface group whose rate is to be switched are not Up. If an interface is Up, shut down the interface and then change the rate mode.After the **port mode 10G** command is run on an interface, a medium is installed or pre-configured on the interface, and the interface is Down.

**Precautions**

* The remote interface must be configured with the same rate mode.
* After the port mode { 10G | GE } command is run on an interface, the **clear configuration interface** command does not clear the port mode { 10G | GE } configuration when a medium is installed on the interface. The port mode { 10G | GE } configuration can be cleared when no medium is installed on the interface.
* The CE6820H, CE6820S, CE6820H-K, CE6881H and CE6881H-K do not support this command.


Example
-------

# Configure 25GE1/0/1 to work at the rate of 10 Gbit/s.
```
<HUAWEI> system-view
[~HUAWEI] interface 25ge 1/0/1
[~HUAWEI-25GE1/0/1] port mode 10G

```

# Set the rate of 25GE1/0/1 to 1 Gbit/s.
```
<HUAWEI> system-view
[~HUAWEI] interface 25ge 1/0/1
[~HUAWEI-25GE1/0/1] port mode GE
Warning: The port(s)(25GE1/0/1 to 25GE1/0/8) will be converted to GE mode.Continue? [Y/N]:y
Info: Set the same speed mode on the peer end.

```