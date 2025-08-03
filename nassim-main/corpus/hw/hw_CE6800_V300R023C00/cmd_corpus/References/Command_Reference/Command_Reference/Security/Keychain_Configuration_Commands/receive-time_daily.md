receive-time daily
==================

receive-time daily

Function
--------



The **receive-time** command makes a key act as a receive-key for the specified interval of time.



By default, no receive-time is configured.


Format
------

**receive-time daily** *start-time* **to** *end-time*

**undo receive-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-time* | Specifies the start receive time. | In HH:MM format. The value ranges from 00:00 to 23:59. |
| **to** | Acts as a separator. | - |
| *end-time* | Specifies the end receive time. | In HH:MM format. The value ranges from 00:00 to 23:59. The end-time should be greater than the start-time. |
| **daily** | Specifies the daily receive timing for the given key. | - |



Views
-----

daily Key-ID view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A keychain consists of multiple key IDs and different key IDs are active in different time periods. In this manner, authentication algorithms can be dynamically switched, improving protocol data transmission security. To make different key IDs take effect in different time periods, you need to configure the sending time and receiving time of each key ID.



**Implementation Procedure**

There are two keychain validity modes:

* Absolute time range: In this mode, keychains are valid within a certain period and are invalid out of the period.
* Periodic time range: In this mode, keychains are valid periodically. After one period ends, keychains continue to be valid within next period.The mode in which key IDs for packet receiving become valid must be identical with that configured for the keychain.

**Precautions**



Only one key ID is valid within a time period. In other words, the send time periods of different key-ids cannot overlap with each other.




Example
-------

# Configure the receive time with the timing mode as daily periodic.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei3 mode periodic daily
[*HUAWEI-keychain-huawei3] key-id 5
[*HUAWEI-keychain-huawei3-keyid-5] receive-time daily 14:52 to 18:10

```