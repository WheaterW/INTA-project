timer spf (IS-IS view)
======================

timer spf (IS-IS view)

Function
--------



The **timer spf** command configures a delay for SPF calculation.

The **undo timer spf** command restores the default configuration.



By default, the delay for SPF calculation is 5 seconds.


Format
------

**timer spf** *max-interval* [ *init-interval* [ *incr-interval* ] ]

**undo timer spf**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-interval* | Specifies the maximum delay for SPF calculation. | The value is an integer ranging from 1 to 120, in seconds. The default value is 5s. |
| *init-interval* | Specifies the delay for the first SPF calculation. | The value is an integer ranging from 1 to 60000, in milliseconds. The default value is 50 ms. |
| *incr-interval* | Specifies the incremental delay between two times of SPF calculation. | The value is an integer ranging from 1 to 60000, in milliseconds. The default value is 200 ms. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

For IS-IS, when the LSDB changes, SPF calculation is triggered. If SPF calculation occurs frequently, a large number of system resources are consumed, deteriorating the system performance. A delay for SPF calculation can improve the SPF calculation efficiency. However, if the delay is too long, route convergence slows down.To speed up the route convergence without affecting the efficiency of routers, you can configure an intelligent timer for SPF calculation. This timer automatically adjusts the interval according to the LSDB change frequency.The delay for SPF calculation is described as follows:

* The delay for the first SPF calculation is init-interval; the delay for the second SPF calculation is incr-interval. From the third time on, the delay for SPF calculation doubles each time until the delay reaches max-interval.If network flapping persists within the max-interval period, max-interval is used as the delay for SPF calculation. If network flapping does not occur within the max-interval period or if the IS-IS process is restarted, init-interval is used as the delay for SPF calculation.
* If incr-interval is not specified, the delay for SPF calculation for the first time is init-interval. From the second time on, the delay is max-interval. If the local routing information keeps being updated within the max-interval period, the delay remains at max-interval until the time the local routing information is not updated within the max-interval period or the IS-IS process is restarted. Then the delay decreases to init-interval.
* When only max-interval is specified, the intelligent timer functions as an ordinary one-time triggering timer.

Example
-------

# Set the maximum delay to 15s, the initial delay to 10 ms, and the incremental delay to 5000 ms.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] timer spf 15 10 5000

```

# Set the delay for SPF calculation to 5s.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] timer spf 5

```