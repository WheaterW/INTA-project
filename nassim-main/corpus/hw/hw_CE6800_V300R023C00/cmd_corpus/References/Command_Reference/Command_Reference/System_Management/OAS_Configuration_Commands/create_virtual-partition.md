create virtual-partition
========================

create virtual-partition

Function
--------



The **create virtual-partition** command creates a virtual partition.




Format
------

**create virtual-partition size** *partition-size* **type** **rootfs** **slot** *slot-id*

**create virtual-partition size** *partition-size* **type** **image**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **type** | Specifies the type of the partition to be created. | - |
| **rootfs** | Creates a virtual partition for the root directory. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **size** *partition-size* | Specifies the size of the virtual partition to be created. | The value is a 32-bit unsigned integer. The value range of the root path partition for application running is 1 to 102400, and the value range of the image storage partition is 1 to 2048. |
| **image** | Creates an image virtual partition. | - |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* If the type rootfs parameter is specified in the command, the device creates the root path partition for storing application running information.
* If type image is specified in the command, the device creates an image storage partition to store the image software package and public key file.
* After a virtual partition is created, the actual available space is less than the specified size because the file system on the virtual partition occupies some space. You can run the display oas virtual-partition command to view the available space.

Example
-------

# Create an image storage partition.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] create virtual-partition size 2048 type image
Warning: The virtual partition will be created. Continue? [Y/N]:y
Info: Operating, please wait for a moment.......done.
Info: The virtual partition is created successfully.

```

# Create the root directory partition for running applications.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] create virtual-partition size 2048 type rootfs slot 1
Warning: The virtual partition will be created. Continue? [Y/N]:y
Info: Operating, please wait for a moment........done.
Info: The virtual partition is created successfully.

```