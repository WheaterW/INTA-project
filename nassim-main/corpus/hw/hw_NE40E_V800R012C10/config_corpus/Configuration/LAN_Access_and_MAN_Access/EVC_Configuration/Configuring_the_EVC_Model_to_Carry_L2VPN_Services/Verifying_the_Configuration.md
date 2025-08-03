Verifying the Configuration
===========================

After configuring the EVC model to carry L2VPN services, verify the configuration.

#### Prerequisites

The EVC model has been configured to carry L2VPN services.


#### Procedure

* Run the [**display vsi**](cmdqueryname=display+vsi) [ **name** *vsi-name* ] [ **verbose** ] command to check detailed VSI information.
* Run the [**display
  mpls l2vc**](cmdqueryname=display+mpls+l2vc) **brief** command to check brief VPWS connection information.

#### Verifying the Configuration

Run the [**display vsi**](cmdqueryname=display+vsi) command. The command output shows that the VSI status is **up** and the BD that accesses the VSI is **bridge-domain 10**.

Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) **brief** command. The command output shows that one VC has been set up and is in the Up state.