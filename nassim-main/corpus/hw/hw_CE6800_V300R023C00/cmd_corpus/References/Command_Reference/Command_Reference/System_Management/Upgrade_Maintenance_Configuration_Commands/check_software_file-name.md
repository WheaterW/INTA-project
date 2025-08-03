check software file-name
========================

check software file-name

Function
--------



The **check software file-name** command enables you to check the integrity of a software package file.



By default, the system checks whether a specified software package is damaged.


Format
------

**check software file-name** *name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specify the name of a software package file. | The value is a string of 4 to 127 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before loading a software package, run the **check software** command to check whether the software package is damaged.

* If the software package is not damaged, the system displays a message indicating that the software package is complete. Otherwise, the system displays a message indicating that the software package is incomplete.
* If the entered software package name does not exist, the system displays a message indicating that the software package does not exist.
* If the format of the entered software package is incorrect (identified format: .cc, .ccx, .cch, .MOD, or .PAT), the system displays a message indicating that the file format cannot be identified.


Example
-------

# Verify the integrity of a software package in an invalid format.
```
<HUAWEI> check software file-name XXXXXXX.zz

```

# Verify the integrity of the software package XXXXXXX.cc.
```
<HUAWEI> check software file-name XXXXXXX.cc

```

# Verify the integrity of the XXXXXXX.PAT patch package.
```
<HUAWEI> check software file-name XXXXXXX.PAT

```