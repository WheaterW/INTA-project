pack enable
===========

pack enable

Function
--------



The **pack enable** command enables the device to combine sampled data packets and send the sampled data.



By default, the device does not combine sampled data packets and send the sampled data.


Format
------

**pack enable**

**undo pack enable**


Parameters
----------

None

Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When telemetry-based static subscription is configured to collect sampled data and multiple sampling paths are configured, the device may need to frequently send data to the server. In this case, you can run the **pack enable** command to enable the device to combine multiple sampled data packets and send them to the server. This reduces the number of data sending times and improves the server performance.

**Precautions**

* When the transmission protocol is UDP, the device does not support the **pack enable** command.
* After telemetry adaptive sampling is configured, the combined packet sending interval is still the same as the sampling interval specified before adaptive sampling is configured.
* If the same subscription has different sampling intervals, the maximum sampling interval is used as the combined packet sending interval. If the sampling interval is 0, the combined packet sending interval is 1 second.

Example
-------

# Configure two sensor groups in the same subscription view, set the sampling interval to 10000 ms, and send combined sampled data to the client.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription 1
[~HUAWEI-telemetry-subscription-1] sensor-group 1 sample-interval 10000
[~HUAWEI-telemetry-subscription-1] sensor-group 2 sample-interval 10000
[~HUAWEI-telemetry-subscription-1] pack enable

```