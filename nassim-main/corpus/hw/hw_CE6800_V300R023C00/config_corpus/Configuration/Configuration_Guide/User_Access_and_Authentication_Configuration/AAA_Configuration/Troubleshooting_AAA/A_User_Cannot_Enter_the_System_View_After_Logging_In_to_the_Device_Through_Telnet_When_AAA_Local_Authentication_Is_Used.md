A User Cannot Enter the System View After Logging In to the Device Through Telnet When AAA Local Authentication Is Used
=======================================================================================================================

A User Cannot Enter the System View After Logging In to the Device Through Telnet When AAA Local Authentication Is Used

#### Fault Symptom

A user successfully logs in to the device through Telnet, but cannot run the [**system-view**](cmdqueryname=system-view) command to enter the system view or run other commands at the configuration level.


#### Possible Causes

* The user is not authorized to run commands at the configuration level.
* Users are only authorized to run commands at their privilege level or below. For example, a user at privilege level 2 can run only the commands at privilege levels 0, 1, and 2.
* If the user cannot run commands at the configuration level (privilege level 2), the user privilege level may be lower than privilege level 2. There is a possibility that no user privilege level is specified for the user, so the user privilege level is the default one.

#### Troubleshooting Procedure

The administrator logs in to the device through the console port, and runs the [**local-user**](cmdqueryname=local-user) *user-name* **privilege level** *level* command to configure the user privilege level.

```
<HUAWEI> system-view
[HUAWEI] aaa
[HUAWEI-aaa] local-user user1-huawei privilege level 3  //Set the user privilege level of user1-huawei to 3.
```