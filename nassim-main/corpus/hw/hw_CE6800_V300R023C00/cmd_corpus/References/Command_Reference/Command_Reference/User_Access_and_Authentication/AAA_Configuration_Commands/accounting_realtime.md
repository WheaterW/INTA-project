accounting realtime
===================

accounting realtime

Function
--------



The **accounting realtime** command enables the real-time accounting function and sets the interval for real-time accounting in an accounting scheme.

The **undo accounting realtime** command disables the real-time accounting function.



By default, the device performs accounting based on user online duration, the real-time accounting function is disabled.


Format
------

**accounting realtime** *interval*

**undo accounting realtime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval for real-time accounting. | The value is an integer in the range from 0 to 65535. |



Views
-----

Accounting scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to the users who are charged based on online duration. If a user goes offline unexpectedly, the accounting server cannot receive the accounting-stop packet, so it keeps charging the user while they are not receiving a service. To solve the problem, configure the real-time accounting function on the device. After the real-time accounting function is configured, the device periodically sends real-time accounting packets to the accounting server. After receiving the real-time accounting packets, the accounting server charges the user. If the device detects that the user goes offline, it stops sending real-time accounting packets and the accounting server stops accounting. The result of real-time accounting is precise.

**Precautions**

* When the accounting interval is set using both the **accounting realtime** command and the Acct-Interim-Interval attribute, if the Acct-Interim-Interval value range is 60-3932100, the interval set by Acct-Interim-Interval has a higher priority. Otherwise, the interval set by the **accounting realtime** command takes effect.
* If an accounting scheme is applied to a domain, the **accounting realtime** command does not affect online users, but only takes effect for the users who go online after the command is executed.
* If interval is set to 0 and the IP address of the client is changed, the device still sends a real-time accounting packet carrying the changed IP address information to the RADIUS server.
* A short interval for real-time accounting requires high performance of the device and accounting server. If there are more than 1000 users, setting a long interval for real-time accounting is recommended. The following table lists the suggested real-time accounting intervals for different user quantities.
* User Quantity: 1-99; Interval for Real-Time Accounting: 3 minutes
* User Quantity: 100-499; Interval for Real-Time Accounting: 6 minutes
* User Quantity: 500-999; Interval for Real-Time Accounting: 12 minutes
* User Quantity: more than 1000; Interval for Real-Time Accounting: more than 15 minutes

Example
-------

# In the accounting scheme scheme1, enable the real-time accounting function and set the interval for real-time accounting to 6 minutes.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] accounting-scheme scheme1
[*HUAWEI-aaa-accounting-scheme1] accounting realtime 6

```