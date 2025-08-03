ecc local-key-pair destroy
==========================

ecc local-key-pair destroy

Function
--------



The **ecc local-key-pair destroy** command deletes the local ECC keys.



By default, no local ECC host key pair exists in the system.


Format
------

**ecc local-key-pair destroy**


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

A local key pair is a prerequisite to a successful SSH login. If you no longer need the local ECC key pairs, run the **ecc local-key-pair destroy** command to delete them.

**Configuration Impact**



The **ecc local-key-pair destroy** command deletes the local ECC host key pair, from the files on the device. Exercise caution when you run this command.



**Precautions**

The **ecc local-key-pair destroy** command is not saved in the configuration file. It only needs to be run once and takes effect even after the device restarts.Do not delete the ECC key file from the device.


Example
-------

# Delete the local ECC host key pair and server key pair.
```
<HUAWEI> system-view
[~HUAWEI] ecc local-key-pair destroy
Info: The name of the key which will be destroyed is HUAWEI_Host_ECC.
Warning: These keys will be destroyed. Continue? Please select [Y/N]:y
Info: Succeeded in destroying the ECC host keys.

```