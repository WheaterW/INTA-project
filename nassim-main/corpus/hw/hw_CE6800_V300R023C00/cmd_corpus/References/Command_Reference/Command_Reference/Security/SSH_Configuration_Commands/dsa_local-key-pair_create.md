dsa local-key-pair create
=========================

dsa local-key-pair create

Function
--------



The **dsa local-key-pair create** command generates the local DSA host key pair and the server key pair.



By default, no local DSA host key pair or server key pair is set.


Format
------

**dsa local-key-pair create**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dsa** | Displays information about a DSA key pair. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

A local key pair is a prerequisite for a successful SSH login. Digital Signature Algorithm (DSA) is an asymmetric encryption algorithm. DSA key is used in SSH connection similar to dsa algorithm for SSH authentication and DSA public key authentication of user. When the dsa local-key-pair create command is used, if the DSA key exists, the system prompts the user to confirm whether to change the original key or not. The generated DSA host key pair is named in the format of device name\_Host\_DSA, such as HUAWEI\_Host\_DSA.

**Precautions**

* The dsa local-key-pair create command is not saved in the configuration file. It only needs to be run once and takes effect even after the device restarts.
* Do not delete the DSA key file from the device.
* If no local key pair is configured when you log in to the device through SSH for the first time, the system automatically generates a local key pair. To ensure that this local key pair is not changed after the system restarts, run the **save** command to save the configuration file. Otherwise, the system generates a new local key pair after it restarts. You need to use the new local key pair to log in to the device through SSH.

Example
-------

# Generate a local DSA host key pair.
```
<HUAWEI> system-view
[~HUAWEI] dsa local-key-pair create
Info: The key name will be: HUAWEI_Host_DSA
Info: The key modulus can be any one of the following : 2048.
Info: Key pair generation will take a short while.
Info: Generating keys...
Info: Succeeded in creating the DSA host keys.

```