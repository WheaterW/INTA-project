bfd (System view)
=================

bfd (System view)

Function
--------



The **bfd** command enables Bidirectional Forwarding Detection (BFD) globally and displays the global BFD view.

The **undo bfd** command disables BFD globally.



By default, BFD is disabled.


Format
------

**bfd**

**undo bfd**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To use BFD to rapidly detect a link failure, run the bfd command to enable BFD globally.

**Prerequisites**

Before running the **bfd session-name** command, use one of the following commands to create a BFD session:

* bfd bind peer-ip
* bfd bind peer-ip default-ip
* bfd bind peer-ip source-ip auto

**Configuration Impact**

After the bfd command is run, BFD is enabled globally, and BFD-associated configurations are allowed.

**Precautions**

Note the following before the configuration:

* BFD must be enabled globally before BFD-associated configurations are performed.
* You can run the **undo bfd session-name** command to delete a specified BFD session and cancel the BFD session binding.
* When virtual access port extension is enabled, BFD is enabled. When virtual access port extension is disabled, BFD is not disabled together.

Example
-------

# Enable BFD globally.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd]

```

# After enables the re-confirmation function, disabled BFD globally.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] undo bfd
Warning: The BFD process will be deleted. Continue? [Y/N]:Y

```