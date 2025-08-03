cd (User view)
==============

cd (User view)

Function
--------



The **cd** command changes the current working directory.



By default, the current working directory is the flash directory.


Format
------

**cd** *directory*

**cd**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *directory* | Specifies the remote directory name. | The value is a character string in the format of [ <drive> ][ <path> ]. An absolute <path> name is a string of 1 to 255 characters. A relative <path> name is a string of 1 to 128 characters. Up to 8 levels of directories are supported.  An absolute <path> is in the format of <drive> [ <path> ], and a relative <path> is in the format of <path> . That is, a relative <path> is the root <path> of the current working <path> . |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **cd** command to change the current working directory.

**Configuration Impact**

The **cd** command changes the working directory of only the current user but not other users because each user uses a separate working directory.


Example
-------

# Change the current working directory to the directory named directorA on the Router.
```
<HUAWEI> pwd
flash:/
<HUAWEI> cd logfile/
<HUAWEI> pwd
flash:/logfile/

```