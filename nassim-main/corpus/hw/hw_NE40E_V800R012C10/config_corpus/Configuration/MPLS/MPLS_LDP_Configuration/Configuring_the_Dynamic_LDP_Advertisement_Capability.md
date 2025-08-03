Configuring the Dynamic LDP Advertisement Capability
====================================================

On devices enabled with global LDP, the dynamic LDP advertisement capability allows extended LDP functions to be dynamically enabled or disabled when the LDP session is working properly, ensuring stable LSP operation.

#### Usage Scenario

On a device disabled from dynamic LDP advertisement, if an extended LDP function is enabled after an LDP session is created, the LDP session will be interrupted and the extended LDP function will be negotiated, affecting LSP stability. After the dynamic LDP advertisement capability is enabled, the LDP features that support the dynamic LDP advertisement capability can be dynamically enabled or disabled without interrupting sessions, improving the stability of LSPs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The dynamic LDP advertisement capability does not affect existing LDP functions. You are advised to enable this function immediately after LDP is enabled globally, as it facilitates dynamic advertisement of new extended functions.

Before enabling the dynamic LDP advertisement capability, enable MPLS and MPLS LDP globally.



#### Pre-configuration Tasks

Before configuring the dynamic LDP advertisement capability, complete the following task:

* [Enable MPLS LDP globally](dc_vrp_ldp-p2p_cfg_0004.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**capability-announcement**](cmdqueryname=capability-announcement)
   
   
   
   The dynamic LDP advertisement capability is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Enabling dynamic LDP advertisement after an LDP session is established will result in reestablishment of the LDP session.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring a local LDP session, run the [**display mpls ldp**](cmdqueryname=display+mpls+ldp) command to check whether the dynamic LDP advertisement capability has been enabled. The capability has been enabled if the **Capability-Announcement** field in the command output is **On**.