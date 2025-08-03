environment
===========

environment

Function
--------



The **environment** command configures an environment variable.

The **undo environment** command deletes a configured environment variable.



By default, no environment variable is configured.


Format
------

**environment** *env-name* *env-value*

**undo environment** *env-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *env-name* | Specifies the name of an environment variable. | The value is a string of 1 to 31 case-sensitive characters. The string can contain only letters, digits, and underscores (\_) and must start with letters. |
| *env-value* | Specifies the value of an environment variable. | The value is a string of 1 to 256 case-sensitive characters, spaces not supported.  When you enter a string with double quotes at both ends, you can enter spaces in the string. |



Views
-----

OPS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The OPS supports the following environment variables:

* System environment variables: environment variables that are automatically generated during system running.
* User environment variables: environment variables that are configured using the **environment** command.Intermediate data generated during Python script running is lost after the Python is shut down. You can run the **environment** command to configure the Python script's running variable as an environment variable so that data is saved or used by other users.

Example
-------

# Configure an environment variable named absolute and set its value to aaadfdf.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] environment absolute aaadfdf

```