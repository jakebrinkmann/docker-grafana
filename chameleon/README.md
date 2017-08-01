# Grafana JSON API 

For the grafana [simple-json-datasource plugin](https://github.com/grafana/simple-json-datasource),
 we need an API backend to expose 4 url resources:

* `/` return 200ok
* `/search` find metric options
* `/query` return metrics by input
* `/annotations` return annotations

This is served up with gunicorn inside the docker applications, but can be
tested out using:

```bash
from chameleon import app
app.run(debug=True)
```

```
GET localhost:5000/
```

```
POST localhost:5000/query -d '{  
   "panelId":1,
   "range":{  
      "from":"2017-05-01T15:01:19.283Z",
      "to":"2017-05-01T21:01:19.283Z",
      "raw":{  
         "from":"now-6h",
         "to":"now"
      }
   },
   "rangeRaw":{  
      "from":"now-6h",
      "to":"now"
   },
   "interval":"15s",
   "intervalMs":15000,
   "targets":[  
      {  
         "type":"timeserie"
      }
   ],
   "format":"json",
   "maxDataPoints":1365,
   "scopedVars":{  
      "__interval":{  
         "text":"15s",
         "value":"15s"
      },
      "__interval_ms":{  
         "text":15000,
         "value":15000
      }
   }
}'
```

