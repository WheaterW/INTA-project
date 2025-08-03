undo send-time receive-time
===========================

undo send-time receive-time

Function
--------



The **undo send-time** command deletes the send-time configuration.

The **undo receive-time** command deletes the receive-time configuration.



By default, no send-time is configured.

By default, no receive-time is configured.




Format
------

**undo send-time**

**undo receive-time**


Parameters
----------

None

Views
-----

weekly Key-ID view,yearly Key-ID view,monthly Key-ID view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A keychain consists of multiple key IDs and different key IDs are active in different time periods. In this manner, authentication algorithms can be dynamically switched, improving protocol data transmission security. To make different key IDs take effect in different time periods, you need to configure the sending time and receiving time of each key ID.



**Precautions**



Only one key ID is valid within a time period. In other words, the send time periods of different key-ids cannot overlap with each other.




Example
-------

# Undo the receive time with the timing mode as daily periodic.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode periodic daily
[*HUAWEI-keychain-huawei] key-id 1
[*HUAWEI-keychain-huawei-keyid-1] receive-time daily 1:00 to 2:00
[*HUAWEI-keychain-huawei-keyid-1] undo receive-time

```