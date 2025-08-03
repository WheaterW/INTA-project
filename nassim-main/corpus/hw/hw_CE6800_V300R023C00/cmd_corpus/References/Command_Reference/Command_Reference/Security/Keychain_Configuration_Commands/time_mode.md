time mode
=========

time mode

Function
--------



The **time mode** command configures the time mode for Keychain.

The **undo time mode** command restores the default time mode for Keychain.



By default, the time mode of Keychain is Local Mean Time (LMT).


Format
------

**time mode utc**

**time mode lmt**

**undo time mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lmt** | Specifies that the configured time is in LMT format. | - |
| **utc** | Specifies that the configured time is in Universal Time Coordinated (UTC) format. | - |



Views
-----

Keychain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Each keychain consists of multiple key IDs that are valid within different time periods and each key ID is configured with an authentication algorithm. When a key ID becomes valid, the corresponding authentication algorithm is used, ensuring the dynamic change of authentication algorithms. Configure different key IDs for packet sending and receiving to be valid within different time periods.To configure the time mode for Keychain, run the time mode command. You can configure UTC or LMT for Keychain based on the network planning. Ensure that the time mode remains the same on the entire network.




Example
-------

# Configure the time mode for Keychain as UTC.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] time mode utc

```