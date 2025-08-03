display radius-server { dead-count | dead-interval | detect-cycle }
===================================================================

display radius-server { dead-count | dead-interval | detect-cycle }

Function
--------



The **display radius-server** command displays the configured RADIUS server detection interval, maximum number of consecutive unacknowledged packets in each detection interval, and number of times the detection interval cycles.




Format
------

**display radius-server** { **dead-count** | **dead-interval** | **detect-cycle** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dead-count** | Display configuration information about the maximum number of consecutive packets that are not acknowledged by the RADIUS server in each detection interval. | - |
| **dead-interval** | Display configuration information about the RADIUS server detection interval. | - |
| **detect-cycle** | Display configuration information about the number of times the RADIUS server detection interval cycles. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the RADIUS server detection interval, maximum number of consecutive unacknowledged packets in each detection interval, and number of times the detection interval cycles are configured, you can run the display radius-server { dead-count | dead-interval | detect-cycle } command to check the configured RADIUS server detection interval, maximum number of consecutive unacknowledged packets in each detection interval, and number of times the detection interval cycles.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configuration information about the number of times the RADIUS server detection interval cycles.
```
<HUAWEI> display radius-server detect-cycle
Radius server down detect cycle is 2.

```

# Display configuration information about the RADIUS server detection interval.
```
<HUAWEI> display radius-server dead-interval
Current Radius server detected duration is 5.

```

# Display configuration information about the maximum number of consecutive packets that are not acknowledged by the RADIUS server in each detection interval.
```
<HUAWEI> display radius-server dead-count
Radius server state detected count is 2.

```

**Table 1** Description of the **display radius-server { dead-count | dead-interval | detect-cycle }** command output
| Item | Description |
| --- | --- |
| Radius server state detected count is | Maximum number of consecutive packets that are not acknowledged by the RADIUS server. |
| Radius server down detect cycle is | Number of times the RADIUS server detection interval cycles. |
| Current Radius server detected duration is | Detection interval of the current RADIUS server. |