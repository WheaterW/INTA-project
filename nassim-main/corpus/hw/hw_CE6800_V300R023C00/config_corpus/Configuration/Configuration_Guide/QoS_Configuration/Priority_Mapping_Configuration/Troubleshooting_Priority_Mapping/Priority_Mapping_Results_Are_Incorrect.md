Priority Mapping Results Are Incorrect
======================================

Priority Mapping Results Are Incorrect

#### Fault Symptoms

Priority mapping results are incorrect.


#### Possible Causes

Possible causes are as follows:

* On the outbound interface, packets do not enter queues mapped to external priorities.
* The priority types trusted by the inbound and outbound interfaces are incorrect.
* The priority mappings configured in the DiffServ domains bound to the inbound and outbound interfaces are incorrect.
* There are configurations affecting priority mapping on the inbound and outbound interfaces.


#### Procedure

1. Check whether packets enter correct queues on the outbound interface.
   
   
   
   Run the [**display qos queue statistics**](cmdqueryname=display+qos+queue+statistics) **interface** *interface-type interface-number* command to check whether packets enter correct queues on the outbound interface.
   
   * If packets enter incorrect queues, locate the fault. For details, see [Packets Enter Incorrect Queues](galaxy_qos_priority_mapping_cfg_0015.html).
   * If packets enter correct queues, go to step 2.
2. Check whether the priority types trusted by the inbound and outbound interface are correct.
   
   
   
   Run the [**display this**](cmdqueryname=display+this) command in the inbound or outbound interface view to check whether the priority type trusted using the [**trust**](cmdqueryname=trust) command is correct.
   
   * If the trusted priority type is incorrect, run the [**trust**](cmdqueryname=trust) command to specify the correct priority type.
   * If the trusted priority type is correct, go to step 3.
3. Check whether the priority mappings in the DiffServ domain bound to the inbound or outbound interface are correct.
   
   
   
   Run the [**display this**](cmdqueryname=display+this) command in the inbound or outbound interface view to check whether the [**trust upstream**](cmdqueryname=trust+upstream) command is configured.
   
   Run the [**display diffserv domain**](cmdqueryname=display+diffserv+domain) [ *ds-domain-name* | **brief** ] command to check whether the mappings between internal priorities/colors and external priorities are correct.
   
   * If the priority mappings are incorrect, run the [**ip-dscp-outbound**](cmdqueryname=ip-dscp-outbound), or [**8021p-outbound**](cmdqueryname=8021p-outbound) command to configure the mappings between internal priorities/colors and external priorities.
   * If the priority mappings are correct, go to step 4.
4. Check whether there are configurations affecting priority mapping on the inbound and outbound interfaces.
   
   On an interface:
   * If the [**qos phb marking dscp enable**](cmdqueryname=qos+phb+marking+dscp+enable) command is not configured, the system does not perform mapping between PHBs and DSCP values for outgoing packets on the interface.
   * If the **qos phb marking 8021p disable** command is configured, the system does not perform mapping between PHBs and 802.1p values for outgoing packets on the interface.
   * If the [**trust upstream none**](cmdqueryname=trust+upstream+none) command is configured, the system does not perform priority mapping for outgoing packets on the interface.
   * If packets match a traffic policy that is applied to the inbound or outbound direction (using the [**traffic-policy**](cmdqueryname=traffic-policy) command) and contains the action of [**remark 8021p**](cmdqueryname=remark+8021p) or [**remark dscp**](cmdqueryname=remark+dscp), the packet priority is the re-marked external priority.
   
   Run the [**display this**](cmdqueryname=display+this) command in the inbound or outbound interface view to check whether there are any configurations affecting priority mapping. If such configurations are found, delete or modify them.