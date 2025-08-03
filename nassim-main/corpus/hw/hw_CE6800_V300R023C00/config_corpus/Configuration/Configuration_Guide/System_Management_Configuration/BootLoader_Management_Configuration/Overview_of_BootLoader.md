Overview of BootLoader
======================

Overview of BootLoader

#### Definition

The BootLoader loads and upgrades system software, and commissions and checks the system after power-on.

The BootLoader menu contains a series of operational menu options provided by uBoot, the underlying control software. The uBoot program mainly provides two functions: system software loading and menu control. During device startup, start the uBoot program and load the system software through it. The menu control function is presented by the BootLoader menu to facilitate the loading of system software.


#### Purpose

In most cases, you do not need to use the BootLoader menu if the device can be started normally. However, you can use the BootLoader menu to perform the following operations:

* Restore or upgrade the system when it stops responding and the CLI cannot be displayed.