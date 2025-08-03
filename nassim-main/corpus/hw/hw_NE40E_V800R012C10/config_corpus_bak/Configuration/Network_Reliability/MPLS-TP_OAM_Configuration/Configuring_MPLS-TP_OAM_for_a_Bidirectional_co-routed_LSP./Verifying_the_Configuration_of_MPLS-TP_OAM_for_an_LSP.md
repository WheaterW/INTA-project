Verifying the Configuration of MPLS-TP OAM for an LSP
=====================================================

After configuring MPLS-TP OAM function for a LSP, verify the configuration by querying performance statistics and fault detection information.

#### Prerequisites

MPLS-TP OAM has been configured for an LSP.


#### Procedure

* Run the [**display mpls-tp oam current-alarm**](cmdqueryname=display+mpls-tp+oam+current-alarm) command to check alarms associated with a MEG.
* Run the [**display mpls-tp oam me**](cmdqueryname=display+mpls-tp+oam+me) **brief** command to check information about MEs in a MEG.
* Run the [**display mpls-tp oam meg**](cmdqueryname=display+mpls-tp+oam+meg) command to check MEG information on the MEP.
* Run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** command to check MPLS-TP OAM performance statistics.