receive-time month
==================

receive-time month

Function
--------



The **receive-time** command makes a key act as a receive-key for the specified interval of time.



By default, no receive-time is configured.


Format
------

**receive-time month** *start-month* **to** *end-month*

**receive-time month** { *start-month* } &<1-12>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-month* | Specifies the month of the year to be configured as the start receive month for the given key. | The value ranges from January to December.  * jan * feb * mar * apr * may * jun * jul * aug * sep * oct * nov * dec |
| **to** | Acts as a separator. | - |
| *end-month* | Specifies the end receive month. | The value ranges from February to December.  * feb * mar * apr * may * jun * jul * aug * sep * oct * nov * dec  The end month should be later than the start month. |
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



Each keychain consists of multiple key IDs that are valid within different time periods and each key ID is configured with an authentication algorithm. When a key ID becomes valid, the corresponding authentication algorithm is used, ensuring the dynamic change of authentication algorithms. Configure different key IDs for packet sending and receiving to be valid within different time periods.



**Implementation Procedure**

There are two keychain validity modes:

* Absolute time range: In this mode, keychains are valid within a certain period and are invalid out of the period.
* Periodic time range: In this mode, keychains are valid periodically. After one period ends, keychains continue to be valid within next period.The mode in which key IDs for packet receiving become valid must be identical with that configured for the keychain.

**Precautions**



Only one key ID is valid within a time period. In other words, the send time periods of different key-ids cannot overlap with each other.




Example
-------

# Configure the receive time with the timing mode as yearly periodic.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei6 mode periodic yearly
[*HUAWEI-keychain-huawei6] key-id 5
[*HUAWEI-keychain-huawei6-keyid-5] receive-time month oct to dec

```