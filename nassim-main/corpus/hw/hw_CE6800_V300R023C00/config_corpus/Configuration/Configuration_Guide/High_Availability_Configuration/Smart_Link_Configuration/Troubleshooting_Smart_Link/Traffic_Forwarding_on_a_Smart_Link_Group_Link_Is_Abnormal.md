Traffic Forwarding on a Smart Link Group Link Is Abnormal
=========================================================

Traffic Forwarding on a Smart Link Group Link Is Abnormal

#### Possible Causes

The configurations of the master and slave interfaces in the Smart Link group may be abnormal.


#### Procedure

* Run the [**display smart-link group**](cmdqueryname=display+smart-link+group) *groupId* and [**display smart-link protocol-parameter group**](cmdqueryname=display+smart-link+protocol-parameter+group) *groupId* commands to check whether the active and inactive member interfaces in the Smart Link group are normal, whether the state machine where the member interfaces reside is normal, and whether the events triggered by the state machine are normal.