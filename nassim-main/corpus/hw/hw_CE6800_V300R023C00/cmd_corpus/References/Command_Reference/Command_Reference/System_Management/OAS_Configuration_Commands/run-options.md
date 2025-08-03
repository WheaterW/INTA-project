run-options
===========

run-options

Function
--------



The **run-options** command configures the run option of an application.

The **undo run-options** command restores the default run option of an application.



By default, the run option information is specified in the configuration file during application installation.


Format
------

**run-options** *options*

**undo run-options**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *options* | Specifies the run option of an application. | The value is a string of 1 to 255 case-sensitive characters without spaces. |



Views
-----

OAS application view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

For details about how to use the running options, see the help document on the Docker official website.

* The --blkio-weight option is used to set the block I/O (relative weight). The value ranges from 10 to 1000. If the value is set to 0, this function is disabled. The default value is 0.
* The --cap-add option is used to add the Linux capability set.
* The --cap-drop option is used to delete the Linux capability set.
* The --cpu-shares option is used to set the number of shared CPUs (relative weight).
* The --cpus option is used to set the number of CPUs.
* The --env option is used to set environment variables.
* The --env-file option is used to set the environment variable file.
* The --memory option is used to set the memory limit.
* The --oom-kill-disable option is used to disable the OOM Killer function.
* The --restart option is used to set the restart policy when the container exits. The options are no (the container does not restart when it exits), on-failure (the container restarts when it exits abnormally), always (the container always restarts when it exits), and unless-stopped (Containers that are stopped before the Docker daemon process is started are not restarted. Other containers are always restarted when they exit.)
* The --business-ip address option is used to specify the IP address of the service interface.
* The --manage-ip address option is used to specify the IP address of the management interface.
* The --port-range lowPort-highPort option is used to specify the range of ports to be bound.-The --volume-size option is used to specify the size of the container volume.
* The --volume-mount-path option is used to specify the container path to which the storage volume is mounted.
* The --cpuset-cpus option is used to specify the number of the CPU that can be executed (for example, 0-3, 0, or 1).
* The --volume-type option is used to specify the application storage volume type. Only internal and external are supported.

**Precautions**

* All configurations modified during application startup take effect upon the next startup. You can also manually restart the application for the modification to take effect.
* The storage space specified by volume-size uses the space of the rootfs virtual partition. If the allocated space is too large, it may conflict with the application running data, causing application service exceptions. You are advised to reserve at least 25% of the rootfs virtual partition space.

Example
-------

# Configure application running options.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] application app1
[*HUAWEI-oas-app1] run-options "--blkio-weight 16"
[*HUAWEI-oas-app1] run-options "--cpus 3"

```

# Restore the default running option of the application.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] application app1
[*HUAWEI-oas-app1] undo run-options
Warning: Run-options will be restored to its default settings. Continue? [Y/N]:y

```