Managing VSs by a PS Administrator
==================================

A Physical System (PS) administrator has the authority to manage Virtual Systems (VSs), including configuring VSs, allocating resources to VSs, and configuring services on VSs.

#### Usage Scenario

To fully utilize hardware resources and share board resources, a PS can be divided into multiple VSs. Each VS can bear a new type of service independently.


#### Pre-configuration Tasks

Before configuring VSs, complete the following tasks:

* Install the PS and power it on properly.
* Ensure that the PS administrator has the authority to create VSs.


[Creating a VS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vs_cfg_0004.html)

A Physical System (PS) administrator can create Virtual Systems (VSs) on the PS, but cannot create, or delete the Admin-VS. The Admin-VS is the default VS on a PS and manages the entire PS. The Admin-VS is automatically created when a PS is being started. All the unassigned resources on a PS belong to the Admin-VS by default. A VS is started as soon as it is created.

[Configuring Hardware Resources for the VS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vs_cfg_0005.html)

A Physical System (PS) administrator can allocate board and interface resources to Virtual Systems (VSs) so that the VSs can carry services, or delete board and interface resources so that the services on the VSs can be stopped.

[(Optional) Configuring Logical Resources for the VS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vs_cfg_0015.html)

A Physical System (PS) administrator can allocate logical resources to Virtual Systems through two methods.

[(Optional) Switching a VS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vs_cfg_0006.html)

A Physical System (PS) administrator can switch from one Virtual System (VS) to another.

[Verifying the VS Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vs_cfg_0007.html)

Verify the VS configuration as a PS administrator.