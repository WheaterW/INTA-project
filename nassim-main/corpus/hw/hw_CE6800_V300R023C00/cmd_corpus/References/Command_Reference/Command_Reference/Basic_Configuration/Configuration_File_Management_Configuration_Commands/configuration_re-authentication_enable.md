configuration re-authentication enable
======================================

configuration re-authentication enable

Function
--------



The **configuration re-authentication enable** command enables secondary authentication for the execution of risky commands.

The **undo configuration re-authentication enable** command disables secondary authentication for risky command execution.



By default, secondary authentication is disabled.


Format
------

**configuration re-authentication enable**

**undo configuration re-authentication enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Some **undo** commands on the device will delete related feature configurations if they are incorrectly executed. As a result, services and user networks are interrupted. To prevent misoperations, you need to perform secondary authentication to protect the system when running these **undo** commands.

**Precautions**

* To prevent some services from being unavailable due to misoperations, you are advised to enable secondary authentication for risky commands.
* Secondary authentication for risky commands takes effect only in the command line view.


Example
-------

# Enable secondary authentication for risky command execution.
```
<HUAWEI> system-view
[~HUAWEI] configuration re-authentication enable

```

# Disable secondary authentication for risky command execution.
```
<HUAWEI> system-view
[~HUAWEI] undo configuration re-authentication enable
Info: This command is a high-risk command. Enter the login password of the current user again.
Enter Password:
[*HUAWEI]

```