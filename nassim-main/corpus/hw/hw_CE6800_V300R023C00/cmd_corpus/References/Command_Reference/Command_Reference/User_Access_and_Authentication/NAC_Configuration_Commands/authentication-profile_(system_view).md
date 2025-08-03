authentication-profile (system view)
====================================

authentication-profile (system view)

Function
--------



The **authentication-profile** command creates an authentication profile and displays the authentication profile view.

The **undo authentication-profile** command deletes the authentication profile.



By default, the device has two built-in authentication profiles: default\_authen\_profile and dot1x\_authen\_profile.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication-profile name** *authentication-string*

**undo authentication-profile name** *authentication-string*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *authentication-string* | Specifies the name of an authentication profile. | The value is a string of 1-31 case-sensitive characters, which cannot be configured to - and --. It cannot contain spaces and the following symbols: / \ : \* ? " < > | @ ' %. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NAC can implement access control on users. The device uses authentication profiles to uniformly manage NAC configuration so that users can easily configure NAC functions. The parameters (for example, the bound access profile and authentication type) in the authentication profile can be configured to provide various access control modes for different users.

**Follow-up Procedure**



Configuring an authentication profile: Configure an access profile, and authorization information in the authentication profile.Applying an authentication profile: Run the authentication-profile (interface view) command to apply the authentication profile to the interface.



**Precautions**



The built-in authentication profile default\_authen\_profile and the compatibility profile converted after an upgrade are not counted in the configuration specification. The built-in authentication profiles default\_authen\_profile and dot1x\_authen\_profile can be modified and applied, but cannot be deleted.Before deleting an authentication profile, ensure that the authentication profile is not bound to any interface. You can run the **display authentication-profile configuration** command to check whether the authentication profile is bound to an interface.




Example
-------

# Create the authentication profile default\_authen\_profile.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name default_authen_profile

```