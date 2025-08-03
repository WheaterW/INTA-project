receive-time date
=================

receive-time date

Function
--------



The **receive-time** command makes a key act as a receive-key for the specified interval of time.



By default, no receive-time is configured.


Format
------

**receive-time date** *start-date* **to** *end-date*

**receive-time date** { *start-date* } &<1-31>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-date* | Specifies the start date of the month to be configured as the receive date for the given key. <startDate>&<1-31> specifies the dates of the month. A maximum of 31 can be configured. | The value ranges from 1 to 31. |
| **to** | Acts as a separator. | - |
| *end-date* | Specifies the end receive date of the month. | The value ranges from 2 to 31. The end date should be greater than the start date. |
| **date** | Specifies the date of the month. | - |



Views
-----

monthly Key-ID view


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

# Configure the receive time with the timing mode as monthly periodic.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei5 mode periodic monthly
[*HUAWEI-keychain-huawei5] key-id 5
[*HUAWEI-keychain-huawei5-keyid-5] receive-time date 12 to 25

```