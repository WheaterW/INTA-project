authorization-cmd no-response-policy
====================================

authorization-cmd no-response-policy

Function
--------

The **authorization-cmd no-response-policy** command configures a policy used when the command line-based authorization mode.

The **undo authorization-cmd no-response-policy** command restores the default setting.

By default, the policy is used to keep the user online though the authorization fails.



Format
------

**authorization-cmd no-response-policy** { **online** | **offline** [ **max-times** *max-times-value* ] }

**undo authorization-cmd no-response-policy**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **online** | Indicates that the user is online when the command line-based authorization fails. | - |
| **offline** | Indicates that the user is offline when the command line-based authorization fails. | - |
| **max-times** *max-times-value* | Specifies the number of times of failed command line-based authorization. | The value is an integer that ranges from 1 to 10. The default value is 5. |




Views
-----

Authorization scheme view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

This command is used only when the authorization fails because the HWTACACS server fails or the local user is not configured. The following cases cannot trigger using the policy:

* When the HWTACACS server works normally, the input command fails to pass the authorization.
* When the HWTACACS server fails, the command-line based authorization mode is changed to the local authorization mode. The authorization remains failed because the input command level is higher than that configured on the local end.


Example
-------

# Disconnect the user after three times of failed authorization.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authorization-scheme scheme1
[*HUAWEI-aaa-author-scheme1] authorization-cmd no-response-policy offline max-times 3

```