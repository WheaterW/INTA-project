Overview of MD-CLI
==================

Overview of MD-CLI

#### Definition

The Model-Driven Command Line Interface (MD-CLI) is a YANG-based CLI.


#### Purpose

The CLI is a common tool for users to interact with devices. It is widely used in scenarios such as new service provisioning and routine O&M. After the system displays the command line prompt for a login user, it indicates that the user has entered the CLI. The system provides a series of commands for users to interact with the device. The CLI parses the commands entered by users to allow device configuration and management. Currently, devices support the following two types of CLIs:

* Traditional CLI
* MD-CLI

The traditional CLI mode is used by default.

The MD-CLI provides a method for users to access YANG model nodes through directories. After learning the node hierarchy in the YANG model, users can automatically deduce the corresponding MD-CLI operation command lines, and vice versa. The MD-CLI reduces the cost of learning multiple operational interfaces of the device and simplifies the logic of command line script programming through the homogeneous structure of the CLI and YANG model.

Compared with the traditional CLI, the MD-CLI has the advantages shown in [Table 1](#EN-US_TOPIC_0000001563994421__table139618490455).

**Table 1** Comparison between MD-CLI and traditional CLI
| Difference | Traditional CLI | MD-CLI |
| --- | --- | --- |
| Configuration logic | When executing a command, the traditional CLI checks the dependencies between command operation objects. As such, users need to strictly follow the sequence of dependencies between commands during configuration. | MD-CLI dependency verification is performed in the commit phase, instead of in the configuration phase. Users only need to ensure that the configuration dependencies meet requirements when committing configurations. During the editing phase/process, users do not need to strictly comply with the dependency logic between services. |
| Objects | The traditional CLI is mainly used for human-machine interaction. The system provides a series of commands for users to interact with the device. The CLI parses the commands entered by users to allow device configuration and management. The traditional CLI focuses on human readability (for example, table output), but such output cannot be easily parsed by machines. | The MD-CLI is a YANG-based CLI that is oriented to machine-machine and human-machine interaction. The output of the MD-CLI is in JSON format and complies with the definition and related standards of YANG, facilitating parsing and processing of machines. |
| Learning costs | The traditional CLI contains a large number of commands, each of which has its own function. It is costly to learn and understand the functions of all commands. | The MD-CLI has only a few basic operation commands. Most command elements are generated based on the nodes defined in a YANG model. After learning the structure of the YANG model, users can deduce the MD-CLI commands without learning the command line manual, reducing learning costs. |


![](../public_sys-resources/note_3.0-en-us.png) 

This document is written according to device information obtained under lab conditions and therefore may not cover all scenarios. Due to factors such as version upgrades and differences in device models, the content provided in this document may differ from the information on user device interfaces. Such information takes precedence over the content provided by this document.