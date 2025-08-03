dsa local-key-pair destroy
==========================

dsa local-key-pair destroy

Function
--------



The **dsa local-key-pair destroy** command deletes all local DSA key pairs, including the host key pair and server key pair.



By default, no local DSA keys are created.


Format
------

**dsa local-key-pair destroy**


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

If you no longer need the local DSA key pairs, run the **dsa local-key-pair destroy** command to delete them.

**Configuration Impact**



The **dsa local-key-pair destroy** command deletes the local DSA host key pair, from the files on the device. Exercise caution when you run this command.



**Precautions**

The dsa local-key-pair create command is not saved in the configuration file. It only needs to be run once and takes effect even after the device restarts.


Example
-------

# Delete the local DSA host key pair.
```
<HUAWEI> system-view
[~HUAWEI] dsa local-key-pair destroy
Info: The name of the key which will be destroyed is HUAWEI_Host_DSA.
Warning: These keys will be destroyed. Continue? Please select [Y/N]: Y

```