display configuration replace file
==================================

display configuration replace file

Function
--------



The **display configuration replace file** command displays the differences between the replacement configuration and the target configuration.




Format
------

**display configuration replace file**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After configurations are replaced, run the display configuration replace file command to check the differences between the replacement configuration and the target configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display commands that fail to be replaced.
```
<HUAWEI> system-view
[~HUAWEI] display configuration replace file
#
+ interface Tunnel1
  #
+ interface Tunnel2
  #
+ interface a
  #
- interface b

```

**Table 1** Description of the **display configuration replace file** command output
| Item | Description |
| --- | --- |
| + | New configuration.  For each modified configuration, both "-" indicating the deleted configuration and "+" indicating the created configuration are displayed. |
| - | Deleted configuration.  For each modified configuration, both "-" indicating the deleted configuration and "+" indicating the created configuration are displayed. |