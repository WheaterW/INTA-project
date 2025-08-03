(Optional) Adjusting BFD Parameters
===================================

BFD parameters are adjusted on the ingress of a tunnel either globally or on a tunnel interface.

#### Context

Perform either of the following operations:

* [Adjust global BFD parameters](#EN-US_TASK_0172368265__step_dc_vrp_cfg_00381101) if a majority of TE tunnels on the ingress use the same BFD parameters.
* [Adjust BFD parameters on an interface](#EN-US_TASK_0172368265__step_dc_vrp_cfg_00381102) if some TE tunnels on the ingress need BFD parameters different from global BFD parameters.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Effective local interval at which BFD packets are sent = MAX { Configured local interval at which BFD packets are sent, Configured remote interval at which BFD packets are received }
* Effective local interval at which BFD packets are received = MAX { Configured remote interval at which BFD packets are sent, Configured local interval at which BFD packets are received }
* Effective local detection interval = Effective local interval at which BFD packets are received x Configured remote detection multiplier

On the egress of the TE tunnel enabled with the capability of passively creating BFD sessions, the default values of the receiving interval, the sending interval, and the detection multiplier cannot be adjusted. The default values of these three parameters are the configured minimum values on the ingress. Therefore, the BFD detection interval on the ingress and that on the egress of a TE tunnel are as follows:

* Effective detection interval on the ingress = Configured interval at which BFD packets are received on the ingress x 3
* Effective detection interval on the egress = Configured local interval at which BFD packets are sent on the ingress x Configured detection multiplier on the ingress


#### Procedure

* Adjust global BFD parameters on the ingress of a TE tunnel.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te bfd**](cmdqueryname=mpls+te+bfd) { **min-tx-interval** *tx-interval* | **min-rx-interval** *tx-interval* | **detect-multiplier** *multiplier* } \*
     
     
     
     BFD time parameters are adjusted globally.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Adjust BFD parameters on the tunnel interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The TE tunnel interface view is displayed.
  3. Run [**mpls te bfd**](cmdqueryname=mpls+te+bfd) { **min-tx-interval** *tx-interval* | **min-rx-interval** *rx-interval* | **detect-multiplier** *multiplier* } \*
     
     
     
     BFD time parameters are adjusted.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.