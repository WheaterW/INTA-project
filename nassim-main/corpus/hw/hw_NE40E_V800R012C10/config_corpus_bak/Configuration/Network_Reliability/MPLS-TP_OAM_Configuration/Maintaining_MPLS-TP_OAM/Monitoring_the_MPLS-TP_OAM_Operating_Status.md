Monitoring the MPLS-TP OAM Operating Status
===========================================

This section describes how to monitor the Multiprotocol Label Switching Transport Profile (MPLS-TP) operation, administration and maintenance (OAM) operating status.

#### Context

You can run the following commands in any view to check the MPLS-TP OAM operating status in routine maintenance.


#### Procedure

* Run the [**display mpls-tp oam current-alarm**](cmdqueryname=display+mpls-tp+oam+current-alarm) [ **meg** *meg-name* ] command to check alarms associated with a maintenance entity group (MEG).
* Run the [**display mpls-tp oam me brief**](cmdqueryname=display+mpls-tp+oam+me+brief) command to check information about maintenance entities (MEs) in a MEG.
* Run the [**display mpls-tp oam meg**](cmdqueryname=display+mpls-tp+oam+meg) *meg-name* command to check MEG information on a local device.
* Run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) **meg** *meg-name* **statistic-type** { **lost-measure** { **single-ended** | **dual-ended** } | **delay-measure** { **one-way** | **two-way** } } command in any view to check MPLS-TP OAM performance statistics.