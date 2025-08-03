ospf suppress-flapping peer multi-area
======================================

ospf suppress-flapping peer multi-area

Function
--------



The **ospf suppress-flapping peer disable multi-area** command disables OSPF neighbor relationship flapping suppression on a multi-area adjacency interface.

The **undo ospf suppress-flapping peer disable multi-area** command enables OSPF neighbor relationship flapping suppression on a multi-area adjacency interface.

The **ospf suppress-flapping peer hold-max-cost disable multi-area** command disables the Hold-max-cost mode on a multi-area adjacency interface.

The **undo ospf suppress-flapping peer hold-max-cost disable multi-area** command enables the Hold-max-cost mode on a multi-area adjacency interface.

The **ospf suppress-flapping peer multi-area** command configures detection parameters for OSPF neighbor relationship flapping suppression on a multi-area adjacency interface.

The **undo ospf suppress-flapping peer multi-area** command restores the default detection parameters.

The **ospf suppress-flapping peer hold-down multi-area** command configures the Hold-down mode and sets duration for this mode on a multi-area adjacency interface.

The **undo ospf suppress-flapping peer hold-down multi-area** command cancels the Hold-down mode on a multi-area adjacency interface.



By default, OSPF neighbor relationship flapping suppression is enabled on all multi-area adjacency interfaces.

By default, the Hold-max-cost mode is enabled on a multi-area adjacency interface.

By default, the detection interval of OSPF neighbor relationship flapping suppression on multi-area adjacency interfaces is 60s, the suppression threshold is 10, and the interval for exiting from suppression is 120s.

By default, the Hold-down mode is disabled on a multi-area adjacency interface.




Format
------

**ospf suppress-flapping peer** { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \* **multi-area** { *area-id* | *area-id-ipv4* }

**ospf suppress-flapping peer disable multi-area** { *area-id* | *area-id-ipv4* }

**ospf suppress-flapping peer hold-down** *interval* **multi-area** { *area-id* | *area-id-ipv4* }

**ospf suppress-flapping peer hold-max-cost disable multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf suppress-flapping peer** { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \* **multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf suppress-flapping peer disable multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf suppress-flapping peer hold-down** [ *interval* ] **multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf suppress-flapping peer hold-max-cost disable multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **detecting-interval** *detecting-interval* | Specifies the detection interval of OSPF neighbor relationship flapping suppression.  Each OSPF interface on which OSPF neighbor relationship flapping suppression is enabled starts a flapping counter. If the interval between two successive neighbor status changes from Full to a non-Full state is shorter than detecting-interval, a valid flapping\_event is recorded, and the flapping\_count increases by 1. | The value is an integer ranging from 1 to 300, in seconds. The default value is 60s. |
| **threshold** *threshold* | Specifies the threshold of OSPF neighbor relationship flapping suppression.  When the flapping\_count reaches or exceeds threshold, flapping suppression takes effect. | The value is an integer ranging from 1 to 1000. The default value is 10. |
| **resume-interval** *resume-interval* | * Specifies the interval for exiting OSPF neighbor relationship flapping suppression.   If the interval between two successive neighbor status changes from Full to a non-Full state is longer than resume-interval, the flapping\_count is reset.   * If OSPF neighbor relationship flapping suppression works in Hold-max-cost mode, resume-interval indicates the duration of this mode.   resume-interval must be greater than detecting-interval. | The value is an integer ranging from 2 to 1000, in seconds. The default value is 120s. |
| *area-id* | Specifies the ID of an OSPF area. The value is an integer. | The value is a decimal integer ranging from 0 to 4294967295. |
| *area-id-ipv4* | Specifies the ID of an OSPF area, in the format of an IP address. | The value is in the format X.X.X.X, where each X represents a value from 0 to 255 |
| **hold-down** *interval* | Specifies the duration of the Hold-down mode. | The value is an integer ranging from 1 to 86400, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, OSPF neighbor relationship flapping suppression is enabled on all multi-area adjacency interfaces in the same OSPF process. To disable the function from one of the interfaces, run the **ospf suppress-flapping peer disable multi-area area-id** command.When a multi-area adjacency interface enters the flapping suppression state, all neighbor relationships on the interface enter the state accordingly.Flapping suppression works in either Hold-down or Hold-max-cost mode.

* Hold-down mode: In the case of frequent flooding and topology changes during neighbor relationship establishment, interfaces prevent neighbor relationship reestablishment during Hold-down suppression, which minimizes LSDB synchronization attempts and packet exchanges.
* Hold-max-cost mode: If the traffic forwarding path changes frequently, interfaces use 65535 as the cost of the flapping link during Hold-max-cost suppression, which prevents traffic from passing through the flapping link.Flapping suppression can also work first in Hold-down mode and then in Hold-max-cost mode.By default, the Hold-max-cost mode takes effect on a multi-area adjacency interface. To configure the Hold-down mode and set duration for this mode, run the **ospf suppress-flapping peer hold-down interval multi-area area-id** command.To configure detection parameters for OSPF neighbor relationship flapping suppression on a multi-area adjacency interface, run the ospf suppress-flapping peer multi-area command. However, keeping the default configurations is recommended.

Example
-------

# Set the detection interval of OSPF neighbor relationship flapping suppression to 5s, the suppression threshold to 40, and the interval for exiting from suppression to 20s on multi-area adjacency interface.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 0
[*HUAWEI-ospf-1-area-0.0.0.0] quit
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] quit
[*HUAWEI-ospf-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0
[*HUAWEI-100GE1/0/1] ospf enable multi-area 1
[*HUAWEI-100GE1/0/1] ospf suppress-flapping peer detecting-interval 5 threshold 40 resume-interval 20 multi-area 1

```

# Disable the Hold-max-cost mode on multi-area adjacency interface.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 0
[*HUAWEI-ospf-1-area-0.0.0.0] quit
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] quit
[*HUAWEI-ospf-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0
[*HUAWEI-100GE1/0/1] ospf enable multi-area 1
[*HUAWEI-100GE1/0/1] ospf suppress-flapping peer hold-max-cost disable multi-area 1

```

# Disable OSPF neighbor relationship flapping suppression on multi-area adjacency interface.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 0
[*HUAWEI-ospf-1-area-0.0.0.0] quit
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] quit
[*HUAWEI-ospf-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0
[*HUAWEI-100GE1/0/1] ospf enable multi-area 1
[*HUAWEI-100GE1/0/1] ospf suppress-flapping peer disable multi-area 1

```

# Configure the Hold-down mode and set its duration to 200s on multi-area adjacency interface.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 0
[*HUAWEI-ospf-1-area-0.0.0.0] quit
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] quit
[*HUAWEI-ospf-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0
[*HUAWEI-100GE1/0/1] ospf enable multi-area 1
[*HUAWEI-100GE1/0/1] ospf suppress-flapping peer hold-down 200 multi-area 1

```