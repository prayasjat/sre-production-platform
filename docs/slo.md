# Service Level Objective

## Availability SLO

Target availability:

99%

## Measurement

Availability = successful requests / total requests

## Example

If there are 10,000 requests:

Maximum failed requests allowed:

100

## Error Budget

Error budget = 1%

For 10,000 requests:

100 failed requests are allowed.

## SRE Principle

If the service consumes too much of its error budget,
reliability work should take priority over new feature work.
