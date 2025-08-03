send-time (absolute Key-ID view)
================================

send-time (absolute Key-ID view)

Function
--------



The **send-time** command makes a key act as a send key for the specified interval of time.



By default, no send-time is configured.


Format
------

**send-time** *start-time* *start-date* { **duration** { *duration-value* | **infinite** } | { **to** *end-time* *end-date* } }

**undo send-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-time* | Specifies the start send time. | In HH:MM format. The value ranges from 00:00 to 23:59. |
| *start-date* | Specifies the send date. | In YYYY-MM-DD format. The value ranges from 1970-01-01~2050-12-31. |
| **duration** *duration-value* | Specifies the duration of the send time in minutes. | The value ranges from 1 to 26280000. |
| **infinite** | Specifies that the key will be acting as an active send key forever from the configured start-time. | - |
| **to** | Acts as a separator. | - |
| *end-time* | Specifies the end send time. | In HH:MM format. The value ranges from 00:00 to 23:59. The end-time should be greater than the start-time. |
| *end-date* | Specifies the end date. | In YYYY-MM-DD format. The value ranges from 1970-01-01~2050-12-31. |



Views
-----

absolute Key-ID view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Each keychain consists of multiple key IDs that are valid within different time periods and each key ID is configured with an authentication algorithm. When a key ID becomes valid, the corresponding authentication algorithm is used, ensuring the dynamic change of authentication algorithms. Configure different key IDs for packet sending and receiving to be valid within different time periods.



**Implementation Procedure**

There are two keychain validity modes:

* Absolute time range: In this mode, keychains are valid within a certain period and are invalid out of the period.
* Periodic time range: In this mode, keychains are valid periodically. After one period ends, keychains continue to be valid within next period.The mode in which key IDs for packet sending become valid must be identical with that configured for the keychain.

**Precautions**



Only one key ID is valid within a time period. In other words, the send time periods of different key-ids cannot overlap with each other.




Example
-------

# Configure the send time with the timing mode as absolute.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei1 mode absolute
[*HUAWEI-keychain-huawei1] key-id 5
[*HUAWEI-keychain-huawei1-keyid-5] send-time 14:52 2018-10-1 to 14:52 2040-10-1

```