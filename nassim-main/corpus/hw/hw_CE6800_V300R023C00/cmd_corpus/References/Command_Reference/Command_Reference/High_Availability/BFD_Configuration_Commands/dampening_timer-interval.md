dampening timer-interval
========================

dampening timer-interval

Function
--------



The **dampening timer-interval** command configures a flapping suppression time for a BFD session.

The **undo dampening timer-interval** command restores the default flapping suppression time.



By default, the flapping suppression timer is started.


Format
------

**dampening timer-interval maximum** *maximum-milliseconds* **initial** *initial-milliseconds* **secondary** *secondary-milliseconds*

**dampening timer-interval bundle-member maximum** *bundle-maximum-milliseconds* **initial** *bundle-initial-milliseconds* **secondary** *bundle-secondary-milliseconds*

**dampening timer-interval bundle-member l3-only-mode**

**undo dampening timer-interval** [ **maximum** *maximum-milliseconds* **initial** *initial-milliseconds* **secondary** *secondary-milliseconds* ]

**undo dampening timer-interval bundle-member** [ **maximum** *bundle-maximum-milliseconds* **initial** *bundle-initial-milliseconds* **secondary** *bundle-secondary-milliseconds* ]

**undo dampening timer-interval bundle-member l3-only-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *maximum-milliseconds* | Specifies a maximum flapping suppression time for a BFD session. | The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 12000. |
| **initial** | Initial dampening timer interval. | - |
| *initial-milliseconds* | Specifies an initial flapping suppression time for a BFD session. | The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 2000. |
| **secondary** | Secondary dampening timer interval. | - |
| *secondary-milliseconds* | Specifies a secondary flapping suppression time for a BFD session. | The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 5000. |
| **bundle-member** | Indicates that a flapping suppression time is configured for a BFD for link-bundle session. | - |
| **maximum** | Maximum dampening timer interval. | - |
| *bundle-maximum-milliseconds* | Specifies a maximum flapping suppression time for a BFD for link-bundle session. | The value is an integer ranging from 20000 to 3600000, in milliseconds. The default value is 600000. |
| *bundle-initial-milliseconds* | Specifies an initial flapping suppression time for a BFD for link-bundle session. | The value is an integer ranging from 6000 to 3600000, in milliseconds. The default value is 16000. |
| *bundle-secondary-milliseconds* | Specifies a secondary flapping suppression time for a BFD for link-bundle session. | The value is an integer ranging from 10000 to 3600000, in milliseconds. The default value is 20000. |
| **l3-only-mode** | Indicates that flapping suppression takes effect only for a main BFD for link-bundle session. | - |



Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If BFD detects link Down, services are switched. A penalty mechanism is provided to delay BFD session establishment and prevent frequent service switchovers, protecting link resources and reducing link resource consumption.Flapping suppression can take effect for the following BFD sessions:

* Non-BFD for link-bundle sessions
* BFD for link-bundle sessions (bundle-member must be specified)In flapping suppression detection for BFD, BFD flapping suppression is started if BFD detects two consecutive down events within 10 minutes. For the first time when flapping suppression starts, the BFD session remains Down within a period specified using the initial bundle-initial-milliseconds parameter. After the period of time expires, BFD session negotiation is restarted. If the BFD session detects a Down event again, for the second time when flapping suppression starts, the BFD session remains Down within a period specified using the secondary secondary-milliseconds parameter. After the period of time elapses, BFD session negotiation is restarted.If the BFD session detects a Down event for the third time, the flapping suppression time is incremented based on the formula of secondary secondary-milliseconds multiplied by 2 and multiplied by (total number of flapping times - 3). The flapping suppression time keeps increasing till it reaches the maximum maximum-milliseconds value, and stays at the maximum value.For non-BFD for link-bundle sessions, the default initial flapping suppression period is 2000 ms, the secondary negotiation suppression period is 5000 ms, and the maximum negotiation suppression period is 12000 ms. The suppression periods of the BFD down event are 0, 2000, 5000, 10000, and 12000. The value 0 indicates that flapping suppression is not performed the first time BFD detects a down event. For link-bundle sessions, the initial flapping suppression period is 16000 ms, the secondary flapping suppression period is 20000 ms, and the maximum flapping suppression period is 600000 ms. The suppression periods of the BFD down event are 0, 16000, 20000, 40000, 80000, 120000, 160000, and 600000, respectively.

**Prerequisites**

BFD has been globally enabled using the bfd command.

**Precautions**

It is recommended that the secondary flapping suppression time be greater than the initial flapping suppression time and less than the maximum flapping suppression time.


Example
-------

# Set the initial flapping suppression time for a BFD session to 8000 ms, the secondary suppression time for a BFD session to 20000 ms, and the maximum suppression time for a BFD session to 30000 ms.
Flapping suppression is not performed the first time BFD detects a down event.
The suppression period for the second BFD down event is 8000 ms.
The suppression period for the third BFD down event is 20000 ms.
The suppression period for the fourth BFD down event is 30000 ms.
...
The suppression period for the Nth BFD down event is 30000 ms.
When BFD goes down, the suppression timer starts. If no BFD down event is detected with 10 minutes after the timer starts, flapping suppression is no longer performed.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] dampening timer-interval maximum 30000 initial 8000 secondary 20000

```

# Set the maximum flapping suppression time for a BFD session to 10000 ms, the initial flapping suppression time for a BFD session to 8000 ms, and the secondary flapping suppression time for a BFD session to 9000 ms.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] dampening timer-interval maximum 10000 initial 8000 secondary 9000

```