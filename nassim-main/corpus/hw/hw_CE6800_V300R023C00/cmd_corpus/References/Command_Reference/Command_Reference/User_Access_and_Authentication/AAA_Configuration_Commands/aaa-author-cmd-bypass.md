aaa-author-cmd-bypass
=====================

aaa-author-cmd-bypass

Function
--------

The **aaa-author-cmd-bypass** command sets the command-line bypass authorization timeout interval.

The **undo aaa-author-cmd-bypass** command cancels the command-line bypass authorization timeout interval.

By default, no command-line bypass authorization timeout interval is set.



Format
------

**aaa-author-cmd-bypass enable time** *time-value*

**undo aaa-author-cmd-bypass enable**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Enables remote command-line bypass authorization. | - |
| **time** *time-value* | Specifies the command-line bypass authorization timeout interval. | The value is an integer that ranges from 1 to 1440, in minutes. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to the scenarios that require fast command-line authorization response. When a user in a user domain where multiple command-line authorization modes (for example, HWTACACS authorization and local authorization) are configured, command-line bypass authorization is enabled, and the command-line bypass authorization timeout interval is configured, the user will be authorized using the local authorization mode and the command-line bypass authorization timer is enabled simultaneously if the HWTACACS server does not respond to the command-line authorization request. When other users in the same domain are authorized during the configured command-line bypass authorization timeout interval, the users are directly authorized using the local authorization mode, so that the users can be authorized without waiting until the HWTACACS server responds to their authorization requests, accelerating the authorization response.

**Precautions**

When only one command-line authorization mode is configured in a user domain and the command-line bypass authorization timer is enabled, other users in the same domain are directly considered to fail the command-line authorization during the command-line bypass authorization timeout interval.



Example
-------

# Set the command-line bypass authorization timeout interval to 3 minutes.
```
<HUAWEI> system-view
[~HUAWEI] aaa-author-cmd-bypass enable time 3

```