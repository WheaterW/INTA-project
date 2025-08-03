send-time month
===============

send-time month

Function
--------



The **send-time** command makes a key act as a send key for the specified interval of time.



By default, no send-time is configured.


Format
------

**send-time month** *start-month* **to** *end-month*

**send-time month** { *start-month* } &<1-12>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-month* | Specifies the month of the year to be configured as the start send month for the given key. | The value ranges from January to December.  * jan * feb * mar * apr * may * jun * jul * aug * sep * oct * nov * dec |
| **to** | Acts as a separator. | - |
| *end-month* | Specifies the end send month. | The value ranges from January to December.  * feb * mar * apr * may * jun * jul * aug * sep * oct * nov * dec  The end month should be greater than the start month. |
| **month** | Specifies the months of the year. | - |



Views
-----

yearly Key-ID view


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

# Configure the send time with the timing mode as yearly periodic, and a few months are available.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei6 mode periodic yearly
[*HUAWEI-keychain-huawei6] key-id 5
[*HUAWEI-keychain-huawei6-keyid-5] send-time month oct to dec

```

# Configure the send time with the timing mode as yearly periodic.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei5 mode periodic yearly
[*HUAWEI-keychain-huawei5] key-id 5
[*HUAWEI-keychain-huawei5-keyid-5] send-time month apr

```