Configuring ARP VLAN CAR
========================

ARP VLAN CAR allows you to limit the rate of ARP packets on the attacked interface without affecting other interfaces. This minimizes the impact of attacks on devices and services. After the alarm function is enabled for ARP VLAN CAR and the number of ARP packets to be sent to the CPU exceeds the threshold configured for ARP VLAN CAR, an alarm is reported.

#### Context

Configure ARP VLAN CAR on interfaces of the Router

In VS mode, this feature is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**undo alarm drop-rate arp-vlan-car disable**](cmdqueryname=undo+alarm+drop-rate+arp-vlan-car+disable)
   
   
   
   The alarm function is enabled for ARP VLAN CAR.
4. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*sub-interface-number* ]
   
   
   
   The interface view is displayed.
6. Run [**arp rate-limit**](cmdqueryname=arp+rate-limit) *rate*
   
   
   
   The rate limit of ARP VLAN CAR for ARP packets on an interface is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you configure a rate limit (1024 pps, for example) which is larger than the default rate limit of CP-CAR, the configured ARP VLAN CAR cannot take effect. CP-CAR can be configured by running the [**car**](cmdqueryname=car) **arp cir** *cir-value* command. For details, see [Configuring the CAR](dc_ne_sysattack_cfg_0017.html). The configuration of CP-CAR can be checked by running the [**display cpu-defend car information**](cmdqueryname=display+cpu-defend+car+information) command.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. (Optional) Set the percentage of the bandwidth of level-2 CAR for ARP VLAN CAR in the bandwidth of CP-CAR for the ARP packets.
   1. (Optional) Run [**slot**](cmdqueryname=slot) *slot-id*
      
      
      
      The slot view is displayed.
   2. Run [**arp attack rate-limit-percent**](cmdqueryname=arp+attack+rate-limit-percent) *rate-value*
      
      
      
      The percentage of the bandwidth of level-2 CAR for ARP VLAN CAR in the bandwidth of CP-CAR for ARP protocol packets is configured.
   3. (Optional) Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.