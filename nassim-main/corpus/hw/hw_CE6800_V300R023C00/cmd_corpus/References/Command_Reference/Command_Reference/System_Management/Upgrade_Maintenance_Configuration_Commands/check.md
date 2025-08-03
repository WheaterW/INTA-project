check
=====

check

Function
--------



The **check** command checks the integrity of a patch package.




Format
------

**check patch** { *PkgName* | **startup** }

**check module** { *PkgName* | **startup** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *PkgName* | Specifies the patch file to be checked for integrity.  The value of this parameter can consist of the path where the patch file is stored and the name of the patch file, or consist of only the name of the patch file. | The value is a string of 5 to 127 case-sensitive characters without spaces. The length of the patch file storage path ranges from 0 to 64 characters, and the length of the patch file name ranges from 5 to 63 characters. |
| **startup** | Checks the integrity of the patch package used for the next startup. | - |
| **module** | Checks the integrity of the module package. | - |
| **patch** | Checks the integrity of the patch package. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before you load a module file, run the **check module** command to check whether the file is damaged. If the module file is not damaged, a message is displayed indicating that the file is complete. Otherwise, a message is displayed indicating that the file is incomplete. If the specified module file name does not exist, a message is displayed indicating that the file does not exist. If you specify the startup parameter without setting any next-startup module file, a message is displayed indicating that the required module file does not exist. In this case, run the install-module [ next-startup ] command to specify the next-startup module file.

Before you load a patch package, run the **check patch** command to check whether the patch package is damaged. If the patch package is not damaged, a message is displayed indicating that the patch is complete. Otherwise, a message is displayed indicating that the patch is incomplete. If the specified patch package name does not exist, a message is displayed indicating that the patch file does not exist. If you specify the startup parameter without setting any next-startup patch file, a message is displayed indicating that the required patch file does not exist. In this case, run the **startup patch all** command to specify the next-startup module package.


Example
-------

# Check module package integrity when no module package exists.
```
<HUAWEI> check module startup
Error: No module exists.

```

# Check the integrity of the patch package used for the next startup.
```
<HUAWEI> check patch startup
Warning: Patch package verification consumes system CPU resources. Continue? [Y/N]: Y

```

# Check the integrity of the patch package named xxxx.PAT.
```
<HUAWEI> check patch xxxx.PAT
Warning: Patch package verification consumes system CPU resources. Continue?[Y/N]: Y

```

# Check the integrity of a specified common module package.
```
<HUAWEI> check module TEST.MOD
Warning: Package verification consumes system CPU resources. Continue? [Y/N]: Y
Info: Prepare to check file flash:/$_install_mod/TEST.MOD, please waitâ¦done.
Info: The module is complete.

```

# Check the integrity of the next-startup common module package.
```
<HUAWEI> check module startup
Warning: Package verification consumes system CPU resources. Continue? [Y/N]: Y
Info: Prepare to check file flash:/$_install_mod/TEST.MOD, please waitâ¦done.
Info: The module is complete.

```

# Check the integrity of a specified module package with digital signatures.
```
<HUAWEI> check module TEST.MOD
Warning: Package verification consumes system CPU resources. Continue? [Y/N]: Y
Info: Prepare to check file flash:/$_install_mod/TEST.MOD, please waitâ¦done. 
Info: Digital signature verification of the system module succeeded.

```

# Check the integrity of the next-startup module package with digital signatures.
```
<HUAWEI> check module startup
Warning: Package verification consumes system CPU resources. Continue? [Y/N]: Y
Info: Prepare to check file flash:/$_install_mod/TEST.MOD, please waitâ¦done.
Info: Digital signature verification of the system module succeeded.

```