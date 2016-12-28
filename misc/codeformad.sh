BEARER=v1tKUaiU3KniADB4K1U3l46WPD9wDj

curl -v -v -v -X POST -H "Authorization: Bearer v1tKUaiU3KniADB4K1U3l46WPD9wDj" -H "content-type: application/json" https://codeformadison.com/graphql? -d '{"query":"query{\n  allBusstops \n  {\n    edges \n    {\n      node {\n        stopId\n        name\n      }\n    }\n  }\n}","variables":"null"}'
