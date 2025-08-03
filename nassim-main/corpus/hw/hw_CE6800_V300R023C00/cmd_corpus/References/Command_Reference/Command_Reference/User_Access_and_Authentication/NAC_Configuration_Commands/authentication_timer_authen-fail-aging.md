authentication timer authen-fail-aging
======================================

authentication timer authen-fail-aging

Function
--------



The **authentication timer authen-fail-aging** command configures the aging time for entries of the users who fail to be authenticated.

The **undo authentication timer authen-fail-aging** command restores the default aging time for entries of the users who fail to be authenticated.



By default, the aging time for entries of the users who fail to be authenticated is 23 hours.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication timer authen-fail-aging** *aging-time*

**undo authentication timer authen-fail-aging**


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

After network access policies are configured for users who fail to be authenticated, the device creates entries for these users. If the user still fails to be authenticated when the user aging time expires, the user entry is deleted.The entries of the users who fail to be authenticated share device resources with the entries of the users who are authenticated. If there are excess entries of the users who fail to be authenticated, other users fail to be authenticated. To solve this problem, run the authentication timer authen-fail-aging command to reduce the aging time for entries of the users who fail to be authenticated. In addition, if the time that the users who fail to be authenticated have network access policies should be shortened, you can run this command to decrease the aging time for the user entries.

**Precautions**

This function takes effect only for users who go online after this function is successfully configured. Only wired users support this function.


Example
-------

# In the authentication profile p1, configure the aging time for entries of the users who fail to be authenticated to 3600 seconds.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name p1
[*HUAWEI-authen-profile-p1] authentication timer authen-fail-aging 3600

```