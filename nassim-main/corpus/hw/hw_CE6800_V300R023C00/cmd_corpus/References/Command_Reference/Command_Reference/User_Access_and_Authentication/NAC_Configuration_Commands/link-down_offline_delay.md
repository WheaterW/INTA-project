link-down offline delay
=======================

link-down offline delay

Function
--------



The **link-down offline delay** command configures the user logout delay when an interface link is faulty.

The **undo link-down offline delay** command restores the default configuration.



By default, the user logout delay is 10 seconds when an interface link is faulty.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**link-down offline delay** { *delay-value* | **unlimited** }

**undo link-down offline delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *delay-value* | Specifies the user logout delay when an interface link is faulty. | The value is an integer that ranges from 0 to 60, in seconds. If the value is 0, users are logged out immediately when an interface link is faulty. |
| **unlimited** | Indicates that users are not logged out when an interface link is faulty. | - |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a link is faulty, the interface is interrupted and users are directly logged out. To solve this problem, you can configure the user logout delay function. When the interface link is faulty, the users remain online within the delay. In this case, if the link is restored, the users do not need to be re-authenticated. If the users are disconnected after the delay and the link is restored, the users need to be re-authenticated.

**Precautions**

* This function takes effect only for wired users who go online through Layer 2 physical interfaces or Eth-Trunk interfaces that have NAC authentication configured. This command does not take effect for wired users who go online through VLANIF interfaces.
* To make the function take effect, it is recommended that the configured delay be greater than the time during which the interface is up.

Example
-------

# In the authentication profile p1, set the user logout delay when the link is faulty to 5 seconds.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name p1
[*HUAWEI-authen-profile-p1] link-down offline delay 5

```