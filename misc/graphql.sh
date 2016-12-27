BEARER=v1tKUaiU3KniADB4K1U3l46WPD9wDj

curl -v -v -v -X POST -H "Authorization: Bearer v1tKUaiU3KniADB4K1U3l46WPD9wDj" -H "content-type: application/json" http://localhost:8000/graphql? -d '{"query":"query{\n  allBusstops \n  {\n    edges \n    {\n      node {\n        stopId\n        name\n      }\n    }\n  }\n}","variables":"null"}'
