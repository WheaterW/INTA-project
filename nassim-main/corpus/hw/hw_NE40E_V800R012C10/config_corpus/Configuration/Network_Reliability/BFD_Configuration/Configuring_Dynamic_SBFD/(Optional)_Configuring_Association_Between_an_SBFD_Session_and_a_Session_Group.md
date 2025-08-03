(Optional) Configuring Association Between an SBFD Session and a Session Group
==============================================================================

You can associate the BFD session status with the session group status to implement fast switching upon multiple points of failure on a segmented cascaded network.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001290518566__fig_dc_vrp_bfd_cfg_200802), transmission devices exist on the link. When the link between transmission devices fails, fast switching upon multiple points of failure is required on the segmented cascaded network. BFD session 1 is established between DeviceA and DeviceB, and BFD session 2 is established between DeviceB and DeviceD. DeviceB is the SBFD reflector and establishes an SBFD session with DeviceC. BFD session 1 and BFD session 2 are added to the session group on DeviceB. After the SBFD reflector discriminator is associated with the session group, the status change of the BFD session group on DeviceB affects the status of the session between DeviceB and DeviceC.

**Figure 1** Association between SBFD and a session group

![](figure/en-us_image_0000001307088854.png)



#### Pre-configuration Tasks

Before associating an SBFD session with a session group, complete the following tasks:

* Create BFD sessions.
* Configure an SBFD session.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd-track-manager**](cmdqueryname=bfd-track-manager)
   
   
   
   Association between BFD and a session group is enabled globally.
3. Run **[**group**](cmdqueryname=group)** *group-name*
   
   
   
   A BFD session group is created.
4. Run **[**bfd session**](cmdqueryname=bfd+session)** *session-name*
   
   
   
   A session is added to the BFD session group.
5. Run **s****bfd reflector** *unsigned-integer-value* **track** **group** *group-name* or **sbfd reflector** *ip-address-value* **track** **group** *group-name*
   
   
   
   The SBFD reflector discriminator is associated with the session group.