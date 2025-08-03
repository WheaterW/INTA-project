keychain
========

keychain

Function
--------



Using the **keychain** command, you can create a new set of keychain rules or enter a keychain view.

Using the **undo keychain** command, you can delete the keychain configuration.



By default, no keychain is configured.


Format
------

**keychain** *keychain-name*

**keychain** *keychain-name* **mode** **absolute**

**keychain** *keychain-name* **mode** **periodic** **daily**

**keychain** *keychain-name* **mode** **periodic** **weekly**

**keychain** *keychain-name* **mode** **periodic** **monthly**

**keychain** *keychain-name* **mode** **periodic** **yearly**

**undo keychain** *keychain-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *keychain-name* | Specifies keychain name. All the applications identify the set of keychain rules by keychain name. | The value is a string of 1 to 47 case-insensitive characters, It cannot contain question marks (?). If spaces are used, the string must start and end with double quotation marks (&quot;). |
| **mode** | Specifies the time mode in which the keychain takes effect. | - |
| **absolute** | Specifies that the given keychain is non-periodic. | - |
| **periodic** | Specifies that the given keychain is periodic. | - |
| **daily** | Specifies that the given keychain is day-periodic. | - |
| **weekly** | Specifies that the given keychain is week-periodic. | - |
| **monthly** | Specifies that the given keychain is month-periodic. | - |
| **yearly** | Specifies that the given keychain is year-periodic. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In keychain authentication mode, secure protocol packet transmission is provided by changing the authentication algorithm and key dynamically. This can prevent unauthorized users from obtaining the key, and authentication and encryption algorithms, and reduce the workload of changing the algorithm and key manually.Each keychain consists of multiple key IDs that are valid within different time periods and each key ID is configured with an authentication algorithm. When a key ID becomes valid, the corresponding authentication algorithm is used.There are two keychain validity modes:

* Absolute time range: In this mode, keychains are valid within a certain period and are invalid out of the period.
* Periodic time range: In this mode, keychains are valid periodically. After one period ends, keychains continue to be valid within next period.

**Implementation Procedure**



Specify the validity mode when creating a keychain. The keychain view is displayed when a keychain name is specified.



**Follow-up Procedure**



After a keychain is created, configure the time period within which each key ID is valid. Otherwise, protocol packets cannot be authenticated and encrypted.The time period within which a key ID for packet sending or receiving is valid, and the time mode configured for the key ID must be identical with that configured for the keychain.



**Precautions**



The **keychain keychain-name** command displays only the keychain view. If keychain-name does not exist, the **keychain keychain-name** command cannot be executed. To create a keychain, you must run the **keychain keychain-name mode** { absolute | periodic { daily | weekly | monthly | yearly } } command.




Example
-------

# Configure the keychain huawei and enter keychain view.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute

```