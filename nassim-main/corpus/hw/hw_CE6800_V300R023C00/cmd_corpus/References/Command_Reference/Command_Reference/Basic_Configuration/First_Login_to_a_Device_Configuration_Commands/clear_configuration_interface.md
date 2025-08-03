clear configuration interface
=============================

clear configuration interface

Function
--------



The **clear configuration interface** command deletes configurations on an interface at one time.




Format
------

**clear configuration interface** { *interface-type* *interface-number* | *interface-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Deletes configurations on a specified type interface. | - |
| *interface-number* | Deletes configurations on a specified number interface. | - |
| *interface-name* | Deletes configurations on a specified name interface. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To configure an interface on a device for other use, original configurations on the interface need to be deleted one by one. If the interface has a large number of configurations, deleting these configurations one-by-one takes a long time and increases the maintenance workload. To reduce the maintenance workload and simplify the deletion operation, you can use this command to perform one-touch configuration clearance on an interface.



**Configuration Impact**

* After you run this command, the system prompts you whether to clear the configuration on the interface. If you enter y, all configurations on the specified interface are cleared and the default configurations are restored.
* You can run this command to clear the configuration on an interface or restore the default configuration in one-click mode. This is similar to running the **undo** commands in batches on interfaces. If an **undo** command fails to be executed on an interface, the corresponding configuration on the interface is not deleted.
* This command is used to clear the configuration on an interface in one-click mode and restore the default configuration. The configuration takes effect immediately after this command is executed. Therefore, exercise caution when running this command.


Example
-------

# Delete configurations on 100GE 1/0/1 at one time.
```
<HUAWEI> system-view
[~HUAWEI] clear configuration interface 100GE 1/0/1
Warning: All running configurations of the interface will be cleared immediately. Continue? [Y/N]:y

```