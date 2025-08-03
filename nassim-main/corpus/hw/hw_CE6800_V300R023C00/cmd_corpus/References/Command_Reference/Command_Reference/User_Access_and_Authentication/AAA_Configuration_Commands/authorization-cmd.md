authorization-cmd
=================

authorization-cmd

Function
--------

The **authorization-cmd** command configures command-specific authorization for an administrator of a specific level. After command-specific authorization is enabled and an administrator of a specific level logs in to the device, the commands that the administrator enters can be executed only after being authorized by the HWTACACS server.

The **undo authorization-cmd** command disables command-specific authorization for an administrator of a specific level.

By default, the command-specific authorization is disabled. That is, an administrator of any level can execute only commands of or below its level after logging in to the device.



Format
------

**authorization-cmd** [ *privilege-level* ] { **hwtacacs** | **local** } \* [ **none** ]

**undo authorization-cmd** [ *privilege-level* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *privilege-level* | Specified the administrator level. | The value is an integer that ranges from 0 to 3. |
| **hwtacacs** | Indicates HWTACACS authorization. | - |
| **local** | Indicates local authorization. | - |
| **none** | Indicates that command line authorization is directly performed for a user if the HWTACACS server does not respond to the authorization request of the user. | - |




Views
-----

Authorization scheme view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After being authorized, the users at a certain level can run the commands of the same or lower levels. Command line authorization can be configured to implement minimum user rights control. When command line authorization is enabled, each command entered by users can be executed only after being authorized. After command line authorization is enabled for users at a certain level, the commands run by the users at that level must be authorized by an HWTACACS server.

**Precautions**

* To ensure device or network security, you are not advised to set the command authorization mode to none authorization.
* You are advised to configure the local authorization mode as the backup of the HWTACACS authorization mode. In this manner, when the HWTACACS server is faulty and does not respond to the authorization request, the command authorization mode is switched to the local authorization mode.
* After the **authorization-cmd** command is run, command authorization does not take effect immediately. Command authorization takes effect only after the command authorization scheme is correctly applied to the domain.
* This command does not take effect on the MD-CLI.



Example
-------

# Configure command line authorization administrators at level 2.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authorization-scheme scheme1
[*HUAWEI-aaa-author-scheme1] authorization-cmd 2 hwtacacs

```