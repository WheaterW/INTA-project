alias
=====

alias

Function
--------



The **alias** command creates an alias for a command.

The **undo alias** command deletes an alias.



By default, no alias is created.


Format
------

**alias** *alias-string* [ **parameter** { *parameter* } &<1-32> ] **command** *command*

**undo alias** *alias-string*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *alias-string* | Specifies an alias string. | The value is a string of 1 to 63 case-insensitive characters, supporting letters, digits, and hyphens (-). It must start with a letter and cannot contain spaces between characters. |
| **parameter** *parameter* | Specifies a parameter for an alias. | The value is a string of 2 to 63 case-insensitive characters, supporting letters, digits, and hyphens (-). It must start with the $ sign. |
| **command** *command* | Specifies a command for which an alias is to be created. | The value is a string of 1 to 511 characters. If a space exists in the command, the character string of command must be enclosed in double quotation marks ("). An alias can be configured for each command supported by the device. |



Views
-----

Command alias view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The **alias** command can be used in the following scenarios:

* Configure an easy-to-remember string of characters as the alias for a command. Then, you can just enter the alias string when you need to run the command. For example, define the alias for display as show. You can enter the alias show to substitute display.
* Change the order of parameters. For example, after you configure the alias showif parameter $ifnum $iftype command "display interface $iftype $ifnum" command, you can enter showif 1 Eth-Trunk to substitute display interface Eth-Trunk 1.

**Precautions**

* After the alias is defined, the original command line can still be used.
* The **alias** command string must reference all defined parameter fields in sequence, and each parameter can be referenced only once.
* After the parameter field is referenced in the **alias** command character string, the **alias** command character string can contain only parameters (starting with $) and cannot be followed by command keywords. For example, the following configuration is invalid: alias showif parameter $ifnum $iftype command "display interface $iftype iftype $ifnum verbose"
* If cyclic nesting occurs in the alias definition or the nesting level exceeds 16, the alias node is invalid and the character string is not replaced.
* The alias configured using the **alias** command takes effect only after the alias feature is enabled using the **terminal command alias** command.
* If the command character string after alias replacement contains only spaces, the original character string before alias replacement is delivered.


Example
-------

# Create an alias for a command.
```
<HUAWEI> system-view
[~HUAWEI] command alias
[~HUAWEI-cmdalias] alias show command display

```