display paf
===========

display paf

Function
--------



The **display paf** command displays information about a PAF file in the system.




Format
------

**display paf**

**display paf verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Detailed information about PAF(Product Adaptive File). | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

A PAF file effectively controls product features or resources to be used. To view information about all the specifications configured in the PAF file, run the display paf command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all information in the PAF file.
```
<HUAWEI> display paf
----------------------------------------------------------------------------------------------------------------------
PafName                                                             PafValue             Description    
----------------------------------------------------------------------------------------------------------------------
SPEC_FUNC_DRIVER_PRODUCT_TYPE                                       50                   The default product type value              
----------------------------------------------------------------------------------------------------------------------

```

# Display details about the PAF file.
```
<HUAWEI> display paf verbose

SPEC_MAX_VTY_NUM
Value        : 21
Default value: 21
Min value    : 0
Max value    : 32
Description  : Max number of VTY supported

```

**Table 1** Description of the **display paf** command output
| Item | Description |
| --- | --- |
| PafName | Name of a specification item in the PAF file. |
| PafValue | Value of a specification item in the PAF file, for example:  SPEC\_MAX\_VTY\_NUM: maximum number of VTY access users, which is 21 by default. |
| Description | Definition of a specification item in the PAF file. |
| Value | Value of a specification item in the PAF file, for example:  SPEC\_MAX\_VTY\_NUM: maximum number of VTY access users, which is 21 by default. |
| Default value | Default value of a specification item in the PAF file. |
| Min value | Minimum value of a specification item in the PAF file. |
| Max value | Maximum value of a specification item in the PAF file. |