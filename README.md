# Recommendation_System_Fjong_Docker
Quick documentation of the REST-api as it currently exists.
Any methods not documented here have yet to be defined.
## /recsys/ping
###### GET
returns a form:
```
{"response": "Pong!"}
```

## /recsys/metrics
###### GET
returns a set of metrics. Actual return values of course heavily subject to change.
```
{
"average_latency": <average recsys post latency>
"latencies": <json array of all latencies experienced>
}
```

## /recsys/
###### GET
returns a form
```
{"response": "Hello World!"}
```

###### PUT
requires json body data including the field "item_ids", example:
```
{
"user_id": "user.adaf918fc0364873a48255897a2b13d8",
"item_ids": ["outfit.00004b4d01ca4ab0a70cf073ba74fefa", "outfit.001bf665330140cf854dcfb1cbff6b5f", "outfit.00234201fa2d4ee49a572d650c775213"]
}
```
returns a list of selected recommended items. In this dummy implementation these are simply the input items in the "item_ids" field.
```
{
["outfit.00004b4d01ca4ab0a70cf073ba74fefa", "outfit.001bf665330140cf854dcfb1cbff6b5f", "outfit.00234201fa2d4ee49a572d650c775213"]
}
```