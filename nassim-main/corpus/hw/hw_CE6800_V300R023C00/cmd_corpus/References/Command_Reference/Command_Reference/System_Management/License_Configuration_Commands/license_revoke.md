license revoke
==============

license revoke

Function
--------



The **license revoke** command revokes a license file on a device.




Format
------

**license revoke**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

A license is a certificate file. You can apply for, update, and activate a license file to obtain corresponding permission.If new devices are deployed, you can purchase new licenses as required to enable license-controlled features and functions on the devices. This reduces purchase costs. If the capacities of the existing devices are expanded, you can apply for new licenses to support larger capacities and support existing functions.Generally, you need to update the license file in the following scenarios to ensure the performance of the device:

* New features are added.
* The original performance is optimized.
* Issues in the current version are resolved.

Before updating the license file, run the **license revoke** command to revoke the original license file on the device. A revocation code is returned. The revocation code indicates that the license key is invalid and a new license file can be applied for.A license revocation code is a character string generated after a license file becomes invalid. You can determine that a license file is invalid based on the corresponding revocation code.

**Precautions**

* When the existing license file that has been activated is about to expire, apply for and activate a new license file or upgrade the existing license file. Otherwise, the license file will become ineffective when the validity period expires. As a result, functional modules are disabled, which may interrupt services. Therefore, apply for a new license file and activate it before it expires.
* After the **license revoke** command is run, the services associated with the license do not expire immediately. Instead, the system enters a 60-day grace period. You need to apply for and activate a new license as soon as possible.
* If a license is in the trial or default state, the license cannot be revoked.

Example
-------

# Revoke a license file.
```
<HUAWEI> license revoke
Warning: The license will enter the Trial state and will not be activated again. Continue? [Y/N]:y,
Info: Succeeded in revoking the license. The revoke ticket is xxxx.

```