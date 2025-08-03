isis suppress-flapping peer
===========================

isis suppress-flapping peer

Function
--------



The **isis suppress-flapping peer disable** command disables IS-IS neighbor relationship flapping suppression from an interface.

The **undo isis suppress-flapping peer disable** command enables IS-IS neighbor relationship flapping suppression on an interface.

The **isis suppress-flapping peer** command configures detection parameters for IS-IS neighbor relationship flapping suppression.

The **undo isis suppress-flapping peer** command restores the default detection parameters.

The **isis suppress-flapping peer hold-down** command configures the Hold-down mode and sets duration for this mode.

The **undo isis suppress-flapping peer hold-down** command cancels the Hold-down mode.

The **isis suppress-flapping peer hold-max-cost disable** command disables the Hold-max-cost mode.

The **undo isis suppress-flapping peer hold-max-cost disable** command enables the Hold-max-cost mode.



By default, IS-IS neighbor relationship flapping suppression is enabled on all interfaces.

By default, the detection interval of IS-IS neighbor relationship flapping suppression is 60s, the suppression threshold is 10, and the interval for exiting from suppression is 120s.

By default, the Hold-down mode is disabled, and the Hold-max-cost mode is enabled.

By default, the Hold-max-cost mode is enabled.




Format
------

**isis suppress-flapping peer disable**

**isis suppress-flapping peer** { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \*

**isis suppress-flapping peer hold-down** *interval*

**isis suppress-flapping peer hold-max-cost disable**

**undo isis suppress-flapping peer disable**

**undo isis suppress-flapping peer** { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \*

**undo isis suppress-flapping peer hold-down** [ *interval* ]

**undo isis suppress-flapping peer hold-max-cost disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **detecting-interval** *detecting-interval* | Specifies the detection interval of IS-IS neighbor relationship flapping suppression.  Each IS-IS interface on which IS-IS neighbor relationship flapping suppression is enabled starts a flapping counter. If the interval between two successive neighbor status changes from Full to a non-Full state is shorter than detecting-interval, a valid flapping\_event is recorded, and the flapping\_count increases by 1. | The value is an integer ranging from 1 to 300, in seconds. The default value is 60s. |
| **threshold** *threshold* | Specifies the threshold of IS-IS neighbor relationship flapping suppression.  When the flapping\_count reaches or exceeds threshold, flapping suppression takes effect. | The value is an integer ranging from 1 to 1000. The default value is 10. |
| **resume-interval** *resume-interval* | * Specifies the interval for exiting from IS-IS neighbor relationship flapping suppression.   If the interval between two successive neighbor status changes from Full to a non-Full state is longer than resume-interval, the flapping\_count is reset.   * If IS-IS neighbor relationship flapping suppression works in hold-max-cost mode, resume-interval indicates the duration of this mode. The value of resume-interval must be greater than that of detecting-interval. | The value is an integer ranging from 2 to 1000, in seconds. The default value is 120s. |
| **hold-down** *interval* | Specifies the duration of the Hold-down mode. | The value is an integer ranging from 1 to 600, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, IS-IS neighbor relationship flapping suppression is enabled on all interfaces in the same IS-IS process. To disable the function from one of the interfaces, run the **isis suppress-flapping peer disable** command.When an interface enters the flapping suppression state, all neighbor relationships on the interface enter the state accordingly.



**Prerequisites**



IS-IS neighbor relationship flapping suppression must have been enabled globally before you enable the function on an interface using the **undo isis suppress-flapping peer disable** command. By default, the function is enabled globally. If it is disabled, run the **undo suppress-flapping peer disable** command to enable it first.IS-IS neighbor relationship flapping suppression must have been enabled globally before you configure detection parameters for it. By default, the function is enabled. If it is disabled, run the **undo suppress-flapping peer disable** command to enable it before you configure the detection parameters.IS-IS neighbor relationship flapping suppression must have been enabled globally before you configure the Hold-down mode and set duration for this mode. By default, the function is enabled. If it is disabled, run the **undo suppress-flapping peer disable** command to enable it before you configure the Hold-down mode and set duration for this mode.



**Precautions**



Execution of the command may affect neighbor relationship stability. Therefore, exercise caution when using the command.The Hold-max-cost mode takes effect only unidirectionally. If a remote device does not support IS-IS neighbor relationship flapping suppression, bidirectional traffic between the local and remote devices may travel along different paths.




Example
-------

# Disable IS-IS neighbor relationship flapping suppression from 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis suppress-flapping peer disable

```

# Disable the Hold-max-cost mode on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis suppress-flapping peer hold-max-cost disable

```

# Set the detection interval of IS-IS neighbor relationship flapping suppression to 5s, the suppression threshold to 40, and the interval for exiting from suppression to 20s on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis suppress-flapping peer detecting-interval 5 threshold 40 resume-interval 20

```

# Configure the Hold-down mode and set its duration to 200s on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis suppress-flapping peer hold-down 200

```