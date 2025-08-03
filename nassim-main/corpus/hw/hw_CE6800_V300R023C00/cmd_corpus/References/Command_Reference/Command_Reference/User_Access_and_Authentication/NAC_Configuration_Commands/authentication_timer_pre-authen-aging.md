authentication timer pre-authen-aging
=====================================

authentication timer pre-authen-aging

Function
--------



The **authentication timer pre-authen-aging** command configures the aging time for entries of the users who fail to be authenticated.

The **undo authentication timer pre-authen-aging** command restores the default aging time for entries of the users who fail to be authenticated.



By default, the aging time for pre-connection user entries is 23 hours.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication timer pre-authen-aging** *aging-time*

**undo authentication timer pre-authen-aging**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *aging-time* | Specifies the aging time. | The value is an integer that ranges from 0 or 60 to 4294860, in seconds.  The value 0 indicates that the entry does not age. |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a pre-connection is established between the device and a user, the device creates the pre-connection user entry. If the user still fails to be authenticated when the user aging time expires, the user entry is deleted.The pre-connection user entries share device resources with the entries of the users who are authenticated. If there are excess pre-connection user entries, other users fail to be authenticated. To solve this problem, run the authentication timer pre-authen-aging command to reduce the aging time for the pre-connection user entries. In addition, if the time that the pre-connection users have network access policies should be extended, you can run this command to increase the aging time for the pre-connection user entries.

**Precautions**

This function takes effect only for users who go online after this function is successfully configured. Only wired users support this function.


Example
-------

# In the authentication profile p1, configure the aging time for the pre-connection user entries to 3600 seconds.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name p1
[*HUAWEI-authen-profile-p1] authentication timer pre-authen-aging 3600

```