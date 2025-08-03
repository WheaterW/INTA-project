reset cpu-defend host-car drop-packet record
============================================

reset cpu-defend host-car drop-packet record

Function
--------



The **reset cpu-defend host-car drop-packet record** command clears records about packet loss caused by user-level rate limiting.




Format
------

**reset cpu-defend host-car drop-packet record** [ **car-id** *car-id* ] [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **car-id** *car-id* | Specifies a bucket. | The value is an integer that ranges from 0 to 8191. |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After user-level rate limiting is configured and packet loss monitoring for user-level rate limiting is enabled, you can run this command to clear information about packet loss caused by user-level rate limiting.


Example
-------

# Clear statistics about packets discarded due to user-level rate limiting in a specified slot.
```
<HUAWEI> reset cpu-defend host-car drop-packet record

```