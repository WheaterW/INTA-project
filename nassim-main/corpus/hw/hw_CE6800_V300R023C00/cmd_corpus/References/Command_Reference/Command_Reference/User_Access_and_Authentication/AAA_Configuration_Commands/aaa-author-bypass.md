aaa-author-bypass
=================

aaa-author-bypass

Function
--------

The **aaa-author-bypass** command sets the bypass authorization timeout interval.

The **undo aaa-author-bypass** command cancels the bypass authorization timeout interval.

By default, no bypass authorization timeout interval is set.



Format
------

**aaa-author-bypass enable time** *time-value*

**undo aaa-author-bypass enable**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Enables remote bypass authorization. | - |
| **time** *time-value* | Specifies the bypass authorization timeout interval. | The value is an integer that ranges from 1 to 1440, in minutes. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to the scenarios that require fast authorization response. When a user in a user domain where multiple authorization modes (for example, HWTACACS authorization and local authorization) are configured, bypass authorization is enabled, and the bypass authorization timeout interval is configured, the user will be authorized using the local authorization mode and the bypass authorization timer is enabled simultaneously if the HWTACACS server does not respond to the authorization request. When other users in the same domain are authorized during the configured bypass authorization timeout interval, the users are directly authorized using the local authorization mode, so that the users can be authorized without waiting until the HWTACACS server responds to their authorization requests, accelerating the authorization response.

**Precautions**

If only one authorization mode is configured in a user domain, the bypass authorization timer does not take effect after being configured.



Example
-------

# Set the bypass authorization timeout interval to 3 minutes.
```
<HUAWEI> system-view
[~HUAWEI] aaa-author-bypass enable time 3

```