load security weak-password-dictionary
======================================

load security weak-password-dictionary

Function
--------



The **load security weak-password-dictionary** command loads a weak password dictionary.




Format
------

**load security weak-password-dictionary** *filePath*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *filePath* | Specifies the name of the weak password dictionary file. | The value is a string of case-sensitive characters. The value can contain uppercase letters, lowercase letters, digits, and special characters, but cannot contain spaces. The value is a string of 1 to 255 characters (including the suffix).  The following special characters are not allowed: ~? \* /\: "| < > []; & $`! The first and last characters cannot be periods (.).  The file name extension must be .txt.  The value can be a path. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* A device supports the pre-configuration of a weak password dictionary. A user-configured password cannot be the same as any password in the weak password dictionary (completely match). A weak password dictionary can be checked only when a new user is added or the user password is changed. Weak password dictionary check is not supported in upgrade scenarios.
* A weak password dictionary is stored in .txt format. Each weak password is stored in a line. The dictionary file can only be in the .txt format.

Example
-------

# Load a weak password dictionary file.
```
<HUAWEI> load security weak-password-dictionary wkpass.txt

```