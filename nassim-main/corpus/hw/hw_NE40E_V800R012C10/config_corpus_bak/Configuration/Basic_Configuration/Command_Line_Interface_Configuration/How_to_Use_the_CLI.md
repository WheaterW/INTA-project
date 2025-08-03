How to Use the CLI
==================

You can use the CLI to configure and process the command view, command edit function, command template, displayed information, and error information.

#### Usage Scenario

Before using the CLI to configure services, you must understand basic CLI operations.


#### Pre-configuration Tasks

Before using the CLI, complete the following tasks:

* Install the Router and power it on.
* Log in to the Router through a PC.


[Entering a Command View](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0009.html)

The CLI provides multiple command views. All commands are registered in one or more command views. In general, you can run a command only after entering its view.

[Editing a Command](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0010.html)

The command editing function enables you to edit a command or obtain help using certain keys.

[Regular Expression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0043.html)



[Verifying the Command Line Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0012.html)

After completing basic configuration, run display commands to verify the configuration.

[Checking the Diagnostic Information](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0030.html)

If a fault occurs in the system and the module that causes the fault cannot be identified, run the **display diagnostic-information** command to collect diagnostic information for fault locating.

[Command Display Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0013.html)

All commands have the same display feature. You can flexibly specify a display mode as required.

[Error Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0014.html)

If an entered command passes the validation check, the command is executed correctly. If an entered command does not pass the validation check, the system displays an error message.

[Configuring an Alias for a Command](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0033.html)

To facilitate operations, you can use the command alias function to configure a character string as an alias for a command.

[Intelligent Rollback](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0038.html)

The CLI supports the intelligent rollback function. That is, in the current view, you can run commands in other views.

[Enabling Secondary Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cli_cfg_0041.html)

Secondary authentication prevents service interruptions caused by misoperations.