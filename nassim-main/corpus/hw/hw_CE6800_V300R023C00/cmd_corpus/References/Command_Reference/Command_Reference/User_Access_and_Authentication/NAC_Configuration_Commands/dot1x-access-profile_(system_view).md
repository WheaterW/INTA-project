dot1x-access-profile (system view)
==================================

dot1x-access-profile (system view)

Function
--------



The **dot1x-access-profile** command creates an 802.1X access profile and displays the 802.1X access profile view.

The **undo dot1x-access-profile** command deletes an 802.1X access profile.



By default, the device has a built-in 802.1X access profile named dot1x\_access\_profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x-access-profile name** *access-profile-name*

**undo dot1x-access-profile name** *access-profile-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *access-profile-name* | Specifies the name of an 802.1X access profile. | The value is a string of 1-31 case-sensitive characters, which cannot be configured to - and --. It cannot contain spaces and the following symbols: / \ : \* ? " < > | @ ' %. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device uses 802.1X access profiles to uniformly manage all 802.1X users access configurations. To perform 802.1X authentication for the users in the interface, bind the authentication profile applied to the interface to an 802.1X access profile.

**Follow-up Procedure**

Run the **dot1x-access-profile** command in the authentication profile view to bind the authentication profile to an 802.1X access profile.

**Precautions**

Before deleting an 802.1X access profile, ensure that this profile is not bound to any authentication profile.


Example
-------

# Create the 802.1X access profile named dot1x\_access\_profile1.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name dot1x_access_profile1

```