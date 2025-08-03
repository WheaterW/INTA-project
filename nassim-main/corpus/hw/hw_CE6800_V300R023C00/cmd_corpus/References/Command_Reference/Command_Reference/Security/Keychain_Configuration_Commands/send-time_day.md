send-time day
=============

send-time day

Function
--------



The **send-time** command makes a key act as a send key for the specified interval of time.



By default, no send-time is configured.


Format
------

**send-time day** *start-day* **to** *end-day*

**send-time day** { *start-day* } &<1-7>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-day* | Specifies the day of the week to be configured as the start send day for the given key. | The options are as follows:   * mon: Monday * tue: Tuesday * wed: Wednesday * thu: Thursday * fri: Friday * sat: Saturday * sun: Sunday |
| **to** | Acts as a separator. | - |
| *end-day* | Specifies the end send day for the given key. | The value ranges from Monday to Sunday.  * tue * wed * thu * fri * sat * sun  The end day should be greater than the start day. |
| **day** | Specifies the days of the week. | - |



Views
-----

weekly Key-ID view


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
* Periodic time range: In this mode, keychains are valid periodically. After one period ends, keychains continue to be valid within next period.The mode in which key IDs for packet sending become valid must be identical with that configured for the keychain.

**Precautions**



Only one key ID is valid within a time period. In other words, the send time periods of different key-ids cannot overlap with each other.




Example
-------

# Configure the send time with the timing mode as weekly periodic.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei3 mode periodic weekly
[*HUAWEI-keychain-huawei3] key-id 5
[*HUAWEI-keychain-huawei3-keyid-5] send-time day mon

```