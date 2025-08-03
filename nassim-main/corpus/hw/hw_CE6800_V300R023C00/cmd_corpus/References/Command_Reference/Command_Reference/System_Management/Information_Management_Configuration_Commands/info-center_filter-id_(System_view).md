info-center filter-id (System view)
===================================

info-center filter-id (System view)

Function
--------



The **info-center filter-id** command enables the filtering of specified logs or traps.

The **undo info-center filter-id** command disables the filtering of specified logs or traps.



Logs and traps are not filtered out by default.


Format
------

**info-center filter-id** { *filter-id* | **bymodule-alias** *modname* *alias* }

**undo info-center filter-id** { *filter-id* | **bymodule-alias** *modname* *alias* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *filter-id* | Specifies the ID of logs or traps to be filtered out. This parameter indicates the ID of a log or trap. If this parameter fails to be configured, the log or trap specified by this ID does not exist. | The value is an integer ranging from 0 to 4294967295. |
| **bymodule-alias** *modname* *alias* | Specifies the module name or alias name of logs or traps to be filtered out. You are advised to use the module name and alias for filtering. The modname value can be obtained by running the display configuration data running table-data ModuleInfo command in the diagnostic view. The alias value can be displayed after you enter a module name. | * modname: The value is a string of 1 to 255 case-insensitive characters, spaces not supported. * alias: The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If logs or traps with the same ID are repeatedly generated, other logs or traps cannot be recorded. To filter out logs or traps of the specified ID, run the info-center filter-id command. Then logs or traps of the specified ID will not be generated and output to a destination.

**Configuration Impact**



Information about the filtered log or trap will be lost.



**Precautions**

* To add multiple IDs at a time, use a space to separate IDs. The result of each ID is displayed.
* The system prompts a message when the same ID or alias name is specified repeatedly.
* If the ID of a log or trap is not registered or the alias name does not exist, the system displays a message indicating that the log or trap is failed to be filtered out.
* When 50 log IDs have been specified in this command, adding more log IDs is prohibited, and a message is displayed, indicating that the filtering list is full. In this case, you must delete previous IDs before adding new ones.


Example
-------

# Filter out logs or traps based on a module name and alias name.
```
<HUAWEI> system-view
[~HUAWEI] info-center filter-id bymodule-alias snmp snmp_reset

```

# Filter out the log with the ID of 177209348.
```
<HUAWEI> system-view
[~HUAWEI] info-center filter-id 177209348

```