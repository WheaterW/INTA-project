accounting interim-fail
=======================

accounting interim-fail

Function
--------



The **accounting interim-fail** command sets the maximum number of real-time accounting failures and configures a policy used after the number of real-time accounting failures exceeds the maximum.

The **undo accounting interim-fail** command restores the default maximum number of real-time accounting failures and the default policy.



By default, the maximum number of real-time accounting failures is 3 and the device keeps users online after the number of real-time accounting failures exceeds the maximum.


Format
------

**accounting interim-fail** [ **max-times** *times* ] { **online** | **offline** }

**undo accounting interim-fail**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **max-times** *times* | Specifies the maximum number of real-time accounting failures. If the maximum number of real-time accounting failures is reached and the next accounting request still has no response, the device considers that accounting fails and takes a policy for users. | The value is an integer that ranges from 1 to 255. The default value is 3. |
| **online** | Keeps users online if real-time accounting fails. | - |
| **offline** | Disconnects users if real-time accounting fails. | - |



Views
-----

Accounting scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After the real-time accounting function takes effect, the device sends real-time accounting requests to an accounting server, and the accounting server responds to the accounting requests. If the network is unstable, for example, a jitter occurs, the device may not receive response packets. As a result, accounting is interrupted for a short period of time. To reduce or prevent accounting interruption, run the **accounting interim-fail** command to set the maximum number of real-time accounting failures. The device considers that real-time accounting fails only after the number of consecutive real-time accounting failures exceeds the maximum.Choose one of the following policies to be applied after the maximum number of real-time accounting failures is reached:

* online: To prevent users from being affected by network faults, use the online policy to allow paid users to go online.
* offline: To stop providing services when accounting fails, use the offline policy to disconnect paid users.

**Prerequisites**

The real-time accounting function has been enabled by using the **accounting realtime** command.

**Precautions**

The **accounting interim-fail** command does not take effect for online users, but takes effect for the users who go online after the command is executed.


Example
-------

# In the accounting scheme scheme1, set the maximum number of real-time accounting failures to 5 and disconnects users if real-time accounting fails.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] accounting-scheme scheme1
[*HUAWEI-aaa-accounting-scheme1] accounting realtime 3
[*HUAWEI-aaa-accounting-scheme1] accounting interim-fail max-times 5 offline

```