Configuring Association Between a BFD Session and a Session Group
=================================================================

You can associate the BFD session status with the session group status to implement fast switching upon multiple points of failure on a segmented cascaded network.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001343304189__fig5100171974212), transmission devices exist on the link. When the link between transmission devices fails, fast switching upon multiple points of failure is required on the segmented cascaded network. BFD session 1 is established between DeviceA and DeviceB, BFD session 2 is established between DeviceB and DeviceD, and BFD session 3 is established between DeviceB and DeviceC. BFD session 1 and BFD session 2 are added to the session group on DeviceB. After BFD session 3 is associated with the BFD session group, the status change of the BFD session group on DeviceB affects the status of the session between DeviceB and DeviceC.**Figure 1** Association between the BFD session status and the session group status  
![](figure/en-us_image_0000001359728969.png)


#### Pre-configuration Tasks

Before associating a BFD session with a session group, complete the following task:

* Create BFD sessions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd-track-manager**](cmdqueryname=bfd-track-manager)
   
   
   
   Association between BFD and a session group is enabled globally.
3. Run **group** *group-name*
   
   
   
   A BFD session group is created.
4. Run **bfd session** *session-name*
   
   
   
   A session is added to the BFD session group.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BFD track view.
6. Run any of the following commands:
   
   
   * To associate a BFD session with the session group, run the **bfd session** *session-name* **track** **group** *group-name* command.
   * To associate a static BFD session with automatically negotiated discriminators and a dynamic multi-hop BFD session with the session group, run the **bfd multi-hop** { **peer-ip** *peer-ip-value* | **peer-ipv6** *peer-ipv6-value* } [ **vpn-instance** *vpnname-value* ] **track** **group** *group-name* command.
   * To associate a static BFD session with automatically negotiated discriminators, a link-bundle session, and a dynamic single-hop BFD session bound to an interface with the session group, run the **bfd single-hop** { **ipv4** | **ipv6** } **bind-interface** { *interface-name* | *interface-type* *interface-num* } **track** **group** *group-name* command.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the **display bfd track-manager** command to check information about the BFD session group.
* Run the **display bfd session verbose** command to check detailed information about BFD sessions.