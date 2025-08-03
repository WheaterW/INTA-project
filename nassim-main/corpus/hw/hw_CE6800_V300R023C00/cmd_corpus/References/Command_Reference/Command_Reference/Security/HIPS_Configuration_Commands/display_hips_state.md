display hips state
==================

display hips state

Function
--------



The **display hips state** command displays the status of each HIPS detection module.




Format
------

**display hips state**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The policy file determines whether each detection module is enabled. By default, all detection modules are enabled.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of each HIPS detection module.
```
<HUAWEI> display hips state
---------------------------------------------------------------------------     
  Name                             State                                        
---------------------------------------------------------------------------     
  file-privilege-escalation        on                                           
  abnormal-shell                   on                                           
  rootkit-attack                   on                                           
  key-file-tampering               on                                           
  unauthorized-root-user           on                                           
  abnormal-shell-invoke            on                                           
---------------------------------------------------------------------------

```

**Table 1** Description of the **display hips state** command output
| Item | Description |
| --- | --- |
| Name | Detection module:   * file-privilege-escalation: file privilege escalation detection module. * abnormal-shell: abnormal shell detection module. * rootkit-attack: rootkit detection module. * key-file-tampering: key file tampering detection module. * unauthorized-root-user: unauthorized root user detection module. * abnormal-shell-invoke: abnormal shell command invoking detection module. |
| State | Status of a detection module. The value is on or off. |