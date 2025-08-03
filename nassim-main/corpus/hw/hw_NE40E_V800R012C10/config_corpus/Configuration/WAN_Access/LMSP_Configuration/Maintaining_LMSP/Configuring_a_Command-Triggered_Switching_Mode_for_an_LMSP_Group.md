Configuring a Command-Triggered Switching Mode for an LMSP Group
================================================================

Command-triggered LMSP switching modes include protection lockout, forcible switching to the working link, forcible switching to the protection link, manual switching to the working link, and manual switching to the protection link. Command-triggered LMSP switching is used during a device upgrade, link troubleshooting, testing, and maintenance.

#### Context

The switching modes are prioritized in descending order:

Protection lockout > Forcible switching to the working link > Forcible switching to the protection link > Manual switching to the working link > Manual switching to the protection link

* Protection lock: Services are being transmitted on the working link and are unable to switch to the protection link even though the working link becomes unavailable.
* Forcible switching to the working link: After services have been switched to the protection link, the services can be forcibly switched back to the working link. Even if an SD or SF fault occurs on the working link, the services will not be switched to the protection link. As a result, services are interrupted.
* Forcible switching to the protection link: If the working link fails, services are forcibly switched to the protection link. If an SD fault occurs on the protection link, the services may be interrupted. If an SF fault occurs on the protection link, a device sends a request to its peer to switch the services back to the working link.
* Manual switching to the working link: If a traffic switchover has been performed in an LMSP group and the working link has no fault, services can be manually switched to the working link. A device will send a request to its peer to switch services to the protection link if an SF or SD fault occurs on the working link.
* Manual switching to the protection link: If the working and protection links have no SF or SD fault, services can be manually switched to the protection link. A device will send a request to its peer to switch services to the working link if an SF or SD fault occurs on the protection link.

Perform the following steps on a protection interface in an LMSP group:


#### Procedure

* Configure a command-triggered switching mode for an LMSP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* or [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
     
     
     
     The protection interface view of the LMSP group is displayed.
  3. Run [**aps switch-command**](cmdqueryname=aps+switch-command) { **lockout** | { **force** | **manual** } [ **section** *section-number* ] }
     
     
     
     A switching mode is configured for the LMSP group.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When using an [**aps switch-command**](cmdqueryname=aps+switch-command) command instance, ensure that the priority of the switch command is higher than that of an existing switch command. Otherwise, the command to be used does not take effect.
     
     If the **force** or **manual** parameter is configured, the [**display this**](cmdqueryname=display+this) command does not display configurations. You can run the [**display aps group**](cmdqueryname=display+aps+group) *aps-group-id* command to view configurations.