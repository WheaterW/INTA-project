ospfv3 suppress-flapping peer (interface view)
==============================================

ospfv3 suppress-flapping peer (interface view)

Function
--------



The **ospfv3 suppress-flapping peer** command configures detection parameters for OSPFv3 neighbor relationship flapping suppression.

The **undo ospfv3 suppress-flapping peer** command restores the default detection parameters.

The **ospfv3 suppress-flapping peer disable** command disables OSPFv3 neighbor relationship flapping suppression from an interface.

The **undo ospfv3 suppress-flapping peer disable** command enables OSPFv3 neighbor relationship flapping suppression on an interface.

The **ospfv3 suppress-flapping peer hold-down** command configures the Hold-down mode and sets duration for this mode.

The **undo ospfv3 suppress-flapping peer hold-down** command cancels the Hold-down mode.

The **ospfv3 suppress-flapping peer hold-max-cost disable** command disables the Hold-max-cost mode.

The **undo ospfv3 suppress-flapping peer hold-max-cost disable** command enables the Hold-max-cost mode.



By default, the detection interval of OSPFv3 neighbor flapping suppression is 60s, the suppression threshold is 10, and the interval for exiting from suppression is 120s.

By default, OSPFv3 neighbor flapping suppression is enabled on all interfaces.

By default, the Hold-down mode is disabled and the Hold-max-cost mode is enabled.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 suppress-flapping peer disable** [ **instance** *instance-id* ]

**ospfv3 suppress-flapping peer hold-down** *interval* [ **instance** *instance-id* ]

**ospfv3 suppress-flapping peer hold-max-cost disable** [ **instance** *instance-id* ]

**ospfv3 suppress-flapping peer** { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \* [ **instance** *instance-id* ]

**undo ospfv3 suppress-flapping peer disable** [ **instance** *instance-id* ]

**undo ospfv3 suppress-flapping peer hold-down** [ *interval* ] [ **instance** *instance-id* ]

**undo ospfv3 suppress-flapping peer hold-max-cost disable** [ **instance** *instance-id* ]

**undo ospfv3 suppress-flapping peer** { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \* [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Specifies the interface instance ID. | The value is an integer ranging from 0 to 255. |
| **hold-down** *interval* | Specifies the duration of the Hold-down mode. | The value is an integer ranging from 1 to 86400, in seconds. |
| **detecting-interval** *detecting-interval* | Specifies the detection interval of OSPFv3 neighbor relationship flapping suppression.  Each OSPF interface on which OSPFv3 neighbor relationship flapping suppression is enabled starts a flapping counter. If the interval between two successive neighbor status changes from Full to a non-Full state is shorter than detecting-interval, a valid flapping\_event is recorded, and the flapping\_count increases by 1. | The value is an integer ranging from 1 to 300, in seconds. The default value is 60s. |
| **threshold** *threshold* | Specifies the threshold of OSPF neighbor relationship flapping suppression.  When the flapping\_count reaches or exceeds threshold, flapping suppression takes effect. | The value is an integer ranging from 1 to 1000. The default value is 10. |
| **resume-interval** *resume-interval* | * Specifies a flapping detection clearance threshold for OSPFv3 neighbor flapping suppression.   If the interval between two successive neighbor status changes from Full to a non-Full state is greater than resume-interval, the flapping\_count is cleared.   * If OSPFv3 neighbor flapping suppression works in Hold-max-cost mode, resume-interval specifies the duration of the Hold-max-cost mode.   The value of resume-interval must be greater than that of detecting-interval. | The value is an integer ranging from 2 to 1000, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure detection parameters for OSPFv3 neighbor relationship flapping suppression on an interface, run the ospfv3 suppress-flapping peer command. However, keeping the default configurations is recommended.By default, OSPFv3 neighbor relationship flapping suppression is enabled on all interfaces in the same OSPFv3 process. To disable the function from one of the interfaces, run the **ospfv3 suppress-flapping peer disable** command.Flapping suppression works in either Hold-down or Hold-max-cost mode.

* Hold-down mode: In the case of frequent flooding and topology changes during neighbor relationship establishment, interfaces prevent neighbor relationship reestablishment during Hold-down suppression, which minimizes LSDB synchronization attempts and packet exchanges.
* Hold-max-cost mode: If the traffic forwarding path changes frequently, interfaces use 65535 as the cost of the flapping link during Hold-max-cost suppression, which prevents traffic from passing through the flapping link.Flapping suppression can also work first in Hold-down mode and then in Hold-max-cost mode.By default, the Hold-max-cost mode takes effect. To configure the Hold-down mode and set duration for this mode, run the ospfv3 suppress-flapping peer hold-down command.

**Prerequisites**



OSPFv3 neighbor flapping suppression must have been enabled globally before you set detection parameters for OSPFv3 neighbor flapping suppression. By default, OSPFv3 neighbor flapping suppression is enabled. If OSPFv3 neighbor flapping suppression is disabled, run the **undo suppress-flapping peer disable** command to enable it globally.OSPFv3 neighbor flapping suppression must have been enabled globally before you run the **undo ospfv3 suppress-flapping peer disable** command to enable OSPFv3 neighbor flapping suppression on a specified interface. By default, OSPFv3 neighbor flapping suppression is enabled. If OSPFv3 neighbor flapping suppression is disabled, you can run the **undo suppress-flapping peer disable** command to enable it globally.OSPFv3 neighbor flapping suppression must have been enabled globally before you configure the Hold-down peer flapping mode and set duration for this mode. By default, OSPFv3 neighbor flapping suppression is enabled. If it is disabled, run the **undo suppress-flapping peer disable** command to enable it globally.



**Precautions**



The Hold-max-cost mode takes effect only unidirectionally. If a remote device does not support OSPFv3 neighbor relationship flapping suppression, bidirectional traffic between the local and remote devices may travel along different paths.




Example
-------

# Configure the Hold-down mode and set its duration to 200s on an interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 suppress-flapping peer hold-down 200

```

# Set the detection interval of OSPFv3 neighbor relationship flapping suppression to 5s, the suppression threshold to 40, and the interval for exiting from suppression to 20s on an interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 suppress-flapping peer detecting-interval 5 threshold 40 resume-interval 20

```

# Disable OSPFv3 neighbor relationship flapping suppression from an interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 suppress-flapping peer disable

```

# Disable the Hold-max-cost mode on an interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 suppress-flapping peer hold-max-cost disable

```