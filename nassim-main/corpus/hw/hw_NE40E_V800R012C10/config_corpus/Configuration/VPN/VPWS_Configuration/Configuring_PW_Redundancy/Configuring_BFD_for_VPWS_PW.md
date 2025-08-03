Configuring BFD for VPWS PW
===========================

Configuring BFD for VPWS PW accelerates PW fault detection, resulting in fast switching of upper-layer applications.

#### Usage Scenario

On an MPLS L2VPN, if PWs exist between PEs, you can configure BFD for PW to rapidly detect link faults, so that upper-layer applications can quickly switch to another link when a link encounters a fault.

A BFD session can be either static or dynamic. Determine which one to use as needed.

#### Pre-configuration Tasks

Before configuring BFD for VPWS PW, complete the following tasks:

* Configure network layer parameters for devices to communicate.
* Configure PWs.
* If interworking with non-Huawei devices that do not support the BFD CV Type of 0x08 in VCCV is required, run the [**mpls l2vpn vccv bfd-cv-negotiation**](cmdqueryname=mpls+l2vpn+vccv+bfd-cv-negotiation) command to change the BFD CV Type in Label Mapping packets to be the same as that on the remote peer.
* Static BFD for VLL PW does not support a CV type of 0x10 or 0x20 in control word mode. If the CV type in the PW negotiation result is 0x10 or 0x20, the BFD session cannot go Up.


#### Procedure

* Configure a static BFD session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally, and the global BFD view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Determine how to configure BFD based on networking.
     
     
     + Create a BFD session for the VPWS PW.
       
       Run the [**bfd**](cmdqueryname=bfd) *session-name* **bind pw** **interface** *interface-type1 interface-number1* [ **remote-peer** *remote-peer-address* **pw-ttl** { **auto-calculate** | *ttl-number* } ] [ **track-interface** [ *interface* { *interface-name2* | *interface-type2 interface-number2* } ] ] [ **secondary** ] command to create BFD configuration items.
     
     
     
     The following describes the meanings of interface parameters used when a BFD session detects the service PW and mPW.
     
     + If the BFD session is used to monitor a service PW:
       - The interface specified by **interface** *interface-type1 interface-number1* is the AC interface on which the PW resides.
       - After **track-interface** is configured, the BFD session enters the down state when the AC interface goes down.
       - *interface-type2 interface-number2* cannot be used to specify the type or number of an associated interface.
     + If the BFD session is used to monitor an mPW:
       - The interface specified by **interface** *interface-type1 interface-number1* is a loopback interface.
       - **track-interface** *interface-type2 interface-number2* can be used to specify the type and number of an associated interface. If the specified interface goes down, the BFD session enters the down state.
       - You can use **controller** *interface-type2 interface-number2* to specify the type and number of an associated CPOS interface.
     
     If the PW to be detected is a secondary PW, configure **secondary**.
     
     The PW to be detected can be either an SS-PW or an MS-PW.
  5. Configure discriminators.
     
     
     + Run the [**discriminator**](cmdqueryname=discriminator) **local** *discr-value* command to configure the local discriminator.
     + Run the [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value* command to configure the remote discriminator.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The local BFD session discriminator on one end must be the remote BFD session discriminator on the other end.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     If the PW to be detected is down, the BFD session can be established but cannot go up.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + You must configure or cancel BFD for PW on both endpoint PEs of a PW. Otherwise, the PW status on both endpoint PEs may be inconsistent.
     + If you want to modify the parameters of an existing BFD session, run the corresponding commands, such as [**min-tx-interval**](cmdqueryname=min-tx-interval), [**min-rx-interval**](cmdqueryname=min-rx-interval), and [**detect-multiplier**](cmdqueryname=detect-multiplier).
* Configure a dynamic BFD session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally, and the global BFD view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Adjust BFD detection parameters.
     
     
     1. Run the [**pw-template**](cmdqueryname=pw-template) *pw-template-name* command to enter the PW template view.
     2. Run the [**control-word**](cmdqueryname=control-word) command to enable the control word function.
     3. Run the [**bfd-detect**](cmdqueryname=bfd-detect) [ **detect-multiplier** *multiplier* | **min-rx-interval** *rx-interval* | **min-tx-interval** *tx-interval* ] \* [ **track** **group** *group-name* ] command to set BFD session detection parameters.![](../../../../public_sys-resources/note_3.0-en-us.png) BFD detection parameters are described as follows:
        + **detect-multiplier** *multiplier* indicates the BFD detection multiplier.
        + **min-rx-interval** *rx-interval* indicates the Required Min Rx Interval (RMRI), which is the supported minimum interval at which the local device receives BFD control packets.
        + **min-tx-interval** *tx-interval* indicates the Desired Min Tx Interval (DMTI), which is the desired minimum interval at which the local device sends BFD control packets.
        The BFD detection parameters actually used may be different from the ones configured:
        + Actual local detection interval = Actual interval at which the local device receives BFD packets x Configured remote BFD detection multiplier
        + Actual interval at which the local device receives BFD packets = Max { Configured remote DMTI, Configured local RMRI }
        + Actual interval at which the local device transmits BFD packets = Max { Configured local DMTI, Configured remote RMRI }
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
  5. Trigger the establishment of a dynamic BFD session.
     
     
     1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The AC interface view is displayed.
     2. Run [**mpls l2vpn pw bfd**](cmdqueryname=mpls+l2vpn+pw+bfd) [ **detect-multiplier** *multiplier* | **min-rx-interval** *rx-interval* | **min-tx-interval** *tx-interval* ] \* [ **track** **group** *group-name* ] [ **remote-vcid** *vc-id* ] [ **track-interface** ] [ **secondary** ]
        
        Dynamic BFD for PW is enabled to trigger the establishment of a dynamic BFD session to detect the VPWS PW connectivity.
        
        If the PW to be detected is a secondary PW, configure **secondary**.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring BFD for VPWS PW, verify the configuration.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) command to check BFD session configurations.
* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) **interface** *interface-type* *interface-number* command to check dynamic BFD session configurations.