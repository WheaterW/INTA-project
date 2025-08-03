rsa local-key-pair
==================

rsa local-key-pair

Function
--------



The **rsa local-key-pair create** command generates local RSA host and server key pairs.

The **rsa local-key-pair destroy** command removes all local RSA keys including the host key pair and the server key pair.



By default, no local RSA host or server key pairs are generated.


Format
------

**rsa local-key-pair create**

**rsa local-key-pair destroy**


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

When you run this command, if the RSA key already exists, the system prompts you to confirm whether to replace the original key. The generated key pair is named in the format of Host\_Server and Host. This command is not saved in the configuration file.After running the destroy key-pair command, you need to confirm whether to remove all local RSA keys. This command is a one-time operation command and therefore is not saved in the configuration file.

**Precautions**

* To ensure high security, you are advised to use an RSA key pair of 3072 bits or more.
* You only need to run this command once. After the device is restarted, you do not need to run this command again.
* After you run this command, the system prompts you to enter the length of the RSA key pair to be generated. Currently, the system supports three types of RSA key pairs: 2048 bits, 3072 bits, and 4096 bits. If you press Enter without entering the key pair length, a 3072-bit RSA key pair is generated. If you do not perform any operation, the device does not generate the RSA key pair. You are advised to use an RSA key pair of 3072 bits or more, which is more secure.
* The prerequisite for a successful SSH login is that a local RSA key pair is generated. You can generate a local RSA key pair in either of the following ways:
* Run the **rsa local-key-pair create** command to generate a local RSA key pair.
* The system automatically generates a local RSA key pair.After the local key pair is generated in either mode, you need to run the **save** command to save the configuration file. In this way, the local key pair generated after the system restarts does not change. If the configuration file is not saved, the system generates a new local key pair after the restart. You need to use the new key pair to log in to the device through SSH.

Example
-------

# Remove all local RSA keys on the server.
```
<HUAWEI> system-view
[~HUAWEI] rsa local-key-pair destroy
The name for the keys which will be destroyed is Host.
Confirm to destroy these keys? Please select [Y/N]: Y

```

# Configure a device to generate local host and server key pairs.
```
<HUAWEI> system-view
[~HUAWEI] rsa local-key-pair create
The key name will be:Host
The range of public key size is (2048, 4096). 
NOTE: Key pair generation will take a short while. 
Please input the modulus [default = 3072]:3072

```