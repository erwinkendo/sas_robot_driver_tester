# Testing code for PR deployments

## Testing original code

``` bash
docker compose -f compose_original.yaml up --build --remove-orphans
docker compose -f compose_original.yaml stop -t 1 
docker compose -f compose_original.yaml rm 
```

## Testing tool_gpio branch
``` bash
docker compose -f compose_tool_gpio.yaml up --build --remove-orphans
docker compose -f compose_tool_gpio.yaml stop -t 1 
docker compose -f compose_tool_gpio.yaml rm 
```