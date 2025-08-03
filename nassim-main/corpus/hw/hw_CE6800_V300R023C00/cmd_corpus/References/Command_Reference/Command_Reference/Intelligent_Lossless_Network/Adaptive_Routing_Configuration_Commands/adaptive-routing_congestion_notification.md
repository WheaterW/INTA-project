adaptive-routing congestion notification
========================================

adaptive-routing congestion notification

Function
--------



The **adaptive-routing congestion notification** command sets the interval at which ARN packets are sent in a dragonfly profile.

The **undo adaptive-routing congestion notification** command restores the default interval.



By default, the interval for sending ARN packets is 500 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**adaptive-routing congestion notification tx-interval** *tx-interval-value*

**undo adaptive-routing congestion notification tx-interval** *tx-interval-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tx-interval** *tx-interval-value* | Specifies the interval for sending ARN packets. | The value is an integer that can be 100, 200, 500, 1000, 2000, 5000 or 10000, in milliseconds. The default value is 500 ms. |



Views
-----

Dragonfly-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the adaptive routing function is enabled, you can run this command to set the interval for sending ARN packets.


Example
-------

# Set the interval at which ARN packets are sent to 200 ms in the default dragonfly profile.
```
<HUAWEI> system-view
[~HUAWEI] dragonfly profile default
[~HUAWEI-dragonfly-profile-default] adaptive-routing congestion notification tx-interval 200

```