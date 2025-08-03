ospf suppress-flapping peer
===========================

ospf suppress-flapping peer

Function
--------



The **ospf suppress-flapping peer** command configures detection parameters for OSPF neighbor relationship flapping suppression.

The **undo ospf suppress-flapping peer** command restores the default detection parameters.

The **ospf suppress-flapping peer disable** command disables OSPF neighbor relationship flapping suppression from an interface.

The **undo ospf suppress-flapping peer disable** command enables OSPF neighbor relationship flapping suppression on an interface.

The **ospf suppress-flapping peer hold-down** command configures the Hold-down mode and sets duration for this mode.

The **undo ospf suppress-flapping peer hold-down** command cancels the Hold-down mode.

The **ospf suppress-flapping peer hold-max-cost disable** command disables the Hold-max-cost mode.

The **undo ospf suppress-flapping peer hold-max-cost disable** command enables the Hold-max-cost mode.



By default, the detection interval of OSPF neighbor flapping suppression is 60s, the suppression threshold is 10, and the interval for exiting from suppression is 120s.

By default, OSPF neighbor flapping suppression is enabled on all interfaces.

By default, the Hold-down mode is disabled and the Hold-max-cost mode is enabled.




Format
------

**ospf suppress-flapping peer disable**

**ospf suppress-flapping peer hold-down** *interval*

**ospf suppress-flapping peer hold-max-cost disable**

**ospf suppress-flapping peer** { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \*

**undo ospf suppress-flapping peer disable**

**undo ospf suppress-flapping peer hold-down** [ *interval* ]

**undo ospf suppress-flapping peer hold-max-cost disable**

**undo ospf suppress-flapping peer** { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hold-down** *interval* | Specifies the duration of the Hold-down mode. | The value is an integer ranging from 1 to 86400, in seconds. |
| **detecting-interval** *detecting-interval* | Specifies the detection interval of OSPF neighbor relationship flapping suppression.  Each OSPF interface on which OSPF neighbor relationship flapping suppression is enabled starts a flapping counter. If the interval between two successive neighbor status changes from Full to a non-Full state is shorter than detecting-interval, a valid flapping\_event is recorded, and the flapping\_count increases by 1. | The value is an integer ranging from 1 to 300, in seconds. The default value is 60s. |
| **threshold** *threshold* | Specifies the threshold of OSPF neighbor relationship flapping suppression.  When the flapping\_count reaches or exceeds threshold, flapping suppression takes effect. | The value is an integer ranging from 1 to 1000. The default value is 10. |
| **resume-interval** *resume-interval* | * Specifies a flapping detection clearance threshold for OSPF neighbor flapping suppression.   If the interval between two successive neighbor status changes from Full to a non-Full state is greater than resume-interval, the flapping\_count is cleared.   * If OSPF neighbor flapping suppression works in Hold-max-cost mode, resume-interval specifies the duration of the Hold-max-cost mode.   The value of resume-interval must be greater than that of detecting-interval. | The value is an integer ranging from 2 to 1000, in seconds. The default value is 120s. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can set detection parameters for OSPF neighbor flapping suppression on a specified interface according to the actual situation of the network. The default values are recommended.By default, OSPF neighbor flapping suppression is enabled globally. That is, OSPF neighbor flapping suppression is enabled on all interfaces in a process. To disable OSPF neighbor flapping suppression on a specified interface, run the **ospf suppress-flapping peer disable** command.After an interface enters the flapping suppression state, all neighbors connected to the interface enter the flapping suppression state.OSPF neighbor flapping suppression has two modes: Hold-down and Hold-max-cost.

* Hold-down mode: To prevent frequent flooding and topology changes during neighbor relationship establishment, the neighbor relationship cannot be re-established within a period of time. This prevents frequent LSDB synchronization and a large number of packets from being exchanged.
* Hold-max-cost mode: In this mode, the link cost is set to the maximum value (65535) within a period of time to prevent service traffic from passing through flapping links.The Hold-down mode and Hold-max-cost mode can be used together. If both modes take effect, the system enters the Hold-down mode first. After the system exits the Hold-down mode, the system enters the Hold-max-cost mode.By default, the Hold-max-cost mode takes effect. To configure the Hold-down mode and set duration for this mode, run the **ospf suppress-flapping peer hold-down interval** command.When OSPF neighbor flapping suppression uses the Hold-max-cost mode, you can run the **ospf suppress-flapping peer resume-interval resume-interval** command to set the duration of the Hold-max-cost mode. The value ranges from 2 to 1000, in seconds. The default value is 120s.

**Prerequisites**



OSPF neighbor relationship flapping suppression must have been enabled globally before you configure detection parameters for it. By default, the function is enabled. If it is disabled, run the **undo suppress-flapping peer disable** command to enable it before you configure the detection parameters.OSPF neighbor relationship flapping suppression must have been enabled globally before you enable the function on an interface using the **undo ospf suppress-flapping peer disable** command. By default, the function is enabled globally. If it is disabled, run the **undo suppress-flapping peer disable** command to enable it first.OSPF neighbor relationship flapping suppression must have been enabled globally before you configure the Hold-down mode and set duration for this mode. By default, the function is enabled. If it is disabled, run the **undo suppress-flapping peer disable** command to enable it before you configure the Hold-down mode and set duration for this mode.OSPF neighbor relationship flapping suppression must have been enabled globally before you configure duration for the Hold-max-cost mode. By default, the function is enabled. If it is disabled, run the **undo suppress-flapping peer disable** command to enable it before you configure duration for the Hold-max-cost mode.



**Precautions**



The Hold-max-cost mode takes effect only unidirectionally. If a remote device does not support OSPF neighbor relationship flapping suppression, bidirectional traffic between the local and remote devices may travel along different paths.When the OSPF neighbor relationship flaps again, the hold-max-cost timer will be restarted. If the flapping persists, the corresponding link may fail to exit from the flapping suppression state.If hold-down is configured, flapping suppression works first in hold-down mode and then in hold-max-cost mode by default. If only the hold-down mode is required, run the ospf suppress-flapping peer hold-max-cost disable command to disable the hold-max-cost mode.




Example
-------

# Configure the Hold-down mode and set its duration to 200s on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf suppress-flapping peer hold-down 200

```

# Disable OSPF neighbor relationship flapping suppression from an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf suppress-flapping peer disable

```

# Set the detection interval of OSPF neighbor relationship flapping suppression to 5s, the suppression threshold to 40, and the interval for exiting from suppression to 20s on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf suppress-flapping peer detecting-interval 5 threshold 40 resume-interval 20

```

# Disable the Hold-max-cost mode on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf suppress-flapping peer hold-max-cost disable

```