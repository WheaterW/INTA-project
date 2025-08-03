display configuration candidate (All views except the user view)
================================================================

display configuration candidate (All views except the user view)

Function
--------



The **display configuration candidate changes** command displays the difference between the candidate configuration and current running configuration.

The **display configuration candidate merge** command displays all configurations, including uncommitted and committed ones.




Format
------

**display configuration candidate merge**

**display configuration candidate changes**


Parameters
----------

None

Views
-----

All views except the user view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before committing configurations, you can run the **display configuration candidate changes** command to view the difference between the modified configuration and the current running configuration.The **display configuration candidate changes** command displays the difference between the uncommitted configuration in the candidate database and the running configuration in the running database. If any difference exists, the command output is as follows:

* Commands that exist in the candidate configuration rather than the current running configuration are prefixed with "+".
* Commands that exist in the current running configuration rather than the candidate configuration are prefixed with "-".
* If a command in the current running configuration is modified in the candidate configuration, two commands that are prefixed with "-" and "+", respectively, are displayed in sequence.To check whether the configuration to be committed is correct and whether it conflicts with the existing configurations, you can run the **display configuration candidate merge** command.

**Precautions**



This command applies only to the two-phase validation mode.Before you run the **commit** command to commit a configuration, a configuration conflict occurs if the current running configuration is changed. In this case, run the **refresh configuration candidate** command to resolve the configuration conflict, and then run the **display configuration candidate changes** command to view the configuration difference.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all configurations, including uncommitted and committed ones.
```
<HUAWEI> system-view
[~HUAWEI] sftp server enable
[*HUAWEI] display configuration candidate merge
#
sysname HUAWEI
#
interface 100GE1/0/1
#
sftp server enable
#
user-interface con 0
set authentication password cipher $1d$a3XtEok2LJ$;&(SUt9vy0`JlWP6-z0<=01'5B+8NT8n9'<PL3oM$
history-command max-size 30
user-interface vty 0 4

```

# Display the difference between the candidate configuration and current running configuration.
```
<HUAWEI> system-view
[~HUAWEI] display configuration candidate changes
Building configuration
  #
  interface Tunnel1
- mtu 1400
+  mtu 1300
  #
+ interface Tunnel3
  #

```

**Table 1** Description of the **display configuration candidate (All views except the user view)** command output
| Item | Description |
| --- | --- |
| Building configuration | Generation of differential configuration. |
| - | Deleted configuration. |
| + | Added configuration. |